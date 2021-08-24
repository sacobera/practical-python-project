temp = 75 
forecast = "sunny"


IF ELIF 
if temp > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temp < 60:
    print("It's too cold!")
else: 
    print("Enjoy the outdoors")

OR 
if temp > 80 or temp < 60:
    print("Stay inside!")
else: 
    print("Enjoy the outdoors!")

#AND
if temp < 80 and forecast != "rain":
    print ("Go outside")
else:
    print("Stay inside")

#NOT 
if not forecast == "rain": #not and == equals to False;  not and != equals to TRUE
    print("Go outside!")
else:
    print("Stay inside!")

# boolean
raining = True

if not raining:
    print("Go outside!")
else:
    print("Stay inside! ")
