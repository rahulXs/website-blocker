import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("working hour")
        with open(hosts_path, 'r+') as file:       #working hour
            content= file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("non working hour")
        with open(hosts_path, 'r+') as file:       #non working hour
            content= file.readlines()
            file.seek(0)                           #to seek pointer to begining of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)               #overwrite
            file.truncate()                        #remove everything else

    time.sleep(5)