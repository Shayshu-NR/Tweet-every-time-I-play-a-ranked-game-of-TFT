#~~~~~Libraries~~~~~
import random
#~~~~~~~~~~~~~~~~~~~

#~~~~~Functions~~~~~
def compose_tweet(level, placement, trait, damage):
    random.seed(None)

    starting_phrases_bad = ["Oh boy this was a rough one, ",
                            "Welp another day another L, ",
                            "Ah jeez Rick I'm pretty bad, ", 
                            "LMAOOO GUESS WHO'S A CLOWN??",
                            "Press F in chat pls, ",
                            "Ahaha fuuuuuuuuuuuuu, ",
                            "Was I dropped on my head as a child? Because ",
                            "Ayo turns out I'm trraaaaaashhh, ",
                            "How do I unistall? ",
                            "BRUUUHHHH ",
                            "I just might 'yeet' myself, ya feel? ",
                            "End my suffering, ",
                            "I am stupid, ",
                            "*Megolovania song* ",
                            "Mom just called me a n00b cuz "]

    starting_phrases_good = ["WOWZA what a pleasant surprise, ",
                             "It is I decent gamer2000 here, ",
                             "*whips and nae-naes* ",
                             "TSM SIGN ME ALREADY ",
                             "Heck yea, ",
                             "I AM LITTERYALLY GODDD, ",
                             "Look at me now MOM, ",
                             "noice, ",
                             "Would ya look at that ",
                             "They call me theLegend27 cos, ",
                             "Wahoo ",
                             "Ok I actually did aight, ",
                             "I'm basically Diamond 1, ",
                             "yaaa bbbbbooiiiiiiiii... ",
                             "They call me salad cuz I be dressin, "]

    tweet = ""

    if(int(placement) > 4):
        
        tweet = starting_phrases_bad[random.randint(0, 15)] + "I just placed " + str(placement) + "th, "
        tweet = tweet + "I ended up at level " + str(level) + ". "
        tweet = tweet + "My comp was mostly " + trait + " this game. "
        tweet = tweet + "In total I did " + str(damage) + " damage"

        return tweet
    else:
        tweet = starting_phrases_good[random.randint(0, 15)] + "I just placed " + str(placement)

        if(int(placement) == 1):
            tweet = tweet + "st, "
        elif(int(placement) == 2):
            tweet = tweet + "nd, "
        else:
            tweet = tweet + "rd, "
        
        tweet = tweet + "I ended up at level " + str(level) + ". "
        tweet = tweet + "My comp was mostly " + trait + " this game. "
        tweet = tweet + "In total I did " + str(damage) + " damage"   

        return tweet

def get_relavent_photo(trait):
    file_path = ""

    return file_path

#~~~~~~~~~~~~~~~~~~~
