def names():
    s1=set()
    s1.update(['a','b','c','d'])
    print(s1)
    l1=list(s1)
    l1[0]='A'
    s2=set(l1)
    s2.remove('c')
    print(s2)
names()