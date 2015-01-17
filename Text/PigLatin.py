__author__ = 'ryan@barnett.io'
#does not truly address all consonant sound rules, this is a simplified solution to the concept of pig latin


def pig_latin(string):
    vowels = 'aeiouAEIOU'
    if string[0] in vowels:
        return string+'way'
    else:
        return string[1:]+string[0]+'ay'