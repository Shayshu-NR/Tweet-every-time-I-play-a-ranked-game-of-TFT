#Runs the methods in order to generate results

#~~~~~Libraries~~~~~
from TFT_data import *
from tweet_bot import *
from compose_tweet import *
#~~~~~~~~~~~~~~~~~~~

#~~~~~Global Variable~~~~~
API_KEY = '?api_key=RGAPI-5c6959a1-3ab3-4542-ae9f-81376fc6eff5'
USER_NAME = 'DotsXL'
#~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
def main():
        database = mysql_database()
        riotAPI = TFTData()
        twitter_bot = Twitter_Bot()

        #Connect to mysql data base
        connection = database.mysql_server_connect()

        #Get the puuid and all the match IDs
        puuid = riotAPI.get_puuid(API_KEY, USER_NAME)
        match_ids = riotAPI.get_match_ids(API_KEY, puuid)

        #Authorize and prep the twitter bot
        authorize = twitter_bot.authorize(CONSUMER_KEY, SECRET_CONSUMER_KEY)
        authorize = twitter_bot.access_token(authorize, ACCESS_TOKEN, SECRET_ACCESS_TOKE)
        api = twitter_bot.get_api(authorize)

        for i in range(len(match_ids)):
                #Get match data 
                match_data = riotAPI.get_match_data(API_KEY, match_ids[i])
                sql_data = riotAPI.get_sql_data(match_data, puuid)

                #Check if the data is already in the database
                if database.check_new_entry(match_ids[i], connection) :
                        database.new_entry(USER_NAME, puuid, match_ids[i], sql_data)

                        tweet = 

        

#~~~~~~~~~~~~~~~~~~~

main()