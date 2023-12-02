from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re as ree
from selenium import webdriver
import json
from django.http import JsonResponse 

# Create your views here.
def news_info(request):
    # https://m.stock.naver.com/investment/news/mainnews 
    # 여기서 경제 뉴스 기사 제목, 링크, 이미지, 신문사 최신 10개 가져오기
    url = "https://m.stock.naver.com/investment/news/mainnews"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    pattern = ree.compile(r'^NewsList_item_')
    data = soup.find_all(class_ = pattern)
    news_data = []
    for item in data[:10]:
        link = item.find('a').get('href')
        title = item.find('strong').text
        content = item.find('p').text
        img_link = item.find('img').get('src')
        cite = item.find('cite').text
        news_data.append({'link': link,
                        'img_link': img_link,
                        'title': title,
                        'content': content,
                        'cite': cite})

    final_data = {'news_data': news_data}
    return JsonResponse(final_data, status=200)

def search_news(request, query):
    if request.method == 'GET':
        # query = request.GET.get('query')  # GET 요청으로부터 검색어를 가져옵니다.

        # 네이버 API 요청을 위한 클라이언트 아이디와 시크릿
        client_id = 'zuupf4b56FrdfO8TVHfO'
        client_secret = 'sulBZ4u2ZD'

        # Naver API URL 및 요청 헤더 설정
        url = f'https://openapi.naver.com/v1/search/news?query={query}'
        headers = {
            'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret,
        }

        # Naver API에 GET 요청을 보냅니다.
        response = requests.get(url, headers=headers)

        # 응답 데이터를 JSON 형식으로 변환하여 클라이언트에게 반환합니다.
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    


def kospi_info(request):
    # https://m.stock.naver.com/domestic/index/KOSPI/total 여기서 코스피 지수 가져오기 -> 동적 페이지
    max_retries = 3  # 최대 재시도 횟수 설정

    for attempt in range(max_retries):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("headless") # 브라우저 창 뜨지 않게 하는 옵션
            driver = webdriver.Chrome(options=options)

            url = "https://m.stock.naver.com/domestic/index/KOSPI/total"
            driver.get(url)

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            pattern = ree.compile(r'^GraphMain_price_')
            price = soup.find(class_=pattern)

            pattern = ree.compile(r'^VGap_gap_')
            tmp = soup.select('.VGap_gap__i0BuQ')
            fluctuation = {'value': tmp[0].get_text()[0:len(tmp[0].get_text()) // 2], 'percent': tmp[1].get_text()[:-1]}
            index_data = {'name': '코스피', 
                        'value': price.text, 
                        'fluctuation': fluctuation}

            driver.quit()
            break  # 성공하면 반복문 종료
        except IndexError:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed. Retrying...")
                continue
            else:
                print("Max retries reached. Unable to fetch data.")

    return JsonResponse(index_data, status=200)