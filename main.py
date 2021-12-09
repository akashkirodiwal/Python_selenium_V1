
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import pytz 
import os
from os import error
from internet_check import check_internet
from config_file_reader import read_config
from mail_send_template import send_mail
from Ui import popupmsg


##Check the connection
connectivity_status=check_internet()
if connectivity_status==False:
    popupmsg("LTI CAO","No Internet Connection")
    exit()
else:
    pass
# If connection is available
while connectivity_status:
    #Check for the correctness of inputs
    input_data,flags=read_config()
    try:    
        if flags==1:
            message="Dear User,\nEnter the correct URL"
            send_mail(input_data["tomail"],"Input Error",message) 
            current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
            time_stamp=current_time[0:19]
            logpath=input_data['Logfolderpath']
            file_name='log.txt'
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:User Notified on Input Error\n")
            f.close()
            raise error('Enter Correct URL')
        elif flags==2:
            raise error('Enter Correct Email ID')
        elif flags==3:
            raise error('Enter Correct URL and Email ID')
        else:
            pass
        
    except error as e:
        popupmsg("LTI CAO",str(e))
        exit(str(e)) 

    # Check the Power Automate URL 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  
    driver=webdriver.Chrome(executable_path="E:\soft\chromedriver_win32\chromedriver.exe",options=options)
    
    try:
        driver.get(input_data['AppURL'])
        current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        time_stamp=current_time[0:19]
        logpath=input_data['Logfolderpath']
        file_name='log.txt'
        completeName = os.path.join(logpath, file_name)
        f = open(completeName, "a")
        f.write(f"[{time_stamp}]:Power Automate URL Loaded Successfully.\n")
        f.close()
    except error as e:
        message="Dear User,\nPower Automate URL Loading Failed"
        send_mail(input_data["tomail"],"Power Automate URL Error",message) 
        current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        time_stamp=current_time[0:19]
        logpath=input_data['Logfolderpath']
        file_name='log.txt'
        completeName = os.path.join(logpath, file_name)
        f = open(completeName, "a")
        f.write(f"[{time_stamp}]:User Notified on Power Automate URL Error\n")
        f.close()
        print(str("Power Automate URL not Loaded Successfully"))

    # Check Products Tab
    try:
        
        prod_tab=driver.find_element_by_xpath("//*[@id='bapi-header']/div/div[4]/ul[1]/li[1]/button")
        if prod_tab.is_enabled():
            prod_tab.click()
            prod_tab_submenu=driver.find_element_by_xpath("//*[@id='products']/li[1]/a")
            val=prod_tab_submenu.is_enabled()
            prod_tab_submenu.click()
            
            if val==False:
                message="Dear User,\nPower Automate Product tab Loading Failed"
                send_mail(input_data["tomail"],"Product Tab Error",message) 
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:User Notified on Product Tab Error\n")
                f.close()
                raise error("Power Automate Product tab Loading Failed")
            else:
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:Product Tab Loaded Successfully.\n")
                f.close()
                
    except error as e:
        print(str(e))

    # Check the Capabilities Tab
    try:
        
        cap_tab=driver.find_element_by_xpath("//*[@id='bapi-header']/div/div[4]/ul[1]/li[2]/button")
        if cap_tab.is_enabled():
            cap_tab.click()
            cap_tab_submenu=driver.find_element_by_xpath("//*[@id='capabilities']/li[1]/a")
            val_2=cap_tab_submenu.is_enabled()
            cap_tab_submenu.click()
            
            if val_2==False:
                message="Dear User,\nPower Automate Capabilities tab Loading Failed"
                send_mail(input_data["tomail"],"Capabilties Tab Error",message) 
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:User Notified on Capabilities Tab Error\n")
                f.close()
                raise error("Power Automate Capabilities tab Loading Failed")
            else:
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:Capabilties Tab Loaded Successfully.\n")
                f.close()
                
    except error as e:
        print(str(e))

    # Check the Pricing Tab
    try:
        
        price_tab=driver.find_element_by_xpath("//*[@id='bapi-header']/div/div[4]/ul[1]/li[3]/a")
        val_3=price_tab.is_enabled()
        
            
        if val_3==False:
            message="Dear User,\nPower Automate Pricing tab Loading Failed"
            send_mail(input_data["tomail"],"Pricing Tab Error",message) 
            current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
            time_stamp=current_time[0:19]
            logpath=input_data['Logfolderpath']
            file_name='log.txt'
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:User Notified on Pricing Tab Error\n")
            f.close()
            raise error("Power Automate Pricing tab Loading Failed")
        else:
            price_tab.click()
            current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
            time_stamp=current_time[0:19]
            logpath=input_data['Logfolderpath']
            file_name='log.txt'
            completeName = os.path.join(logpath, file_name)
            f = open(completeName, "a")
            f.write(f"[{time_stamp}]:Pricing Tab Loaded Successfully.\n")
            f.close()
                
    except error as e:
        print(str(e))

    # Check the Learn Tab
    try:
        
        learn_tab=driver.find_element_by_xpath("//*[@id='bapi-header']/div/div[4]/ul[1]/li[5]/button")
        if learn_tab.is_enabled():
            learn_tab.click()
            learn_tab_submenu=driver.find_element_by_xpath("//*[@id='learn']/li[1]/a")
            val_2=learn_tab_submenu.is_enabled()
            learn_tab_submenu.click()
            
            if val_2==False:
                message="Dear User,\nPower Automate Learn tab Loading Failed"
                send_mail(input_data["tomail"],"Learn Tab Error",message) 
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:User Notified on Learn Tab Error\n")
                f.close()
                raise error("Power Automate Learn tab Loading Failed")
            else:
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:Learn Tab Loaded Successfully.\n")
                f.close()
                message="Dear User,\nApplication Sanity Check on Power Automate URL succeeded."
                send_mail(input_data["tomail"],"Application Sanity Check Success",message) 
                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                time_stamp=current_time[0:19]
                logpath=input_data['Logfolderpath']
                file_name='log.txt'
                completeName = os.path.join(logpath, file_name)
                f = open(completeName, "a")
                f.write(f"[{time_stamp}]:User Notified on Power Automate URL Sanity Check succeeded.\n")
                f.close()
                
    except error as e:
        print(str(e))

    driver.quit()
    break
        





