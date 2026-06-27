# macchanger for linux.py
A tiny Python script that generates a random MAC address and applies it to a Linux network interface (hardcoded to "eth0") by calling ifconfig to bring the interface down, set the hardware (MAC) address, then bring it back up. It prints the new MAC.

# macchanger for Windows.py
A tiny Python script that generates a random MAC address and applies it to a Windows network interface (hardcoded to "eth0") by calling ip link to bring the interface down, set the hardware (MAC) address, then bring it back up. It prints the new MAC.
