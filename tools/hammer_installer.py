import subprocess

def check_hammer():
    try:
        subprocess.run("hammer version", shell=True) 
        subprocess.check_output("hammer version", shell=True)
        return True
    except Exception as e:
        print(f"Error while checking hammer : {e}")

def install_hammer():
    try:
        subprocess.run("brew tap pivotal/hammer https://github.com/pivotal/hammer; brew install hammer", shell=True)
        subprocess.run("hammer version", shell=True) 
    except Exception as e:
        print(f"Error while installing hammer : {e}")
