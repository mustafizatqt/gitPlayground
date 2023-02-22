# def quicksort(li,st,en):
#     piv = st+(en-st)//2
#     r=en
#     l = st
#     while(st<en):
#         while(li[st]<li[piv] and st<en):
#             st+=1
#         while(en>st and li[piv]<li[en]):
#             en-=1
#         li[st]^=li[en]
#         li[en]^=li[st]
#         li[st]^=li[en]
#     quicksort(li,l,en-1)
#     quicksort(li,en+1,r)
# li = [2,4,6,1,3,7]
# quicksort(li,0,len(li)-1)
# print(li)

def partition(li,st,en):
    pivot = li[st]
    low = st+1
    high = en
    while(True):
        while(low<=high and li[high]>=pivot):
            high = high-1
        while(low<=high and li[low] <= pivot):
            low=low+1
        if low<=high:
            li[low],li[high]=li[high],li[low]
        else:
            break
    li[st],li[high] = li[high],li[st] 
    return high
def qs(li,st,en):
    if st>=en:
        return
    p = partition(li,st,en)
    qs(li,st,p-1)
    qs(li,p+1,en)
li = [2,4,6,1,3,7]
qs(li,0,len(li)-1)
print(li)
