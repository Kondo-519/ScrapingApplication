import json
import boto3

def store_apartment(json_data):
    #https://recipe.kc-cloud.jp/archives/10058
    s3 = boto3.resource('s3') 

    bucket = 'apartment-history'
    key = city_id + '_'+ building_id + '_'+ regist_date + '.json' 
    file_contents = json_data

    obj = s3.Object(bucket,key) 
    obj.put( Body=file_contents )
