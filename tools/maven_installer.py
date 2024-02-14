import os
import shutil
import urllib.request
import zipfile
import subprocess

def download_maven(maven_version, download_path):
    maven_url = f"https://apache.osuosl.org/maven/maven-3/{maven_version}/binaries/apache-maven-{maven_version}-bin.zip"
    try:
        print(f"Downloading Apache Maven {maven_version}...", maven_url , download_path)
        urllib.request.urlretrieve(maven_url, f"apache-maven-{maven_version}-bin.zip")
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading Maven: {e}")

def set_maven_home(install_path, maven_version):
    maven_bin = f"/apache-maven-{maven_version}"
    maven_home = install_path + maven_bin
    os.environ["M2_HOME"] = maven_home
    print("maven_home", maven_home)
    os.environ["PATH"] = f"{maven_home}/bin:{os.environ['PATH']}"

def check_maven(version):
    try:
        result = subprocess.run(['maven', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            maven_version=""
            # Parse the output to extract the OpenJDK version
            output = result.stdout.strip() + result.stderr.strip()
            lines = output.split('\n')
            for line in lines:
                if line.startswith("Apache Maven"):
                    maven_version = openjdk_version + line.split()[2].replace('"', '')
                    if maven_version == version :
                        return True
            return False
        else:
            print("Error:", result.stderr)
        return None
    except Exception as e:
        print(f"Error while checking Maven version : {e}")
        return None


def get_version():
    subprocess.run("maven -version", shell=True)

def extract_maven(download_path, extract_path):
    try:
        print("Extracting Maven archive...", download_path, extract_path)
        with zipfile.ZipFile("apache-maven-3.9.6-bin.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
        print("Extraction complete!")
        permissions = 0o755
        os.chmod("apache-maven-3.9.6/bin/mvn", permissions)
    except Exception as e:
        print(f"Error extracting Maven: {e}")

def install_maven(maven_version, install_path):
    download_path = f"apache-maven-{maven_version}-bin.zip"
    extract_path = f"apache-maven-{maven_version}"
    download_maven(maven_version, download_path)
    extract_maven(download_path, extract_path)
    set_maven_home(install_path, maven_version)
    try:
       subprocess.run("echo $PATH", shell=True)
       subprocess.run("mvn -version", shell=True)
    except Exception as e:
        print(f"Error installing Maven: {e}")
