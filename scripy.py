import requests
from time import sleep
from colored import fg, bg, attr
color1 = fg('#8e44ad')
color2 = fg('#c0392b')
color3 = fg('#27ae60')
print(color1+'''
  _   _           ____       _       ____   _____   ____  
 | | | |         |  _ \     / \     / ___| | ____| / ___| 
 | |_| |  _____  | |_) |   / _ \   | |  _  |  _|   \___ \ 
 |  _  | |_____| |  __/   / ___ \  | |_| | | |___   ___) |
 |_| |_|         |_|     /_/   \_\  \____| |_____| |____/ 

 >>> CODED BY : ABDELRAHMAN ABOULDAHAB
 >>> GITHUN   : rootxnova
 >>> FACEBOOK : AbdelrahmanAbouldahabOfficial
 
''')
link = input(color1+'- Extract Header From : ')

y = requests.get(link)
print('[ '+'='*40+'HEADER'+'='*40+' ]'+'\n')
print(y.headers)
print('\n'+'[ '+'='*40+'HEADER'+'='*40+' ]')

sleep(1000)
