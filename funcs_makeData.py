'''
webよりデータを取得するための関数群
'''
import requests
import bs4 #beautiful soup

'''
なろうのジャンル別ランキングから、100作品のURLをurlList[]に格納。
'''
def getURLFromRank(url):

    '''
    urlからソースコードを取得
    '''
    get_url_info = requests.get(url)
    get_url_info.encoding = get_url_info.apparent_encoding #文字化けが直る
    #print(get_url_info.text)

    '''
    beautifulsoup4を使う（スクレイピングに便利）
    '''
    bs4Obj = bs4.BeautifulSoup(get_url_info.text,'lxml')
    list = bs4Obj.find_all(class_='tl') #'tl'クラスに作品情報がある
    #print(list[0])

    workDict = dict() #上位100作品の辞書{'作品名':URL}
    for work in list:
        text = work.get_text() #タイトルを取得
        workDict[text] = work['href']

    return workDict

'''
1作品のURLから、セクションのURLリストをurlList[]に格納。
'''
def getSectionFromURL(url):
    get_url_info = requests.get(url)
    get_url_info.encoding = get_url_info.apparent_encoding #文字化けが直る

    bs4Obj = bs4.BeautifulSoup(get_url_info.text,'lxml')
    list = bs4Obj.find_all(class_='subtitle')
    urlList = []
    if list == []:
        urlList.append(url)
    else:
        for work in list:
            tmp = work.find("a")
            urlList.append('https://ncode.syosetu.com' + tmp['href'])
    return urlList

'''
1セクション、すなわち本文を含むページのURLからテキストを取得。
'''
def getTextFromSection(url):
    get_url_info = requests.get(url)
    get_url_info.encoding = get_url_info.apparent_encoding

    bs4Obj = bs4.BeautifulSoup(get_url_info.text,'lxml')
    honbun = bs4Obj.find(id='novel_honbun')
    honbun = honbun.find_all('p')
    text = ''
    for line in honbun:
        text = text + line.get_text()
    return text
