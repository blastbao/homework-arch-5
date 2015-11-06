#!.usr/bin/python
#coding=utf-8


class unit(object):
    def __init__(self):
        self.blood_max = self.blood
class attacker(unit):
    def attack(self, u):
        u.blood -= self.dps
        if u.blood <= 0:
            print u.name + " was dead!!!"
            del u
        else:
            print u.name + " was attacked! bool = " + str(u.blood)
class boomer(attacker):
    def __init__(self, name):
        self.name = name
        self.blood = 50
        self.dps = 150
        super(boomer, self).__init__()
    def boom(self, u):
        u.blood -= self.dps
        print self.name + " was boom!!"
        if u.blood <= 0:
            print u.name + " was dead!!!"
            u.__delattr__
        del self
class machineGun(attacker):
    def __init__(self, name):
        self.blood = 100
        self.name = name
        super(machineGun, self).__init__()
        self.dps = 30
        print self.name + " created"
class tree(unit):
    def __init__(self, name):
        self.name = name
        self.blood = 50
        super(tree, self).__init__()
        print self.name + " created"
class healer(unit):
    def __init__(self, name):
        self.name = name
        self.blood = 50
        super(healer, self).__init__()
        self.hps = 15
        print self.name + " created"
    def heal(self, u):
        u.blood += self.hps
        if u.blood >= u.blood_max:
            u.blood = u.blood_max
        print u.name + " was healed ! blood = " + str(u.blood)
j1 = machineGun("j1")
j2 = machineGun("j2")
t1 = tree('t1')
h1 = healer('h1')
j2.attack(t1)
h1.heal(t1)
b1 = boomer("b1")
#j1.attack(b1)
b1.boom(j1)
