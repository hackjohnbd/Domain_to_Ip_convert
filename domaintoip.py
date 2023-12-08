#!/user/bin/python2
import socket
import pyfiglet # color package
from termcolor import colored #for color text
print (colored(",,,,,,,,,,Domain,,,,,,,,To,,,,,,,Ip,,,,,,Conveter,,,,,,,,,,,",'red'))
print (colored(",,,,,,,,,,Created,,,,,,,,By,,,,,,John,,,,,,,,,,,,,,",'yellow'))

banner =colored(pyfiglet.figlet_format("Ip converter"), 'green') # use banner
print(banner)
domain_name = input ("input your domain here :")
ip = socket.gethostbyname(domain_name)
print("ip for {}	: {}".format(domain_name,ip))
