import random

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.iguess = 0
        self.scores = []

    def addScore(self, score: int):
        self.scores.append(abs(score))

class Game:
    def __init__(self):
        self.ndist = 6
        self.dist = []
        self.sumdist = 0
        self.fin = True
        self.players = {}
        self.lb = []

    def newGame(self):
        self.fin = False

    def checkSesh(self, id: int) -> bool:
        print(f"Checking: {id}")
        return id in self.players.keys()

    def createPlayer(self, n):
        id = genId()
        self.players[id] = Player(n, id)
        return id

    def handleGuess(self, g) -> tuple:
        return (0, self.fin)

def genId() -> int:
    return random.randint(10000, 99999)
