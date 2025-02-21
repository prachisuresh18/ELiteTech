Email_ID=input("Enter your email ID: ")
index_of_attherate=0
for i in range(len(Email_ID)):
    if Email_ID[i]=="@":
        index_of_attherate=i
        break  
if index_of_attherate>0:
    Username=Email_ID[:index_of_attherate]
    Domain=Email_ID[index_of_attherate+1:]
    print("Username: ",Username)
    print("Domain: ",Domain)
else:
    print("Invalid email format. Please enter a valid email.")

'''
output

Enter your email ID : prachisuresh2018@gmail.com
Username: prachisuresh2018
Domain: gmail.com
'''
'''
output

Enter your email ID: aayAjay Ajay AjayAjaAjA
Invalid email format. Please enter a valid email.

'''