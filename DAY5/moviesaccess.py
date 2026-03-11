import smtplib #smtp= simple mail tranfer protocol
from email.mime.text import MIMEText
#Go into Python’s email library, open the MIME toolbox, then open the text section, and bring me the MIMEText class so I can use it to create plain text emails.
#MIME= MULTIPURPOSE INTERNET MAIL EXTENTIONS
def send_mail(to_email, child_name, status):
    #this is the function to take childs email, name and their denied or accepted status
    msg= MIMEText(f"hello{child_name}, your movie access status = {status}")#CREATES AN ACTUAL EMAIL BODY
    msg['subject']= "movie access reult"
    msg['from']= "nidhifake@gmail.com"
    msg['to']= to_email

    #this is just a concept
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login("nidhifake@gmail.com", " password") #these are not real
        server.send_message(msg)

def movie_access():
    print("this is the movie access scanner")
    with open("movie_log.txt","a") as log:
        while True:
            child_name=input("enter child name (or type 'exit' to stop):" )
            if child_name.lower()==  "exit":
                print("scanner shutting down...")
                break
            #ERROR 
            try:
                age = int(input(f"Enter {child_name}'s age: "))
                if age < 0:
                    print(" Age cannot be negative. Try again.")
                    continue
            except ValueError:
                print(" Invalid age. Please enter a number.")
                continue

            aadhaar = input(f"Enter {child_name}'s Aadhaar number: ")
            email = input(f"Enter {child_name}'s email: ")

            # Decide status
            if age >= 18:
                status = " Allowed"
            else:
                status = " Denied"

            result = f"{child_name} | Age: {age} | Aadhaar: {aadhaar} | Email: {email} | Status: {status}\n"
            print(result.strip())
            log.write(result)

            # Error handling for choice input
            choice = input("Do you want the result sent to your email? (yes/no): ").strip().lower()
            if choice == "yes":
                try:
                    send_mail(email, child_name, status)
                    print("Email sent successfully.")
                except Exception as e:
                    print(f"Failed to send email: {e}")
            elif choice == "no":
                print("Result not sent to email, only printed.")
            else:
                print("Invalid choice. Result only printed.")

movie_access()

