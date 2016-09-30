j=0
def jonny(j):
    i = j 
    j = "image%s.jpg"%(i)
    i = i+1
    return j
while True:
    g = jonny(j)
    j = j+1
    print g
    g = jonny(j)
    j = j+1
    print g
