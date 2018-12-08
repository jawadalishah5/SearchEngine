from bs4 import BeautifulSoup
import codecs
import os

def dataExtractor(fileRead,fileWrite):


#   fileRead=fileRead.replace("\\","\\\\")

    with open(fileRead, "r", encoding="ISO-8859-1") as file:
        data = BeautifulSoup(file.read(), "lxml")


    
#   print(data.title.text)
#   print(data.get_text())

    
        
    writeData=open(fileWrite,"w",encoding="utf-8")

    if data.title!=None:
        
        writeData.write(data.title.text+"\n")

    writeData.write(data.get_text())
    writeData.close()


def extractAll():

    fileRead="C:\\Users\\Shah_G\\Downloads\\project data structure\\wiki-data"
    totalFiles=0;

    for root,dirs,files in os.walk(fileRead):
        for i in files:
            if i.endswith((".html","htm")):
                totalFiles+=1
                dataExtractor(str(root)+"\\"+i,i)
                print(totalFiles)
            
    

extractAll()

#    fileWrite="C:\\Users\\Shah_G\\Desktop\\fileWrite\\fileWrite.csv"
#fileRead ="C:\\Users\\Shah_G\\Downloads\\data structures\\Elon Musk - Wikipedia.html"

