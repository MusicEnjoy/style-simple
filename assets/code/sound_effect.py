import random 
import os 
num=random.randint(1,3)
print(num)
os.system("clear")
print("\033[1m\033[33m[\033[32m────────────Booting Termux Terminal─────────────\033[33m]\033[0m")


# Condition 

if num == 1:
    os.system("mpv /data/data/com.termux/files/home/style-simple/mp3/Access-Granted.mp3")
elif num==2:
    os.system("mpv /data/data/com.termux/files/home/style-simple/mp3/Jarvis2.mp3")
else :
    os.system("mpv /data/data/com.termux/files/home/style-simple/mp3/JARVIS.mp3")
 
###########################################