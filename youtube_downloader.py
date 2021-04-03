from termcolor import colored
from pytube import *

logo = """


Y88b   d88P                 888             888                                            
 Y88b d88P                  888             888                                            
  Y88o88P                   888             888                                            
   Y888P   .d88b.  888  888 888888 888  888 88888b.   .d88b.                               
    888   d88""88b 888  888 888    888  888 888 "88b d8P  Y8b                              
    888   888  888 888  888 888    888  888 888  888 88888888                              
    888   Y88..88P Y88b 888 Y88b.  Y88b 888 888 d88P Y8b.                                  
8888888b.  "Y88P"   "Y88888  "Y888  "Y88888888888P"   "Y8888          888                  
888  "Y88b                                 888                        888                  
888    888                                 888                        888                  
888    888  .d88b.  888  888  888 88888b.  888  .d88b.   8888b.   .d88888  .d88b.  888d888 
888    888 d88""88b 888  888  888 888 "88b 888 d88""88b     "88b d88" 888 d8P  Y8b 888P"   
888    888 888  888 888  888  888 888  888 888 888  888 .d888888 888  888 88888888 888     
888  .d88P Y88..88P Y88b 888 d88P 888  888 888 Y88..88P 888  888 Y88b 888 Y8b.     888     
8888888P"   "Y88P"   "Y8888888P"  888  888 888  "Y88P"  "Y888888  "Y88888  "Y8888  888     


"""

print(colored(logo, 'green'))
url = input("Paste the url you want to download: ")
destination = input("Where do you want to download: ")

def download(url):
    yt = YouTube(str(url))
    vid = yt.streams.get_highest_resolution()
    vid.download(str(destination))
    print(f"{yt.title} is suscefully downloaded at path {destination}")

if input('Do you want to download, y or n: ') == 'y':
    download(url)