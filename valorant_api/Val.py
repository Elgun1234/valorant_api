from urllib.parse import quote, urlencode
from valorant_api.utils import scrape

class valorant:
    def __init__(self):
        self.base = "https://vlrggapi.vercel.app/"

    def get_news(self,keywords):
        url = self.base + "news"
        data = scrape(url)
        keywords = keywords.split(",")



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

d = valorant()
print(d.get_news("100,Riot"))