import os
import yaml
from tools import go_installer, compile_tile, openjdk_installer, om_installer, maven_installer, hammer_installer


RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def read_config(file_path):
    with open(file_path, 'r') as yaml_file:
        config_data = yaml.safe_load(yaml_file)
    return config_data

if __name__ == "__main__":
    config_data = read_config("config.yaml")
   
    print(RED + "---------Building newrelic-service-broker-tile ----------") 
    print(BLUE + "---------GOLANG installation ----------") 
    print(GREEN)
    go_installed = go_installer.check_go()
    if not go_installed :
        go_installer.install_go()
    print(BLUE + "---------END of GOLANG installation ----------") 

    print(BLUE + "---------OPENJDK installation ----------") 
    print(GREEN)
    openjdk_version = config_data.get('openjdk')
    java_installed = openjdk_installer.check_java_version(openjdk_version)
    if not java_installed :
        print("Insatlling openjdk in local path, it will not override global settings ", openjdk_version)
        openjdk_install_path = os.getcwd()
        openjdk_installer.install_openjdk(openjdk_version, openjdk_install_path)
    print(BLUE + "---------END of OPENJDK installation ----------") 

    print("---------MAVEN installation ----------") 
    print(GREEN)
    maven_version = config_data.get('maven')
    maven_installed = maven_installer.check_maven(maven_version)
    if not maven_installed :
        print("Insatlling maven in local path , it will not override global settings", maven_version)
        maven_install_path = os.getcwd()
        maven_installer.install_maven(maven_version, maven_install_path)
    print(BLUE + "---------END of MAVEN installation ----------") 
    
    print("---------Hammer installation ----------") 
    print(GREEN) 
    hammer_installed = hammer_installer.check_hammer()
    if not hammer_installed :
        hammer_installer.install_hammer()
    print(BLUE + "---------End of Hammer installation ----------") 

    print("---------om installation ----------") 
    print(GREEN)
    om_installed = om_installer.check_om()
    if not om_installed :
        om_installer.install_om()
    print(BLUE + "---------End of om installation ----------") 
    
    print("---------Tile creation ----------") 
    print(GREEN)
    old_licence = config_data.get('old_licence')
    new_licence = config_data.get('new_licence')
    compile_tile.compile_tile_generator(openjdk_version, maven_version, old_licence, new_licence)
    print(RED + "---------Created pivot in ----------  " + os.getcwd()+"/newrelic-service-broker-tile/product")
    print(RED + "DONE !!!")
