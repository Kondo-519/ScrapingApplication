
import requests
import json
from bs4 import BeautifulSoup, SoupStrainer
 
# textからlistとかに変換
url = "https://s.fudousan.or.jp/system/?act=d&type=31&pref=13&stype=l&city[]=13101&n=20&p=1&v=on&s=&bid=14090023&org=ZN"
 
# Webサイトからデータ取得
response = requests.get(url)

# 文字コードを判定させ、エンコードを指定
response.encoding = response.apparent_encoding

#パーサーの指定
#http://kondou.com/BS4/#parser-installation
use_parser = "lxml" #lxml’s HTML parser

#ドキュメントのどの部分をパースするかを指定（不要箇所は処理対象外にする）
tag_name = "table"
class_name = "tb_syousai"

#スープ渡し器オブジェクトを生成
parse_only_header = SoupStrainer(tag_name, class_=class_name)
#html構造の取得
soup = BeautifulSoup(response.text, use_parser , parse_only=parse_only_header)

tag = soup.find_all("th")
tag.name = "td"



#soup結果から、tr要素を持つ行をrowオブジェクトとして定義し、リスト化。for文でぐるぐる回す。
#row要素からタグ名を指定してtextを引っ張り出す。
table_data = [[row.th.text, row.td.text]
                         for row in BeautifulSoup(response.text, use_parser , parse_only=parse_only_header)("tr")]

#もし、同じタグ要素のセルが連続していたら、以下のようにfor文でぐるぐる回すように。
#参考URL：https://stackoverflow.com/questions/18544634/convert-a-html-table-to-json
#table_data = [[cell.text for cell in row("td")]
#                         for row in BeautifulSoup(response.text, use_parser , parse_only=parse_only_header)("tr")]


#配列データを辞書形式に変更し、それをjson形式に変更。Unicodeエスケープされないよう、オプションで指定。
print(json.dumps(dict(table_data), ensure_ascii=False))