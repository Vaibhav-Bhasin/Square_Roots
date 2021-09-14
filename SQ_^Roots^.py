import random
w = random.randint(1,5)
for j in range(w):
  print(w)
  i = int(input("Please Enter Any Number Between 1 to 30 To Find Out Its Squaroot"))
  #formula = i^1/2
  print(i)
  g=(i**1/2)
  if i > 30 :
    print("Number is not supported")
  else:
    print(g,i)
  f = open("Squares.txt","a")
  f.write(str(i))
  f.write("-")
  f.write(str(g))
  f.write("\n")
  f.close()
