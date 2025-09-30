import platform
import os
import socket
import subprocess
import time
arc = None
print(f'\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;92mCHECKING FOR UPDATED ')
os.system('git pull --quiet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f'\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;92m32BIT DETECTED')
        print(f'\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;92mSTARTING SILENT TOOL')
        time.sleep(5)
        os.system('chmod 777 SILENT32;./SILENT32')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f'\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;92m64BIT DETECTED')
        print(f'\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;92mSTARTING SILENT TOOL')
        time.sleep(5)
        os.system('chmod 777 ERROR64;./SILENT64')
    else:
        arc = "INVALID"
        exit("\x1b[1;92m[\x1b[1;97m=\x1b[1;92m] \x1b[1;91mUNKNOWN DEVICE TYPE")

if __name__ == "__main__":
    main()
