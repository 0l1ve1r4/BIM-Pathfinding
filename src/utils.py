import importlib
import subprocess

def debug(text, type):
    if type == "error":
        print("\033[1;31m" + "[Error]: " + "\033[0m" + text)
            
    elif type == "warning":
        print("\033[1;33m" + "[Warning]: " + "\033[0m" + text)
    
    elif type == "info":
        print("\033[1;34m" + "[Info]: " + "\033[0m" + text)
        
    elif type == "success":
        print("\033[1;32m" + "[Success]: " + "\033[0m" + text)
              
    else:
        print("\033[1;35m" + "[Debug]: " + "\033[0m" + text)
        


def check_and_install_libraries():
    required_libraries = [
        'matplotlib',
        'tkinter',
        'PIL',
        'concurrent.futures',
    ]

    missing_libraries = []

    for lib in required_libraries:
        try:
            importlib.import_module(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        debug("Some libraries are missing, installing them...", "error")
        install_libraries(missing_libraries)
    else:
        debug("All required libraries are installed.", "success")

def install_libraries(libraries):
    for lib in libraries:
        subprocess.check_call(['pip', 'install', lib])
        print(f"Installed {lib}.")


