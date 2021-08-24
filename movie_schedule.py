current_movies = {'The Grinch' : "11:00 am",
                    'Rudolph' : "1:00 pm",
                    'Frosty the snowman' : "3:00 PM",
                    'Christmas Vacation': "5:00 PM"}

print ("We're showing the following movies:")
for key in current_movies: #this loops over the list of objects
    print(key) 

movie = input("what movie would you like the showtime for?\n")

showtime = current_movies.get(movie) #if the movie exists, it will get the movie from the list 
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, "is playing at", showtime )
