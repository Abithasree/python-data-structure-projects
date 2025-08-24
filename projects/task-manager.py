
class TaskManager:
    def __init__(self):
        self.tasks=[]
        self.completed_tasks=[]
        self.task_status=[]
        self.all_tasks=[]

    def add_task(self,task):
        self.tasks.append(task)
        self.all_tasks.append(task)
        self.task_status.append(1)
        print("task added :)")

    def list_tasks(self):
        # Implement logic to display all tasks
        j=0
        print("tasks waiting to be completed!:\n")
        if self.tasks !=None:
            for i in self.tasks:
                print("\u26AA "+i+"\n")
        else:
            print("None :)")
        if self.completed_tasks !=None:
            print("completed tasks here!:")
            for comp_task in self.completed_tasks:
                print(f"'{comp_task}' \u2705")
        print("status info of all tasks ever: ") #for future purpose
        print(self.task_status)
        

    def mark_as_completed(self, task_title):
        # Implement logic to mark a task as completed
        for task in self.tasks:
            if task_title in task:
                self.completed_tasks.append(task)
                self.tasks.remove(task)
                break
            else:
                print("task not found")
                break
        index = self.all_tasks.index(task)
        self.task_status[index]=0  
        
        
        if self.completed_tasks !=None:
            for comp_task in self.completed_tasks:
                print(f"'{comp_task}' \u2705")
        

    def remove_task(self, task_title):
        # Implement logic to remove a task from the list
        for task in self.tasks:
            if task_title in task:
                self.tasks.remove(task)
                break
        print(f"'{task}'" + " - removed!")
        

    def search_tasks(self, keyword):
        # Implement logic to search for tasks based on keyword
        key_list =[]
        for task in self.tasks:
            if keyword in task:
                return task
        print("sry task not found, try key words")
                

task_manager = TaskManager()


while(True):

    print("""Welcome to the Task Manager! \n

    1. Add Task \n
    2. List Tasks \n
    3. Mark Task as Completed \n
    4. Remove Task \n
    5. Search Tasks \n
    6. Exit\n
    note: while asking for 'what task?' u can use keywords..u dont have to remember the task!""")
    a = input()
    if a=='6':
        break;
    
    elif a=='1':
        print("whats your task?")
        task=input()
        task_manager.add_task(task)

    elif a=='2':
        task_manager.list_tasks()

    elif a=='3':
        print("got it! what task to be marked?")
        finished_task=input()
        task_manager.mark_as_completed(finished_task)

    elif a=='4':
        print("what task to be removed?")
        rem_task=input()
        task_manager.remove_task(rem_task)

    elif a=='5':
        print("whats the task?")
        keyWord= input()
        found=str(task_manager.search_tasks(keyWord))
        print(f"'{found}'" + " - task found!")
    
#conclusion i am shit smart
# print("hi")
