import sys
import pexpect
import time
import re
import os

#step 1: connect by uart
UARTs = ['ttyUSB_board01', 'ttyUSB_board02']
for device in UARTs:
    print(f"Test {device}")
    uart = os.readlink(f"/dev/{device}")
    child = pexpect.spawn(f"sudo /usr/bin/miniterm /dev/{uart} 115200")
    time.sleep(5)
    child.sendline('\n\n\n\n')
    try:
    # Step 2: check login   
        child.expect("ubuntu login:.*", timeout=60)
        child.sendline('hiptech')
        child.expect("Password:")
        child.sendline('q')
        print("Login success")
    except pexpect.TIMEOUT:
        print("Login timed out")

    #Step 3: checking IP Raspberry pi
        child.expect('IP Address')
        # child.sendline("ip addr show wlan0 | grep 'inet\\b' | awk '{print $2}' | grep -oP '(\\d+\\.){3}\\d+' | head -n 1")        
        child.sendline("/sbin/ip -o -4 addr list wlan0 | awk '{print $4}' | cut -d/ -f1")
    try:
        child.expect('(?i)192.168.*', timeout=60)
        ipv4 = re.findall( r'[0-9]+(?:\.[0-9]+){3}', child.after.decode())              
        print(f"Step 03: Get IP success: {ipv4}")
    except pexpect.TIMEOUT:
        print("Step 03: Get IP failed.")

    # try:
    #     child.expect('Check SSH conect')
    #     child.sendline('ss | grep -i ssh')
    # except:
    #     print("")
