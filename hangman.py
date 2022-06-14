from invalidassignmentexception import InvalidAssignmentException
import re

class Hangman:
    def __init__(self):
        self.word = ''
        self.lista = []
        self.lifes = 5
        self.tries = []
        self.clue = ''
    
    def set_word(self, word):
        self.word = word
        self.clue = '_ ' * len(word)

    def assign(self, letter):
        self.tries.append(letter)
        self.lista = list(self.word)
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.clue = self.clue[:i] + letter + self.clue[i+1:]

        if letter not in self.lista:
            self.lifes -= 1
            raise InvalidAssignmentException
    
    def winner(self):
        self.word = self.word.lower()
        self.clue = self.clue.lower()
        if self.word == self.clue:
            return True
        else:
            return False
    
    def play(self):
        while True:
            letter = input("Ingrese una letra: ")
            self.assign(letter)
            if self.lifes == 0:
                return 'Perdiste'
            elif self.winner() and self.lifes > 0:
                return 'Ganaste'
    
    def show(self):
        return f'Lifes: {self.lifes} - Word: {self.clue}'
    

