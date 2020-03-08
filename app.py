import nltk
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class TextProcessing:
    def __init__(self):
        self.article=''
        self.myfile=None
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.adjective_set=['JJ','JJR','JJS']



    def find_adjectives_verbs(self,file):
        #open the file to get the data
        with open(file,'r+') as self.myfile:
            self.article=self.myfile.read()
       # Tokenize the article into sentences: senteces
        sentences = nltk.sent_tokenize(self.article)
        #Tokenize each sentence into words: token_sentences
        token_sentences_words = [self.tokenizer.tokenize(sent) for sent in sentences] #filter all thhe words only not commass and fulstops
        filter_word_set=[]
        for sent in token_sentences_words:      #getting one sentence at a time
            filter_words=[word for word in sent if word not in stopwords.words('english')]  #removing the srtopwords from sentence
            filter_word_set.append(filter_words)        # add the result in the list

        # Tag each words of sentence into parts of speech: pos_sentences
        pos_sentences = [nltk.pos_tag(sent) for sent in filter_word_set]

        for sent in pos_sentences:                      #this iteration give one sentence at a time.
            for a_sent in sent:                         #get each word from sentence in the form of tupple that define its pos(parts of speech) also
                for adjective in self.adjective_set:         #get one type of adjecctive at a time from our defined list
                    if adjective in a_sent:             #check if the currently adjective from list appears in sentence word
                        self.finding_synonyms(a_sent[0])


    def finding_synonyms(self,word):
        synonyms=[]

        for syn in wordnet.synsets(word):
            for syn_words in syn.lemmas():
                synonyms.append(syn_words.name())   #syn_words.name() return the synonym and append it to synonyms list
                if word in synonyms:  #remove the actual word from synonym list if it was added by syn_words.name()
                    synonyms.remove(word)
        if len(synonyms) == 0:
            print('No synonym found for word: '+word)
        else:
            print('Synonym of '+word+' is : '+synonyms[0])
            if word in self.article:
                self.article=self.article.replace(word,synonyms[0])
    def save_result(self,file):
        with open(file,'w') as self.myfile:
            self.myfile.write(self.article)
            print('File have been updated !')

    def display_result(self):
        print(self.article)


text_process_obj=TextProcessing()  #creating an instance of a class
file='data.txt'
text_process_obj.find_adjectives_verbs(file)
print('Updated file is: ')
text_process_obj.display_result()
text_process_obj.save_result(file)
print('Complete process !')


