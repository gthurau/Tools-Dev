"""
Information Gathering Tool

Written by Gabe Thurau

Description of Tool
    The purpose of this tool is to be run on a remote server or client machine and gather as much information about the specs of the machine, running processes, 
    network info, and any additional information needed. 


Last Updated - 23/01/2022 - Created Project and Outlined the functions wanted

"""

"""
Outline / Pseudo-code

1. Base System Information
    - OS (Type, Version, etc.)
    - Hostname
    - User Running Code
    - 


"""


### Import Libaries ###

import subprocess
import sys
import platform
from datetime import datetime
from tabulate import tabulate

### Install Needed Libaries ###

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip3", "install", package])

try:
    install("psutil")
except:
    print("PSUtil already installed...")

import psutil


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_basesytem_info():
    uname = platform.uname()
    system = uname.system
    release = uname.release
    version = uname.version
    machine = uname.machine
    hostname = uname.node
    


get_basesytem_info()


