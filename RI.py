
def reverseI(docId,titles,headings,contents):
    tempDic=dict()
    #tempDic2=dict()
    
    nt,nh,nc=1,1,1
    for word in titles:
        if len(tempDic)==0:
            tempDic[word]=[docId,1,0,0]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1]+1,0,0]
            else:
                tempDic[word]=[docId,1,0,0]
                #tempDic.update(tempDic2)
    
    for word in headings:
        if len(tempDic)==0:
            tempDic[word]=[docId,0,1,0]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1],tempDic[word][2]+1,0]
            else:
                tempDic[word]=[docId,0,1,0]
                #tempDic.update(tempDic2)

    for word in contents:
        if len(tempDic)==0:
            tempDic[word]=[docId,0,0,1]
        else:
            if word in tempDic.keys():
                
                tempDic[word]=[docId,tempDic[word][1],tempDic[word][2],tempDic[word][3]+1]
            else:
                tempDic[word]=[docId,0,0,1]
                #tempDic.update(tempDic2)

        

    #print("nt: ",nt,"nh :",nh,"nc :",nc)
    for word in tempDic.keys():
        if tempDic[word][2]>1 and tempDic[word][3]>1:
            print(tempDic)
    
    
