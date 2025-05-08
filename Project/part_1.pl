% Definicje filmów
movie('Forrest Gump', drama, 5, 'Robert Zemeckis', 1994).
movie('Avengers', action, 4, 'Joss Whedon', 2012).
movie('The Godfather', drama, 5, 'Francis Ford Coppola', 1972).
movie('Airplane!', comedy, 4, 'Jim Abrahams', 1980).
movie('Hereditary', horror, 4, 'Ari Aster', 2018).
movie('Pulp Fiction', crime, 5, 'Quentin Tarantino', 1994).
movie('The Shawshank Redemption', drama, 5, 'Frank Darabont', 1994).
movie('The Dark Knight', action, 5, 'Christopher Nolan', 2008).
movie('Spirited Away', animation, 5, 'Hayao Miyazaki', 2001).
movie('Parasite', thriller, 5, 'Bong Joon-ho', 2019). 
movie('La La Land', musical, 4, 'Damien Chazelle', 2016).
movie('Inception', sci_fi, 4, 'Christopher Nolan', 2010).
movie('Interstellar', sci_fi, 5, 'Christopher Nolan', 2014).
movie('The Silence of the Lambs', thriller, 5, 'Jonathan Demme', 1991).
movie('Fight Club', drama, 4, 'David Fincher', 1999).
movie('The Matrix', action, 4, 'Lana Wachowski', 1999).
movie('Back to the Future', adventure, 4, 'Robert Zemeckis', 1985).
movie('Casablanca', romance, 5, 'Michael Curtiz', 1942).
movie('Psycho', horror, 5, 'Alfred Hitchcock', 1960).
movie('The Lion King', animation, 4, 'Roger Allers', 1994).
movie('Gladiator', historical, 4, 'Ridley Scott', 2000).
movie('Titanic', romance, 4, 'James Cameron', 1997).
movie('Avatar', sci_fi, 4, 'James Cameron', 2009).
movie('Django Unchained', western, 4, 'Quentin Tarantino', 2012).
movie('Arrival', sci_fi, 4, 'Denis Villeneuve', 2016).

% Filmy wg Gatunku
movies_by_genre(Genre, MovieList) :-
    findall(Title, movie(Title, Genre, _, _, _), MovieList).

% Filmy wg Oceny
movies_by_rating(MinRating, MovieList) :-
    findall(Title, (movie(Title, _, Rating, _, _), Rating >= MinRating), MovieList).

% Filmy wg Reżysera
movies_by_director(Director, MovieList) :-
    findall(Title, movie(Title, _, _, Director, _), MovieList).

% Filmy z Roku Produkcji
movies_by_year(Year, MovieList) :-
    findall(Title, movie(Title, _, _, _, Year), MovieList).

% Wyświetlanie wyników zapytań
display_movies_by_genre(Genre) :-
    movies_by_genre(Genre, MovieList),
    write('Movies of genre '), write(Genre), write(': '), write(MovieList), nl.

display_movies_by_rating(MinRating) :-
    movies_by_rating(MinRating, MovieList),
    write('Movies with rating at least '), write(MinRating), write(': '), write(MovieList), nl.

display_movies_by_director(Director) :-
    movies_by_director(Director, MovieList),
    write('Movies directed by '), write(Director), write(': '), write(MovieList), nl.

display_movies_by_year(Year) :-
    movies_by_year(Year, MovieList),
    write('Movies from year '), write(Year), write(': '), write(MovieList), nl.

% Zalecane wysoko oceniane filmy
recommend_highly_rated :-
    findall(Film, (movie(Film, _, Rating, _, _), Rating >= 4.5), MovieList),
    random_member(RandomFilm, MovieList),
    write('Recommended highly rated film: '), write(RandomFilm), nl.

% Przykładowe zapytania
:- display_movies_by_genre(drama).
:- display_movies_by_rating(4).
:- recommend_highly_rated.
:- display_movies_by_director('Christopher Nolan').
:- display_movies_by_year(1994).