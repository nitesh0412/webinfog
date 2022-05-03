""" import os


def get_ip_address(url):
    command = "ping " + url
    process = os.popen(command)
    results = str(process.read())
    results , sep, tail = results.partition('] with 32')
    return results
    

print(get_ip_address("ltce.in")) """


import socket

def get_ip(url):
    
    IP_address = socket.gethostbyname(url)
    results = IP_address
    return results

#print(get_ip("google.com"))