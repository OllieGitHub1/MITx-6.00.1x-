#Exercise: how many
#5.0/5.0 points (graded)
#
#Consider the following sequence of expressions:
#
#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#We want to write some simple procedures that work on dictionaries to return information.
#
#First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:
#
#>>> print(how_many(animals))
#6

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for keys in aDict.keys():
        for values in aDict[keys]:
            count +=1
    return count

#Correct 