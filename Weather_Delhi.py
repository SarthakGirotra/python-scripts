import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
head={'User-Agent':'Mozilla/5.0'} 
page= requests.get('https://www.accuweather.com/en/in/new-delhi/187745/weather-forecast/187745', headers=head)
soup= BeautifulSoup(page.content, 'html.parser')
three_day= soup.find(class_='three-day-panel three-day-forecast full-mobile-width non-ad')
items=three_day.find_all(class_='day-panel')


times = [item.find(class_='module-header').get_text() for item in items]
dates = [item.find(class_='module-header sub date').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]
real_feel = [item.find(class_='real-feel').get_text() for item in items]
phrase = [item.find(class_='cond').get_text() for item in items]

def remove_sp(string_l):
    
    temp_=[]
    temp_= [re.sub('\s+',' ',string_l[x]) for x in range(4)]
    string_l=temp_
    
    return string_l

times= remove_sp(times)
dates=remove_sp(dates)
temps=remove_sp(temps)
real_feel=remove_sp(real_feel)
phrase =remove_sp(phrase)


weather = pd.DataFrame(
    {
        '-Period-':times,
        '-Time-':dates,
        '-Temp-':temps,
        '-Real Feel-':real_feel,
        '-Desc-    ':phrase


})


def inp():
    ch = input('Enter 1 for current weather or 2 for full weather forecast')
    print()
    ch=int(ch)
    if(ch==2):
        print(weather)
    elif(ch==1):
        print(weather.iloc[0])    
    else:
        return
inp()