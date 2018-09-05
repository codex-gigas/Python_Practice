print("What is your name?"),
name = input()
gender = input("Are you male or female? ")
if gender == "male":
  print("How old are you? Mr.%s " % name),
  age = input()
  else
    print("How old are you? Mrs.%s " % name)
	
print("Hi! %r \nits glad to meet you and I have found that your just %r years old " % (name, age))
