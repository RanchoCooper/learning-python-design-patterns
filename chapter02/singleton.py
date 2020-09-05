#!/usr/bin/env python
# encoding: utf-8

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


if __name__ == '__main__':
    s = Singleton()
    print("object created: ", s)
    s2 = Singleton()
    print("create again: ", s2)
