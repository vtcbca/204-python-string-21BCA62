def createList():
    l=[]
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
    return(l)
a=createList()
print(a)
def strlen(s):
    count=0
    for i in s:
        count+=1
    return(count)
ans=strlen(s)
print(ans)

            
