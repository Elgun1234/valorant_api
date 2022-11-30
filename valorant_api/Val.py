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

    def get_rankings(self):
        regions = ["na","eu","ap","oce","kr","mn","gc","br","cn"]
        top_3 = []

        for i in regions:
            url = self.base + "rankings/" + i

            data = scrape(url)
            for k in range(3):
                top_3.append(data["data"][k])
        return top_3





