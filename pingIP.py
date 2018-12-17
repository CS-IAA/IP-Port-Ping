'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
pingIP.py
Version 1.0
'''

import socket
import time

lst = []
count = 100 #cause start off with 100 in 172.17.2.100
while count <= 254:
    a = '172.17.2.' + str(count) #updates IP address
    lst.append(a)
    count += 1 #increases each count
#print(lst)


port = [80, 22, 20]

# get local machine name
#host = socket.gethostname()

retry = 1
delay = .5
timeout = 1
for x in lst: #goes through the list of IP address one by one
    for y in port: #goes through each port for each IP address
        def isOpen(x, y):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)
                try: #checks to see if able to connect, if error caused, return False
                        s.connect((x, int(y)))
                        s.shutdown(socket.SHUT_RDWR)
                        return True
                except: #connection error, timed error
                        return False
                finally:
                        s.close()

        def checkHost(x, y):
                ipup = False
                for i in range(retry): #how many times to check if port is open on each IP address
                        if isOpen(x, y):
                                ipup = True
                                break
                        else:
                                time.sleep(delay)
                return ipup

        if checkHost(x, y):
            outfile = open("openip.txt", "a")
            file = ("IP:" + x + " Port:" + str(y) + " Open") #writes to a file with IP, Port
            outfile.write(file + '\n')
            outfile.close()
