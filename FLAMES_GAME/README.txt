--------------------<< flames >>-----------------------------
In this game you must enter your name then the other player must do the same.
System will remove the same letters in your names and count the remained letter.(e.g. player1=asd   player2=abcd   remained=bcs count=3)
we have this dictionary
flames={
    "f":"friend",
    "l":"love",
    "a":"affection",
    "m":"marriage",
    "e":"enemy",
    "s":"sibling"
}

then the system gets flames and based on the count number it removes the letter which in here is 'a' then from here it counts 3 and again remove the letter which is 's' it continues untill 1 letter
lefts then it check the letter with key-value in the dictionary and returns the result for example f=friend so your friends.