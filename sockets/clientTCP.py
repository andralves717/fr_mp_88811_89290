import socket
import signal
import sys
import psutil
import time
from random import *

class colors:
    RED   = "\033[1;31m"
    YELLOW = "\033[1;33m"
    MAGENTA = "\033[1;35m"
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[1;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[1;7m"

def random_color():
    color_pick = randrange(8)
    if color_pick < 1:
        return colors.RED
    elif color_pick < 2:
        return colors.YELLOW
    elif color_pick < 3:
        return colors.MAGENTA
    elif color_pick < 4:
        return colors.BLUE
    elif color_pick < 5:
        return colors.CYAN
    elif color_pick < 6:
        return colors.GREEN
    elif color_pick < 7:
        return colors.BOLD
    elif color_pick < 8:
        return colors.REVERSE
    else:
        return colors.RESET

def color_per(per):
    if per < 40:
        return colors.GREEN + str(per)
    elif per < 80:
        return colors.YELLOW + str(per)
    else:
        return colors.RED + str(per)

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

async def sleep(delay):
    await asyncio.sleep(delay)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:
    try:
        time.sleep(3)
        message = random_color() +"Percentagem de Memoria usada:"
        message = message + colors.RESET + "\t\t" + color_per(psutil.virtual_memory()[2]) + "%\n"
        message = message + random_color() + "Percentagem de utilização do CPU:"
        message = message + colors.RESET + "\t" + color_per(psutil.cpu_percent(interval=1)) + "%\n"
        print(message)
        message = message.encode()
        if len(message)>0:
            sock.send(message)
            response = sock.recv(4096).decode()
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)

