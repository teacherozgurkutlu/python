# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:23:43 2017

@author: k
"""

squares = [1, 4, 9, 16, 25]
print (squares)
print (squares[0])
print (squares[-1])
print (squares[-3:])
print (squares[:])

print (squares + [36, 49, 64, 81, 100])
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print (cubes)
cubes.append(216)
print (cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)
letters[2:5] = ['C', 'D', 'E']
print (letters)
letters[2:5] = []
print (letters)
letters[:] = []
print (letters)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)