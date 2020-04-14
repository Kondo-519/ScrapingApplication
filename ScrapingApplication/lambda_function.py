import json
import scrape_apartment
import store_apartment

def lambda_handler(event, context):
    #SQSからURL群を受領。
    #Todo パラメータNull時のError処理
    #for url in event['URLs']:
    #   json_data = scrape_apartment(url)
    #   store_apartment(json_data)

    url = "https://s.fudousan.or.jp/system/?act=d&type=31&pref=13&stype=l&city[]=13101&n=20&p=1&v=on&s=&bid=14090023&org=Z"
    json_data = scrape_apartment(url)
    store_apartment(json_data)

    print('Test Is OK')