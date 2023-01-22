print("Multiplication Game")
print("Lets see if you know your multiples!!")
print()
select=int(input("Choose a number to multiply by"))

counter=0
for i in range (1,11):
  correct=i*select
  print(i,"x",select)
  answer=int(input(">"))
  if answer==correct:
    print("Good job")
    counter+=1
  else:
    print("That was wrong,the correct answer was",correct)
if counter ==10:
  print("PERFECT SCORE")
else:
  print("You answered",counter,"out of 10")




        

