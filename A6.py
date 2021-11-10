name="Bank.txt"
File=open(name,'a+')
Words=[]
def read():
    i=1
    for line in File:
        k=len(Words)
        if(i%2!=0):
            Words.append([])
            Words[k].append(line)
        else:
            Words[k].append(line)
        i+=1
def add_new():
    w=input("Word: ")
    t=input("Translate: ")
    flag=True
    for i in range(len(Words)):
        if(w in Words[i][0]):
            flag=False
            break
    if(flag==True):
        File.write(w)
        File.write(t)
        Words.append([])
        Words[len(Words)-1].append(w)
        Words[len(Words)-1].append(t)
def translate(ch):
    word=input("Text: ").split(" ")
    trans=""
    no_mean=[]
    flag=False
    for i in range(len(Words)):
        for j in range(len(word)):
            if(word[j]==Words[i][ch]):
                flag=True
                #print("Text: ",Words[i][ch])
                if(ch==1):
                    trans=trans+Words[i][ch-1]+" "
                    #print("Translate: ",Words[i][ch-1])
                else:
                    trans=trans+Words[i][ch+1]+" "
                    #print("Translate: ",Words[i][ch+1])
        if(flag==False):
            print("not available!")
            return
    print("Translat: ",trans)
read()
while(True):
    print("""Enter the number of your sellection:
1. Add new word
2.Translation english2persian
3.Translation persian2english
4.EXIT""")
    n=input()
    n=int(n)
    if(n==1):
        add_new()
    elif(n==2):
        translate(0)
    elif(n==3):
        translate(1)
    elif(n==4):
        break