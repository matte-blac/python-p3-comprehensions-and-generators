#!/usr/bin/env python3

def return_evens(num_list):
    # use list comprehension to make a new list
    return [num for num in num_list
            if num % 2 == 0]
    # returns a new list that consists all of even 
    # integers of a sequence of integers 
pass

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
    # returns a new list that takes a list of sentence 
    # strings with exclamation marks at the end
pass