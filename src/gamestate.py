import random

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.iguess = 0
        self.scores = []

    def addScore(self, score: int):
        self.scores.append(abs(score))

'''Do not change these values directly, use/create wrapper functions'''
nguess = 6
fin = False
players = {}
lb = []

def genId() -> int:
    return random.randint(10000, 99999)

def checkSesh(id: int) -> bool:
    print(f"Checking: {id}")
    return id in players.keys()

def createPlayer(n):
    id = genId()
    players[id] = Player(n, id)
    return id

def handleGuess(g) -> tuple:
    return (0, False)
