#Runs the methods in order to generate results

#~~~~~Libraries~~~~~
from TFT_data import mysql_database
from TFT_data import TFTData
#~~~~~~~~~~~~~~~~~~~

#~~~~~Global Variable~~~~~
API_KEY = '?api_key=RGAPI-65c978e9-fc20-47df-9621-0a34c2826471'
USER_NAME = 'DotsXL'
#~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
def main():
    database = mysql_database()
    riotAPI = TFTData()

    #Connect to mysql data base
    database.mysql_server_connect()

    #
    puuid = riotAPI.get_puuid(API_KEY, USER_NAME)
    match_ids = riotAPI.get_match_ids(API_KEY, puuid)
    
    for i in range(0, len(match_ids)):
        print(i)
#~~~~~~~~~~~~~~~~~~~

main()