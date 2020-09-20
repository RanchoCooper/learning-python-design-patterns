#!/usr/bin/env python
# encoding: utf-8
from abc import ABCMeta, abstractmethod


class NewsPublisher(object):
    def __init__(self):
        self.__subscribers = []
        self.__lastNews = None

    def register(self, subscriber):
        self.__subscribers.append(subscriber)

    def unregister(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def addNews(self, news):
        self.__lastNews = news

    def getNews(self):
        return "got news:", self.__lastNews


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    newsPublisher = NewsPublisher()
    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(newsPublisher)

    print("\nsubscribers:", newsPublisher.subscribers())

    newsPublisher.addNews("hello, world!")
    newsPublisher.notify()

    print("detached:", type(newsPublisher.unregister()).__name__)
    print("subscribers:", newsPublisher.subscribers())
    newsPublisher.addNews("second news!")
    newsPublisher.notify()
