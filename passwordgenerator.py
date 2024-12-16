# program to generate random passwords.
import random #a python library, used to randomly generate numbers
#uppercase lists
u_case=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#lowercase lists
l_case=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#numbers list
numbers=["1","2","3","4","5","6","7","8","9","0"]
#special characters list
s_chars=["!","@","#","$","%","^","&","*","(",")",":","|"]
print("Hi, this is Asmi, and I've developed this Password Generator!")
print(" ")
while(True):
  password=[0,0,0,0,0,0,0,0,0,0] #an empty list, to store the password
  password[0]=random.choice(u_case)
  password[1]=random.choice(l_case)
  password[2]=random.choice(l_case)
  password[3]=random.choice(numbers)
  password[4]=random.choice(s_chars)
  password[5]=random.choice(numbers)
  password[6]=random.choice(u_case)
  password[7]=random.choice(l_case)
  password[8]=random.choice(numbers)
  password[9]=random.choice(s_chars)
  pw=''.join(password) #join function joins the elements of the list and stores it in a string
  print("The new password")
  print(" ")
  print(pw)
  print(" ")
  answer=input("Do you want to generate a new password (Yes/No)")
  if(answer=="Yes"):
    continue
  elif(answer=="No"):
    print("Good day!")
    break
  else:
    print("Enter only in YES/NO. (Case-sensitive) Try again!")
    break