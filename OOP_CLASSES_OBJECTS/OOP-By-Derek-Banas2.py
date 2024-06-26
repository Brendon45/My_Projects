#!/usr/bin/python3
"""
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game over"""


import random
import math

# Warrior & Battle Class


class Warrior:
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

# Battle Class capability of looping until 1 warrior dies


class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # A static method is a method or a capability of the class
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        print("{} attacks {} and deals {} damage".format(warriorA.name,
              warriorB.name, damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is Victorious".format(warriorB.name,
                  warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()
    battle.startFight(maximus, galaxon)


main()