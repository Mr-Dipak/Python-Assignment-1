''' 
1. Create 3 variables to store street, city and country, now create address variable to store entire address.
Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, 
city and country prints in a separate line

'''

street = "Chalisgaon Road "
city = "Kannad "
country = "India"

address = street + city + country
print("This Output is printed by using + operator: " + address)

address2 = f"{street}{city}{country}"
print("This output is printed by using f-string: "+address2)




