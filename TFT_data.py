#Check on TFT data and update the mysql database

#~~~~~Libraries~~~~~
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
import requests
#~~~~~~~~~~~~~~~~~~~    

#~~~~~Global Variable~~~~~
API_KEY = '?api_key=RGAPI-65c978e9-fc20-47df-9621-0a34c2826471'
USER_NAME = 'DotsXL'
#~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
class mysql_database():
    #Establish connection with MySQL database
    def mysql_server_connect(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                database ='sql_match_history',
                                user ='root',
                                password ='datalog')
            
            if connection.is_connected():
                print("Connected to database!")
                return connection
                
        except mysql.connector.Error as error :
            print("Failed to connect to database {}".format(error))
            return False

    #Close connection with MySQL database
    def mysql_server_close(self, connection):
        try:
            connection.close()
        except mysql.connector.Error as error :
            print("Failed to close database connection {}".format(error))
            return False

    #Return the match history
    def mysql_get_match_history(self, ID, connection):
        try:
            cursor  = connection.cursor()
            sql_query = """select * from match_history"""
            cursor.execute(sql_query, (ID))
            records = cursor.fetchall()

            #Print out each row from the database
            for row in records:
                print(row[0])
                print(row[1])
                print(row[2])

            return records

        except mysql.connector.Error as error :
            print("Failed to read {}".format(error))
            return False

    #Check if a match ID is already in the database
    def check_new_entry(self, match_id, connection):
        try:
            cursor  = connection.cursor()
            sql_query = """select * from match_history where Match_History_ID in ('%s')"""
            cursor.execute(sql_query, (match_id))
            records = cursor.fetchall()

            #Print out each row from the database
            for row in records:
                print(row[0])
                print(row[1])
                print(row[2])

            if not records :
                return False
            else :
                return True

        except mysql.connector.Error as error :
            print("Failed to read {}".format(error))
            return False
    
    #Add a new entry to the mysql database
    def new_entry(self, userName, puuid, match_id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                database='sql_match_history',
                                user='root',
                                password='datalog')
            cursor = connection.cursor()
            sql_query = """insert into match_history (Summoner_Name, Puuid, Match_History_ID) VALUES(%s, %s, %s)"""
            dataTuple = (userName, puuid, match_id)
            cursor.execute(sql_query, dataTuple)
            connection.commit()

            print("Added to database...")
            return

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            return False


#TFT Data class
class TFTData():
    #Make a requrest to riot api and get the puuid from an:
    #API key, and summoner name, 
    def get_puuid(self, key, summonerName):
        url_request = 'https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/' +  summonerName + key
        responseJson = requests.get(url_request).json()
        puuid = responseJson['puuid']

        return puuid

    #Get the number of matches and their respective ids
    def get_match_ids(self, key, puuid):
        url_request = 'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/' + puuid + '/ids' + key
        responseJson = requests.get(url_request).json()
        match_ids = responseJson

        return match_ids

    #Get the match data for a given match id
    def get_match_data(self, key, match_id):
        url_request = 'https://americas.api.riotgames.com//tft/match/v1/matches/' + match_id + key
        responseJson = requests.get(url_request).json()

        return responseJson
#~~~~~~~~~~~~~~~~~~~

