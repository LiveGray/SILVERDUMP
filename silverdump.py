# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os, sys, ssl, io, argparse
import urllib.request
import bs4 as bs

class SILVERDUMP:
    def __init__(self, brand):
        self.brand = brand 

    def SILVERDUMPBanner(self):
        logo = '''\033[1;31m
    ------------[SILVERDUMP]------------    
    ***523 vendors, 2084 passwords***
    Simple tool that was made to search default credentials for routers,
    network devices, web applications and more. Useful for the OSCP.
    \033[1;32m'''
        return logo

def FormatTable(table):
    text=''
    rows=table.find_all('tr')
    text+='\n\033[1;31m[X]  %s\n\033[1;31m' % rows[0].text

    for row in rows[1:]:
        data = row.find_all('td')
        text += '\033[1;32m[->  %s:\033[1;32m \033[1;33m%s\n\033[1;33m' % ((data[0].text),data[1].text)

    return text

def VendorSearch(brand):

    vendor = brand
    urlenc = urllib.parse.quote(vendor)
    url = "https://cirt.net/passwords?criteria=" + urlenc
    vrequest = urllib.request.Request(url)
    gcontext = ssl.SSLContext()
    response = urllib.request.urlopen(vrequest, context=gcontext)
    soup = bs.BeautifulSoup(response,"html.parser")
    print("")
    print("\033[1;32m[*] Searching for credentials... ")

    for links in soup.find_all('table'):
        print(FormatTable(links))
    print('\033[1;31m---------------------------')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', help='Brand of device to check', dest='brand')

    args = parser.parse_args()
    brand = args.brand
    initSILVERDUMP = SILVERDUMP(brand)
    print(initSILVERDUMP.SILVERDUMPBanner())
    print("")
    
    try:
        if brand != " ":
            VendorSearch(brand)
        else:
            pass  

    except KeyboardInterrupt:
        print('\033[1;31m[!] \033[#] Exiting: Ctrl + c detected\n [!] Exiting')
        print("")
        sys.exit(0)
    except EOFError:
        print('\033[1;31m[!] \033[#] Exiting: Ctrl + D detected \n [!] Exiting')
        print("")
        sys.exit(0)

if __name__ == "__main__":
    main()
