#cretae a print function that prints
# out of the string "hello world"
print("hello World")
#Ask user for day of the week 
# day_of_week=input("What day of the week is it?")
# print("Today is"+ day_of_week)
#concatenation is when you add two strings together
#using a plus sign(+)
# movies_this_week=input("What movies are you watching this week?")
# print("I am watching "+ movies_this_week+ " this week")
# mood=input("how are you feeling today?")
# print("I am feeling"+mood)

#data types for variables in python
#strings-text
name="john"# this is a string data type
#whenever its wrapped in qoutes its a string
year="2024"

#integers- whole numbers
year=2024 # this is an integer data type
#does need to be wrapped in qoutes
yearfourfromnow=2028
subtract=yearfourfromnow-year
print(subtract)

#floats- decimal numbers
pricebigmac= 3.99 #this is a float data type
pricedoublepounder=4.99
totalprice=pricebigmac+pricedoublepounder
print(totalprice)
#neweds to have a decimal point

#booleans- true or false
israining= False # this is a boolean data type
print(israining)

#lists- a collection of items
groceries=("apples "+" banannas"+" carrots")
print(groceries)

#challenge 1
#you and your family are going to a movie and a dinner> You need a list of movies to choose from
#place of resturant
#time of movie
#time of dinner
#name of movie
#price of movie
#price of dinner 
#is the movie playing in the evening?
#how many people are going
#print in one sentence

movies=("beetleJuice"+"Deadpool and wolverine"+"Inside out")
print(movies)
dinner="Chilis"
movietime="6:00 pm"
dinnertime=("10:00 pm")
moviename=("beetlejuice")
movieprice=10.45
dinnerprice= 20.50
eveningtime= True
howmany= 6
peoplegoing=int(input("how many people are going?"))

print("We are going to see"+moviename+"at"+movietime+"and then eat dinner at"+dinner+"at"+dinnertime+"with"+peoplegoing+"people")
