#!/usr/bin/python
import time;
import calendar;
import os;
import webbrowser;
#Different Selenium library automation tools will be required 
from selenium import webdriver;
import nmap;



# Creating a Menu:

print ("===============================================")
print ("\n Menu")
print ("===============================================")
print ("1. Show Date.")
print ("2. Show Calendar.")
print ("3. Create a file")
print ("4. Create a directory")
print ("5. Logout")
print ("6. Print the ip Addresses of all connected systems.")
print ("7. Search something on google")
print ("8. To reboot your system.")
print ("9. open your whatsapp account using your web browser.")
choice= raw_input("Enter your choice : ")
print ("Received input is : ", choice)


if choice == '1':

 localtime=time.asctime(time.localtime(time.time()))
 print ("Local current time : ",  localtime)

elif choice == '2':

 cal = calendar.month(2018, 6)
 print ("Here is the calendar:")
 print (cal)

elif choice == '3':
 input = raw_input('Enter the file name : ')
 print (input)
 f = open(input,'w+')
 f.close()
 
elif choice == '4':
 input = raw_input('Enter the Directory name : ')
 print (input)
 os.mkdir(input)

elif choice == '5':

 os.system("pkill -KILL -u " + os.getlogin())

elif choice == '6':
 nm = nmap.PortScanner()
 nm.scan('192.168.0.1','*')
 nm.command_line()
 'nmap -sV -sP 192.168.0.1'
 nm.scaninfo()
 {'tcp':{'services': '*', 'method': 'connect'}}

elif choice == '7':

 print ("Searching on google")
 msg=raw_input("type to search")
 webbrowser.open_new_tab('https://www.google.com/search?q='+msg)

elif choice == '8':

 print ("Close all your apps system is rebooting.....") 
 msg1= "achha theek hh thoda time or deta hu"
 time.sleep(2)
 os.system('echo '+msg1+' | festival --tts') 
 msg2= "are apps band kr na"
 time.sleep(3)
 os.system('echo '+msg2+' | festival --tts' )
 os.system('reboot')

elif choice == '9':

 print ("Sending msg on WhatsApp")
 webbrowser.open_new_tab('https://web.whatsapp.com') 
else:

 print ("Unknown Choice...")
