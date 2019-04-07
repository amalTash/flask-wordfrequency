from PyLyrics import *
import re
import json

class WordFreq():
    def __init__(self,artist,song):
        self.artist=artist
        self.song=song
        global lyricDict
        lyricDict={}

    def cleanData(self):
        content=PyLyrics.getLyrics(self.artist,self.song)
        newContent=''
        for word in content.strip():
            #converts everything to lowercase, removes special chars with regx
            newContent=re.sub(r"[^a-z0-9]"," ",content.lower())
        return newContent

    def pushToDict(self,textData):
        #will only print first letter if 'findall' not included
        splitWord=re.findall(r"[\w']+",textData)
        for word in splitWord:
            if(word in lyricDict):
                lyricDict[word]=lyricDict[word]+1
            else:
                lyricDict[word]=1
        return lyricDict

    def writeToFile(self):
        with open("freqword.json","w") as file:
            #writes alphabetically sorted dictionary to freqword file
            #indent=2 is used to for newline
            json.dump(lyricDict,file,sort_keys=True,indent=2)


    def appearMost(self):
        mostWord = max(lyricDict,key=lyricDict.get)
        return mostword;
