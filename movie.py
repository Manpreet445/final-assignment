class Movie:
    '''
    Movie class to represent a movie in a rental system.
    Each movie has an ID, title, director, genre, availability status,
    rental price, fine rate, and rental count.
    '''
    GENRE_NAMES = [
        "Action", "Comedy", "Drama", "Horror", "Sci-Fi",              
        "Romance", "Thriller", "Animation", "Documentary", "Fantasy"
    ]   # List of genre names for easy reference
    
    ''' Constructor to initialize a Movie object with the given attributes.'''
    def __init__(self, movie_id, title, director, genre, available=True, price=0.00, fine_rate=0.00, rental_count=0):
        self.__id = movie_id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__fine_rate = fine_rate
        self.__rental_count = rental_count

    # Getters
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_director(self):
        return self.__director

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return f"{self.__price:.2f}"

    def get_fine_rate(self):
        return self.__fine_rate

    def get_rental_count(self):
        return self.__rental_count

    def get_genre_name(self):
        # Retrieve the genre name from the GENRE_NAMES list using the genre index
        return Movie.GENRE_NAMES[self.__genre]

    def get_availability(self):  ## Check if the movie is available for rent
        # Return "True" if available, otherwise "False"
        if self.__available:
            return "True"
        else:
            return "False"

    # Setters
    def set_id(self, movie_id):
        self.__id = movie_id

    def set_title(self, title):
        self.__title = title

    def set_director(self, director):
        self.__director = director

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price

    def set_fine_rate(self, fine_rate):
        self.__fine_rate = fine_rate

    # Borrow movie
    def borrow_movie(self):
        self.__available = False    # Mark as not available
        self.__rental_count += 1
        

    # Return movie
    def return_movie(self):
        self.__available = True   # Mark as available

    # String representation
    def __str__(self):
        return (f"{'ID':<4}{'Title':<35}{'Director':<25}{'Genre':<15}{'Availability':<12}   {'Price $':<1} {'Rental Count':<10}\n "
                f"{'-' * 104}\n"
                f"{self.__id:<4}{self.__title:<35}{self.__director:<25}{self.get_genre_name():<15}{self.get_availability():<12}   {self.__price:<2}    {self.__rental_count:<10}")
         