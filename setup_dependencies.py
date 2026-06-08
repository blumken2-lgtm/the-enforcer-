# Script to setup project dependencies

import os

def install_dependencies():
    print("Installing required dependencies...")
    os.system('pip install -r requirements.txt')

if __name__ == "__main__":
    install_dependencies()