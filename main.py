from general import *
#from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import os



def get_pyfiglet(url):
    command = "pyfiglet " + url
    process=os.popen(command)
    results = str(process.read())
    return results

print(get_pyfiglet("webinfog"))                          

print("Welcome to WebInfoG :)")
print("This Tool is use for education purpose ")

val = input("Project name :- ")
url = input("Enter your domain :- ")


ROOT_DIR = val
create_dir(ROOT_DIR)

def gather_info(url):
    #domain_name = get_domain_name(url)
    nmap = get_nmap(url)
    whois = get_whois(url)
    robots_txt = get_robots_txt(url)
    ip_address = get_ip(url)
    create_report(val, url, whois, ip_address, nmap,  robots_txt)

def create_report(val, url, whois, ip_address, nmap, robots_txt):
    project_dir = ROOT_DIR + '/' 
    create_dir(project_dir)
   # write_file(project_dir + 'url.txt', url)
    write_file(project_dir + 'ip_address.txt', ip_address)
    write_file(project_dir + 'nmap.txt', nmap)
    write_file(project_dir + 'whois.txt', whois)
    write_file(project_dir + 'robots.txt', robots_txt)
    #write_file(project_dir + 'domain_name.txt', domain_name)


gather_info(url)

