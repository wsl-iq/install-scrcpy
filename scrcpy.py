import os
from design.colors import (R, G, B, Y, C, M, W, D, S)
from design.Terminal import(sign, Enter, ERROR, INFO, Information, Working, NotWorking, warning,
                            Complete, successfully, Failed, please, Question, Help, note, other, 
                            Running, Retrying, Ready, Loading, OK, Okay, stop, Critical, paused,
                            Retrying, Skip, SCAN, Chacking, Hacking, security, AI)
from design.BackGround import(Red, Green, Blue, Yellow, Cyan, Magenta, White, Black,Dark, Reset)

os.system("cls" if os.name == 'nt' else 'clear')

print(f'''   
{G}                                               
  ___ __ _ _ __ _ __ _  _ 
 (_-</ _| '_/ _| '_ \ || |
 /__/\__|_| \__| .__/\_, |
               |_|   |__/      
{W}''')    

def connect_via_usb():
    print(f"""{Y}     
         _   
 _ _ ___| |_ 
| | |_ -| . |
|___|___|___|           
{W}""")
    print(f"""{note} Following Tracks About {G}[{Y}USB{G}]{W}
+----+-------------------+
| {M}ID{W} | {G}Tracking{W}          |
+----+-------------------+
| {B}1{W}  | {Y}Settings{W}          |
| {B}2{W}  | {Y}Developer Options{W} |
| {B}3{W}  | {Y}USB debugging{W}     |
+----+-------------------+
If complete click [Enter]""")
    os.system("pkill scrcpy")
    os.system("adb kill-server")
    os.system("adb start-server")
    os.system("adb devices")
    os.system("scrcpy -d")

def connect_via_wifi(device_ip):
    os.system("pkill scrcpy")
    os.system("adb tcpip 5555")
    os.system(f"adb connect {device_ip}:5555")
    os.system(f"scrcpy -b 2M --max-size 800 --display {device_ip}")
    os.system("scrcpy -e")
def main():
    try:
        print(f"{B}[1] {G}Connect By USB{W}")
        print(f"{B}[2] {G}Connect By TCP/IP{W}")

        choice = input(f"{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}WSL.IQ{R}]─[{G}Enter option [1 - 2]{R}]\n└──╼ {R}❯{Y}❯{G}❯{B} ")
        print(f"{W}")
        if choice == "1":
            connect_via_usb()
        elif choice == "2":
            print(f"""{Y}
     ___
    __H__        _            
     [{Red}:{S}{Y}] ___   _| |_ ___ ___ 
     [{Red}:{S}{Y}]| . | |_   _|  _| . |
     [{Red}.{S}{Y}]|  _|   | | |___|  _|
      V |_|     |_|     |_|         
    {W}""")
            print(f"""{note} Following Tracks About {G}[{Y}IP/TCP{G}] {W}
    +----+--------------------+
    | {M}ID{W} | {G}Tracking{W}           |
    +----+--------------------+
    | {B}1{W}  | {Y}Settings{W}           |
    | {B}2{W}  | {Y}About Phone{W}        |
    | {B}3{W}  | {Y}Status information{W} |
    | {B}4{W}  | {Y}IP arrress{W}         |
    +----+--------------------+""")
            device_ip = input(f"{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}WSL.IQ{R}]─[{G}Enter the IP address of the device{R}]\n└──╼ {R}❯{Y}❯{G}❯{B} ")
            print(f"{W}")
            connect_via_wifi(device_ip)
        else:
            print(f"{ERROR} the Enter option {W}")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
