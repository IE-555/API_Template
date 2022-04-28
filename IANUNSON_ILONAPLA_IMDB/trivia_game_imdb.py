import imdb
ia = imdb.Cinemagoer()
import numpy as np
from random import randint

newquestion = 0
while newquestion == 0:
    #From a list of the Top 250 Movies, select a random movie and random actor/character pair
    top_m = ia.get_top250_movies()
    current_ID = top_m[np.random.randint(0,len(top_m))].movieID
    movie = ia.get_movie(current_ID)
    actor = movie['cast'][np.random.randint(0,len(movie['cast']))]
    print("In the movie: \"" + movie['title'] + "\" the role of \"" + actor.currentRole['name'] + "\" is played by \"" + "____________" + "\".")

    #Randomly Select other actors
    othervalues = [randint(0, 249), randint(0, 249), randint(0, 249)]
    othermovie1=top_m[othervalues[0]].movieID
    othermovie2=top_m[othervalues[1]].movieID
    othermovie3=top_m[othervalues[2]].movieID
    otheractor1=ia.get_movie(othermovie1)['cast'][1]
    otheractor2=ia.get_movie(othermovie2)['cast'][1]
    otheractor3=ia.get_movie(othermovie3)['cast'][1]
    otheractor1 = otheractor1['name']
    otheractor2 = otheractor2['name']
    otheractor3 = otheractor3['name']

    #Shuffle the correct answer into a list with the incorrect ones and give the options
    correctA = actor['name']
    answers = [correctA,otheractor1,otheractor2,otheractor3]
    mix = list(answers)
    ABCD = ['A','B','C','D']
    np.random.shuffle(mix)

    tryagain = 1
    while tryagain == 1:
        for i in range(4):
            print(ABCD[i] + ") " + mix[i])
        print("Type in the letter (case sensitive) of the correct answer:")
        input1 = input()
        ABCD.index(input1)

        if mix[ABCD.index(input1)] == correctA:
            print("Correct!! You did it!!")
            tryagain = 0
        else:
            print("Oh no. Would you like to try again? (Type Y for yes)")
            input2 = input()
            tryagain = (input2=="Y")

    print("Would you like to play again with a new question? (Type Y for yes)")
    input3 = input()
    if input3 == "Y":
        newquestion = 0
    else:
        newquestion = 1