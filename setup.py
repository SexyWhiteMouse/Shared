#!/usr/bin/env python3.6
import subprocess,os
from pyfiglet import Figlet
from termcolor import colored
from tabletext import to_text


def check_status():
    
    telg = str(subprocess.check_output('systemctl status influxdb | grep Active',shell=True)).split()
    influxdb =str(subprocess.check_output('systemctl status telegraf | grep Active',shell=True)).split()
    
    table = [["InfluxDB","Service:"+influxdb[2]],
         ["Telegraf","Service:"+telg[2]]]
    
    return to_text(table,padding=(2,10))



if __name__=="__main__":
    
    subprocess.call('clear')
   
    
    print(colored(Figlet(font='roman').renderText('Influx_Angie'),"yellow"))
    print(check_status())
    print(input())
    
