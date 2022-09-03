## Sample Output

We used to play the cricket game as children using a book ([Book Cricket](https://www.traditionalgames.in/book-cricket)). We open any page of the book at random, and the last digit of the page number determines our score. For instance, if the final digit is zero, the player is dismissed.

I made this single-player game with the same logic in mind. To hit the ball, the user must enter '1'. The programme then assigns a random score to the ball. After each hit, the user can view his or her scorecard. The user can also set overs to play.

You can view the result as shown below when you execute the [main.py](main.py) file on your device.

```
== Welcome to the Cricket Game ==

How many overs of match (5/10/20)? 2

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
0/1 | 0.1 - WICKET!
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 3

Either '1' or '0'...

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): hit

Either '1' or '0'...

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
1/1 | 0.2 - Single run
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
4/1 | 0.3 - Three runs
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
7/1 | 0.4 - Three runs
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
10/1 | 0.5 - Three runs
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
11/1 | 1.0 - Single run
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
11/1 | 1.1 - No run
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
14/1 | 1.2 - Three runs
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
15/1 | 1.3 - Single run
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
18/1 | 1.4 - Three runs
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
18/1 | 1.5 - No run
-------------------------

RULE: '1' to Hit and '0' to Quit the Game
-> Enter (either '1' or '0'): 1

-------------------------
18/1 | 2.0 - No run
-------------------------

Final Scorecard : 18/1 | 2.0
Game Over.
```

Go to [Repository](https://github.com/chiragkumargohil/cricket-game.git).
