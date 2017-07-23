import fresh_tomatoes
import media

# Toy Story movie code
toystory = media.Movie(
    "Toy story",
    "A story of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")


# Avatar movie code
avatar = media.Movie(
    "Avatar",
    "On the lush alien world of Pandora live the Na'vi,"
    " beings who appear primitive but are highly evolved."
    " Because the planet's environment is poisonous,"
    " human/Na'vi hybrids, called Avatars,"
    " must link to human minds to allow for free movement on Pandora."
    " Jake Sully (Sam Worthington), a paralyzed former Marine, becomes"
    " mobile again through one such Avatar and falls in love with a Na'vi"
    " woman (Zoe Saldana). As a bond with her grows, he is drawn into"
    " a battle for the survival of her world.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


# Lone Survivor movie code
lone_survivor = media.Movie(
    "Lone Survivor",
    "In 2005 Afghanistan, Navy SEALs Marcus Luttrell (Mark Wahlberg),"
    " Michael Murphy (Taylor Kitsch), Danny Dietz (Emile Hirsch)"
    " and Matthew Axe Axelson (Ben Foster) deploy on a mission of"
    " surveillance and to take out Taliban leader Ahmad Shah."
    " Though spotted by goatherds, Luttrell and his team decide"
    " not to kill them. But one of the Afghans alerts a group of"
    " Taliban fighters to the invaders, and a terrible battle"
    " ensues, in which the SEALs find themselves hopelessly outnumbered"
    " and outgunned",
    "https://upload.wikimedia.org/wikipedia/en/b/bd/Lone_Survivor_poster.jpg",
    "https://www.youtube.com/watch?v=yoLFk4JK_RM")

# School Of Rock movie code
school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# American Sniper movie code
american_sniper = media.Movie(
    "American Sniper",
    "U.S. Navy SEAL Chris Kyle (Bradley Cooper) takes his sole mission"
    " -- protect his comrades -- to heart and becomes one of the"
    " most lethal snipers in American history. His pinpoint accuracy"
    " not only saves countless lives but also makes him a prime"
    " target of insurgents. Despite grave danger and his struggle"
    " to be a good husband and father to his family back in the"
    " States, Kyle serves four tours of duty in Iraq. However,"
    " when he finally returns home, he finds that he"
    " cannot leave the war behind",
    "https://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5bP1f_1o-zo")

# R.I.P.D movie code
ripd = media.Movie(
    "R.I.P.D",
    "Veteran lawman Roy Pulsifer (Jeff Bridges) works"
    " for the R.I.P.D., a legendary police force charged"
    " with finding monstrous spirits who are disguised as"
    " ordinary people but are trying to avoid their final"
    " judgment by hiding out among the living. When Roy"
    " and his new partner, Nick Walker (Ryan Reynolds),"
    " uncover a plot that could end all life, they must"
    " discover a way to restore the cosmic balance or"
    " else watch the tunnel to the afterlife start"
    " sending angry souls back to the world of the living.",
    "https://upload.wikimedia.org/wikipedia/en/8/80/R.I.P.D._Poster.jpg",
    "https://www.youtube.com/watch?v=X07xNrVd7DU")

# Star Wars movie code
star_wars = media.Movie(
    "Star Wars",
    "Obi-Wan Kenobi (Ewan McGregor) is a young"
    " apprentice Jedi knight under the tutelage"
    "of Qui-Gon Jinn (Liam Neeson) ; Anakin Skywalker"
    " (Jake Lloyd), who will later father Luke Skywalker"
    " and become known as Darth Vader, is just a"
    " 9-year-old boy. When the Trade Federation cuts"
    " off all routes to the planet Naboo, Qui-Gon"
    " and Obi-Wan are assigned to settle the matter.",
    "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

# array list of the movies from above
movies = [toystory, avatar,
          lone_survivor, school_of_rock,
          american_sniper, ripd, star_wars]

fresh_tomatoes.open_movies_page(movies)
