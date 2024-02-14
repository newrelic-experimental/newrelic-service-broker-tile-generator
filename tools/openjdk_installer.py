import os
import urllib.request
import tarfile
import subprocess


def check_java_version(version):
    try:
        result = subprocess.run(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) 
        if result.returncode == 0:
            openjdk_version=""
            # Parse the output to extract the OpenJDK version
            output = result.stdout.strip() + result.stderr.strip() 
            lines = output.split('\n')
            for line in lines:
                if line.startswith("java version"):
                    openjdk_version = openjdk_version + line.split()[1].replace('"', '')
                    if openjdk_version == version :
                        return True
            return False 
        else:
            print("Error:", result.stderr)
        return None  
    except Exception as e:
        print(f"Error while checking Java version : {e}") 
        return None


def get_version():
    subprocess.run("java -version", shell=True)

def download_openjdk(java_version, download_path):
    jdk_url = f"https://download.oracle.com/java/{java_version}/latest/jdk-{java_version}_macos-x64_bin.tar.gz"
    try:
        print(f"Downloading OpenJDK {java_version}...")
        urllib.request.urlretrieve(jdk_url, download_path)
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading OpenJDK: {e}")

def extract_openjdk(download_path, extract_path):
    try:
        print("Extracting OpenJDK archive...", download_path, extract_path)
        with tarfile.open(download_path, 'r:gz') as tar:
            tar.extractall(path=os.path.join(extract_path))
        print("Extraction complete!")
    except Exception as e:
        print(f"Error extracting OpenJDK: {e}")

def set_java_home(java_version, extract_path):
    entries = os.listdir(extract_path)
    tmp_var = extract_path + "/" + entries[0] + "/Contents/Home"
    java_home = tmp_var
    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = f"{java_home}/bin:{os.environ['PATH']}"


def install_openjdk(java_version, install_path):
    download_path = f"openjdk-{java_version}_macos-x64_bin.tar.gz"
    extract_path = f"jdk-{java_version}"
    download_openjdk(java_version, download_path)
    extract_openjdk(download_path, extract_path)
    try:
        set_java_home(java_version, extract_path)
        subprocess.run("java -version", shell=True)     
        print(f"OpenJDK {java_version} installed successfully at {install_path}")
    except Exception as e:
        print(f"Error installing OpenJDK: {e}", extract_path, install_path)
