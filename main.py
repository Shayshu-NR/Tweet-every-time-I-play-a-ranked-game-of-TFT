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

        print(match_ids)

        for i in range(len(match_ids)):
                #Get match data 
                match_data = riotAPI.get_match_data(API_KEY, match_ids[i])
                sql_data = riotAPI.get_sql_data(match_data, puuid)

                #Check if the data is already in the database
                if database.check_new_entry(match_ids[i], connection) :
                        database.new_entry(USER_NAME, puuid, match_ids[i], sql_data)

        return
#~~~~~~~~~~~~~~~~~~~

main()