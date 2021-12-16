
"This is a module for creating animal instance."

__author__ = "xianglun918"

'''
Class Dog()
for creating an animal instance
'''
class Dog():
    '''
    This class is aimed to provide full functionality of a dog.
    '''
    def __init__(self):
        print("This is a animal instance.")
    @classmethod
    def say_hello(cls):
        ''' Just say Hello.
        '''
        print("Hello.")
    @classmethod
    def are_you_ok(cls):
        '''
        Say yo.
        '''
        print('Yo')


def run_twice():
    ''' Actually run twice.
    '''
    print("Run twice as a fast animal.")
