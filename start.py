#!/usr/bin/python3
# This Programm write by Mr.nope
# Instagram-Profile-Downloader 1.2

import os
import time
import sys
import platform
try:
    import instaloader
except ImportError:
    os.system("pip3 install instaloader")
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")

system = platform.uname()[0]
End = '\033[0m'
opt = F"\nEnter Instagram " + Fore.GREEN + "UserName: " + End
down_help = """
Instagram-Profile-Downloader:
                              --menu | Start Menu
                              -i <USERNAME>
                              --help
                              """

banner = Fore.CYAN + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWWNNNXXXXXXXXXXXXXXXNNWWMMMMMMMMMMMMM
MMMMMMMMMWXOkdoolllllllllllllllllllodxOKWMMMMMMMMM
MMMMMMMWKdc:codxxxkkkkkkkkkkkkxxxxddlc:cdKWMMMMMMM
MMMMMMNkc:cxKNWWMMMMMMMMMMMMMMMMMWWNX0xc:ckNMMMMMM
MMMMMWOc;l0WMMMMMMMMMMWWWWWWMMMMW0xdxKN0l:cOWMMMMM
MMMMMXd;:kWMMMMMMMWX0kxddddxk0XWNxc:cOWNk::dXMMMMM
MMMMMKl;c0MMMMMMN0dl::cllllc::ldOK0OKNWWOc:oKMMMMM
MMMMMKl;l0MMMMWXxc:lx0XNNNNX0xl:cdKWMMMW0l:oKMMMMM """ + Fore.RED + "Version: " + Fore.YELLOW + "1.2" + Fore.CYAN + """
MMMMMKl:lKMMMMXxccdKWMMMMMMMMWKd::dXMMMW0l:lKMMMMM
MMMMMKl:oKMMMW0lcoKWMMMMMMMMMMWKo:cOWMMM0l:lKMMMMM
MMMMMKocoKMMMWOlcxXMMMMMMMMMMMMXd:ckWMMM0l:lKMMMMM
MMMMMKdcdKMMMWKdlo0WMMMMMMMMMMWOl:o0WMMW0l:lKMMMMM
MMMMMKdldKMMMMW0dodOXWWMMMMMWXklclOWMMMW0l:oKMMMMM
MMMMMXxodKMMMMMWXkdodkO0000OxollxKWMMMMWOl:oKMMMMM
MMMMMNkoxKWMMMMMMWX0kxdddddddxOKNMMMMMMWOc:dXMMMMM
MMMMMW0xxONMMMMMMMMMWNXXXXXXNWMMMMMMMMMXd:cxNMMMMM
MMMMMMXOxk0NWMMMMMMMMMMMMMMMMMMMMMMMMWKdccdKWMMMMM
MMMMMMWNKOO0KXNNNNNNNNNNNNNNNNNXXXK0OxlclxXWMMMMMM
MMMMMMMMWNXK0000000000000OOOOkkxxddooodkKNMMMMMMMM
MMMMMMMMMMMWWNNNNNNXXXXXXXXXKKKK0000KXWWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""" + End
def title():
    if system == 'Linux':
        os.system("printf '\033]2;Instagram-Profile-Downloader\a'")
    elif system == 'Windows':
        os.system("title Instagram-Profile-Downloader")
    else:
        print("\nPlease, Run This Programm on Windows, Linux, MacOS!\n")
        sys.exit()
def ext():
    cls()
    print(Fore.GREEN + "Exiting..." + End)
    sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPlease, Run This Programm on Windows, Linux, MacOS!\n\n")
        sys.exit()
def arg():
    if sys.argv[1] == '-i':
        title()
        user = sys.argv[2]
        start = instaloader.Instaloader()
        print("\n")
        start.download_profile(user, profile_pic_only=True)
        print("\n")
        sys.exit()
    elif sys.argv[1] == '--help':
        print(down_help)
        sys.exit()
    elif sys.argv[1] == '--menu':
        main()
    else:
        print("\nArgument Not Found!\n")
        sys.exit()
def main():
    title()
    start = instaloader.Instaloader()
    cls()
    print(banner)
    print("\nUsage: Ctrl + D To Exit!\n")
    user = input(opt)
    time.sleep(1)
    print("\n")
    start.download_profile(user, profile_pic_only=True)
    print("\n")
    try1()
def try1():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        main()
    elif try_again == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
if __name__ == '__main__':
    try:
        try:
            try:
                arg()
                main()
            except IndexError:
                print("\npython3 start.py --help\n")
                sys.exit()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()