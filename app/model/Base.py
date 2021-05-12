#from flask_mysqldb import MySQL as mysql
from app import mysql


class Model:
    def _filter(self,query):
        #filter query for SQL inyection
        return query
        
    #Search something in database
    def _query(self,query):
        filterQuery = self._filter(query)

        if type(filterQuery) is str:
            cur = mysql.connection.cursor()
            cur.execute(filterQuery)
            data = cur.fetchall()
            return data
        else:
            return None

    
    #Insert something in database
    def _insert(self,sentence):
        filterSentence = self._filter(sentence)

        if type(filterSentence) == str:
            cur = mysql.connection.cursor()
            cur.execute(filterSentence)

            mysql.connection.commit()
        else:
            return None