
from connection import create_connection


def reverseI(docId,titles,headings,contents):
    tempDic=dict()      #temporary dictionary for single document
                        #having words as keys which refer to a list
                        #having docId,frequency in title,headings,contents

    
    
    for word in titles:         #count in titles
        if len(tempDic)==0:
            tempDic[word]=[docId,1,0,0]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1]+1,0,0]
            else:
                tempDic[word]=[docId,1,0,0]

    
    for word in headings:       #count in headings
        if len(tempDic)==0:
            tempDic[word]=[docId,0,1,0]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1],tempDic[word][2]+1,0]
            else:
                tempDic[word]=[docId,0,1,0]


    for word in contents:       #count in contents
        if len(tempDic)==0:
            tempDic[word]=[docId,0,0,1]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1],tempDic[word][2],tempDic[word][3]+1]
            else:
                tempDic[word]=[docId,0,0,1]

    reversePushInDB(tempDic,docId)        #pushing dictionary in database


#function which push data in database
def reversePushInDB(dic,docId):


 
    # create a database connection
    conn = create_connection('reverse.db')
    cur = conn.cursor()

    #table has columns: word,docId,title freq,heading freq, content freq
    for token in dic.keys():
        sql=''' INSERT INTO reverseIndex(word,docId,tfreq,hfreq,cfreq)
                VALUES(?,?,?,?,?) '''
        
        insert_in=(token,docId,dic[token][1],dic[token][2],dic[token][3])
        cur.execute(sql,insert_in)
    conn.commit()

    
