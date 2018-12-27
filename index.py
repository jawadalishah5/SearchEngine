from bs4 import BeautifulSoup
import codecs
import nltk
from nltk.stem import PorterStemmer
import os
import re
from FI import forwardI
from RI import reverseI


#remove the given line from heading
def removeHead(data):
    end=data.rfind('Simple English Wikipedia, the free encyclopedia')
    return data[0:end]



#strip main text from webpage
def removeText(data):
    start=data.find('From Wikipedia, the free encyclopedia')
    end =data.rfind('External links')
    return data[start+40:end]



#this function remove useless words from the content
def removeStopwords(word_tokens):
    stop=["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(stop)
    filtered_list = [] 
    for w in word_tokens: 
        if w not in stopwords and w!="":
            filtered_list.append(w.lower())
    return filtered_list



#this function is only called in dataExtractor Function which returns
#tokenized data neatly filtered out
def returnNeatData(text):
    text=removeText(text)
    text=re.sub(r'\d+', '', text)   #removes numbers from content
    text=re.sub(r'[^\w]', ' ', text)  #removes symbols from tokens
    return removeStopwords(nltk.word_tokenize(text))

    
    
#function which parse the single html page and
#write its title and content in another html file
def dataExtractor(fileRead):

    with open(fileRead, "rb") as file:                      #file reading
        data = BeautifulSoup(file.read(), "lxml") 
    
    headings=[]    
    
    #writeData=open(fileWrite,"w",encoding='utf-8')        #file writing in a csv file
                                                           #which was just used for testing
    

    if data.title!=None:                                   #getting title

        title=(data.title.text).lower()
        #writeData.write(title+"\n")           
        
    for heading in data.find_all(re.compile('^h[1-6]$')): 
        head=heading.text.strip()
        head=head.split()
        headings.extend(head)
        headings=removeStopwords(headings)
        
    #for heading in headings:
        #writeData.write(heading)        

        
    text=returnNeatData(data.get_text())                #for filtering text

    
    
    

    #writeData.write(str(text)) 
    #writeData.close()
    
   
    return data.title,headings,text        #return title,tokenized headings and content





#function which is used to find all the html files from wikipedia data set
#and then call the extract() function to parse them all one by one

def extractAll():

    #fileWrite="C:\\Users\\Shah_G\\AppData\\Local\\Programs\\Python\\Python36-32\\htmlPages\\csvFile.csv"
    fileRead="C:\\Users\Shah_G\\Downloads\\project data structure\\wiki-data\\wiki-data\\articles"
    totalFiles=0;
    done=0
    for root,dirs,files in os.walk(fileRead):
        for i in files:
            
            if i.endswith((".html","htm")):
                totalFiles+=1
                url=root+"\\"+i;
                
                title,headings,content=dataExtractor(url)       #calling data Extractor Function
                if title==None:
                    title=i[:-5]
                    title=removeHead(title)
                    title=returnNeatData(title)                 #tokeninzing title
                else:
                    title=title.text
                    title=removeHead(title)
                    title=returnNeatData(title)
                
                #forwardI(totalFiles,title,headings,content,url.replace('"',"'").replace("\\","/"))    #forward indexing function is called
                reverseI(totalFiles,title,headings,content,url.replace('"',"'").replace("\\","/"))                         #reverse indexing funtion is called
                print(totalFiles)


extractAll()        #main method

