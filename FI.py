#forward indexer


from connection import create_connection


def forwardI(docId,title,headings,content,url):
    
    dic=dict()     #dictionary for a single document
                    #having docIds as keys which refer to a
                    #list having sublist of titles,headings,contents
    
    dic[docId]=[title,headings,content,url]


    pushInDB(dic,docId) #push data into the database



#this function push forward indexed data into database for a single file
def pushInDB(dic,docId):


 


    # create a database connection
    conn = create_connection('tf.db')
    cur = conn.cursor()
    
    #database has 4 tables: [titles,headings,contents,urls]
    #each table has a docId column
    #and another colum of title,heading,content,url respectively
    
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
        
       
    
    
