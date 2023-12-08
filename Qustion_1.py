'''

1. Create 3 variables to store street, city and country, now create address variable to store entire address.
Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, 
city and country prints in a separate line

GitHub Repositories : https://github.com/Mr-Dipak/Python-Assignment-1

'''

street = "Chalisgaon Road "
city = "Kannad "
country = "India"

address = street+"\n" + city + "\n" + country
print("This Output is printed by using + operator: \n" + address)

address2 = f"{street}\n{city}\n{country}"
print("This output is printed by using f-string: \n"+address2)




