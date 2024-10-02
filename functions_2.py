"""
(enter module docstring)
"""

import random


def password_8chars(letters, caps, numbers):
    """
    Create an 8-character password with characters randomly selected from
    `letters`, `caps`, and `numbers`.
    :param letters: string of lowercase letters
    :param caps: string of uppercase letters
    :param numbers: string of decimal digit characters
    :return: string of 8 characters
    """
    my_password1 = ""
    possibles = letters + caps + numbers
    for numorletter in range (8):
        ran_char = random.choice(possibles)
        my_password1 = ran_char + my_password1
    return my_password1


def password_4words(nouns, verbs, adj):
    """
    Create a passowrd of 3 words, randomly selected from `nouns`, `verbs`,
    and `adj` lists.
    :param nouns: list of noun words
    :param verbs: list of verb words
    :param adj: list of adjective words
    :return: string
    """
    password_4words = nouns + verbs + adj
    threewords = ""
    for word_at_random in range (3):
        ran_string = random.choice(password_4words)
        threewords = threewords + ran_string
    return threewords


def password_4words_better(nouns, verbs, adj):
    """
    Call password_4words() to create the password and then replace some
    letters as follows:
        - 'o' is replaced with '0'
        - 'l' is replaced  '!'
        - 'a' is replaced with '@'
        - 'e' is replaced with '3'
    :param nouns: list of noun words
    :param verbs: list of verb words
    :param adj: list of adjective words
    :return: string
    """
    better_pass = ""
    newpassword = password_4words(nouns, verbs, adj)
    better_pass = newpassword.replace('o','0')
    better_pass = better_pass.replace('l','!')
    better_pass = better_pass.replace('a','@')
    better_pass = better_pass.replace('e','3')
    return better_pass
    




def test_password_8chars():
    lower_letters = 'abc'
    upper_letters = 'ABC'
    digits = '123'
    my_password1 = password_8chars(lower_letters, upper_letters, digits)
    print(my_password1)

    my_password2 = password_8chars(lower_letters, upper_letters, digits)
    print(my_password2)

    my_password3 = password_8chars(lower_letters, upper_letters, digits)
    print(my_password3)

def test_password_4words():
    nouns = ['president', 'manhattan', 'table'] 
    verbs = ['run', "stop"]
    adj = ['quickly', 'awkwardly']
    my_password2 = password_4words(nouns, verbs, adj) 
    print(my_password2)

def test_password_4words_better():
    nouns = ['president', 'manhattan', 'table'] 
    verbs = ['run', "stop"]
    adj = ['quickly', 'awkwardly']
    my_password3 = password_4words_better(nouns, verbs, adj)
    print(my_password3)

def main():
    """
    Test the functions defined in this module.
    """
    test_password_8chars()
    test_password_4words()
    test_password_4words_better()


main()
