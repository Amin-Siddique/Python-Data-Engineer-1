from bs4 import BeautifulSoup
 
import requests


response = requests.get("http://www.imdb.com/chart/top")
soup = BeautifulSoup(response.text,'html.parser')
title = soup.select('.titleColumn')
rating = soup.select('.imdbRating')



# Get data based on rating: 
def get_titles(rating_input):
    titles = []
    for index,val in enumerate(title):
        listoftit = title[index].find('a').contents  
        listofrat = float("".join(rating[index].find('strong').contents))
        if listofrat > rating_input :
            titles.append({'title':listoftit,'rating':listofrat})
    return titles

  
  
print(get_titles(int(input())))
