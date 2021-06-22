#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DNA_Generator.py
@Time    :   2021/04/12 16:16:08
@Author  :   xianglun xu 
@Contact :   xianglun918@gmail.com
'''

# Libraries Used
from ctypes import WINFUNCTYPE
import pyperclip
import time

# Decorator to show the running time.
def timeCounter(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        print("Running time: %s seconds." % round(end_time - start_time, 2))
        return result
    return wrapper


class DNA_Generator:
    def __init__(self, text='None', direction='horizontal'):
        while True:

            self._text = input("Input the content text or enter 'exit' to exit: ")
            if self._text == '':
                print('Empty input is not acceptable !!!')
                continue
            if self._text == 'help':
                while True:
                    mode = input("Current direction: %s. " % direction + 'You want to change to horizontal? [Yes|no]')
                    if mode == '' or mode == 'Yes':
                        direction = 'horizontal'
                        print('Got it. Direction changed to horizontal.')
                        break
                    elif mode == 'no':
                        break
                    else:
                        print('Invalid answer. Try again.')
                continue


            if self._text == 'exit' or self._text == 'exit':
                break
            if direction == 'horizontal':
                self.draw_h()
            else:
                self.draw()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise ValueError('The attribute input should be string type!')
        self._text = value

    # (Default) Draw vertically.
    @timeCounter
    def draw(self, width=9, height=30):
        str_len = len(self._text)
        sub_matrix = []
        for i in range(height):
            template = [' '] * width
            word = self._text[i % str_len]

            template[i % width] = word
            template[width - i % width - 1] = word
            sub_matrix.append(''.join(template) + '\n')
        print(''.join(sub_matrix))
        pyperclip.copy(''.join(sub_matrix))

    # (Optional) Draw horizontally.
    @timeCounter
    def draw_h(self, width=4, height=30):
        str_len = len(self._text)
        sub_matrix = []
        for i in range(height):
            tmp_index = i % (width*2)
            if tmp_index // width == 0:
                left_str = ' ' * (tmp_index % width) + self._text + ' ' * (str_len + width - tmp_index % width)
                right_str = left_str[::-1]
                sum_str = left_str + right_str
            else:
                left_str = ' ' * (str_len + width - tmp_index % width) + self._text + ' ' * (tmp_index % width)
                right_str = left_str[::-1]
                sum_str = left_str + right_str
            sum_str += '\n'
            sub_matrix.append(sum_str)
        print(''.join(sub_matrix))
        pyperclip.copy(''.join(sub_matrix))



if __name__ == '__main__':
    tmp = DNA_Generator()
