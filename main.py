#Runs the methods in order to generate results

#~~~~~Libraries~~~~~
from TFT_data import *
from tweet_bot import *
from compose_tweet import *
from twitter_keys import *
from time import sleep
#~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
def main():
        database = mysql_database()
        riotAPI = TFTData()
        twitter_bot = Twitter_Bot()

        #Authorize and prep the twitter bot
        authorize = twitter_bot.authorize(CONSUMER_KEY, SECRET_CONSUMER_KEY)
        authorize = twitter_bot.access_token(authorize, ACCESS_TOKEN, SECRET_ACCESS_TOKE)
        api = twitter_bot.get_api(authorize)

        while(True):
                #Connect to mysql data base
                connection = database.mysql_server_connect()

                #Get the puuid and all the match IDs
                puuid = riotAPI.get_puuid(API_KEY, USER_NAME)
                match_ids = riotAPI.get_match_ids(API_KEY, puuid)

                for i in range(1):
                        #Get match data 
                        match_data = riotAPI.get_match_data(API_KEY, match_ids[i])
                        sql_data = riotAPI.get_sql_data(match_data, puuid)

                        print(sql_data)

                        #Check if the data is already in the database
                        if database.check_new_entry(match_ids[i], connection) :
                                database.new_entry(USER_NAME, puuid, match_ids[i], sql_data, connection)

                                tweet = compose_tweet(sql_data[0], sql_data[1], sql_data[2], sql_data[3])

                                api.update_with_media(get_relavent_photo(sql_data[2]), status = tweet)

                #Sleeping so that I don't overwhelm the twitter or riot api
                sleep(300)
                database.mysql_server_close(connection)
#~~~~~~~~~~~~~~~~~~~

main()