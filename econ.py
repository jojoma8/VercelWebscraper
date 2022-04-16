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
        p = [[x.get_text()] for x in s.find_all(class_="article__body-text")]
        article_headline = [x.get_text()
                            for x in s.find_all(class_="article__headline")]
        article_subheadline = [x.get_text()
                               for x in s.find_all(class_="article__subheadline")]
        article_description = [x.get_text()
                               for x in s.find_all(class_="article__description")]
        # article_date = [x.get_text()
        #                 for x in s.find_all(class_="article__dateline-datetime")]
        article_image = [s.find_all(class_="article__lead-image")
                         [0].find_all('img')[0]['src']]
        data = {}
        data['content'] = p
        data['article_headline'] = article_headline
        data['article_subheadline'] = article_subheadline
        data['article_description'] = article_description
        data['article_image'] = article_image
        # data['article_date'] = article_date
        data['related_article_link'] = s.find_all(
            class_="related-article")[0].find_all(class_="headline-link")[0]['href']
        data['related_article_text'] = s.find_all(
            class_="related-article")[0].find_all(class_="headline-link")[0].get_text()

        print(data)
        return data
    except Exception as e:
        return {"status": False, "error": e}


read('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
