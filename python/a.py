def wordcount(mystr:str):
    mystr =mystr.lower()
    mydict:dict ={}
    word = ''
    for i in mystr:
        if i>='a' and i <='z':
            word+=i
        else:
            if word=='':
                continue
            if mydict.get(word):
                mydict[word]+=1
            else:
                mydict[word]=1
            word=''
    return mydict

if __name__=='__main__':
    text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""
    print(wordcount(text))