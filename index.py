import csv 
import os
from movie import Movie
#1	load_movies(file_name)	
def load_movies(file_name):
    movies = []
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    movie_id = row[0]
                    title = row[1]
                    director = row[2]
                    genre = int(row[3])
                    available_str = row[4].lower()
                    available = True if available_str == 'true' else False
                    price = float(row[5])

                    movie = Movie(movie_id, title, director, genre, available, price)
                    movies.append(movie)
                except (ValueError, IndexError) as e:
                    print(f"Error reading row: {row} - {e}")
        return movies
    else:
        print(f"The catalog file ({file_name}) is not found\nThe movie library management system starts without catalog")
        return movies

#save_movies(file_name, movies)
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
# rent_movie(movies, movie_id)
def rent_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == movie_id:
            if movie.get_availability():
                movie.borrow_movie()
                print(f"Movie '{movie.get_title()}' has been rented.")
                return
            else:
                print(f"Movie '{movie.get_title()}' is already rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")
# return_movie(movies, movie_id)
def return_movie(movies, movie_id):
    for movie in movies:
        if movie.get_id() == movie_id:
            if not movie.get_availability():
                movie.return_movie()
                print(f"You have successfully returned '{movie.get_title()}'.")
                return
            else:
                print(f"'{movie.get_title()}' was not rented.")
                return
    print(f"Movie with ID '{movie_id}' not found.")
# add_movie(movies)
# remove_movie(movies)
def update_movie_details(movies):
    movie_id = int(input("Enter the movie ID to update: "))
    for movie in movies:
        if movie.get_id() == movie_id:
            print("Current details:")
            print(movie)
            title = input("Enter new title (leave blank to keep current): ")
            if title:
                movie.set_title(title)
            director = input("Enter new director (leave blank to keep current): ")
            if director:
                movie.set_director(director)
            genre = int(input("Enter new genre (leave blank to keep current): "))
            if genre:
                movie.set_genre(genre)
            price = float(input("Enter new price (leave blank to keep current): "))
            if price:
                movie.set_price(price)
            fine_rate = float(input("Enter new fine rate (leave blank to keep current): "))
            if fine_rate:
                movie.set_fine_rate(fine_rate)
            print(f"Movie '{movie.get_title()}' details updated.")
            return
        else:
            print("Movie not found.")
# list_movies_by_genre(movies)
# check_availability_by_genre(movies)
# display_library_summary(movies)
# top_rented_movies(movies)
# print_movies(movies)
# movie_index(movies, movie_id)
def main():
    input_file = input("Enter the catalog file name: ")
    movies = load_movies(input_file)
    choice = ""
    while choice != "0":
        print_menu()
        choice = input("Enter your selection: ")
        if choice == "0":
            update_catalog = input("Would you like to update the catalog (yes/y, no/n)? ")
            if update_catalog.lower() == 'yes' or 'y':
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
            check_availability_by_genre(movies)
        elif choice == "9":
            display_library_summary(movies)
        elif choice == "10":
            top_rented_movies(movies)
        else:
            print("Invalid choice. Please try again.")
  

if __name__ == "__main__":
    main()