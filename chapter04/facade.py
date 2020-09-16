#!/usr/bin/env python
# encoding: utf-8

class Hotelier(object):
    def __init__(self):
        print("arrange the hotel for Marriage? --")

    def __isAvailable(self):
        print("is the hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("registered the booking\n\n")


class Florist(object):
    def __init__(self):
        print("flower decorations for the event? --")

    def setFlowerRequirements(self):
        print("carnotions, roses and lilies would be used for decoration\n\n")


class Caterer(object):
    def __init__(self):
        print("food arrangements for the event --")

    def setCuisine(self):
        print("chinese & continental cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("musical arrangements for the marriage --")

    def setMusicType(self):
        print("jazz and classical will be played\n\n")


class EventManager(object):
    def __init__(self):
        self.hotelier = Hotelier()
        self.florist = Florist()
        self.caterer = Caterer()
        self.musician = Musician()
        print("event manager:: let me talk to the folks\n")

    def arrange(self):
        self.hotelier.bookHotel()
        self.florist.setFlowerRequirements()
        self.caterer.setCuisine()
        self.musician.setMusicType()


class You(object):
    def __init__(self):
        print("you:: whoa! marrige arrangements??!!!")

    def askEventManager(self):
        print("you:: let's contact the event manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("you:: thanks to event manager, all preparations done!")


if __name__ == '__main__':
    you = You()
    you.askEventManager()
