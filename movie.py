class Movie:
    GENRE_NAMES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi","Romance", "Thriller", "Animation", "Documentary", "Fantasy"]

    def __init__(self, movie_id, title, director, genre, available=True, price=0.0, fine_rate=0.0, rental_count=0):
        self.id = movie_id
        self.title = title
        self.director = director
        self.genre = genre
        self.available = available
        self.price = price
        self.fine_rate = fine_rate
        self.rental_count = rental_count

    # Getters
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_director(self):
        return self.director

    def get_genre(self):
        return self.genre

    def get_price(self):
        return self.price

    def get_fine_rate(self):
        return self.fine_rate

    def get_rental_count(self):
        return self.rental_count

    def get_genre_name(self):
        return Movie.GENRE_NAMES[self.genre]

    def get_availability(self):
        if self.available == True:
            return "Available"
        else:
            return "Rented"
        

    # Setters
    def set_id(self, movie_id):
        self.id = movie_id

    def set_title(self, title):
        self.title = title

    def set_director(self, director):
        self.director = director

    def set_genre(self, genre):
        self.genre = genre

    def set_price(self, price):
        self.price = price

    def set_fine_rate(self, fine_rate):
        self.fine_rate = fine_rate

    # Borrow movie
    def borrow_movie(self):
        self.available = False
        self.rental_count += 1


    # Return movie
    def return_movie(self):
        self.available = True


    # String representation
    def __str__(self):
        return "{:^10}{:^30}{:^25}{:^15}{:^15}{:^15.2f}{:^15.2f}{:^15}".format(
            str(self.id),
            self.title,
            self.director,
            self.get_genre_name(),
            self.get_availability(),
            self.price,
            self.fine_rate,
            str(self.rental_count)
        )