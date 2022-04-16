from bs4 import BeautifulSoup as bs
import requests
# import pandas as pd
import re

# notes: replace / with %2f


def read(url):
    try:
        base_url = f"https://www.economist.com/{url}"
        r = requests.get(
            # 'https://www.economist.com/leaders/2021/03/31/how-europe-has-mishandled-the-pandemic')
            # 'https://www.economist.com/leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
            base_url)
        s = bs(r.text, "html.parser")
        p = [x.get_text() for x in s.find_all(class_="article__body-text")]
        article_headline = s.find_all(class_="article__headline")
        data = {}
        data['content'] = p
        data['article_headline'] = article_headline
        print(p)
        return data
    except Exception as e:
        return {"status": False, "error": e}


read('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
