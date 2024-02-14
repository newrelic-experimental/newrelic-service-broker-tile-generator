import subprocess

def check_go():
    try:
        subprocess.run("go version", shell=True) 
        subprocess.check_output("go version", shell=True)
        return True
    except Exception as e:
        print(f"Error while checking go : {e}")

def install_go():
    try:
        subprocess.run("brew install go", shell=True)
        subprocess.run("go version", shell=True) 
    except Exception as e:
        print(f"Error while installing go : {e}")
