#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Summary


Attributes:
    b1 (Bomberman): 造兵：炸弹人
    h1 (Healer): 造兵：奶妈
    j1 (MachineGun): 造兵：机枪手1
    j2 (MachineGun): 造兵：机枪手2
"""

# @Date   : 2015-10-18 15:01:25
# @Author : Kang.cunhua (358608208@qq.com)
# @Link   : https://git.oschina.net/mdr/
# @Version : $Id$


class Unit(object):

    """docstring for unit

    Attributes:
        blood_max (TYPE): Description
    """

    def __init__(self):
        """Summary"""
        self.blood_max = self.blood  # 血上限；
        print self.name + "created"


class Attacker(Unit):

    """docstring for ClassName"""

    def attack(self, u):
        """Summary

        Args:
            u (TYPE): Description

        Returns:
            TYPE: Description
        """
        u.blood -= self.dps  # 被攻击者减血
        if u.blood <= 0:  # 血减没了就挂了
            print u.name + " was dead!!!"
            del u
        else:
            print u.name + " was attacked! blood = " + str(u.blood)


class MachineGun(Attacker):

    """docstring for machineGun

    Attributes:
        blood (int): Description
        dps (int): Description
        name (TYPE): Description
    """

    def __init__(self, name):
        """Summary

        Args:
            name (TYPE): Description
        """
        self.blood = 100
        self.name = name
        Unit.__init__(self)  # 调用父类的构造函数；
        self.dps = 30
        print self.name + " created"


class Tree(Unit):

    """docstring for Tree

    Attributes:
        name (TYPE): Description
    """

    def __init__(self, name):
        """Summary

        Args:
            name (TYPE): Description
        """
        self.name = name
        print self.name + " created"


class Healer(Unit):

    """docstring for Healer

    Attributes:
        blood (int): Description
        hps (int): Description
        name (TYPE): Description
    """

    def __init__(self, name):
        """Summary

        Args:
            name (TYPE): Description
        """
        self.blood = 50  # 奶妈一般血都比较少
        self.name = name
        Unit.__init__(self)
        self.hps = 15
        print self.name + " created"

    def heal(self, u):

        u.blood += self.hps
        if u.blood >= u.blood_max:
            u.blood = u.blood_max
        print u.name + " was healed! blood = " + str(u.blood)


class Bomberman(Unit):

    """docstring for Bomberman
    练习：自己写个炸弹人：炸掉别人200blood，自己也挂掉

    Attributes:
        blood (int): Description
        dps (int): Description
        name (TYPE): Description
    """

    def __init__(self, name):

        self.blood = 200
        self.name = name
        Unit.__init__(self)  # 调用父类的构造函数；
        self.dps = 200
        print self.name + " created"

    def bombe(self, u):

        u.blood -= self.dps  # 被攻击者减血
        if u.blood <= 0:  # 血减没了就挂了
            print u.name + " was dead!!!"
            del u
            print self.name + " was dead!!!"
            del self
        else:
            print u.name + " was bombed! blood = " + str(u.blood)
            print self.name + " was dead!!!"
            del self


j1 = MachineGun("j1")  # 造一个名字叫做j1的机枪兵
j2 = MachineGun("j2")  # 造一个名字叫做j2的机枪兵
h1 = Healer("h1")  # 名字叫h1的奶妈
b1 = Bomberman("b1")


j1.attack(j2)  # j1攻击了j2
j1.attack(j2)  # j1又计了j2
h1.heal(j2)  # h1给j2加血

j1.attack(j2)  # 打
j1.attack(j2)  # 再打
j1.attack(j2)  # 打到死

b1.bombe(j1)  # 炸弹人袭击了j1
