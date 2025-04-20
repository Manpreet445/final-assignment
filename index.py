import csv 
import os
from movie import Movie
#1	load_movies(file_name)	
input_file = input("Enter the catalog file name: ")
def load_movies(file_name):
    movies = []
    #Check if file exists
    if not os.path.exists(file_name):
        
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #Skip empty rows
                if not row:
                    continue

                movie_id = int(row[0])
                title = row[1]    
                director = row[2]   
                genre = int(row[3])      
                availability = row[4] == 'True' 
                price = float(row[5])
                rental_count = int(row[6]) if len(row) > 6 else 0  #Default to 0 if not present
                
                #Create movie object and add to list
                movie = Movie(movie_id, title, director, genre, availability, price, rental_count)
                movies.append(movie)
                
        return movies
    else:
        print(f"The catalog file ({file_name}) is not found.\nThe movie library management system starts without catalog.")
        return movies
#save_movies(file_name, movies)
#Any function with this function in it will save their updates to the CSV file
def save_movies(file_name, movies):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow([movie.get_id(), movie.get_title(), movie.get_director(), movie.get_genre(), movie.get_availability(), movie.get_price(), movie.get_rental_count()])
    print(f"Catalog file '{file_name}' has been updated.")
#print_menu()
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
def search_movies(movies, search_term):
    results = []
    search_term = search_term.strip().lower()  # Make the search term lowercase to make it case-insensitive
    for movie in movies:
        if (search_term in (movie.get_title()).lower() or 
            search_term in (movie.get_director()).lower() or 
            search_term in (movie.get_genre_name()).lower()):
            results.append(movie)
    
    if results:
        print(f"Finding ({search_term}) in title, director, or genre...")
        print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}   {'Price $':<2}")
        print("-" * 95)
        for movie in results:
            if movie.get_availability() == "True":
                available = "Available"
            else:
                available = "Rented"
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}   {movie.get_price():<2}")
    else:
        print(f"Finding ({search_term}) in title, director, or genre...")
        print("No matching movies found.")
# rent_movie(movies, movie_id)
def rent_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):  
            if movie.get_availability() == "True":
                movie.borrow_movie()  
                save_movies('movies.csv', movies)  
                print(f"Movie '{movie.get_title()}' has been rented.")
                return
            else:
                print(f"Movie '{movie.get_title()}' is already rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")
# return_movie(movies, movie_id)
def return_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == int(movie_id):  
            if movie.get_availability() == "False": 
                movie.return_movie()  
                save_movies('movies.csv', movies)  
                print(f"You have successfully returned '{movie.get_title()}'.")
                return
            else:
                print(f"'{movie.get_title()}' was not rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")
# add_movie(movies)
def add_movie(movies):
    movie_id = input("Enter movie ID: ")
    for movie in movies:
        if movie.get_id() == int(movie_id):
            print("Movie ID already exists.")
            return
    title = input("Enter title: ").title()
    director = input("Enter director: ").title()
    genre = int(input("Enter genre (0-9): "))
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
def remove_movie(movies):
    movie_id = input("Enter the movie ID to remove: ").strip()  
    for movie in movies:
        if str(movie.get_id()) == movie_id:  
            movies.remove(movie)
            save_movies('movies.csv', movies) 
            print(f"Movie with ID '{movie_id}' removed successfully.")
            return
    print(f"Movie with ID '{movie_id}' not found.")
# update_movie_details(movies)
def update_movie_details(movies):
    movie_id = int(input("Enter the movie ID to update: "))
    for movie in movies:
        if movie.get_id() == movie_id:
            print("Leave fields blank to keep current values.")
            title = input(f"Enter new title (Current: {movie.get_title()}): ").strip().title()
            if title:
                movie.set_title(title)
            
            director = input(f"Enter new director (Current: {movie.get_director()}): ").strip().title()
            if director:
                movie.set_director(director)
            
            genre = input(f"Enter new genre (Current:{movie.get_genre_name()}): ").strip()
            if genre:
                genre_num = int(genre)
                if 0 <= genre_num <= 9:
                    movie.set_genre(genre_num)
                else:
                    print("Invalid genre. Please enter a number between 0 and 9.")
                    return
            
            price = input(f"Enter new price (Current:{movie.get_price()}): ").strip()
            if price:
                price_val = float(price)
                movie.set_price(round(price_val, 2))
            
            print(f"Movie with ID '{movie_id}' is updated successfully.")
            save_movies('movies.csv', movies)  
            return
    print("Movie not found.")

def list_movies_by_genre(movies):
    genre = int(input("Enter the genre (0-9): "))
    matching_movies = []
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}     {'Price $':>6}")
    print("-" * 105)
    
    for movie in movies:
        if movie.get_genre() == genre:
            available = "Available" if movie.get_availability() == "True" else "Rented"
            matching_movies.append(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}{movie.get_price():>6}")
    
    if matching_movies:
        for movie_line in matching_movies:
            print(movie_line)
    else:
        print(f"No movies available in genre {genre}.")
# check_availability_by_genre(movies)
def check_availability_by_genre(movies):
    genre = int(input("Enter the genre (0-9): "))
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}{'Price $':<6}")
    print("-" * 95)
    for movie in movies:
        if movie.get_genre() == genre and movie.get_availability() == "True":
            print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{'Available':<12}{movie.get_price():<6}")
            break
    else:
        print(f"No movies available in genre {genre}.")
# top_rented_movies(movies)
def top_rented_movies(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.get_rental_count(), reverse=True)
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}{'Price $':<6}")
    print("-" * 95)
    
    for movie in sorted_movies[:5]: 
        available = "Available" if movie.get_availability() == "True" else "Rented"
        print(f"{movie.get_id():<4}{movie.get_title():<35}{movie.get_director():<25}{movie.get_genre_name():<15}{available:<12}{movie.get_price():<6}")


# print_movies(movies)
def print_movies(movies):
    print(f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availablity':<12}{'Price $':<6}")
    print("-" * 95) 
    
    for movie in movies:
        print(f"{movie[0]:<4}{movie[1]:<35}{movie[2]:<25}{movie[3]:<15}{movie[4]:<12}{movie[5]:<6}")
# movie_index(movies, movie_id)
def movie_index(movies,movie_id):
    for movie in movies:
        if movie[0] == movie_id:
            return movies.index(movie)
        else:
            print(f"Movie with ID {movie_id} not found.")
            return 
#display_libary_summary(movies)
def display_library_summary(movies):
    total_movies = len(movies)
    available_movies = 0
    for movie in movies:
        if movie.get_availability() == "True":
            available_movies += 1
    unavailable_movies = total_movies - available_movies
    print(f"Total Movies: {total_movies}")
    print(f"Available Movies: {available_movies}")
    print(f"Unavailable Movies: {unavailable_movies}")
# main()
def main():
    
    movies = load_movies(input_file)
    choice = ""
    while choice != "0":
        print_menu()
        choice = input("Enter your selection: ")
        if choice == "0":
            update_catalog = input("Would you like to update the catalog (yes/y, no/n)? ")
            if update_catalog.lower() in ['yes', 'y']:
                save_movies(input_file, movies)
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