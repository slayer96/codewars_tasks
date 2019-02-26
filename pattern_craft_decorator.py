"""

The Decorator Design Pattern can be used, for example, in the StarCraft game to manage upgrades.

The pattern consists in "incrementing" your base class with extra functionality.

A decorator will receive an instance of the base class and use it to create a new instance with the new things you want "added on it".

Your Task
Complete the code so that when a Marine gets a WeaponUpgrade it increases the damage by 1, and if it is a ArmorUpgrade then increase the armor by 1.

You have 3 classes:

Marine: has a damage and an armor properties
MarineWeaponUpgrade and MarineArmorUpgrade: upgrades to apply on marine. Accepts a Marine in the constructor and has the same properties as the Marine

"""

import test_framework as Test


class Marine:
    def __init__(self, damage, armor):
        self.damage = damage
        self.armor = armor


class Marine_weapon_upgrade:
    def __init__(self, marine):
        self.damage = marine.damage + 1
        self.armor = marine.armor


class Marine_armor_upgrade:
    def __init__(self, marine):
        self.damage = marine.damage
        self.armor = marine.armor + 1


Test.describe('Basic tests')
Test.it('Single upgrade')
marine = Marine(10, 1)
Test.assert_equals(Marine_weapon_upgrade(marine).damage, 11)
Test.assert_equals(Marine_weapon_upgrade(marine).damage, 11)

Test.it('Double upgrade')
marine = Marine(15, 1)
marine = Marine_weapon_upgrade(marine)
marine = Marine_weapon_upgrade(marine)
Test.assert_equals(marine.damage, 17)

Test.it('Triple upgrade')
marine = Marine(20, 1)
marine = Marine_weapon_upgrade(marine)
marine = Marine_weapon_upgrade(marine)
marine = Marine_weapon_upgrade(marine)
Test.assert_equals(marine.damage, 23)
