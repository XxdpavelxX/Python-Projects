import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
 "A story of a boy and his toys that come to life",
 "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print toy_story.storyline

avatar = media.Movie("Avatar",
"A marine on an alien planet",
"http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
"http://www.youtube.com/watch?v=-9ceBgWV8io")
#print avatar.storyline
#avatar.show_trailer()

rockyIV= media.Movie("Rocky IV",
"Rocky Balboa accompanies his friend Apollo Creed in a fight versus the heavyweight Soviet boxing champion",
"http://content7.flixster.com/movie/26/13/261393_det.jpg",
"https://www.youtube.com/watch?v=bN-SShi58cI")

watchmen=media.Movie("Watchmen",
"In an alternate 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it.",
"http://ia.media-imdb.com/images/M/MV5BMTc0NjI2OTYxMF5BMl5BanBnXkFtZTcwMTcxMjkyMg@@._V1_SX214_AL_.jpg",
"https://www.youtube.com/watch?v=R3orQKBxiEg")

borat = media.Movie("Borat",
"Kazakh television personality Borat Sagdiyev leaves Kazakhstan for the 'Greatest Country in the World', the 'U, S and A' to make a documentary at the behest of the Kazakh Ministry of Information.",
"http://upload.wikimedia.org/wikipedia/en/thumb/3/39/Borat_ver2.jpg/220px-Borat_ver2.jpg",
"https://www.youtube.com/watch?v=4_I3tIjztj8")

forestGump = media.Movie("Forest Gump",
"Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
"http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg",
"https://www.youtube.com/watch?v=uPIEn0M8su0")
#rockyIV.show_trailer()


movies=[toy_story,avatar,rockyIV,watchmen,borat,forestGump]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
print media.Movie.__module__



