import xml.etree.ElementTree as ET
import validators
import os
import datetime
import pytz
import re
from Ui import popupmsg


def read_config():
    file_exists = os.path.exists('config.xml')
    if file_exists:
        tree = ET.parse('config.xml')
        root = tree.getroot()
        current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        time_stamp=current_time[0:19]
        input_data={}
        for elem in root:
            input_data[elem.tag]=elem.text

        #print(input_data)

        url=input_data['AppURL']
        to_mail=input_data['tomail']
        logpath=input_data['Logfolderpath']
        file_name='App_Sanity_Check_logs.txt'
        flag=0
        if validators.url(url) and bool(re.search("powerautomate",url)):
            
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[INFO] URL is correct\n")
            f.close()
        else:
            flag+=1
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[ERROR] URL is incorrect\n")
            f.close()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if(re.fullmatch(regex,to_mail)):
            
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[INFO] Email ID is correct\n")
            f.close()
        else:
            flag+=2
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:[ERROR] Email ID is incorrect\n")
            f.close()
        return input_data,flag
    else:
        popupmsg("LTI CAO","Config File is missing")
        exit()

