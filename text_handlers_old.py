import json, re, xml.sax

class TextClassifier(object):
    '''
    TextClassifier detects the language in which a text
    is written, considering the language keywords chosen in
    the configuration file.
    '''
    def __init__(self, config=None):
        self.key_dict = {}
        if config == None:
            with open("config.json") as conf_file:
                config = json.load(conf_file)            
        self.GetConfigInfo(config)
        self.unknown_msg = "I don't know!"
        
    def GetConfigInfo(self, d):
        self.lang = d.keys()
        self.lang.sort()
        for i, v in enumerate(self.lang):
            for word in d[v]:
                self.key_dict[word] = i
                
    def GetUnknownMsg(self):
        return self.unknown_msg
            
    def DetectLanguage(self, text):
        text_list = re.split("[.,;:\s\?\!\"\']+", text)
        # There would be others delimiters, but these should be sufficient.
        counter = [0 for i in range(len(self.lang))]
        for t in text_list:
            l = self.key_dict.get(t.lower())
            if l != None:
                counter[l] += 1
        res = max(counter)
        if res == 0:
            return self.GetUnknownMsg()
        else:
            j = counter.index(res)
            return self.lang[j]        
    

class DocumentHandler(xml.sax.ContentHandler):
    '''
    DocumentHandler handles the content of a XML file, 
    and it searches information about autor, title and in which 
    language is written using the TextClassifier object. 
    '''
    def __init__(self):
        xml.sax.ContentHandler.__init__(self) 
        self.author = ""
        self.title = ""
        self.text = ""
        self.tag = None
        self.TextClassifier = TextClassifier()

    def startElement(self, name, attrs): 
        self.tag = name
        
    def characters(self, content):
        if self.tag == "author":
            self.author += content
        elif self.tag == "title":
            self.title += content
        elif self.tag == "body":
            self.text += content       
        
    def endElement(self, name):
        if name == "document":
            author = self.author.replace("\n", "")
            title = self.title.replace("\n", "")
            language = self.TextClassifier.DetectLanguage(self.text)
            print "Author: %s\nTitle: %s\nLanguage: %s" %(author, title, language)
            print ""
            self.author = ""
            self.title = ""
            self.text = "" 
                     

if __name__ == "__main__": 
    Handler = DocumentHandler()    
    f = raw_input("filename to classify:")
    try:
        xml.sax.parse(f, Handler)
    except:
        print "Some problem occurs! Is the filename correct?"
    