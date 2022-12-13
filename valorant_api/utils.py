from urllib.request import urlopen
from datetime import datetime
import json
import logging
import csv

log = logging.getLogger(__name__)



def scrape(url: str):

    fp = urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return json.loads(mystr)

def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            csv_contents.append(row)
    return csv_contents
def username_check(username):
    data = read_csv("accounts.csv")
    log.info(data)
    if data == [[]]:
        return True
    for i in data:
        if i[1] == username:
            return False
        else:
            return True





def add_account(username,pass1):
    now = datetime.now()
    f = open("accounts.csv","a")
    f.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')},{username},{pass1}\n")

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




