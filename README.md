# tech201_controlflow

# Control flow

- Control flow -> flow through a particular decision process in order to solve problems

## if statement

- It decides whether certain statements need to be executed or not. 

````
age = 17

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")
````
It checks for a given condition, if the condition is true, then the set of code present inside the ” if ” block will be executed otherwise not.

## elif and else
- When the initial condition hasn't been met we can use elif 
- More efficient than using multiple if statements. 
- Else is the capture all keyword when other conditions have not been met.
````
 film_rating = "universal"

 if film_rating.lower() == "universal":
     print("All age groups can watch this film")
elif film_rating.lower() == "pg":
     print("General viewing but parental guidance advised")
 elif film_rating.lower() == "12" or film_rating == "12a":
     print("May not be suitable for those under 12 to watch alone. Supervision recommended")
 elif film_rating.lower() == "15":
     print("You must be 15 to watch 15 rated movies in the cinema")
 elif film_rating.lower() == "18":
     print("You must be 18 to watch 18 rated movies in the cinema")
 else:
     print("This is not a correct rating please use universal, pg, 12, 15, 18")
````
 
 In python there are no 'switch statements' or 'case statements'
 
# For Loops
- For loops are used when you have a block of code which you want to repeat a fixed number of times.

````
list_data = [1, 2, 3, 4, 5, 6]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2) # prints 2, 4, 6, 8 etc
````

## Nested loops
- A nested loop is a loop inside a loop.

- The "inner loop" will be executed one time for each iteration of the "outer loop":

````
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
# to access individual data they must first be identified as parts of their original list.
````

# While loops
- With the while loop we can execute a set of statements as long as a condition is true.
- The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 3.


````
x = 0
while x < 10:
     print(f"It's working -> {x}")
      x +=3 # incrementer
# loops while adding incrementer until it gets to 10 so in this case 3,6,9.
````
## Breaks
- With the break statement we can stop the loop even if the while condition is true:


````
 while x < 10:
     print(f"It's working -> {x}")
     if x == 4:
         break
     x += 1
````

