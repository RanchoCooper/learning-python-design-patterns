#!/usr/bin/env python
# encoding: utf-8
from abc import ABCMeta, abstractmethod


class You(object):
    def __init__(self):
        print("you:: lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def makePayment(self):
        self.isPurchased = self.debitCard.doPay()

    def __del__(self):
        if self.isPurchased:
            print("you::wow! Denim shirt is Mine :=)")
        else:
            print("you::I should earn more money :(")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def doPay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("bank::checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def doPay(self):
        if self.__hasFunds():
            print("bank:: paying the merchant")
            return True
        else:
            print("bank::sorry, not enough funds!")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def doPay(self):
        card = input("proxy::punch in card number: ")
        self.bank.setCard(card)
        return self.bank.doPay()
            

if __name__ == '__main__':
    you = You()
    you.makePayment()
