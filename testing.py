import os

def get_pyfiglet(url, color):
    command = "pyfiglet " + url
    process=os.popen(command)
    results = str(process.read())
    return results

print(get_pyfiglet("VirusGotal",color="blue"))