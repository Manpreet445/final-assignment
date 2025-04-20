''' 
Project: Movie Library Management System
Description: This program is a movie library management system that 
allows users to search, rent, return, add, remove, update, and list 
movies by genre. It also provides options to check availability by genre and display the library summary.
made by : Manpreet Singh,Patrick Chavez,Anthony Nwachukwu Ogamba
'''
import csv 
import os
from movie import Movie
#1	load_movies(file_name)	
'''this function loads the movies from a CSV file and returns a list of Movie objects'''
def load_movies(file_name):
    movies = []
    #Check if file exists
    if os.path.exists(file_name):
        
        with open(file_name, 'r') as csvfile:    #reads the csv file
            reader = csv.reader(csvfile)
            #goes through each row-value in the csv file and creates a movie object
            for row in reader:
                movie_id = int(row[0])
                title = row[1]    
                director = row[2]   
                genre = int(row[3])      
                availability = row[4] == 'True' 
                price = float(row[5])
                
                
                #Create movie object and add to list
                movie = Movie(movie_id, title, director, genre, availability, price,)
                movies.append(movie)
                
        return movies
    #if the file does not exist, it will print a message and return an empty list
    else:
        print(f"The catalog file ({file_name}) is not found.\nThe movie library management system starts without catalog.")
        return movies
#save_movies(file_name, movies)
'''this function saves the movies to a CSV file'''
def save_movies(file_name, movies):
    #opens the file in write mode and writes the movie objects to the file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #goes through each movie object and writes the values to the file
        for movie in movies:
            writer.writerow([movie.get_id(), movie.get_title(), movie.get_director(), movie.get_genre(), movie.get_availability(), movie.get_price()])
    print(f"Catalog file '{file_name}' has been updated.")
#print_menu()
'''this function prints the main menu of the movie library management system'''
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
'''this function searches for movies by title, director, or genre and prints the results'''
def search_movies(movies, search_term):
    results = []  # List to store matching movies
    search_term = search_term.strip().lower()  # Make the search term lowercase to make it case-insensitive
    for movie in movies:
        #this if will check if the search term is in the title, director, or genre and append it to the results list
        if (search_term in (movie.get_title()).lower() or 
            search_term in (movie.get_director()).lower() or 
            search_term in (movie.get_genre_name()).lower()):
            results.append(movie)
    #if the results list is not empty, it will print the results in a formatted table        
    if results != []:
        print(f"Finding ({search_term}) in title, director, or genre...")
        print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}  {'Price $':<2}   {'Rental Count':<10}")
        print("-" * 114)
        for movie in results:
            if movie.get_availability() == "True":
                available = "Available"
            else:
                available = "Rented"
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}   {movie.get_price():<2}         {movie.get_rental_count():<10}")
    #if the results list is empty, it will print a message saying no matching movies were found
    else:
        print(f"Finding ({search_term}) in title, director, or genre...")
        print("No matching movies found.")


# rent_movie(movies, movie_id)
'''this function rents a movie by changing its availability status and updating the rental count'''
def rent_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):        # Check if the movie ID matches
            if movie.get_availability() == "True": # Check if the movie is available
                movie.borrow_movie()               # Change availability to rented   
                save_movies('movies.csv', movies)  # Save the updated movies list to the CSV file
                print(f"Movie '{movie.get_title()}' has been rented.")
                return
            else:                                  # If the movie is already rented
                # Print a message saying the movie is already rented
                print(f"Movie '{movie.get_title()}' is already rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")
# return_movie(movies, movie_id)
def return_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):  # Check if the movie ID matches
            if movie.get_availability() == "False": # Check if the movie is rented
                movie.return_movie()         # Change availability to available
                save_movies('movies.csv', movies)  # Save the updated movies list to the CSV file
                print(f"You have successfully returned '{movie.get_title()}'.")
                return
            else:                            # If the movie is already available
                # Print a message saying the movie is not rented
                print(f"'{movie.get_title()}' was not rented.")
                return
    # If the movie ID is not found in the list of movies
    print(f"Movie with ID '{movie_id}' not found.")

# add_movie(movies)
'''this function adds a new movie to the list of movies and saves it to the CSV file'''
def add_movie(movies):
    movie_id = input("Enter movie ID: ")
    for movie in movies:
        # Check if the movie ID already exists in the list
        if movie.get_id() == int(movie_id):
            print("Movie ID already exists.")
            return
    # Prompt the user for movie details
    # and create a new Movie object 
    title = input("Enter title: ").title()
    director = input("Enter director: ").title()
    genre = int(input("Enter genre (0-9): "))
    # Check if the genre is valid (0-9)
    if genre < 0 or genre > 9:
        print("Invalid genre. Please enter a number between 0 and 9.")
        return
    availability = True
    price = float(input("Enter price: "))
    price = round(price, 2) 
    #Adds the new movie to the list of movies
    new_movie = Movie(int(movie_id), title, director, genre, availability, price, 0)
    movies.append(new_movie)
    #Saves to CSV file
    save_movies('movies.csv', movies)
    print(f"Movie '{title}' added successfully.")


# remove_movie(movies)
'''this function removes a movie from the list of movies and saves it to the CSV file'''
def remove_movie(movies):
    movie_id = input("Enter the movie ID to remove: ").strip()  
    for movie in movies:
        if str(movie.get_id()) == movie_id: # Check if the movie ID matches  
            movies.remove(movie)         # Remove the movie from the list
            save_movies('movies.csv', movies)  # Save the updated movies list to the CSV file
            print(f"Movie '{movie.get_title()}'has been removed.")
            return
    # If the movie ID is not found in the list of movies
    print(f"Movie with ID '{movie_id}' not found.")



# update_movie_details(movies)
'''this function updates the details of a movie and saves it to the CSV file'''
def update_movie_details(movies):
    movie_id = int(input("Enter the movie ID to update: "))
    for movie in movies:
        # Check if the movie ID matches
        # and prompt the user for new details
        if movie.get_id() == movie_id:
            print("Leave fields blank to keep current values.")
            # Prompt the user for new details
            # and update the movie object using setters

            title = input(f"Enter new title (Current: {movie.get_title()}): ").strip().title() 
            # Check if the title is blank
            # If the title is not blank, update it
            if title != "":
                movie.set_title(title)
            
            # check if the director is blank
            # If the director is not blank, update it
            director = input(f"Enter new director (Current: {movie.get_director()}): ").strip().title()
            if director != "":
                movie.set_director(director)
            
            # check if the genre is blank
            # If the genre is not blank, update it
            genre = input(f"Enter new genre (Current:{movie.get_genre_name()}): ").strip()
            if genre != "":
                genre_num = int(genre)
                if 0 <= genre_num <= 9:
                    movie.set_genre(genre_num)
                else:
                    print("Invalid genre. Please enter a number between 0 and 9.")
                    return
            
            # check if the availability is blank    
            # If the availability is not blank, update it
            price = input(f"Enter new price (Current:{movie.get_price()}): ").strip()
            if price != "":
                price_val = float(price)
                movie.set_price(round(price_val, 2))
            
            print(f"Movie with ID '{movie_id}' is updated successfully.")
            save_movies('movies.csv', movies)  
            return
    # If the movie ID is not found in the list of movies
    print("Movie not found.")
# list_movies_by_genre(movies)
'''this function finds all movies by genre and list the results'''
def list_movies_by_genre(movies):
    # Prompt the user for a genre and find all movies in that genre
    genre = int(input("Enter the genre (0-9): "))
    matching_movies = []  # List to store matching movies
    
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}{'Price $':>6}")
    print("-" * 105)
    
    for movie in movies:
        if movie.get_genre() == genre:  # Check if the movie genre matches the input genre
            # Check if the movie is available or rented
            if movie.get_availability() == "True":
                available = "Available"
            else:
                available = "Rented"
            # Append the movie details to the matching_movies list
            matching_movies.append(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}{movie.get_price():>6}")
    # Print the matching movies
    if matching_movies:  # Check if there are any matching movies
        for movie_line in matching_movies:
            print(movie_line)
    else:
        print(f"No movies available in genre {genre}.")
# check_availability_by_genre(movies)
'''this function checks the availability of movies by genre and prints the results'''
def check_availability_by_genre(movies):
    # Prompt the user for a genre and find all available movies in that genre
    genre = int(input("Enter the genre (0-9): "))
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}{'Price $':<6}")
    print("-" * 95)
    for movie in movies:
        if movie.get_genre() == genre and movie.get_availability() == "True":  # Check if the movie genre matches the input genre and is available
            # Print the movie details
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{'Available':<12}{movie.get_price():<6}")
            break
    else:
        print(f"No movies available in genre {genre}.")


# top_rented_movies(movies)
def top_rented_movies(movies):
    # Sort the movies by rental count in descending order
    # and print the top 5 rented movies
    sorted_movies = sorted(movies, key=lambda movie: movie.get_rental_count(), reverse=True)
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}{'Price $':<6}")
    print("-" * 95)
    
    for movie in sorted_movies[:5]: 
        if movie.get_availability() == "True":
                available = "Available"
        else:
            available = "Rented"
        print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}{movie.get_price():<6}")


# print_movies(movies)
'''this function prints the movies in a formatted table'''
def print_movies(movies):
    # Print the movies in a formatted table
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availablity':<12}{'Price $':<6} {'<Rental Count':<10}")
    print("-" * 95) 
    #loops through each movie object and prints the values in a formatted table
    for movie in movies:
        print(f"{movie[0]:<4}{movie[1]:<35}{movie[2]:<25}{movie[3]:<15}{movie[4]:<12}{movie[5]:<6} {movie[6]:<10}")

# movie_index(movies, movie_id)
'''this function finds the index of a movie in the list of movies by its ID'''
def movie_index(movies,movie_id):
    for movie in movies:
        if movie[0] == movie_id: # Check if the movie ID matches
            return movies.index(movie) # Return the index of the movie in the list
    # If the movie ID is not found in the list of movies
        else:
            print(f"Movie with ID {movie_id} not found.")
            return 
#display_libary_summary(movies)
'''this function displays the summary of the movie library'''
def display_library_summary(movies):
    # Print the summary of the movie library
    total_movies = len(movies)      # Get the total number of movies
    available_movies = 0
    for movie in movies:
        if movie.get_availability() == "True": # Check if the movie is available
            available_movies += 1         # Increment the available movies count
    unavailable_movies = total_movies - available_movies # Calculate the unavailable movies count
    # Print the summary
    print(f"Total Movies: {total_movies}")
    print(f"Available Movies: {available_movies}")
    print(f"Unavailable Movies: {unavailable_movies}")
# main()
'''this function is the main function that runs the movie library management system'''
def main():
    file_name = input("Enter the catalog file name: ")   # Prompt the user for the catalog file name
    movies = load_movies(file_name)     # Load the movies from the CSV file
    choice = ""                # Initialize the choice variable
    while choice != "0":        # Loop until the user chooses to exit
        # Print the main menu and prompt the user for a choice
        print_menu()
        choice = input("Enter your selection: ")            # Prompt the user for a choice
        # Check the user's choice and call the corresponding function
        if choice == "0":                                                                   
            update_catalog = input("Would you like to update the catalog (yes/y, no/n)? ")      # Prompt the user to update the catalog
            # Check if the user wants to update the catalog
            if update_catalog.lower() == 'yes'or'y':
                save_movies(file_name, movies)          # Save the updated movies list to the CSV file
            else:
                print("Movie catalog has not been updated.")
            print("Goodbye!")
        elif choice == "1":
            search_term = input("Enter the search term: ")
            search_movies(movies, search_term)
        elif choice == "2":
            movie_id = input("Enter the movie ID to rent: ")
            rent_movie(movies, movie_id)
        elif choice == "3":
            movie_id = input("Enter the movie ID to return: ")
            return_movie(movies, movie_id)
        elif choice == "4":
            add_movie(movies)
        elif choice == "5":
            remove_movie(movies)
        elif choice == "6":
            update_movie_details(movies)
        elif choice == "7":
            list_movies_by_genre(movies)
        elif choice == "8":
            top_rented_movies(movies)
        elif choice == "9":
            check_availability_by_genre(movies)
        elif choice == "10":
            display_library_summary(movies)
        else:
            print("Invalid choice. Please try again.")
  

if __name__ == "__main__":
    main()