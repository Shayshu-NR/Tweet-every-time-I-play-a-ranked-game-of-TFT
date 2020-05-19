#Runs the methods in order to generate results

#~~~~~Libraries~~~~~
from TFT_data import mysql_database
from TFT_data import TFTData
#~~~~~~~~~~~~~~~~~~~

#~~~~~Global Variable~~~~~
API_KEY = '?api_key=RGAPI-5c6959a1-3ab3-4542-ae9f-81376fc6eff5'
USER_NAME = 'DotsXL'
#~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
def main():
        database = mysql_database()
        riotAPI = TFTData()

        #Connect to mysql data base
        connection = database.mysql_server_connect()

        #Get the puuid and all the match IDs
        puuid = riotAPI.get_puuid(API_KEY, USER_NAME)
        match_ids = riotAPI.get_match_ids(API_KEY, puuid)

        #database.new_entry(USER_NAME, puuid, match_ids[0])

        if database.check_new_entry(match_ids[0], connection) : 
                print('found')
#~~~~~~~~~~~~~~~~~~~

main()