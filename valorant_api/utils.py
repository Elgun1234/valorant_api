from urllib.request import urlopen
import json



def scrape(url: str):

    fp = urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return json.loads(mystr)