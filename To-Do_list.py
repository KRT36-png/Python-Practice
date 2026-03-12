class To_do_list:
    def __init__(self,Task_detail):
        
        self.Task_detail=Task_detail
        with open("Task.txt","a") as file:
            file.writelines(str(self.Task_detail)+'\n')
    
    @staticmethod
    def view_Tasks():
        with open("Task.txt","r") as file:
            content= file.read()
            print(content)
    
            
    @staticmethod
    def delete():
        with open("Task.txt","r") as file:
            content=file.read().splitlines
            i=int(input("Enter the index of the task you want to delete:"))
            content.pop(i-1)
        with open("Task.txt","w") as f:
            f=content
    @staticmethod
    def edit():
        with open("Task.txt","r") as file:
            content=file.read().splitlines
            
            i=int(input("Enter the index of the task you want to edit:"))
            t=input("Enter the edited version you want to edit:")

            content[i-1]=t
        with open("Task.txt","w") as f:
            f.write(content)



        


    
        