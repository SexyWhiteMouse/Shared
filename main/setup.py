#!/usr/bin/env python3.6
import subprocess,os
from pyfiglet import Figlet
from termcolor import colored

if __name__=="__main__":
    
    subprocess.call("clear")
    print(colored(Figlet(font='roman').renderText('Influx_Angie'),"yellow"))
    print(input())
    
