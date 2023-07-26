import requests

COMPANY_NAME: str = "stock market"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

parameters_news = {
    'q': COMPANY_NAME,
    'from':'2023-07-01',
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
news_response = requests.get(url='https://newsapi.org/v2/everything',params=parameters_news)
# data = news_response.json()
# print(data)
articles = news_response.json()['articles']
three_articles = articles[::3]
article_1_id = 1
article_1_name = articles[0]['source']['name']
article_1_author = articles[0]['author']
article_1_title = articles[0]['title']
article_1_description = articles[0]['description']
article_1 = [article_1_name,article_1_author,article_1_title,article_1_description]

article_2_id = 2
article_2_name = articles[1]['source']['name']
article_2_author = articles[1]['author']
article_2_title = articles[1]['title']
article_2_description = articles[1]['description']
article_2 = [article_2_name,article_2_author,article_2_title,article_2_description]

article_3_id = 3
article_3_name = articles[2]['source']['name']
article_3_author = articles[2]['author']
article_3_title = articles[2]['title']
article_3_description = articles[2]['description']
article_3 = [article_3_name,article_3_author,article_3_title,article_3_description]

article_4_id = 4
article_4_name = articles[3]['source']['name']
article_4_author = articles[3]['author']
article_4_title = articles[3]['title']
article_4_description = articles[3]['description']
article_4 = [article_4_name,article_4_author,article_4_title,article_4_description]

article_5_id = 5
article_5_name = articles[4]['source']['name']
article_5_author = articles[4]['author']
article_5_title = articles[4]['title']
article_5_description = articles[4]['description']
article_5 = [article_5_name,article_5_author,article_5_title,article_5_description]

article_6_id = 6
article_6_name = articles[5]['source']['name']
article_6_author = articles[5]['author']
article_6_title = articles[5]['title']
article_6_description = articles[5]['description']
article_6 = [article_6_name,article_6_author,article_6_title,article_6_description]

article_7_id = 7
article_7_name = articles[6]['source']['name']
article_7_author = articles[6]['author']
article_7_title = articles[6]['title']
article_7_description = articles[6]['description']
article_7 = [article_7_name,article_7_author,article_7_title,article_7_description]

article_8_id = 8
article_8_name = articles[7]['source']['name']
article_8_author = articles[7]['author']
article_8_title = articles[7]['title']
article_8_description = articles[7]['description']
article_8 = [article_8_name,article_8_author,article_8_title,article_8_description]

article_9_id = 9
article_9_name = articles[7]['source']['name']
article_9_author = articles[7]['author']
article_9_title = articles[7]['title']
article_9_description = articles[7]['description']
article_9 = [article_9_name,article_9_author,article_9_title,article_9_description]

article_10_id = 10
article_10_name = articles[9]['source']['name']
article_10_author = articles[9]['author']
article_10_title = articles[9]['title']
article_10_description = articles[9]['description']
article_10 = [article_10_name,article_10_author,article_10_title,article_10_description]