ab = input("Enter a Day : ")
bc = input("Enter a Rate : ")
try:
  cd = float(ab)
  de = float(bc)
  x = cd*de
  x = x++
  print("Total : ",x)
except:
  print("Error, Please enter numeric input")
