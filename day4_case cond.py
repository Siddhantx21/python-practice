x=float(input("enter a number:"))
match x:
  case _ if x<=10:
    print(x,"\n x is between 1-10")
  case _ if x<=20:
    print(x,"\n x is betweeen 11-20")
  case _ if x<=30:
    print(x,"\n x is between 21-30")
  case _ if x>=0:
    print(x,"\n x is greater than 30")  
