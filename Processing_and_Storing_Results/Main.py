import mysql.connector
from mysql.connector import Error

from PolarityModel import PolarityModel

def main():
    # Make the connection to MySQL database
    conn = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
    # Read the MySQL table
    sql_Query = "select * from training_dataset"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql_Query)

    # For model 01
    model1 = PolarityModel() 
    
    for i in range(1,501):
        row = model1.getTweets(conn,cursor)
        model1.storeSentimentMYSQL(conn,row)
        print(i, "Record is entered successfully")
    
    ##############
    
    # Closing the connection 
    cursor.close()
    conn.close()
    #### """

if __name__ == "__main__": 
    # Calling main function 
    main() 