class Movie:
    GENRE_NAMES = [
        "Action", "Comedy", "Drama", "Horror", "Sci-Fi", 
        "Romance", "Thriller", "Animation", "Documentary", "Fantasy"
    ]
    
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
        return Movie.GENRE_NAMES[self.__genre]

    def get_availability(self):
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
        if self.__available:
            self.__available = False
            self.__rental_count += 1
        else:
            print(f"The movie {self.__title} is already rented.")

    # Return movie
    def return_movie(self):
        self.__available = True

    # String representation
    def __str__(self):
        return "{:^10}{:^30}{:^25}{:^15}{:^15}{:^15.2f}{:^15.2f}{:^15}".format(
            str(self.__id),
            self.__title,
            self.__director,
            self.get_genre_name(),
            self.get_availability(),
            self.__price,
            self.__fine_rate,
            str(self.__rental_count))