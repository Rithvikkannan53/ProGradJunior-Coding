Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Kannan\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.chdir("D:\\")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.chdir("D:\\")
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'D:\\'
>>> os.chdir("C:\\")
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> os.mkdir("Python Projects")
>>> 
>>> 
>>> file = open ("demo.txt","x")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    file = open ("demo.txt","x")
PermissionError: [Errno 13] Permission denied: 'demo.txt'
>>> os.chdir("C:\\Users\\Kannan\\Desktop\\Py")
>>> file = open ("demo.txt","x")
>>> file = open ("demo.txt","r")
>>> if file:
	print("File opened successfully)
	      
SyntaxError: EOL while scanning string literal
>>> file = open ("demo.txt","r")
>>> if file:
	print("File opened successfully")
	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 