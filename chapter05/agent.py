#!/usr/bin/env python
# encoding: utf-8
class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, " is occupied with current movie")

    def available(self):
        self.isBusy = False
        print(type(self).__name__, " is free for the movie")

    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.actor = Actor()
        self.principal = None

    def work(self):
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    agent = Agent()
    agent.work()
