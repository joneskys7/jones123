while True:
    a=(raw_input("please enter value of A"))
    b=(raw_input("please enter value of B"))
    if a>b:
       print "A is greater"
       c=(raw_input("please enter value of c"))
       d=(raw_input("please enter value of d"))
       if c>d:
           print "c is greater"
       if c<d:
           print "d is greater"
       else:
           print "equal"
    if b>a:
       print "B is greater"
       e=(raw_input("please enter value of e"))
       f=(raw_input("please enter value of f"))
       if e>f:
           print "e is greater"
       if e<f:
           print "f is greater"
       else:
           print "equal"
    else:
        print "both are equal"
        
