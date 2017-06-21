#even and odd numbers under n
n=input('number')
a=range(n)
even=[x for x in a if x%2==0]
print 'even',even
odd=[x for x in a if x%2==1]
print 'odd',odd

