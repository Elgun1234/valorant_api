from urllib.parse import quote, urlencode
from valorant_api.utils import scrape,username_check,add_account,number_check,read_csv
import logging

log = logging.getLogger(__name__)

class valorant:
    def __init__(self):
        self.base = "https://vlrggapi.vercel.app/"

    def get_news(self,keywords):
        url = self.base + "news"
        data = scrape(url)
        keywords = keywords.split(",")

        log.info("Get news starting")

        new_data = []

        for k in keywords:
            for i in data["data"]["segments"]:

                if k in i["title"]:
                    new_data.append(i)
                else:
                    if k in i["description"]:
                        new_data.append(i)
                    else:
                        if k in i["date"]:
                            new_data.append(i)
                        else:
                            if k in i["author"]:
                                new_data.append(i)


        if new_data == [] and keywords != "":
            return []
        elif new_data == []:
            return data["data"]["segments"]
        else:
            return new_data

    def get_rankings(self):
        regions = ["na","eu","ap","oce","kr","mn","gc","br","cn"]


        top_3_dict = {}
        log.info("Get rankings starting")
        for i in regions:
            log.info(f"Selected region = {i}")
            top_3 = []
            url = self.base + "rankings/" + i
            log.info(f"Scraping: {url}")
            data = scrape(url)

            for k in range(3):
                top_3.append(data["data"][k])
            if i not in top_3_dict:
                top_3_dict[i.upper()] = top_3
        log.info("Regions complete")
        for i in top_3_dict:
            for k in range(3):
                top_3_dict[i][k]["vlr link"] = top_3_dict[i][k]["team"].lower().replace(" ","-")
        log.info("Links complete")

        return top_3_dict

    def get_region_rank(self,region):
        dictionary = {}
        r = region.lower()
        url = self.base + "rankings/" + r

        data = scrape(url)
        dictionary[r.upper()]=data
        return dictionary

    def login_checker(self,username,pass1):
        accounts = read_csv("accounts.csv")
        for i in accounts:
            if username == i[1] and pass1 == i[2]:
                log.info("good")
                return True
        else:
            log.info("bad")
            return False
    def create_account(self,username,pass1,pass2):



        if pass1 != pass2:
            return "error 1"

        elif len(username) <5:
            return "error 2"

        elif len(pass1) < 5:
            return "error 3"

        elif number_check(pass1) == False :

            return "error 4"

        elif username_check(username) == False:
            return "error 5"

        else:
            add_account(username,pass1)
            return "successful"



