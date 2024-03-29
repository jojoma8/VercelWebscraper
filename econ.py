from bs4 import BeautifulSoup as bs
import requests
# import pandas as pd
import re

# notes: replace / with %2f


def read(url):
    try:
        print('url ' + url)
        base_url = f"https://www.economist.com/{url}"
        # base_url = f"https://www.economist.com/leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338"
        print('base_url ' + base_url)
        r = requests.get(
            # 'https://www.economist.com/leaders/2021/03/31/how-europe-has-mishandled-the-pandemic')
            # 'https://www.economist.com/leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
            base_url)
        s = bs(r.text, "html.parser")

        p = [[x.get_text()] for x in s.find_all(class_="article__body-text")]
        article_headline = [x.get_text()
                            # for x in s.find_all(class_="eoacr0f0")][0]
                            for x in s.find_all(class_="e164j1a30")][0]
        # for x in s.find_all(class_="article__headline")]
        article_subheadline = [x.get_text()
                               #    for x in s.find_all(class_="ecgqxun0")][0]
                               for x in s.find_all(class_="e1fr8l080")][0]
        #    for x in s.find_all(class_="article__subheadline")]
        # article_description = [x.get_text()
        #                        for x in s.find_all(class_="article__description")]
        article_date = [x.get_text()
                        # for x in s.find_all(class_="e11vvcj40")][0].strip()
                        for x in s.find_all(class_="e1fl1tsy0")][0].strip()
        #                 for x in s.find_all(class_="article__dateline-datetime")]
        # article_image = [s.find_all(class_="e3y6nua0")[
        article_image = [s.find_all(class_="e12yhaj20")[
            0].find_all('img')[0]['src']][0]
        #                  [0].find_all('img')[0]['src']]
        data = {}
        data['content'] = p
        data['article_headline'] = article_headline
        data['article_subheadline'] = article_subheadline
        # data['article_description'] = article_description
        data['article_image'] = article_image
        data['article_date'] = article_date
        # data['related_article_link'] = [x.find_all(class_="headline-link")[0]['href'] for x in s.find_all(
        #     class_="related-article")]
        data['related_article_link'] = [
            # x.find('a')['href'] for x in s.find_all(class_="ef0oilz0")]
            x.find('a')['href'] for x in s.find_all(class_="eifj80y0")]
        # data['related_article_text'] = [x.find_all(class_="related-article__headline")[0].get_text() for x in s.find_all(
        #     class_="related-article")]
        data['related_article_text'] = [x.get_text()
                                        for x in s.find_all(class_="eifj80y0")]
        # data['related_article_image'] = [x.find_all('img')[0]['src'] for x in s.find_all(
        #     class_="related-article")]
        data['related_article_image'] = [
            x.find('a')['href'] for x in s.find_all(class_="eifj80y0")]

        print(data)
        return data
    except Exception as e:
        return {"status": False, "error": e}


# read('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
# read('europe/2022/05/22/why-turkey-is-blocking-bids-by-sweden-and-finland-to-join-nato')
read('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338')
# read('leaders%2ffor-all-americas-success-in-helping-ukraine-hard-times-lie-ahead%2f21808338')
