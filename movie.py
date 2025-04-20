class Movie:
    GENRE_NAMES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Animation", "Documentary", "Fantasy"]

    def __init__(self, movie_id, title, director, genre, available=True, price=0.0, rental_count=0):
        self._id = movie_id
        self.title = title
        self.director = director
        self.genre = genre
        self.available = available
        self.price = price
        self.rental_count = rental_count

    def get_id(self):
        return self._id

    def set_id(self, movie_id):
        if movie_id:  # Basic validation to ensure ID is not empty
            self._id = movie_id
        else:
            print("Error: Movie ID cannot be empty.")

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_rental_count(self):
        return self.rental_count

    def get_genre_name(self):
        return Movie.GENRE_NAMES[self.genre]

    def get_availability(self):
        if self.available:
            return "Available"
        else:
            return "Rented"

    def set_availability(self, available):
            self.available = available

    def borrow_movie(self):
        if self.available:
            self.available = False
            self.rental_count += 1
            return 
        
    def return_movie(self):
        if not self.available:
            self.available = True
            return 
       

    def __str__(self):
        return "{:>10}{:>30}{:>25}{:>15}{:>15}{:>15.2f}{:>15}".format(
            str(self._id),
            self.title,
            self.director,
            self.get_genre_name(),
            self.get_availability(),
            self.price,
            str(self.rental_count)
        )