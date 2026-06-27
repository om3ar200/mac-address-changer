#for Windows

import subprocess
import random
def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))
new_mac = generate_random_mac()
interface = "eth0"
subprocess.call(f"ip link {interface} down", shell=True)
subprocess.call(f"ip link {interface} address {new_mac}", shell=True)
subprocess.call(f"ip link {interface} up", shell=True)
print(f"the new MAC address is: {new_mac}")
