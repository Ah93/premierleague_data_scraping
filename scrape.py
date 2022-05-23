# Importing the required libraries
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from DB import insertScrapedPLData

# Starting with latest data for Spanish league, because I'm a Barcelona fan 
url = 'http://stats.football.co.uk/league_tables/2019_2020/premier_league/index.shtml'
res = requests.get(url) 
soup = BeautifulSoup(res.content, "html.parser")# Based on the structure of the webpage, I found that data is in the JSON variable, under 'script' tags 


#  Looking for the table with the class 'standard_tabelle'
table = soup.find('table', class_='table')
table_body = table.find('tbody')

Pldata = []
# Collecting Ddata
rows = table_body.find_all('tr')
for row in rows:   
    # Find all data for each column
    columns = row.find_all('td')
    
    team = columns[1].get_text()
    Pld = columns[2].get_text()
    Pts = columns[3].get_text()
    GD = columns[4].get_text()
    W = columns[5].get_text()
    D = columns[6].get_text()
    L = columns[7].get_text()
    F = columns[8].get_text()
    A = columns[9].get_text()
    season = '2019/2020'

    Pdata = team, Pld, Pts, GD, W, D, L, F, A, season
    Pldata.append(Pdata)
insertScrapedPLData(Pldata)

        # df = df.append({'Team': team,  'M': m, 'W': w, 'L': l, 'Goals': goals, 
        # 'Dif': dif, 'Pts': pts}, ignore_index=True)

        # df.head()

