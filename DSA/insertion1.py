def insertion(lst):
    l1=len(lst)
    i=1
    while i<l1:
        item = lst[i]
        ind = i-1
        while ind>=0 and item<lst[ind]:
            lst[ind+1]=lst[ind]
            ind-=1
        lst[ind+1]=item
        i+=1
    return lst

lst=[64, 34, 25, 12, 22, 11, 90]
print(insertion(lst))
