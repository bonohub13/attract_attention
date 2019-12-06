#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AttentionAdder(object):
    def __init__(self):
        self.attention = {'top':[], 'base':[], 'bottom':[]}
        self.input_message = input('input your message -> ')
        self.__attention_wrapper()
        
    def __attention_wrapper(self):
        self.attention['top'] = ['ー', '人', 'ー']
        self.attention['base'] = ['＞', '＜']
        self.attention['bottom'] = ['ー', 'Ｙ', 'ー']

    def __wrap_msg(self):
        msg = {}
        msg_len = len(self.input_message)
        msg['top'] = self.attention['top'][0]+self.attention['top'][1]*msg_len+self.attention['top'][2]
        msg['base'] = self.attention['base'][0]
        for i in range(msg_len):
            msg['base'] += self.input_message[i]
        msg['base'] += self.attention['base'][1]
        msg['bottom'] = self.attention['bottom'][0]+self.attention['bottom'][1]*msg_len+self.attention['bottom'][2]
        return msg

    def __test(self):
        #print('{}\n{}\n{}'.format(self.attention['top'], self.attention['base'], self.attention['bottom']))
        test_msg = ['a', 'b', 'c']
        for _ in range(5):
            print('\r{}\n{}\n{}'.format(test_msg[0], test_msg[1], test_msg[2]), end='')

    def run(self):
        if self.input_message == 'test':
            self.__test()
        else:
            message = self.__wrap_msg()
            print(message['top'])
            print(message['base'])
            print(message['bottom'])

if __name__ == '__main__':
    attention = AttentionAdder()
    attention.run()
