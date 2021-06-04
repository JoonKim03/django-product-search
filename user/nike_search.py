import requests
from bs4 import BeautifulSoup
import json

class search():

    def start_session():
        # USER_AGENTS = load_user_agent()
        BASE_URL = 'https://www.nike.com/kr/ko_kr'
        user_agent = "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
        session = requests.Session()
        session.verify = False
        session.headers = {
            'User-Agent': user_agent,
            'Referer': BASE_URL,
            'x-ig-capabilities': '36oD',
            'Cache-Control': 'no-cache',
            'Connection': 'close',
            # 'Cookie': cookie
            'Accept': '*/*',
            'Accept-Eencoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
            'cache-control': 'no-cache',
            'dnt': '1',
            'pragma': 'no-cache',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        return session

    def search_item(product_code):
        # product_code = 'DJ2657-104'
        product_code = str(product_code).upper().lstrip().rstrip()

        #headers = {
        #    "user-agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
        #}

        session = search.start_session()
#        url = 'https://www.nike.com/kr/ko_kr/search?q=%s' % (product_code)
#        data = session.get(url)
#        soup = BeautifulSoup(data.text)

        # json 파일 읽기
        with open('nike_product_code.json') as f:
            data = json.loads(f.read())

        product_url = data[product_code]

        # 해당 품번의 제품 링크 찾기
#        href_list = soup.find_all('a', href=True)
#        for i in range(0, len(href_list)):
#            val = href_list[i]['href']
#            if ('/kr/ko_kr/' in val) and (product_code in val) and ('search' not in val):
#                product_url = 'https://www.nike.com' + val

        # 이미지 찾기
        data = session.get(product_url)
        soup = BeautifulSoup(data.text)

        product_img_list = []
        img_list = soup.find_all('img')

        for i in range(0, len(img_list)):
            val = img_list[i]['src']
            if (product_code in val) and ('static-breeze' in val) and ('thumbnail' not in val) and ('option' not in val) and (val[-7:] == 'gallery'):
                if val not in product_img_list:
                    product_img_list.append(val)

        # 제품 이름
        product_name = soup.find_all('span', {'class': 'tit'})[0].text
        # 제품 가격
        price = int(soup.find('span', {'class': 'price'}).text.replace(',', '').replace('원', '').lstrip().rstrip())
        # 제품 내용
        desc = soup.find('div', {'class': 'description-preview'}).text.lstrip().rstrip()
        title = desc.split('.')[0]
        content = '.'.join(desc.split(".")[1:])

        gender = product_url.split("/")[6]
        division = product_url.split("/")[7]
        cat = product_url.split("/")[8]

        result = {
            "product_code": product_code,
            'product_name': product_name,
            'title': title,
            'content' : content,
            'price': price,
            'gender': gender,
            'division': division,
            'category': cat,
            'url': product_url,
            'img': product_img_list
        }
        return result