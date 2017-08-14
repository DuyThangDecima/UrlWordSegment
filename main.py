from wordsegment import segment, clean
import urllib
import string
test = urllib.unquote("https://sites.google.com/site/checkpointinfo2017/?settings%3Ftab=security").decode('utf8')

print string.punctuation
def segment_url(url):
    if url.startswith("https"):
        url = url[8:]
    elif url.startswith("http"):
        url = url[7:]




print segment('facebokdsdsdsdupdate')