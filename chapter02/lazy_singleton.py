#!/usr/bin/env python
# encoding: utf-8

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            print("instance already created.")

    @staticmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == '__main__':
    s = Singleton()
    print("object created: ", Singleton.getInstance(Singleton))
    s1 = Singleton()
