"""19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016."""

class Peliculas():

    def get_movies_estreno_2014(self):
        estreno_2014_movies = Pila()
        for movie in self.__elements:
            if movie['año'] == 2014:
                estreno_2014_movies.push(movie)
        return estreno_2014_movies

    def count_movies_estreno_2018(self):
        count = 0
        for movie in self.__elements:
            if movie['año'] == 2018:
                count += 1
        return count

    def get_marvel_estreno_2016(self):
        marvel_2016_movies = Pila()
        for movie in self.__elements:
            if movie['estudio'] == 'Marvel Studios' and movie['año'] == 2016:
                marvel_2016_movies.push(movie)
        return marvel_2016_movies

from pila import Pila

peliculas = Pila()


pelicula1 = {'título': 'Black Panther', 'estudio': 'Marvel Studios', 'año': 2018}
pelicula2 = {'título': 'Avengers: Infinity War', 'estudio': 'Marvel Studios', 'año': 2018}
pelicula3 = {'título': 'Incredibles 2', 'estudio': 'Pixar Animation Studios', 'año': 2018}
pelicula4 = {'título': 'Deadpool 2', 'estudio': '20th Century Fox', 'año': 2018}
pelicula5 = {'título': 'Mission: Impossible - Fallout', 'estudio': 'Paramount Pictures', 'año': 2018}
pelicula6 = {'título': 'Captain America: Civil War', 'estudio': 'Marvel Studios', 'año': 2016}
pelicula7 = {'título': 'Deadpool', 'estudio': '20th Century Fox', 'año': 2016}
pelicula8 = {'título': 'Rogue One: A Star Wars Story', 'estudio': 'Lucasfilm', 'año': 2016}
pelicula9 = {'título': 'Zootopia', 'estudio': 'Walt Disney Animation Studios', 'año': 2016}
pelicula10 = {'título': 'La La Land', 'estudio': 'Summit Entertainment', 'año': 2016}
pelicula11 = {'título': 'Doctor Strange', 'estudio': 'Marvel Studios', 'año': 2016}
pelicula12 = {'título': 'X-Men: Apocalypse', 'estudio': 'Marvel Studios', 'año': 2016}
pelicula13 = {'título': 'Guardians of the Galaxy', 'estudio': 'Marvel Studios', 'año': 2014}
pelicula14 = {'título': 'Interstellar', 'estudio': 'Paramount Pictures', 'año': 2014}
pelicula15 = {'título': 'The Lego Movie', 'estudio': 'Warner Bros. Pictures', 'año': 2014}
pelicula16 = {'título': 'Captain America: The Winter Soldier', 'estudio': 'Marvel Studios', 'año': 2014}
pelicula17 = {'título': 'Gone Girl', 'estudio': '20th Century Fox', 'año': 2014}

peliculas.push(pelicula1)
peliculas.push(pelicula2)
peliculas.push(pelicula3)
peliculas.push(pelicula4)
peliculas.push(pelicula5)
peliculas.push(pelicula6)
peliculas.push(pelicula7)
peliculas.push(pelicula8)
peliculas.push(pelicula9)
peliculas.push(pelicula10)
peliculas.push(pelicula11)
peliculas.push(pelicula12)
peliculas.push(pelicula13)
peliculas.push(pelicula14)
peliculas.push(pelicula15)
peliculas.push(pelicula16)
peliculas.push(pelicula17)

print ("-----------------------------------------------------------------")

print("Peliculas estrenadas en 2014:")
peliculas_estreno_2014 = peliculas.get_movies_estreno_2014()
while peliculas_estreno_2014.size() > 0:
    pelicula = peliculas_estreno_2014.pop()
    print(pelicula['título'])

print ("-----------------------------------------------------------------")

count_estreno_2018 = peliculas.count_movies_estreno_2018()
print("Numero de peliculas estrenadas en 2018:", count_estreno_2018)

print ("-----------------------------------------------------------------")

print("Peliculas de Marvel Studios estrenadas en 2016:")
marvel_estreno_2016 = peliculas.get_marvel_estreno_2016()
while marvel_estreno_2016.size() > 0:
    pelicula = marvel_estreno_2016.pop()
    print(pelicula['título'])

print ("-----------------------------------------------------------------")
