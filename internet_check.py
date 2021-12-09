import os
import datetime
import pytz
from config_file_reader import read_config
import xml.etree.ElementTree as ET
from Ui import popupmsg
def check_internet():
    file_exists = os.path.exists('config.xml')
    if file_exists:
        tree = ET.parse('config.xml')
        root = tree.getroot()
        current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        time_stamp=current_time[0:19]
        input_data={}
        for elem in root:
            input_data[elem.tag]=elem.text

        logpath=input_data['Logfolderpath']
        file_name='App_Sanity_Check_logs.txt'
        completeName = os.path.join(logpath, file_name)

        current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        time_stamp=current_time[0:19]
        cmd = os.system('ping google.com>clear.txt')
        os.remove("clear.txt")
        
        if cmd == 0:
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[INFO] Internet is connected\n")
            f.close()
            return True
            
        else:
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[ERROR] Internet is not connected\n")
            f.close()
            return False
    else:
        popupmsg("LTI CAO","Config File is missing")
        exit()     

if __name__ == '__main__':
    check_internet()