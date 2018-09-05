counter=0
def binary_search(myitem,mylist):
    found=False
    global counter
    bottom=0
    top=len(mylist)-1
    while bottom<=top and not found:
        
        middle=(bottom+top)//2
        counter=middle
        if mylist[middle]==myitem:
            found=True
        elif mylist[middle]<myitem:
             bottom=middle+1
        else:
             top=middle-1
    return found,str(counter)

if __name__=="__main__":
    nums=[1,4,6,7,8,9,12,15,16,18,21,25,56,78,99]
    item=int(input("What number are you looking for? "))
    print("Entered")
    isitFound,res = binary_search(item,nums)
    
    if isitFound and res:
        print("Your number is found at position ",res)
    else:
        print("Your item is not in the list")
