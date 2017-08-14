from wordsegment import segment, clean
import urllib
import string
import re
test = urllib.unquote("https://si_tes.google.com/site/checkpointinfo2017/?settings%3Ftab=security").decode('utf8')

def segment_url(url):
    if url.startswith("https"):
        url = url[8:]
    elif url.startswith("http"):
        url = url[7:]
    list_split = re.split('[_\W]', url)
    return list_split

print segment_url(test)