##n=int(input("Enter length of list: "))
##T=[]
##for i in range(n):
##    j=int(input())
##    T.append(j)
##s=int(input("Enter searching element: "))
##for item in T:
##    if s==item:
##        print("Element found")
##    else:
##        print("Not found")

counter=0
def linearSearch(myItem,mylist):
    found=False
    position=0
    global counter
    while position<len(mylist) and not found:
        counter+=1
        if mylist[position] == myItem:
            found=True
        position +=1
    return found
if __name__=="__main__":
    shoping=['apples','1','bananas','87','grapes','mangoes']
    item = str(input("What item do you want to search: "))
    isitfound = linearSearch(item,shoping)
    if isitfound:
        print("no of searchs is ",counter)
        print("Item found!")
    else:
        print("no of searchs is ",counter)
        print("Not found!")
        res=input("if you want to add this item to our list Y/N? ")
        if res == 'Y' or 'y':
            shoping.append(item)
            print("successfully item added")
            print(shoping)
        else:
            print("okay! search another one")
            
