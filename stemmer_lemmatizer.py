from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import string
from nltk.corpus import stopwords
#sent="Pack of 8 herb rolls to quickly and easily begin a home garden for delicious foods; includes one grass repair patch"
#sent = "Ultra Fast 3-Port USB DC Car Charger for Smartphones "
#result=open("resultfile_auto_home.txt","w")

StopWords = set(stopwords.words("english"))
StopWords.update(('and', 'may', 'a', 'use', 'us','so', 'your', 'this', 'when', 'it', 'many', 'can', 'set', 'cant',
                            'to', 'yes', 'not', 'no', 'these','keep','enough','use','x','w','d','p','n'))

"""
port = PorterStemmer()
a=" ".join([port.stem(i) for i in sent.split()])
print(a)
"""

wnl = WordNetLemmatizer()
lines = open("testdata.txt", "r").read().split('\n')

homeimprovement=open("auto_home_improvement.txt","w")
homegarden=open("home_garden.txt","w")
mensfashion=open("mensfashion.txt","w")
electronics=open("electronics.txt","w")
womensfashion=open("womensfashion.txt","w")
babykidstoys=open("baby_kids_toys.txt","w")
jewelrywatches=open("jewelry_watches.txt","w")
healthbeauty=open("healthbeauty.txt","w")
sportsoutdoors=open("sports_outdoors.txt","w")
grocery=open("grocery.txt","w")
entertainment=open("entertainment.txt","w")

for line in lines:
    sents=line.split('||')
    if (len(sents) <= 2):
            continue
    sent=sents[1]

    #tex = []
    sent = sent.lower()
    sent = sent.translate(None, string.punctuation)

    #tex = " ".join([wnl.lemmatize(i) for i in sent.split()])
    tex = ' '.join([wnl.lemmatize(word) for word in sent.split() if wnl.lemmatize(word) not in StopWords])
    #for a in nltk.pos_tag(tex.split()):
        #print(a)
    sentence = ' '

    for a in nltk.pos_tag(tex.split()):
        if a[1] == 'NN' or a[1] == 'JJ' or a[1] == 'VBN' or a[1] == 'NNS' or a[1] == 'NNP':
            sentence = sentence + a[0] + ' '
        elif a[1] == 'smartphones':
            sentence = sentence + a[0][0:len(a[0]) - 1] + ' '
    #print(sentence)
    #print(sents[2])
    category=sents[2].split('>')
    print(category[0])
    if("Auto & Home Improvement " in category[0]):
        homeimprovement.write(sentence+'')
    elif ('Home & Garden' in category[0]):
        homegarden.write(sentence + '')
    elif("Men's Fashion " in category[0]):
        mensfashion.write(sentence+'')
    elif ('Electronics ' in category[0]):
        electronics.write(sentence + '')
    elif ("Women's Fashion" in category[0]):
        womensfashion.write(sentence + '')
    elif ("Jewelry & Watches " in category[0]):
        jewelrywatches.write(sentence + '')
    elif ('Baby, Kids & Toys ' in category[0]):
        babykidstoys.write(sentence + '')
    elif ('Health & Beauty ' in category[0]):
        healthbeauty.write(sentence + '')
    elif ('Sports & Outdoors ' in category[0]):
        sportsoutdoors.write(sentence + '')
    elif ('Grocery, Alcohol & Tobacco ' in category[0]):
        grocery.write(sentence + '')
    elif ('Entertainment ' in category[0]):
        entertainment.write(sentence + '')
    #elif ('Appliances' i category[1]):
        # print('a')
        #appliance.write(sentence + '')
   # else:
        #result.write(sentence+'||'+ sents[2]+'\n')

"""
sent='Infrared sensor monitors driveways, doors, and mailboxes for movement and activates chiming receiver placed up to 400 ft. away'
sent = sent.lower()
sent = sent.translate(None, string.punctuation)

tex = " ".join([wnl.lemmatize(i) for i in sent.split()])

for a in nltk.pos_tag(tex.split()):
    print(a)
    sentence = ' '

for a in nltk.pos_tag(tex.split()):
        if a[1] == 'NN' or a[1] == 'JJ' or a[1] == 'VBN' or a[1]=='NNS' or a[1]=='NNP':
            sentence = sentence + a[0] + ' '
        elif a[1] == 'smartphones':
            sentence = sentence + a[0][0:len(a[0]) - 1] + ' '
print(sentence)
"""