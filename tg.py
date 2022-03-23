from bs4 import BeautifulSoup as bs
import requests

# msg = "hello world"
# print(msg)


def telegram(username):
    try:
        base_url = f"https://telegram.dog/{username}"
        r = requests.get(base_url).text
        # r = "hello world"
        # print(r)
        soup = bs(r, "html.parser")
        members_count = soup.find('div', class_="tgme_page_extra").text
        print(members_count)

        data = {}
        data['content'] = members_count
        return data
    except Exception as e:
        return {"status": False, "error": e}


telegram("sprojects")
