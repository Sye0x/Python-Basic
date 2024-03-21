import os
from cryptography.fernet import Fernet
def write_key():
        key=Fernet.generate_key()
        with open('key.key','wb')as f:
            f.write(key)

def load_key():
    with open('key.key',"rb")as f:
        key=f.read()
        return key

def add():
    key=load_key()
    fer=Fernet(key)
    loc=input("Enter Location of User & Pass:")
    user=input("Enter UserName:")
    passw=input("Enter Password:")

    with open('password.txt','a')as f:
        f.write(loc+"|"+user+"|"+fer.encrypt(passw.encode()).decode()+"\n")


def view():
    key=load_key()
    fer=Fernet(key)
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            loc,user, passw = data.split("|")
            print(loc+"\nUserName:" + user + "\nPassword:" + fer.decrypt(passw.encode()).decode())
        input("Press Enter to continue...")
  
    


def create_master_pass():
    key=load_key()
    fer=Fernet(key)
    passw=input("Set a new Master Password:")
    with open('password.txt','a')as f:
        f.write("Master"+"|"+"User"+"|"+fer.encrypt(passw.encode()).decode()+"\n")

def first_start():
    if not os.path.exists('key.key'):
        with open('key.key', 'w') as f:
            pass
    
    f=open('key.key','r')
    if f.readline()=="":
        f.close()
        write_key()
        create_master_pass()

def check_pass(passw):
    key = load_key()
    fer = Fernet(key)
    with open('password.txt', 'r') as f:
        for line in f:
            data = line.rstrip()
            loc, user, pass2 = data.split("|")
            pass2 = pass2.rstrip()
            decrypted_pass = fer.decrypt(pass2.encode()).decode()  # Decode decrypted password
            if passw == decrypted_pass:
                return True
        print("Incorrect Password")
        os.system('pause')
        os.system('cls')
        return False



def main():
    
    first_start()
    while True:
        passw=input("Enter Master Password:")
        
        flag=check_pass(passw)
        if flag==True:
            break
    
    

    while True:
        os.system('cls')

        print("Press V to View all Password")
        print("Press A to Append new Password")
        print("Press E to Exit")
        inp=input("Enter Here:").lower()
        if inp=='a':
            add()
        elif inp=='v':
            view()
        elif inp=='e':
            exit()
        else:
            os.system('cls')
            print("Invalid Input")
            os.system('pause')

main()