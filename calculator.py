
#simple calculator
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y!=0:
      return x/y
  else:
      print("Error! Division is not possible.")
def calculator():
  print("This is a simple calculator.")
  print("1.Addition.")
  print("2.Subtraction.")
  print("3.Multiplication.")
  print("4.Division.")
  while True:
      choice=input("Enter your choice (1/2/3/4): ")
      if choice in["1","2","3","4"]:
          num1=float(input("Enter the first number: "))
          num2=float(input("Enter the second number: "))
          if choice == "1":
              print(f"The result is: {add(num1,num2)}")
          elif choice =="2":
              print(f"The result is: {subtract(num1,num2)}")
          elif choice =="3":
              print(f"The result is: {multiply(num1,num2)}")
          elif choice =="4":
              print(f"The result is: {divide(num1,num2)}")
          next_calculation = input("Do you want to perform another calculation? (yes/no): ")
          if next_calculation.lower()!="yes":
              break
      else:
          print("Invalid input.")
calculator()             
