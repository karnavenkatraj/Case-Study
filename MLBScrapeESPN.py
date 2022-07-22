import pandas as pd
import re
from bs4 import BeautifulSoup
import requests

# Pulling in website source code#

url = 'https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2022'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Pulling in player rows
##Identify Player Rows

players = soup.find_all('tr', attrs={'class': re.compile('.*row player-10-.*')})
columns = soup.find('tr', {'class': 'colhead'})
columns = [x.text for x in columns.find_all('td')]

# Initialize a list of dataframes
final_df_list = []

# Loop through the players 
for player in players:
    ##Pulling stats for each players
    stats = [stat.text for stat in player.find_all('td')]
    ##Create a data frame for the single player stats
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns

    # Put temp_df in a list of dataframes
    final_df_list.append(temp_df)

##Join your list of single players stats
final_dataframe = pd.concat(final_df_list, ignore_index=True)
print(final_dataframe)




