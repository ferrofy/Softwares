import sys
import subprocess
import ensurepip
import importlib

PACKAGES = [""]

def ensure_pip():
    try:
        import pip
        print("pip is already installed")
    except ImportError:
        print("pip not found, installing...")
        ensurepip.bootstrap()
        print("pip installed successfully")

def is_installed(package):
    try:
        importlib.import_module(package)
        return True
    except ImportError:
        return False

def install_or_update(package):
    if is_installed(package):
        print(f"{package} is already installed")
    else:
        print(f"installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"failed to install {package}")

def main():
    print("Python Package Auto Installer\n")
    ensure_pip()
    for pkg in PACKAGES:
        install_or_update(pkg)
    print("\nAll packages processed\n")

if __name__ == "__main__":
    main()

print("All Done")
input("Press Enter To Exit...")
