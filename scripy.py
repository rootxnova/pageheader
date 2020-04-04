import requests
from time import sleep
from colored import fg, bg, attr
color1 = fg('#8e44ad')
color2 = fg('#c0392b')
color3 = fg('#27ae60')
reset  = attr('reset')
print(color1+'''
  _   _           ____       _       ____   _____   ____  
 | | | |         |  _ \     / \     / ___| | ____| / ___| 
 | |_| |  _____  | |_) |   / _ \   | |  _  |  _|   \___ \ 
 |  _  | |_____| |  __/   / ___ \  | |_| | | |___   ___) |
 |_| |_|         |_|     /_/   \_\  \____| |_____| |____/ 

 >>> CODED BY : ABDELRAHMAN ABOULDAHAB
 >>> GITHUN   : rootxnova
 >>> FACEBOOK : AbdelrahmanAbouldahabOfficial
 
'''+reset)
link = input(color1+'- Extract Header From : ')

y = requests.get(link)
print(color2+'\n'+'[ '+'='*40+'[ H E A D E R S ]'+'='*40+' ]'+'\n')
print(y.headers)
print(color2+'\n'+'[ '+'='*40+'[ H E A D E R S ]'+'='*40+' ]')
print('\n')
print('This Script Closing After 5 Min')
sleep(300)
