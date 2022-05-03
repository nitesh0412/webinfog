import os

def get_nmap(url):
    command = "nmap "  + url
    process=os.popen(command)
    results = str(process.read())
    return results

#print(get_nmap("ltce.in"))