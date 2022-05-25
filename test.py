from bs4 import BeautifulSoup as bs
import requests

# msg = "hello world"
# print(msg)


def scraper(url):
    try:
        # base_url = f"https://www.economist.com/{url}"
        base_url = f"https://www.economist.com/leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338"
        r = requests.get(base_url).text
        # r = "hello world"
        # print(r)
        s = bs(r, "html.parser")
        p = [[x.get_text()] for x in s.find_all(class_="article__body-text")]
        # print(p)

        data = {}
        data['content'] = p[0]
        # print(data)
        # return soup
        return data
    except Exception as e:
        return {"status": False, "error": e}


scraper('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
