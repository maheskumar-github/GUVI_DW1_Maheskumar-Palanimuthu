import re
def Home():
     
    print("\t\t WELCOME TO MAHE SignUp & Login!!\n")
    print(" 1 Registration\n")
    print(" 2 Login\n")
    print(" 3 Forget Password\n")
    print(" 0 Exit the Page!!\n")
  
    ch=int(input("->"))
     
    if ch == 1:
        print(" ")
        Registration()
     
    elif ch == 2:
        print(" ")
        Login()
    elif ch == 3:
        print(" ")
        ForgetPass()
    elif ch == 0:
        print("Thanks for using MAHE SignUp Login page!!")
        exit()

def Registration():
    regex = r'\b[a-z._%+-]+@[a-z]+\.[a-z]{2,}\b'
    email = input("Enter the Email ID : ")
    if(re.fullmatch(regex, email)):
        for line in open("userpass.txt","r").readlines(): 
            login_info = line.split() 
            if email == login_info[0]:
                print("You are already registered!!")
                Home()
        pass
    else:
        print("Invalid Email")
        Registration()
    
    def password1():
        global password
        password = input("Enter the password : ")
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
        if re.fullmatch(reg, password):
            print("You are successfully registered!!")
            file = open("userpass.txt","a")
            file.write(email+" "+password)
            file.write("\n")
            file.close()
            pass
        else:
            print("Invalid Password")
            password1()
    password1()
    Home()

def Login():
    username = input("Please enter your Email ID : ")
    password = input("Please enter your password : ")
    for line in open("userpass.txt","r").readlines(): 
        login_info = line.split() 
        if username == login_info[0] and password == login_info[1]:
            print("You are logged in congratulations!!!")
            Home()
    print("You are not registered with us!! \nKindly register!!")
    Home()
    
def ForgetPass():
    username = input("Please enter your Email ID : ")
    for line in open("userpass.txt","r").readlines(): 
        login_info = line.split() 
        if username == login_info[0]:
            print("Your password is : "+login_info[1])
            Home()
    print("You are not registered with us!! \nKindly register!!")
    Home()

 
Home()
