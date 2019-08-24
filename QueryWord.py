import requests
from bs4 import BeautifulSoup
import  re
class Word:
    def __init__(self):

        self.text = ''
        self.voices=[]
        self.props = {}
        self.label_text = ''
        self.changes={}
    def __repr__(self):
        return "voices %s \n props: %s " % (str(self.voices), str(self.props))



class QueryWord:
    def __init__(self):
        self.word = Word()

    def query(self,keyword):
        req = requests.get("http://www.iciba.com/" + keyword)
        bsObj = BeautifulSoup(req.text,'html.parser')
        # print(bsObj.text)
        # props = bsObj.findAll("li",{"class":"clearfix"})
        props = bsObj.findAll("li",class_ = 'clearfix')
        for tag in props:
            if tag['class'][0]== "clearfix":

                key = tag.find("span",class_='prop').text
                key_map =''
                for line in tag.p.findAll("span"):
                    key_map += line.text
                self.word.props[key] = key_map
            elif tag['class'][0] == 'change':
                label_text = tag.h1.text
                self.word.label_text = label_text
                for line in tag.find('p').findAll("span"):
                    words = line.text.split("\n")
                    key = words[0].strip()
                    key_map = words[1].strip()
                    self.word.changes[key] = key_map
                # print(self.word.changes)
        base_speak = bsObj.find("div",class_="base-speak")
        if base_speak:
            for child in base_speak.findAll("span"):
                if child.i:
                    temp1 = child.span.text
                    temp2 = re.findall(r"http:.+\.mp3",str(child.i))
                    temp2 = temp2[0]
                    self.word.voices.append((temp1,temp2))

        return self.word


if __name__ == "__main__":
    key = "test"
    QueryWord().query(key)