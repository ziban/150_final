import socket 
import subprocess 
import os 


#Get the current host_name 
dir_path = str(socket.gethostname())

#Create the necessary directories 
if not os.path.exists(dir_path):
	os.makedirs(dir_path)


os.chdir(dir_path)

#College the traceroute output for messenger 
fb = open('facebook', 'w')
fb_ouput = subprocess.check_output(["traceroute", "www.messenger.com"])
fb.write(fb_ouput)
fb.close()

#Collect the traceroute output for whatsapp
wh = open('whatsapp', 'w')
wh_ouput = subprocess.check_output(["traceroute", "web.whatsapp.com"])
wh.write(wh_ouput)
wh.close()

#Collect the traceroute output for Kik 
kik = open('kik', 'w')
kik_ouput = subprocess.check_output(["traceroute", "www.kik.com"])
kik.write(kik_ouput)
kik.close()

#Collect the traceroute output for Telegram 
tg = open('telegram', 'w')
tg_ouput = subprocess.check_output(["traceroute","-I","www.telegram.org"])
tg.write(tg_ouput)
tg.close()