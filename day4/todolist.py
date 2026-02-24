todo_file = "tasks.txt" #tasks.txt is a text file where all the tasks are stored
def add_task(task):# task is a parameter ie a placeholder variable that the function expects when u call it, when u give the program ur task it gets stored there
    with open (todo_file, "a") as f:#opens task.txt in append mode
     f.write(f"{task}\n") #writes the task into the file
    print(f"task added: {task}")
def show_task():
   try:
      with open(todo_file, "r") as f:
         tasks= f.readlines()  #reads all the lines inot a list each line = one task
         if tasks:
            print("\nyour tasks:")
            for i, task in enumerate(tasks, start=1): #Loops through tasks, numbering them starting at 1.
               print(f"{i} . {task.strip()}") #.strip is used to remove spaces
         else:
            print("no tasks yet")


   except FileNotFoundError:
      print("no tasks saved yet")      

def main():
   while True:
      print("\n to-do list menu")
      print("1 add a task")
      print("2. Show tasks")
      print("3. Exit")
      choice = input("Enter your choice (1/2/3): ")
      if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
      elif choice == "2":
            show_task()
      elif choice == "3":
          print("Goodbye from Nidhi, Stay productive!")
          break
      else:
          print("Invalid choice, try again.")
main()

