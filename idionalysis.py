#!/usr/bin/env python3

import sys

class Analysis:
    ''' a report of data from analysis '''
    def __init__(self, text):
        ''' do the analysis and store the data '''

        # get the words in the text
        self.words = text.split()

        # to be list of bools corresponding to which words are first encounters
        self.initial_encounters = list()

        # keep track of unique words and their number of occurences
        self.occurences = dict()

        # loop through each word
        for word in self.words:
            # record word count
            # and whether its a first encounter
            self.initial_encounters.append(self.count(word))

    def count(self, word):
        ''' increase the number of occurences for a word '''
        # be case insensitive
        word = word.lower()
        # check if it's a first encounter
        initial_encounter = not word in self.occurences
        # make the appropriate record
        self.occurences[word] = 1 if initial_encounter else self.occurences[word] + 1
        # return whether it was a first encounter
        return initial_encounter

    @property
    def length(self):
        ''' return how many words in the text '''
        return len(self.words)

    @property
    def unique(self):
        ''' return how many unique words in the text '''
        return len(self.occurences)

    def __str__(self):
        ''' make a nice report '''
        lines = list()
        lines.append(f'total words:    {self.length}')
        lines.append(f'unique words:   {self.unique}')
        lines.append(f'unique / total: {self.unique / self.length * 100}%')
        print('\n'.join(lines))

def analyse_file(filename):
    with open(filename) as f:
        return Analysis(f.read())

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(analyse_file(sys.argv[1]))
    else:
        print(f'Usage: {sys.argv[0]} [text file]')
