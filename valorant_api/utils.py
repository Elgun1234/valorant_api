from urllib.request import urlopen
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
    if username in data:
        return False
    else:
        return True


def add_account(username,pass1):
    f = open("accounts.txt", "+")
    f.write(f"{username}  {pass1} \n \n")

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



