dict={}
tuple1=((3,"agalya"),(5,"subcode"))
'''for  i in range(0,len(tuple1)):
    if(i%2==0):
        dict.values(tuple1[i])
    else:
        dict.keys(tuple1[i])
print(dict)
    #if
'''
print(dict((y,x))for x,y in tuple1)
