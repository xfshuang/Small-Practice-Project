#Repetition - For Loop (Celsius to Fahrenheit)
#Written by: Shirley Huang
#Date: Feb. 22, 2019



#print the table headings.
print("Celcius\tFahrenheit") #/t is tab
print("------------------")

#declare variables 
start = -20
stop = 19 #stopping at 19 because this would include 18
increment = 2

#write a for loop 
for c in range(start, stop, increment): #looping through the range
    f = 9.0/5.0 * c + 32 # c to f calculation
    print(c,'\t', round(f,1)) #round f to 1 decimal place
