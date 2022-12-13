from urllib.request import urlopen
from datetime import datetime
import json



def scrape(url: str):

    fp = urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return json.loads(mystr)

def username_check(username):
    f = open("accounts.txt", "r")
    data = f.read()
    print(data)
    if username in data:
        return False
    else:
        return True


def add_account(username,pass1):
    now = datetime.now()
    f = open("accounts.txt","a")
    f.write(f"\n\n{now.strftime('%d/%m/%Y %H:%M:%S')}  {username}  {pass1} ")

def number_check(pass1):
    k=0
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in numbers:
        if i in pass1:
            k+=1
    if k>=3:
        return True
    else:
        return False




