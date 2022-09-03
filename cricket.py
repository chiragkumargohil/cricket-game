import random


commentary = {"0": "No run", "1": "Single run", "2": "Two runs", "3": "Three runs", "4": "FOUR!", "6": "SIX!", "W": "WICKET!"}
possibility= ["0", "1", "2", "3", "4", "6", "W"]

class Cricket:

    def __init__(self, overs=30, score=0, wickets=0, balls=0):
        self.overs = overs
        self.score = score
        self.wickets = wickets
        self.balls = balls

    def ball(self):
        result = random.choice(possibility)
        
        if result == "W":
            self.wickets += 1
        else:
            self.score += int(result)
        self.balls += 1
        
        return result
    
    def scorecard(self):
        result = self.ball()
        return f"{self.score}/{self.wickets} | {self.balls//6}.{self.balls%6} - {commentary.get(result)}"

    def match_over(self):
        if self.balls == (self.overs*6) or self.wickets == 10:
            return True

    def end_game(self):
        print(f"Final Scorecard : {self.score}/{self.wickets} | {self.balls//6}.{self.balls%6}")
        print('Game Over')