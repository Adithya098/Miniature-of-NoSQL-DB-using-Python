import os
import time
import json
import datetime



class File_control:
    def __init__(self,postion):
        self.position=postion
        self.localdata=""
        self.list1=["Name","Dept","Role","E-Mail","Salary","TTL(in seconds)"]
        self.set1=set()
        self.time1={}

    def create(self):
        ne=int(input("Enter the no.of employees:")) # Asking the user to enter the no.of Employees
        print("Enter the following details of Employee:")
        final=[]
        final1={}
        for k in range(1,ne+1): #taking the inputs in for loop
            while(True):                                          #This whole while loop is for checking and alerting if user is already creating the existing user
                n1=str(input("Enter the key to save:"))
                if(n1 not in self.set1):
                    self.set1.add(n1)                            # A set is maintained in order to store the keys for previous records
                    break
                print("All ready present!")                      #alerting the user if he creates existing record
            dict1={}
            for i in range(len(self.list1)):
                print("Enter input for",self.list1[i]+str(k)+":")  # entering the details of employee in a dictionary
                dict1[self.list1[i]]=str(input())
            dict1["Time Created"]=int(time.time())               #adding a timestamp in the user details
            final1[n1]=dict1
            self.time1[n1]=int(time.time())
        final.append(final1)                                    #updating  as a dict with all the values as value and key as given key
        self.localdata=final
        with open(self.position,"w") as f:
            json.dump(self.localdata,f)                         #saving in json file

    def print1(self):
        file1 = open(self.position,"r")                 #opening the json file in given location
        data = json.load(file1)
        print("Updated Json File:")                         #printing the updated json in json format
        print(json.dumps(data, indent = 1))


    def read(self):
        f1 = open(self.position,"r")
        data1 = json.load(f1)
        s=input("Enter the key to check:")
        if(int(self.time1[s]-timenow)<=int(data1[0][s]["TTL(in seconds)"])):  #reading if the time has not exceeded
            print("Details of the employee are:",json.dumps(data1[0][s], indent = 1))
        else:
            print(" TIME limit EXCEEDED , NO Operation can be done !!")      #printing error message when the time has exceeded

    def delete1(self):
        while(True):
            number1=str(input("Enter key of record:")) #taking the key to delete
            print(self.set1)
            if(number1 in self.set1):
                self.set1.remove(number1)  #if the key is present,removing from set
                break
            print("No employee by given name:")  #if not present,asking the user to enter the key present
        with open(self.position, 'r') as f2:
            obj = json.load(f2)
            del1=number1
            if(int(self.time1[del1]-timenow)<=int(obj[0][del1]["TTL(in seconds)"])):
                del obj[0][del1]             #deleting in json file
                print("Employee deleted")
            else:
                print("TIME limit EXCEEDED,Cannot DELETE.")  #if time limit exceeded no operation  is done
        with open(self.position,"w") as f:
            json.dump(obj,f)                 #updating in json with the deleted record

    def update1(self):
        f3 = open(self.position,"r")
        data1 = json.load(f3)
        while(True):
            n1=input("Enter the key:")
            if(n1 not in self.set1):
                self.set1.add(n1)         #adding the key to be added in set for future uses
                break
            print("All ready present!.You can only create new Record . ")   #you cannot create an existing record
        dict2={}
        for k in data1:
            for i in range(len(self.list1)):
                print("Enter input for",self.list1[i]+str(n1)+":")
                dict2[self.list1[i]]=str(input())
            k[str(n1)]=dict2
        self.time1[n1]=int(time.time())          # updating as a dict with key and values as entered by the user
        with open(self.position,"w") as f:
            json.dump(data1,f)

#C:\\Users\\Admin\\Desktop\\DataStructures
pathname=str(input("Enter the path of directory:"))
timenow=time.time()   #current time
if(os.path.exists(pathname)==True):
    print("Proceed")        #if it is valid directory proceed with file creation
else:
    pathname="C:\\Users\\Admin\\Desktop"   #if not a valid directory
    print("Saving in desktop:")

jsonname=str(input("Enter the name of jason name you want to create:"))
path1=str(str(pathname)+"\\"+jsonname+".json")
fc=File_control(path1) #creating the file and creating a new instance the class
continueyn="y"
while(continueyn=="y" or continueyn=="Y"):
    print("You can do the following operations:")
    print("1.Create   | 2.Read [A particular key details]   | 3.Delete    | 4.Update by adding a new Record")
    continueyn=str(input(" Do you want to continue ( y / n) : ")) #asking the user if wants to continue
    if(continueyn=="n"):
        break   #exits if user inputs no
    d=int(input("What operation:"))
    if(d in [1,2,3,4]):
        if(d==1):
            fc.create()
            fc.print1()
        if(d==2):
            fc.read()
        if(d==3):
            fc.delete1()
            fc.print1()
        if(d==4):
            fc.update1()
            fc.print1()
    else:
        print("Enter a valid operation !")  #if the operation is not valid or greater than given input




