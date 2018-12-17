#forward indexer
#from connection import connector
import time
import sqlite3
from sqlite3 import Error


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 


def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None






def forwardI(docId,title,headings,content,url):
    
    dic=dict()
    url=url.replace("\\","/")
    
    
    dic[docId]=[title,headings,content,url]
    count=0
    print(dic[docId][3])
    for i in dic[docId][2]:
        count+=1;
    print(count)
    
    pushInDB(dic,docId)


def pushInDB(dic,docId):

    start=time.time()
 


    # create a database connection
    conn = create_connection('tf.db')
    cur = conn.cursor()
    


    for tokens in dic[docId][0]:
        

        sql = ''' INSERT INTO titles(docIds,title)
                  VALUES(?,?) '''

        insert_in=(docId,tokens)
        cur.execute(sql,insert_in )

    for tokens in dic[docId][1]:
        

        sql = ''' INSERT INTO headings(docIds,heading)
                  VALUES(?,?) '''

        insert_in=(docId,tokens)
        cur.execute(sql,insert_in )
    for tokens in dic[docId][2]:
        

        sql = ''' INSERT INTO contents(docIds,content)
                  VALUES(?,?) '''

        insert_in=(docId,tokens)
        cur.execute(sql,insert_in )

        
    sql = ''' INSERT INTO urls(docIds,url)
          VALUES(?,?) '''

    
    iin=(docId,dic[docId][3])
    cur.execute(sql,iin)
    conn.commit()
        

##    for tokens in dic[docId][0]:
##        
##        sql="INSERT INTO `titles` (docIds,title) VALUES ('%s','%s')" % (docId, tokens)
##        
##        mycursor.execute(sql)
##        
##        mydb.commit()
##
##    for tokens in dic[docId][1]:
##            
##        sql1="INSERT INTO `headings` (docIds,heading) VALUES ('%s','%s')" % (docId, tokens)
##
##        mycursor.execute(sql1)
##        
##        
##        mydb.commit()
##
##    for tokens in dic[docId][2]:
##            
##        sql2="INSERT INTO `contents` (docIds,content) VALUES ('%s','%s')" % (docId, tokens)
##        
##
##        mycursor.execute(sql2)
##        
##        mydb.commit()

    
    c=time.time()-start
    print(c)
    
    
