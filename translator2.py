#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'group 8'


def checkWordInTheDictionary(word, dictionary):
    for position in dictionary:
        if word in dictionary[position]:
            return dictionary[position][word], position
    return None

def PositionOfWord(word):
        return word[1]


# for the list of words in my dictionary
myDictionary = {'DET': {'the':'náà', 'that':'náà', 'A':'kan', 'a':'kan','my':'mi','i':'Mo', 'your':'yín','her':'rẹ̀'},
                'AUX': {'will':'ni', 'is':'ni', 'was':'ni'},
                'NOUN': {'olu':'Olú', 'sola':'Sola','bola':'Bọ́lá','man':'Okùnrin', 'babaloja':'Bàbálọ́jà',
                         'mango':'máńgòrò', 'yam':'iṣu','square':'Ojúde','trader':'Oníṣòwò','customer':'Oníbàárà',
                         'shop':'Ìsọ','cloth':'Aṣọ','basket':'Apẹ̀rẹ̀', 'butcher':'Alápatà', 'pepper':'ata',
                         'money':'Owó', 'sack':'Àpò', 'credit':'Àwìn', 'debtor':'Onígbèsè','carton':'Páálí',
                         'scale':'Òsùnwọ̀n', 'carrier':'Alábàárù', 'retailer':'Alátùntà', 'banana':'Ọ̀gẹ̀dẹ̀',
                         'way':'Ọ̀nà', 'path':'Ọ̀nà', 'claypot':'Ìkòkò','woman':'Obìnrin', 'market':'Ọjà',
                         'wares':'Ọjà','table':'tábìlì', 'shop':'Sọ́ọ̀bù', 'onion':'Àlùbọ́sà', 'tomatoes':'Tòmáàtì',
                         'paper':'Pépà','alum':'Álọ́ọ̀mù', 'bread':'Búrẹ́dì','Ìyá':'mother','Tola':'Tólá'},
                'VERB': {'buy':'rà', 'ate':'jẹ', 'bought':'rà', 'sell':'tà', 'carry':'gbé','carried':'gbé',
                         'haggle':'ná','sit':'jókòó','sat':'jókòó', 'cut':'gé', 'arranged':'tò','portion':'lé',
                             'portioned':'lé', 'trek':'rìn', 'hawks':'kiri', 'credit': 'lawin','come':'wá',
                             'came':'wá','collect':'gba'},
                'PREPOSITION': {'on':'sorí', 'behind':'Ẹ̀yìn', 'front':'iwájú', 'centre':'Àárín', 'beside':'Ẹ̀gbẹ́',
                                'of':' ', 'at':'si','to':''},
                'ADJECTIVE': {'very':'dáradára', 'half':'Ìlàjì', 'white':'funfun','whole':'odidi', 'dark':'dúdú',
                                  'unripe':'dúdú', 'very':'gan','four':'merin','reputable':'pataki'}
                }



#step 1
def checkMeaning(text, data):
    splitSentence = []
    for value in text:
        if checkWordInTheDictionary(value, myDictionary) is None:
            print("Error!!! \n " + "Invalid sentence --> "
              + data + "\n" + "word: " + value + " is not in dictionary.")
            exit()
        else:
            splitSentence.append(checkWordInTheDictionary(value, myDictionary))
    return splitSentence



def convertSubject(text, data):
    text = checkMeaning(text, data)
    for i in range(len(text)-1):
        word = text[i]
        if PositionOfWord(word) == 'DET' and PositionOfWord(text[i + 1]) == 'ADJECTIVE':
            text[i], text[i + 1] = text[i + 1], text[i]

    for i in range(len(text)-1):
        word = text[i]
        if PositionOfWord(word) == 'DET' and PositionOfWord(text[i + 1]) == 'NOUN':
            text[i], text[i + 1] = text[i + 1], text[i]

    for i in range(len(text)-1):
        word = text[i]
        if PositionOfWord(word) == 'ADJECTIVE' and PositionOfWord(text[i + 1]) == 'NOUN':
            text[i], text[i + 1] = text[i + 1], text[i]
    return text


def convertVerb(text, data):
    text = checkMeaning(text, data)
    return text


#SVO
Predicate = []
Subject = []
Verb = []
Object = []

def parse(text, data):
    checkMeaning(text, data)
    v = False
    b = text
    for word in b:
        if not v:
            if word in myDictionary['DET'] or word in myDictionary['NOUN'] or word in myDictionary['ADJECTIVE']:
                Subject.append(word)
            elif word in myDictionary['VERB']:
                Verb.append(word)
                v = True
        else:
            if word in myDictionary['PREPOSITION']:
                Predicate.append(word)
            else:
                Object.append(word)


    SS = convertSubject(Subject, data)
    VV = convertVerb(Verb, data)
    OO = convertSubject(Object, data)
    PP = convertVerb(Predicate, data)

    outputsentence = []
    for word in SS:
        outputsentence.append(word[0] + " ")
    for word in VV:
        outputsentence.append(word[0] + " ")
    for word in PP:
        outputsentence.append(word[0] + " ")
    for word in OO:
        outputsentence.append(word[0] + " ")

    cleanoutput = ''.join(outputsentence).strip() + '.'
    print(cleanoutput)

def main():
    #testing data
    rawData = raw_input("Enter the sentence to translate: ")
    data = rawData.lower()
    sentence = data.split()  #split is use to break in easy word
    parse(sentence, data)


if __name__ == '__main__':
    main()
