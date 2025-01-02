#In this Question, we have one Dictionary contains two keys Male and Female
#our goal is to find all the names that ends with Letter 'I', Following is demonstration and implementation



student= {
    "male":["Gaurav","Sumit","Pratik","Omkar"],
    "female":["Apurva","Vaibhavi","Vaishnavi","Bhavika","gargi"]
}
for key in student.keys(): #To iterate between keys
    for name in student[key]: #To store elements from Dictionary
        last = str(name[-1::]) #checking the last element of all the names
        if "i" in last:
            print(name)#Printing names
        

