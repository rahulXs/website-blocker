## Website Blocker
Python script to run as background process and block certain websites for a specified time duration. <br>
It may be used to boost productivity by blocking certain websites in working hour.

#### Host File Location ( file name: hosts, variable in script: hosts_path)
-For windows:       c:\windows\system32\drivers\etc\hosts

-For Linux or Mac:  /etc/hosts

#### To run python script as background process
##### For windows
change extension of file to .pyw <br>
create a new task in task scheduler to run the python script. 

##### For Linux
sudo crontab -e <br> then add the following lines at the end of file: @reboot python3 path-of-script
