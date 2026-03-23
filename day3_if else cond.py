a=int(input("Enter the value of a:"))
print("The value of a:")
if(a<0):
  print("The number is negative")
elif(a>0):
    if(a<11):
     print("the number is between 1-10")
    elif(a<21):
      print("the number is between 11-20")
    elif(a<31):
      print("the number is between 20-30")
    elif(a<41):
      print("the number is between 30-40")
    elif(a<51):
      print("the number is between 40-50")
    else:
      print("the number is greater than 50")
else:
  print("The number is zero")
