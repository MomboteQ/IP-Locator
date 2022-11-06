################################
##                            ##
##    Created by: MomboteQ    ##
##                            ##
################################

# MODULES
from sys import argv
from getopt import getopt, GetoptError

from colorama import Fore, Style, init
from textwrap import dedent

from os import name as system_name
from os import system

from requests import post
from json import loads


# FUNCTIONS

def logo():
    print('''
                        ██┐██████┐ 
                        ██│██┌──██┐
                        ██│██████┌┘
                        ██│██┌───┘ 
                        ██│██│     
                        └─┘└─┘     '''.replace('█', f'{Fore.LIGHTWHITE_EX}█{Fore.LIGHTBLUE_EX}'))
    print(dedent(f'''
    ██┐      ██████┐  ██████┐ █████┐ ████████┐ ██████┐ ██████┐ 
    ██│     ██┌───██┐██┌────┘██┌──██┐└──██┌──┘██┌───██┐██┌──██┐
    ██│     ██│   ██│██│     ███████│   ██│   ██│   ██│██████┌┘
    ██│     ██│   ██│██│     ██┌──██│   ██│   ██│   ██│██┌──██┐
    ███████┐└██████┌┘└██████┐██│  ██│   ██│   └██████┌┘██│  ██│
    └──────┘ └─────┘  └─────┘└─┘  └─┘   └─┘    └─────┘ └─┘  └─┘
    {Fore.LIGHTBLUE_EX}┌─────────────────────────────────────────────────────────┐
    {Fore.LIGHTBLUE_EX}│                     {Fore.LIGHTWHITE_EX}IP Locator Tool                     {Fore.LIGHTBLUE_EX}│
    {Fore.LIGHTBLUE_EX}└─────────────────────────────────────────────────────────┘
    {Fore.LIGHTBLUE_EX}┌───────────────────────────┐ ┌───────────────────────────┐
    {Fore.LIGHTBLUE_EX}│   {Fore.LIGHTBLUE_EX}Created by: {Fore.LIGHTWHITE_EX}@MomboteQ{Fore.LIGHTBLUE_EX}   │ {Fore.LIGHTBLUE_EX}│       {Fore.LIGHTYELLOW_EX}Version: {Fore.LIGHTWHITE_EX}1.0{Fore.LIGHTBLUE_EX}        │
    {Fore.LIGHTBLUE_EX}└───────────────────────────┘ └───────────────────────────┘
    {Fore.LIGHTBLUE_EX}┌─────────────────────────────────────────────────────────┐
    {Fore.LIGHTBLUE_EX}│               {Fore.LIGHTWHITE_EX}https://MomboteQ.github.io                {Fore.LIGHTBLUE_EX}│
    {Fore.LIGHTBLUE_EX}└─────────────────────────────────────────────────────────┘{Style.RESET_ALL}
    '''.replace('█', f'{Fore.LIGHTWHITE_EX}█{Fore.LIGHTBLUE_EX}')))

def help():
    logo()

    print(Fore.LIGHTWHITE_EX + dedent('''
    Usage: IP-Locator.py [-h] [-i IP]

    Arguments:
      -h, --help                  Show this help message and
                                  exit.
      -i IP, --ip IP              IP to locate.
    '''))

def clear():
    system('cls' if system_name == 'nt' else 'clear')

def main(argv):
    ip = None

    try:
        opts, args = getopt(argv, 'hi:', ['help', 'ip ='])

    except GetoptError as e:
        logo()
        print(f'\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}✗{Fore.LIGHTWHITE_EX}] {str(e).capitalize()}\n')
        return

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            return

        if opt in ('-i', '--ip'):
            logo()

            locate_ip(arg)
            return

    help()

def locate_ip(ip):
    r = post(f'http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,zip,lat,lon,isp,org,reverse,mobile,proxy,hosting')

    json = loads(r.text)
    
    if json['status'] == 'success':
        isp = json['isp']
        org = json['org']
        host = json['reverse']
        mobile = json['mobile']
        proxy = json['proxy']
        hosting = json['hosting']

        continent = json['continent']
        country = json['country']
        region = json['regionName']
        city = json['city']
        zip = json['zip']
        lat = json['lat']
        lon = json['lon']
        map = f'https://www.openstreetmap.org/#map=17/{lat}/{lon}'

        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] ISP : {Fore.LIGHTBLUE_EX + isp + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Organization : {Fore.LIGHTBLUE_EX + org + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Hostname : {Fore.LIGHTBLUE_EX + host + Style.RESET_ALL}\n')

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Mobile : {Fore.LIGHTBLUE_EX + str(mobile) + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Proxy : {Fore.LIGHTBLUE_EX + str(proxy) + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Hosting : {Fore.LIGHTBLUE_EX + str(hosting) + Style.RESET_ALL}\n')

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Continent : {Fore.LIGHTBLUE_EX + continent + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Country : {Fore.LIGHTBLUE_EX + country + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Region : {Fore.LIGHTBLUE_EX + region + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] City : {Fore.LIGHTBLUE_EX + city + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] ZIP : {Fore.LIGHTBLUE_EX + zip + Style.RESET_ALL}')
        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Map : {Fore.LIGHTBLUE_EX + map + Style.RESET_ALL}\n')

    else:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Enter valid IP!\n')

if __name__ == '__main__':
    init()
    
    clear()

    main(argv[1:])