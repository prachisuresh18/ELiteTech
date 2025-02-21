phrase = input("Enter a phrase:")
acronym = ""

for i in range(len(phrase)):  
    if i == 0 or phrase[i - 1] == " ": 
        if "A" <= phrase[i] <= "Z":  
            acronym += phrase[i]  

print("Acronym:", acronym)

'''
output:

Enter a phrase:Indian Institute of Technology 
Acronym: IIT
'''