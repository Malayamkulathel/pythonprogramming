listword=list(input("enter the list of word").split())
maxlen=len(listword[0])
word=listword[0]
for i in listword:
    if(len(i)>maxlen):
        maxlen=len(i)
        word=i
print("the longest length of word is:")
print(word)
print("the length of longest word is:")
print(len(word))

