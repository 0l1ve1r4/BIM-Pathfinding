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
        
