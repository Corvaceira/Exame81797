def maxlen(Text):
    count1=0
    count=0
    for elem in Text[1]:
        count1=count1+1
        if elem==" ":
            count1=0
    for elem in Text[0]:
        count=count+1
        if elem==" ":
            count=0
    if count1>count:
        print("Maior palavra tem",count1,"e está na segunda frase")
    else:
        print("Maior palavra tem",count,"e está na primeira frase")
a=["The sky is blue","the Shining"]
maxlen(a)