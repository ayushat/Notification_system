from plyer import notification 
import requests
from bs4 import BeautifulSoup
import time




def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\dell\Desktop\\my pyhon programs\\download.ico" ,
        timeout = 6
   )
def getData(url):
    r = requests.get(url)
    return r.text

if __name__== "__main__":
    while True :
        notifyMe("HELLO USER","Lets stop the spread of Corona virus together") 
        myHtmlData = getData('https://www.mohfw.gov.in')
        soup = BeautifulSoup(myHtmlData,'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
                myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Madhya Pradesh','Maharashtra','Kerala']
        for item in itemList[0:22]:
            dataList =  item.split('\n')
            if dataList[1] in states:
                    nTitle = 'Cases of Covid-19'
                    nText = f"State {dataList[1]} indian: {dataList[2]}\n Foriegn : {dataList[3]}\n Cured {dataList[4]}\n Deaths {dataList[5]}"
                    notifyMe(nTitle,nText)
                    time.sleep(3)
        time.sleep(3600)


            
