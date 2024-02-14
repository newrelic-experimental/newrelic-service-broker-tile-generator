import subprocess
import platform
#import yaml
import ruamel.yaml
from . import maven_installer, openjdk_installer
import os

def check_command(command):
    try:
        subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

#update yaml with version
def update_yaml_default(filename, property_name, new_default):
   yaml = ruamel.yaml.YAML()
   yaml.indent(mapping=2, sequence=4, offset=2) 

   with open(filename, 'r') as file:
        yaml_data = yaml.load(file)   

   if 'forms' in yaml_data:
        for form in yaml_data['forms']:
            if 'properties' in form:
                for prop in form['properties']:
                    if prop.get('name') == property_name:
                        prop['default'] = new_default

   with open(filename, 'w') as file:
        yaml.dump(yaml_data, file)

def clone_servicetile():
    subprocess.run("git clone git@github.com:newrelic/newrelic-service-broker-tile.git", shell=True)
    update_yaml_default("newrelic-service-broker-tile/tile.yml", "default", "1.23")

def compile_jar():
    try:
        subprocess.run("echo $JAVA_HOME", shell=True) 
        subprocess.run("cd newrelic-service-broker-tile; mvn package -Dmaven.test.skip=true", shell=True)     
        subprocess.run("cd newrelic-service-broker-tile; tile build", shell=True) 
    except Exception as e:
        print(f"Error compiling jar file with Maven: {e}") 

def replace_string_in_licencefile(filename, old_string, new_string):
    with open(filename, 'r') as file:
        file_content = file.read()

    file_content = file_content.replace(old_string, new_string)

    with open(filename, 'w') as file:
        file.write(file_content)
    print("Successfully replaced licence string in ", filename)

def compile_tile_generator(java_version, maven_version, old_licence, new_license):
    try:
        print("\033[32m")
        clone_servicetile()
        replace_string_in_licencefile("newrelic-service-broker-tile/THIRD_PARTY_NOTICES.md", "New-Relic_Service-Broker_for_VMware-Tanzu-Cloud-Foundry_"+ old_licence, "New-Relic_Service-Broker_for_VMware-Tanzu-Cloud-Foundry_"+new_license)
        maven_installer.set_maven_home(os.getcwd(), maven_version)
        extract_path = f"jdk-{java_version}"
        extract_path = os.getcwd() + "/" +extract_path
        openjdk_installer.set_java_home(java_version,  extract_path)
        subprocess.run("echo $JAVA_HOME", shell=True)
        compile_jar()
    except Exception as e:
        print(f"Error compiling tile: {e}") 
