import urllib.request
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    request = urllib.request.urlopen('https://www.'+ path + 'robots.txt', data=None)
    return request
print(get_robots_txt("ltce.in"))