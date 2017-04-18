# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:50:36 2017

@author: k
"""
print ('spam eggs')
print ('doesn\'t')
print ("doesn't" )
print ('"Yes," he said.')
print ("\"Yes,\" he said.")
print ('"Isn\'t," she said.')

s = 'First line.\nSecond line.'
print(s)

print('C:\some\name')
print(r'C:\some\name')


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect tofs

""")

print (3 * 'un' + 'ium')
print ('Py' 'thon')

text = ('Put several strings within parentheses '  'to have them joined together.')
print (text)
word = 'Python'
print (word[0])
print (word[5])
print (word[-1])
print (word[-2])
print (word[0:2])
print (word[2:5])
print (word[:2] + word[2:])
print (word[:4] + word[4:])
print (word[:2])
print (word[4:])
print (word[-2:])
print (word[4:42])
print (word[42:])
print ('J' + word[1:])
s = 'supercalifragilisticexpialidocious'
print (len(s))
