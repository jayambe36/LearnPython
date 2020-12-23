num = input("Enter a number : ")
try:
  val = int(num)
  print("Conversion successful!")
except:
  val = -1

if val > 0:
  print("Positive natural number")
elif val == 0:
  print("Entered number is  Zero")
else :
    print("Entered wrong input")
print("Program is End")
