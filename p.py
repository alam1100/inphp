from time import sleep
import os

def menu():
  os.system('clear')
  os.system('neofetch')
  os.system('figlet R4YH4N 471')
  pil = input('masukan pilihan anda :')
  if pil == '1' or pil == '01':
    os.system('sl')
    os.system('python p.py')
  else:
    print ('keluar tekan ctrl+c')
    sleep(2)
    os.system('cmatrix')
menu()
