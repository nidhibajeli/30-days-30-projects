import random
import string #gives us ready‑made sets of characters (letters, digits, punctuation).
password_file = "passwords.txt" #- It tells the computer: “This is a plain text file.” A text file is the simplest kind of file — it only contains readable characters (letters, numbers, symbols), no fancy formatting like Word documents or PDFs.
#this is the file name, each time we save a pasword it gets saved here
def pass_generator(length=6): #when u call the fucntion u can have the length accoridng to u but the defaiult would be 6 if u dont specify
    characters = string.ascii_letters + string.digits+ string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
     #- random.choice(characters) → Picks one random item from the basket of characters.
     #- for _ in range(length) → Repeat this step as many times as the password length.
     #- ''.join(...) → Joins all those random characters together into one string (no spaces).
     #- return ... → Sends the finished password back to whoever called the function.


#string.ascii_letters means all uppercase and lowercase letter
#string.digits for numbers between 0-9
#string.punctuation for - All special symbols (!@#$%^&*(),etc
# + joins them into one big string
#charachters= saves this big set of letters into a var called charachters

#this is now a function to save the password
def save_password(label, password): # label would be the site and password for the pasword hehe
    with open(password_file, "a") as f: #"a" means APPEND MODE ie used to add new stuff without removing the older one
        f.write(f"{label}: {password}\n")
#- as f → Gives the file a short nickname (f) so we can use it easily.
#f.write writes text into file
#f"{label}: {password} is a F-STRING it replaces label with whatever u provide and also replaces the password with the pass generated

#now we make a function to show all saved passwords
def show_passwords():
    try:# python tries running the code in here if something goes wrong it prints the except situatiom
        with open (password_file,"r") as f:#this opens the password.txt coz of read mode "r"
            print("\nsaved passwords:")
            print(f.read()) #reads the entire file and then prints its contents
    except FileNotFoundError:
        print("no passwords saved by you yet nidhi")

#this functions controls the whole program
def main():
    while True:
        print("\nPassword Manager Menu")
        print("1. Generate a new password")
        print("2. Show saved passwords")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            label = input("What is this password for? ")
            length = int(input("How long should the password be? "))
            password = pass_generator(length)
            print("Your password is:", password) #prints ur pass and shows u
            save_password(label, password) #saves ur pass

        elif choice == "2":
            show_passwords()

        elif choice == "3":
            print("Goodbye, Nidhi!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
main()