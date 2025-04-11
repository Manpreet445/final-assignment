'''
- File: test_movie.py 
- Description: This program tests the majority of the methods in the Movie class
- Author: @Hamdy Ibrahim
- Version/Date: Winter 2025
'''
# Import the Movie class
from movie import Movie

def main():
    # Create a list containing 3 movies (test the constructor)
    movie_list = []
    movie_list.append(Movie(1, "Inception", "Christopher Nolan", 4, True, 5.99, 1.50))
    movie_list.append(Movie(2, "The Dark Knight", "Christopher Nolan", 0, True, 6.99, 2.00))
    movie_list.append(Movie(3, "Interstellar", "Christopher Nolan", 5, False, 7.99, 1.75))

    '''
    Test 1 
        - Get the first movie in the list and borrow it
        - Then, using getters, display all information for this movie
    '''
    current_movie = movie_list[0]
    current_movie.borrow_movie()
    print("*** Test 1 Output ***")
    print("ID:", current_movie.get_id(),
          "\nTitle:", current_movie.get_title(),
          "\nDirector:", current_movie.get_director(),
          "\nGenre:", current_movie.get_genre_name(),
          "\nAvailability:", current_movie.get_availability(),
          "\nPrice: ${:.2f}".format(current_movie.get_price()),
          "\nFine Rate: ${:.2f}/day".format(current_movie.get_fine_rate()),
          "\nRental Count:", current_movie.get_rental_count())
    
    '''
    Test 2
        - Find all movies with "dark" in the title
    '''
    print("\n*** Test 2 Output ***")
    search_value = "dark"
    for current_movie in movie_list:
        if search_value.lower() in current_movie.get_title().lower():
            print("Found a match... Title:", current_movie.get_title(),
                   ", ID:", current_movie.get_id())

    '''
    Test 3
        - Get the last movie in the list and return it
        - Then, using setters to update the other information for this movie
    '''
    current_movie = movie_list[-1]
    current_movie.return_movie()
    current_movie.set_id(4)
    current_movie.set_title("The Matrix")
    current_movie.set_director("Lana Wachowski")
    current_movie.set_genre(4)
    current_movie.set_price(4.99)
    current_movie.set_fine_rate(1.25)

    # Lastly, print report of all movies (using implicit call to __str__())
    print("\n*** Test 3/Final Output ***")
    print("{:^10s}{:^30s}{:^25s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}".format("ID", "Title",
        "Director", "Genre", "Availability", "Price $", "Fine Rate $","Rental Count"))
    for movie in movie_list:
        print(movie)
        
if __name__ == "__main__":
    main()