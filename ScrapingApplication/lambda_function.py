import json

def lambda_handler(event, context):
    #SQSからURL群を受領。
    #Todo パラメータNull時のError処理
    for url in event['URLs']:
       json_data = scrape_apartment(url)
       store_apartment(json_data)
