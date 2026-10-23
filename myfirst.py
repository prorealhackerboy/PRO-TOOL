import socket, requests
from colorama import Fore, Style
import re

# Warning fix ke liye r""" use kiya hai
banner = r"""
  ____  ____   ___    _____ ___   ___  _     
 |  _ \|  _ \ / _ \  |_   _/ _ \ / _ \| |    
 | |_) | |_) | | | |   | || | | | | | | |    
 |  __/|  _ <| |_| |   | || |_| | |_| | |___ 
 |_|   |_| \_\\___/    |_| \___/ \___/|_____|
"""

print(Fore.GREEN + banner + Style.RESET_ALL)
print(Fore.CYAN + "=== V4 ULTIMATE TOOL - Created by YOU ===" + Style.RESET_ALL)

url = input(Fore.YELLOW + "\nWebsite daal: " + Style.RESET_ALL).replace("https://","").replace("http://","").strip()

try:
    ip = socket.gethostbyname(url)
    print(Fore.GREEN + f"\n[✓] IP Mila: {ip}" + Style.RESET_ALL)
    
    print(Fore.WHITE + "[+] Website Info nikal raha hu..." + Style.RESET_ALL)
    r = requests.get("https://" + url, timeout=5)
    
    print(Fore.GREEN + f"[✓] Status {r.status_code} - LIVE Hai!" + Style.RESET_ALL)
    
    # Title nikalna
    title = re.search(r'<title>(.*?)</title>', r.text, re.IGNORECASE)
    if title:
        print(Fore.CYAN + f"[✓] Title: {title.group(1)}" + Style.RESET_ALL)
    
    # Chota Port Scanner
    print(Fore.WHITE + "\n[+] Port Scan kar raha hu (80, 443)..." + Style.RESET_ALL)
    for port in [80, 443]:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(Fore.GREEN + f"[✓] Port {port} OPEN Hai" + Style.RESET_ALL)
        except:
            print(Fore.RED + f"[X] Port {port} CLOSED" + Style.RESET_ALL)
        s.close()

except Exception as e:
    print(Fore.RED + f"[X] Error: {e}" + Style.RESET_ALL)

