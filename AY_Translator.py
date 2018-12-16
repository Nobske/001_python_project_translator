# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:00:17 2018

@author: Norbert Adam
"""

pyg = 'ay'

original = input('Enter a word:') #input für die Abfrage

if len(original) > 0 and original.isalpha(): #über 0 und ob es text ist
    word = original.lower() #wird in nur lowercases umgewandelt
    first = word[0] #erstes Zeichen 
    new_word = word + first + pyg #wort +erste zeichen +ay
    new_word = new_word[1:] # ohne erste Zeichen
    print (new_word)
    
else:
    print ('empty')



garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

print (message)
original2 = input('please enter to leave:') #input für die Abfrage

#i am the secret message
