#!/usr/bin/env python
# encoding: utf-8
from abc import ABC, ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("woof, woof!!")


class Cat(Animal):
    def do_say(self):
        print("meow, meow!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("which animal should make_sound? (Dog or Cat)")
    ff.make_sound(animal)
