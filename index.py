'''
Project Name: Movie Library Management System
Description: A Python application designed to manage a movie library system. 
             This system allows users to search, rent, return, add, remove, and update movies. 
             It also provides features to list movies by genre, check availability, view top rented movies, 
             and display a summary of the library.
Group Members: Patrick, Manpreet, Anthony
'''

import csv 
import os
from movie import Movie
#1	load_movies(file_name)	
'''Loads movies from a CSV file and returns them into a list of Movie objects.'''
def load_movies(file_name):
    movies = []
    #Check if file exists
    if os.path.exists(file_name):
        
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: #CSV files require rows to be used instead of lines
                movie_id = int(row[0])
                title = row[1]    
                director = row[2]   
                genre = int(row[3])      
                availability = row[4] == 'True' #This is NOT a real boolean value. It references a string inside the .csv file.
                price = float(row[5])
                
                
                #Create movie object and add to list
                movie = Movie(movie_id, title, director, genre, availability, price,)
                movies.append(movie)
                
        return movies
    else: #If the file does not exist, return an empty list
        print(f"The catalog file ({file_name}) is not found.\nThe movie library management system starts without catalog.")
        return movies

#save_movies(file_name, movies)
'''Any function that calls this function will save their updates to the CSV file'''
def save_movies(file_name, movies):
    with open(file_name, 'w', newline='') as csvfile:   
        writer = csv.writer(csvfile)    ##Open the file in write mode
        for movie in movies:  ##Iterate through the list of movies and write each movie's details to the CSV file
            #Get the details of each movie using the getters from the Movie class
            writer.writerow([movie.get_id(), movie.get_title(), movie.get_director(), movie.get_genre(), movie.get_availability(), movie.get_price()])

#print_menu()
'''Displays the main menu of the movie library system.'''
def print_menu():
    print("\nMovie Library - Main Menu")
    print("="*25)
    print("1) Search for movies")
    print("2) Rent a movie")
    print("3) Return a movie")
    print("4) Add a movie")
    print("5) Remove a movie")
    print("6) Update movie details")
    print("7) List movies by genre")
    print("8) Top rented movies")
    print("9) Check availability by genre")
    print("10) Display library summary")
    print("0) Exit the system")

# search_movies(movies, search_term)
'''This function will search for movies based on the title, director, or genre.'''
def search_movies(movies, search_term):
    results = []
    search_term = search_term.strip().lower()  # Make the search term lowercase to make it case-insensitive
    for movie in movies:
        #this if will check if the search term is in the title, director, or genre and append it to the results list
        if (search_term in (movie.get_title()).lower() or #Uses the getters from the Movie class
            search_term in (movie.get_director()).lower() or 
            search_term in (movie.get_genre_name()).lower()):
            results.append(movie)
            
    if results != []: #Main process if the results list is not empty
        print(f"Finding ({search_term}) in title, director, or genre...")
        print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}  {'Price $':<2}  {'Rental Count':<10}")
        print("-" * 114)
        for movie in results:
            if movie.get_availability() == "True": #Checking for availability
                available = "Available"
            else:
                available = "Rented"
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}   {movie.get_price():<2}    {movie.get_rental_count():<10}")
    else:
        print(f"Finding ({search_term}) in title, director, or genre...")
        print("No matching movies found.")

# rent_movie(movies, movie_id)
'''This function will rent a movie if it is available. Also adds to the rental count.'''
def rent_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):  #Checks for a matching movie ID
            if movie.get_availability() == "True":
                movie.borrow_movie()  #Mark as not available
                save_movies('movies.csv', movies)  
                print(f"You have successfully rented '{movie.get_title()}'.")
                return  
            else:
                print(f"Movie '{movie.get_title()}' is already rented.")
                return
    print(f"Movie with ID {movie_id} not found.")

# return_movie(movies, movie_id)
'''This function will return a movie if it is rented.'''
def return_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):  
            if movie.get_availability() == "False":    #Checks for a matching movie ID
                movie.return_movie()  #Mark as available
                save_movies('movies.csv', movies)  
                print(f"You have successfully returned '{movie.get_title()}'.")
                return
            else:
                print(f"'{movie.get_title()}' was not rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")

# add_movie(movies)
'''This function will add a new movie to the list of movies.'''
def add_movie(movies):
    movie_id = input("Enter movie ID: ")
    for movie in movies:
        if movie.get_id() == movie_id: #Checks for a matching movie ID, doesn't continue if it exists
            print(f"Movie with ID {movie_id} exists.")
            return
    title = input("Enter title: ").title()
    director = input("Enter director: ").title()
    genre = int(input("Enter genre (0-9): "))
    if genre < 0 or genre > 9:
        print("Invalid genre. Please enter a number between 0 and 9.")
        return
    availability = True #Not a boolean value, but a string in the CSV file
    price = float(input("Enter price: "))
    price = round(price, 2) # Ensures the price is 2 decimal places
    #Adds the new movie to the list of movies
    new_movie = Movie(int(movie_id), title, director, genre, availability, price, 0)
    movies.append(new_movie) 
    save_movies('movies.csv', movies) #Saving to the CSV file
    print(f"Movie '{title}' added successfully.")

# remove_movie(movies)
'''This function will remove a movie from the list of movies. '''
def remove_movie(movies):
    movie_id = input("Enter the movie ID to remove: ").strip()  
    for movie in movies:
        if str(movie.get_id()) == movie_id:  
            movies.remove(movie)  #Removes the movie from the list 
            save_movies('movies.csv', movies) #Saving to CSV
            print(f"Movie '{movie.get_title()}' has been removed.")
            return
    print(f"Movie with ID {movie_id} not found.")

# update_movie_details(movies)
'''This function will update the details of an existing movie.'''
def update_movie_details(movies):
    movie_id = int(input("Enter the movie ID to update: "))
    for movie in movies:
        if movie.get_id() == movie_id:
            print("Leave fields blank to keep current values.")
            title = input(f"Enter new title (Current: {movie.get_title()}): ").strip().title()
            #Check if the title is not empty
            #If the title is empty, it will not update the current title
            #doing the same for all the rest of the fields
            #If the title is not empty, it will update the current title
            if title != "":
                movie.set_title(title)
            
            director = input(f"Enter new director (Current: {movie.get_director()}): ").strip().title()
            if director:
                movie.set_director(director)
            
            genre = input(f"Enter new genre (Current:{movie.get_genre_name()}): ").strip()
            if genre != "":
                #Check if the genre is a valid number between 0 and 9
                genre_num = int(genre)
                if 0 <= genre_num <= 9:
                    movie.set_genre(genre_num)
                else:
                    print("Invalid genre. Please enter a number between 0 and 9.")
                    return
            
            price = input(f"Enter new price (Current:{movie.get_price()}): ").strip()
            if price != "":     
                #Check if the price is a valid number
                price_val = float(price)
                movie.set_price(round(price_val, 2)) #Again, ensures that the price is 2 decimal places
            
            print(f"Movie with ID '{movie_id}' is updated successfully.")
            save_movies('movies.csv', movies)  
            return
    print(f"Movie with ID {movie_id} is not found.")

# list_movies_by_genre(movies)
'''this function will list all movies of a specific genre.'''
def list_movies_by_genre(movies):
    genre = int(input("Enter the genre (0-9): "))
    matching_movies = []
    
    for movie in movies:
        if movie.get_genre() == genre:
            if movie.get_availability() == "True":    #Checking for availability
                available = "Available"  ##If the movie is available, it will show "Available"
            else:
                available = "Rented"
            matching_movies.append(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}   {movie.get_price():<2}    {movie.get_rental_count():<10}")
    
    if matching_movies != []: #Main process if the matching movies list is not empty
        print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}   {'Price $':<1} {'Rental Count':<10}")
        print("-" * 105)
        for movie_line in matching_movies:
            print(movie_line)     
    else:
        print(f"Invalid Genre: Enter a valid genre (0-9)")

# check_availability_by_genre(movies)
'''This function will check the availability of movies by genre. Lists all available movies of a specific genre.'''
def check_availability_by_genre(movies):
    genre = int(input("Enter the genre (0-9): ")) 
    available_movies = [] #List to store available movies of the specified genre
    for movie in movies:
        if movie.get_genre() == genre and movie.get_availability() == "True":  #Check if the movie is available and matches the genre'
            available = "Available"
            available_movies.append(movie)
    #If there are available movies, print their details
    if available_movies:
        print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}   {'Price $':<1} {'Rental Count':<10}")
        print("-" * 105)
        for movie in available_movies:
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}   {movie.get_price():<2}    {movie.get_rental_count():<10}")
    else:
        print(f"No movies available in genre {genre}.")

# top_rented_movies(movies)
'''This function will list the top 5 most rented movies.'''
def top_rented_movies(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.get_rental_count(), reverse=True) # The lambda function sorts the movies by rental count in descending order
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}    {'Rentals':<1}")
    print("-" * 100)
    
    for movie in sorted_movies[:5]: # Show top 5 most rented movies
        if movie.get_availability() == "True": #Checking for availability
            available = "Available"  ##If the movie is available, it will show "Available"
        else:
            available = "Rented"  ##If the movie is not available, it will show "Rented"
        print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}    {movie.get_rental_count():<1}")

# print_movies(movies)
'''This function will print all movies in the list.'''  
def print_movies(movies):
    ## Print the header for the movie list
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}   {'Price $':<1}    {'Rental Count':<10}")
    print("-" * 105) 
    ## Iterate through the list of movies and print their details
    for movie in movies:
        print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{movie.get_availability:<12}    {movie.get_price():<2}    {movie.get_rental_count():<10}")

# movie_index(movies, movie_id)
'''Helper function to find the index of a movie in the list based on its ID.'''
def movie_index(movies,movie_id):
    movie_id = input("Enter the movie ID: ").strip()
    for movie in movies:
        if movie.get_id() == movie_id:   
            return movies.index(movie)   #Returns the index of the movie in the list
        else:
            print(f"Movie with ID {movie_id} not found.")
            return 

#display_libary_summary(movies)
'''This function will display a summary of the movie library: total movies, available movies, and unavailable movies.'''
def display_library_summary(movies):
    total_movies = len(movies)
    available_movies = 0
    for movie in movies:
        if movie.get_availability() == "True": ##Checking for availability
            available_movies += 1   #Counting the available movies
    unavailable_movies = total_movies - available_movies #Calculating the unavailable movies
    print(f"Total Movies: {total_movies}")
    print(f"Available Movies: {available_movies}")
    print(f"Unavailable Movies: {unavailable_movies}")

# main()
'''This function will run the main program loop, allowing the user to interact with the movie library system.'''
def main():
    file_name = input("Enter the catalog file name: ")  #For loading the catalog file
    movies = load_movies(file_name)   #Loading the movies from the CSV file
    choice = ""        ## Initialize choice to an empty string
    print_menu()
    while choice != "0":    ## Loop until the user chooses to exit
        choice = input("Enter your selection: ")  
        if choice == "0": 
            update_catalog = input("Would you like to update the catalog (yes/y, no/n)? ") #For updating the catalog
            if update_catalog.lower() == 'yes' or 'y':   #If the user wants to update the catalog
                save_movies(file_name, movies)  #Saving the movies to the CSV file
                print("Movie catalog has been updated. Goodbye!")
            else:
                print("Movie catalog has not been updated. Goodbye!")
           #call the functions based on the user's choice
        elif choice == "1":
            search_term = input("Enter the search term: ")
            search_movies(movies, search_term)
            print_menu()
        elif choice == "2":
            movie_id = input("Enter the movie ID to rent: ")
            rent_movie(movies, movie_id)
            print_menu()
        elif choice == "3":
            movie_id = input("Enter the movie ID to return: ")
            return_movie(movies, movie_id)
            print_menu()
        elif choice == "4":
            add_movie(movies)
            print_menu()
        elif choice == "5":
            remove_movie(movies)
            print_menu()
        elif choice == "6":
            update_movie_details(movies)
            print_menu()
        elif choice == "7":
            list_movies_by_genre(movies)
            print_menu()
        elif choice == "8":
            top_rented_movies(movies)
            print_menu()
        elif choice == "9":
            check_availability_by_genre(movies)
            print_menu()
        elif choice == "10":
            display_library_summary(movies)
            print_menu()
        else:
            print("Invalid choice. Please try again.")
  

if __name__ == "__main__":
    main()