import requests 
import bs4
import re

def download():
    get = requests.get('http://news.gdut.edu.cn/ArticleList.aspx?category=4')
    get.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(get.text,"html.parser")
    title=soup.select('p a')
    time=soup.select('p span')
    data=[]
    for index in range(len(title)):
    #match = re.search(r"\d{4}[/]\d{2}[/]\d{2}",time[2*index-1])
        #print(type(title[index]))
        news = title[index].get('title')
        tag=['考试','事业单位','招聘','预算','监考','放假','研究','比赛','人员']
        for each in tag:
            if each in news:
                data.append(time[2*index+1].contents[0][1:11]+"   "+news)
    #print(data)
    return data

#download()
