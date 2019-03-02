#!/usr/bin/env python3

import sys, re

GRAPH_BINS_MAX = 5
ROUND_DIGITS = 2
#WORD_REGEXP = r'\w+[\'\-]?\w+'
WORD_REGEXP = r'\w*\'?(?:\w+[\'\-]?)*\w+'

def divide(n, m):
    ''' integer divide n by m into explicit divisions

    return each division as a list such that the sum equals m
    '''
    # keep track of each subsequent division
    divisions = list()
    while m:
        division = n // m
        divisions.append(division)
        n -= division
        m -= 1
    return divisions

class Analysis:
    ''' a report of data from analysis '''

    @staticmethod
    def from_text(text):
        ''' create an analysis from a text '''
        analysis = Analysis()
        analysis.analyse(text)
        return analysis

    def __init__(self, words=None, initial_encounters=None, occurences=None):
        self.words = words
        self.initial_encounters = initial_encounters
        self.occurences = occurences

    def analyse(self, text):
        ''' do the analysis and store the data '''
        # get the words in the text
        self.words = re.findall(WORD_REGEXP, text)
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

    def divide(self, chunks):
        ''' divide the analysis into smaller chunks '''
        # i question this method of dividing..
        # it feels like an abuse of this class lol
        # anyway
        # get the amount of words for each chunk
        chunk_lengths = divide(self.length, chunks)
        # get the chunks
        chunks = list()
        # cycle through each chunk length and collect that chunk
        start = 0
        for length in chunk_lengths:
            end = start + length
            initial_encounters = self.initial_encounters[start:end]
            chunk = Analysis(self.words, initial_encounters)
            chunks.append(chunk)
            start += length
        return chunks

    def graph(self, chunks):
        ''' return concentration of initial occurences of vocabulary in each chunk '''
        chunks = self.divide(chunks)
        return list(map(lambda chunk: chunk.unique / self.unique, chunks))

    @property
    def length(self):
        ''' return how many words in the text '''
        return len(self.words)

    @property
    def unique(self):
        ''' return how many unique words in the text '''
        return len(self.occurences) if self.occurences else self.initial_encounters.count(True)

    @property
    def uniques(self):
        ''' return a set of the occuring words '''
        return set(self.occurences.keys())

    @property
    def ratio(self):
        ''' return the ratio of unique to total occurences '''
        return self.unique / self.length

    @property
    def singles(self):
        ''' return the amount of words that occur a single time '''
        return len(list(filter(lambda word: self.occurences[word] == 1, self.uniques)))

    @property
    def sorted(self):
        ''' return a list of occuring words sorted by frequency '''
        return sorted(self.uniques, reverse=True, key=lambda word: self.occurences[word])

    def __str__(self):
        ''' make a nice report '''
        def prettify(value):
            ''' stringify a value as a rounded percentage '''
            return f'{round(value * 100, ROUND_DIGITS)}%'
        lines = list()
        lines.append(f'total words:                 {self.length}')
        lines.append(f'unique words:                {self.unique}')
        lines.append(f'unique / total:              {prettify(self.ratio)}')
        lines.append(f'singly occuring words:       {self.singles}')
        words = self.sorted
        lines.append(f'top 5:                       {words[:5]}')
        lines.append(f'bottom 5:                    {words[-5:]}')
        for bins in range(2, GRAPH_BINS_MAX + 1):
            graph = self.graph(bins)
            graph_str = ' + '.join(map(prettify, graph))
            lines.append(f'initial occurence breakdown: {graph_str} = {prettify(sum(graph))}')
        return '\n'.join(lines)

def analyse_file(filename):
    with open(filename) as f:
        return Analysis.from_text(f.read())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            print(f'{filename}:\n{analyse_file(filename)}\n')
    else:
        print(f'Usage: {sys.argv[0]} [text file]')
