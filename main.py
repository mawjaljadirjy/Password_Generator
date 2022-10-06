import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_let=[]
pass_sym=[]
pass_num=[]

for num in range(1,nr_letters+1):
  choose=random.randint(0,len(letters)-1)
  char1=letters[choose]
  pass_let.append(char1)

for num in range(1,nr_symbols+1):
  choose=random.randint(0,len(symbols)-1)
  char1=symbols[choose]
  pass_sym.append(char1)

for num in range(1,nr_numbers+1):
  choose=random.randint(0,len(numbers)-1)
  char1=numbers[choose]
  pass_num.append(char1)

password_list=pass_let+pass_sym+pass_num
password =''.join(random.sample(password_list, len(password_list))) 
print(password)
