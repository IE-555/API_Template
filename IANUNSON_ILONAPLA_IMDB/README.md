# Trivia Game Based on IMDb Movies

Authors:  **Ian Unson** and **Ilona Platonova**

---

## Introduction ([click here for a video run through of this page](https://youtu.be/j94YJ9B_0W0))
- This Python script is using [IMDb movie](https://www.imdb.com/) all time Top 250 movies as rated by regular IMDb voters.
- It creates a trivia game where a single Player is provided with a name of the movie and four alternative actors, one of whom is playing a role in the movie. Player has to choose one of for letters (A, B, C, D) to choose the answer. If it is correct, game is over. If he gets it wrong, he can try again to guess who is the right actor.
- Information used for the trivia: movie names, lead actor IDs and names are retrieved from the IMDb server during the game, so internet connection has to be available.
- Source of the data is updated daily, however the ratings of top 250 do not change significantly from day to day 

---

## Sources
- The code retrieves data from [IMDb website](https://developer.imdb.com/) via [IMDb API](https://imdb-api.com/)
- The code is based on a Python package [Cinemagoer](https://cinemagoer.github.io/)

---

## Explanation of the Code
If you do not have numpy or Cinemagoer installed, then you can use pip install in the terminal to download those. More details on downloading and installing Cinemagoer can be found [here](https://cinemagoer.github.io/).
```
pip install cinemagoer
pip install numpy
```

The code, `trivia_game_imbd.py`, begins by importing the IMDb library to get the movie data, randint and numpy libraries are used for calculations:
```
import imdb
ia = imdb.Cinemagoer()
from random import randint
import numpy as np
```

We request top 250 movies from [IMDb api](https://imdb-api.com/) as rated by regular IMDb voters
```
top_m = ia.get_top250_movies()
```
We select one of the movie IDs (from the top 250 movies) as the one to request the information from the database. We use the title of the movie, a main character's name and the actor who played that character to populate the question and correct answer. This correct answer is stored as variable correctA:
```
current_ID = top_m[np.random.randint(0,len(top_m))].movieID
movie = ia.get_movie(current_ID)
actor = movie['cast'][np.random.randint(0,len(movie['cast']))]
correctA = actor['name']
```
Using random numbers, we select other movies from the Top 250 list and randomly select other actors from those movies to populate our "wrong answers". 
```
othervalues = [randint(0, 249), randint(0, 249), randint(0, 249)]
othermovie1=top_m[othervalues[0]].movieID
....
otheractor1=ia.get_movie(othermovie1)['cast'][1]
......
otheractor1 = otheractor1['name']
```
The one correct answer and the three incorrect answers are randomly shuffled and assigned as option A, B, C or D.
The output on the screen shows the Player four choices and request an input of the letter they believe corresponds with the correct answer.
```
print("In the movie: \"" + movie['title'] + "\" the role of \"" + actor.currentRole['name'] + "\" is played by \"" + "____________" + "\".")

answers = [correctA,otheractor1,otheractor2,otheractor3]
mix = list(answers)
ABCD = ['A','B','C','D']
np.random.shuffle(mix)
for i in range(4):
    print(ABCD[i] + ") " + mix[i])
```

Received input is compared with variables and the game will check if the correct letter is selected.
If answer is correct player gets response: "Correct!! You did it!!"
```
input1 = input()
ABCD.index(input1)
if mix[ABCD.index(input1)] == correctA:
    print("Correct!! You did it!!")
else:
    print("Oh no. Try Again.")
```
If they are wrong, another trial is possible as they are ask: "Oh no. Would you like to try again? (Type Y for yes)"

Regardless of a right or wrong answer, the player is also given the option to play the game again with a new question: "Would you like to play again with a new question? (Type Y for yes)"

---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Open a terminal window.

2. Change directories to where `trivia_game_imbd.py` is saved.

3. Type the following command:
	```
	python trivia_game_imbd.py
	```
4. Game is started with generated information about the movie and the alternative actors which to guess.
5. Player can enter their guess and can choose to repeat a question if they get it wrong and can choose to continue playing with a new question regardless if they right or wrong.

- *NOTE: Please note that all the content of the data is owned by IMBd and API free access allows to run up to 100 requests per day. More requests per day are available for a subscription fee.*

---

## Suggestions
- This sorce code and package can be used for creation of new trivia games. 
- You can use other data like year of movie or change the sequence of what is given and what player has to guess in similar way. For example, you can swicth the game about actors - give an actor and provide with 4 movies which he might be playing at. 
- With more coding you can use year of first on the screen and then let choose the right one.
- Using other python packages we could make a UI where you can click the answer you think is correct
- Integrating this code with a twitter API you could set up a twitter account to post a daily trivia question
- Through social network analysis or possibly nearest neighbor algorithm to improve wrong answers to be closer to the correct answer
