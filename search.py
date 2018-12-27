

from connection import create_connection


def search(word,h):

    dic=dict()
    
    # create a database connection
    conn = create_connection('reverse.db')
    cur = conn.cursor()

    sql="SELECT * FROM reverseIndex INNER JOIN urls USING(docId) WHERE word LIKE ?"
    for token in word:
        insert_in=token+'%'
        cur.execute(sql,(insert_in,))
        result=cur.fetchall()
        if len(result)!=0:
            for x in range(len(result)):
                if result[x][1] in dic.keys():
                    
                    
                    dic[result[x][1]]=[dic[result[x][1]][0]+" "+result[x][0],dic[result[x][1]][1]+result[x][2]*10,dic[result[x][1]][2]+result[x][3]*5,dic[result[x][1]][3]+result[x][4],result[x][5]]

                else:
                    dic[result[x][1]]=[result[x][0],result[x][2]*10,result[x][3]*5,result[x][4],result[x][5]]

                
                
            
        else:
            print ("no result found")
##    for numb in dic.keys():
##        
##        if numb==11:
##            print(dic[numb])
##            break
##        
    conn.commit()

    #print(dic)
    return(rank(dic,h))


def rank(dic,h):

    ret=[]   
    for i in range(h,0,-1):
        try:
            maxi=list(dic.keys())[0]
            for token in dic.keys():

                    
                if sum(dic[token][1:4]) > sum(dic[maxi][1:4]):
                    token,maxi=maxi,token
            ret.append(dic[maxi][4])
            print(dic[maxi])
            del (dic[maxi])

        except:
            break
    
    return ret

##    done=0;
##    for i in dic.keys():
##        print(dic[i])
##        done+=1
##        if done >=1:
##            break

    


##x=input("enter word: ")
##x=x.lower()
##
##search(nltk.word_tokenize(x))

