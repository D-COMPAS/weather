from os import replace

#Webにリクエストする為
import requests
#Webサイトを読み取る為
from bs4 import BeautifulSoup
#クリップボード操作
import pyperclip
#文字列から辞書を作成する為
import ast

def time(s):
    import datetime as dt

    #s = "2021-04-14T10:42:00+09:00"

    dtl = s.split('T')

    dl = [int(num) for num in dtl[0].split('-')]
    tl =[int(num) for num in dtl[1][:5].split(':')]

    #曜日検索
    date = dt.date(dl[0],dl[1],dl[2])
    weekday ={'Sun':'日曜日','Mon':'月曜日','Tue':'火曜日','Wed':'水曜日','Thu':'木曜日','Fri':'金曜日','Sat':'土曜日'}

    output = date.strftime('%Y年%m月%d日')+weekday[date.strftime('%a')]
    output += str(tl[0]) +"時"+str(tl[1])+"分"

    return output

def today(code):
    #天気概況
    url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/'
    url += str(code)
    url += '.json'

    req = requests.get(url)
    bsObj = BeautifulSoup(req.text,'html.parser')

    dic = ast.literal_eval(bsObj.text)
    #print("type:"+str(type(dic)))

    dickey = [key for key in dic.keys()]
    #print(dickey)
    """
    publishingOffice    #データ元
    reportDatetime      #報告日時
    targetArea          #対象地域
    headlineText        #ヘッドライン
    text                #詳細情報
    """

    """
    output=''
    for key in dic.keys():
        output += dic[key]
        output += '\n'
    """
    output = dic[dickey[0]]+'より\n'
    output += time(dic[dickey[1]])
    output += dic[dickey[2]]+'の天気をお伝えします.\n'
    output += dic[dickey[3]]
    text = dic[dickey[4]].replace('【関東甲信地方】','')
    text = text.replace('\n\n','\n')
    output+=text+"以上です."
    return output
        
def threedays(code):
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/'
    url += str(code)
    url += '.json'

    req = requests.get(url)
    bsObj = BeautifulSoup(req.text,'html.parser')

    dic = ast.literal_eval(bsObj.text)

    #output=''
    #output = bsObj.text

    o = dic[0]['timeSeries'][0]['areas'][0].keys()
    print(o)
    

    """
    for i in range(2):
        for key in dic[i].keys():
            if key != 'timeSeries':
                print(dic[i][key])
            else:
                for j in range(len(dic[i][key])):
                    for tskey in dic[i][key][j].keys():
                        print(dic[i][key][j][tskey])

    return output"""

#threedays(130000)


#w:上書き,a:追記,x:新規作成
f=open('weather output.txt','w')

text = today(130000)
pyperclip.copy(text)
f.write(text)
#f.write(threedays(130000))
f.close