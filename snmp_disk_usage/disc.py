#!/usr/bin/env python3
import os, sys

used_command = "snmpget -v 2c -c public "+sys.argv[1]+" .1.3.6.1.2.1.25.2.3.1.6.$(snmpwalk -v 2c -c public "+sys.argv[1]+" .1.3.6.1.2.1.25.2.3.1.3 | grep C: | awk '{print $1}' | awk -F'.' '{print $NF}') | awk '{print $NF}')" 
USED = int(os.popen(used_command).read())

total_command = "snmpget -v 2c -c public "+sys.argv[1]+" .1.3.6.1.2.1.25.2.3.1.5.$(snmpwalk -v 2c -c public "+sys.argv[1]+" .1.3.6.1.2.1.25.2.3.1.3 | grep C: | awk '{print $1}' | awk -F'.' '{print $NF}') | awk '{print $NF}')" 
TOTAL =  int(os.popen(total_command).read())

return ((TOTAL - USED) / TOTAL) * 100
