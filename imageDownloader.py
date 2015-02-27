"""
Kunal Chavhan
Github username: techcraze
Email: techcraze5@gmail.com
Date: 26/2/2015
Code description: It is an open source code which uses URLLIB module to download images from www.hdwallpapers.in.
                  
"""


import urllib
from bs4 import BeautifulSoup
import os
import re

def download(search):
    urlSearch = "http://www.hdwallpapers.in/search.html?q="+search
    #os module function to get current working directory
    dir = os.getcwd()
    print "searching for keyword "+search+" in hdwallpapers.in"
    url = urllib.urlopen(urlSearch)
    soup = BeautifulSoup(url.read())
    img_urls = []
    for r in soup.findAll('a'):
        img_urls.append("http://www.hdwallpapers.in"+r.get('href'))
    
    if not img_urls:
        print "Sorry no result found for keyword "+search
        return
    
    open = urllib.urlopen(img_urls[29])
    
    
    manchav_soup=BeautifulSoup(open.read())
    for x in manchav_soup.findAll('a',href=re.compile(r'.*walls.*')):
        imgUrl = "http://www.hdwallpapers.in"+x.get('href')
        try:
            imgData = urllib.urlopen(imgUrl)
            filename = imgUrl.split('/')[-1]
            print "Downloading image from "+imgUrl
            print "Please wait.."
            urllib.urlretrieve(imgUrl,filename)
            print filename+" is downloaded in "+dir
            
            break
        except:
            print "error"
    
download(" ")
   
