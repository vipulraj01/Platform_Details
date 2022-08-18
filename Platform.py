import platform
print("*"*45)
user = int(input("1 : Press 1 to know your operating system\n2 : Press 2 to know your Platform Processor\n3 : Press 3 to know your Architecture\n4 : Press 4 to know your Operating System \n5 : Press 5 to know All The Details\n>>"))
if user==1:    
    print("Platform: ",platform.system())
elif user==2:
    print('Platform processor: ',platform.processor())
elif user==3:
    print('Platform Architecture: ',platform.architecture())
elif user==4:
    print('Operating System: ',platform.platform())
elif user==5:
    print("\n",platform.system(),"\n",platform.processor(),"\n",platform.architecture(),"\n",platform.platform())
else:
    print("You have entered wrong input")