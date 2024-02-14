import subprocess

def check_om():
    try:
        subprocess.run("om version", shell=True) 
        subprocess.check_output("om version", shell=True)
        return True
    except Exception as e:
        print(f"Error while checking om : {e}")

def install_om():
    try:
        subprocess.run("brew tap pivotal/om https://github.com/pivotal/om; brew install om", shell=True)
        subprocess.run("om version", shell=True) 
    except Exception as e:
        print(f"Error while installing om : {e}")
