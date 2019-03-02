#!/usr/bin/env python3

import sys, re
import matplotlib.pyplot as plt

GRAPH = True
GRAPH_BINS_VISUAL = 100
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

def round_pretty(value):
    ''' do the convenient rounding '''
    return round(value, ROUND_DIGITS)

def prettify(value):
    ''' stringify a value as a rounded percentage '''
    return f'{round_pretty(value * 100)}%'

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
        initial_encounter = word not in self.occurences
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

    @property
    def top(self):
        ''' return the top 5 most occuring words '''
        return self.sorted[:5]

    @property
    def bottom(self):
        ''' return the top 5 least occuring words '''
        return self.sorted[-5:]

    def __str__(self):
        ''' make a nice report '''
        top = ', '.join(self.top)
        bottom = ', '.join(self.bottom)
        lines = list()
        lines.append(f'total words:                 {self.length}')
        lines.append(f'unique words:                {self.unique}')
        lines.append(f'unique / total:              {prettify(self.ratio)}')
        lines.append(f'singly occuring words:       {self.singles}')
        lines.append(f'singly / unique:             {prettify(self.singles / self.unique)}')
        lines.append(f'top 5:                       {top}')
        lines.append(f'bottom 5:                    {bottom}')
        for bins in range(2, GRAPH_BINS_MAX + 1):
            graph = self.graph(bins)
            graph_str = ' + '.join(map(prettify, graph))
            lines.append(f'initial occurence breakdown: {graph_str} = {prettify(sum(graph))}')
        return '\n'.join(lines)

def graph(name, analysis):
    ''' display the analysis visually '''
    plt.plot(analysis.graph(GRAPH_BINS_VISUAL), label=name)

def analyse_file(filename):
    ''' do an analysis on a file '''
    with open(filename) as f:
        return Analysis.from_text(f.read())

def print_averages(analyses):
    ''' print the average results from a bulk '''
    def get_average(attribute):
        ''' get an average attribute given either a attribute name or a function '''
        f = attribute if callable(attribute) else lambda analysis: getattr(analysis, attribute)
        return sum(map(f, analyses)) / len(analyses)
    def queue(prompt, attribute, wrapper=None):
        ''' add a line to the report '''
        value = get_average(attribute)
        if wrapper: value = wrapper(value)
        lines.append(f'{prompt} {value}')
    lines = list()
    queue('total words:          ', 'length', round_pretty)
    queue('unique words:         ', 'unique', round_pretty)
    queue('unique / total:       ', 'ratio', prettify)
    queue('singly occuring words:', 'singles', round_pretty)
    queue('singly / unique:      ', lambda a: a.singles / a.unique, prettify)
    s = '\n'.join(lines)
    print(f'[AVERAGES]\n{s}')

def bulk_analyse(filenames):
    ''' do an analysis on a bunch of files! '''
    # setup graph if doing that
    if GRAPH:
        plt.figure('idionalysis')
        plt.xlabel('% text position')
        plt.ylabel('% concentration of initial encounters of words')
    # first get each individual analyses
    analyses = list(map(analyse_file, filenames))
    # and print each result
    for filename, analysis in zip(filenames, analyses):
        print(f'[{filename}]\n{analysis}\n')
        # work the graph if doin that
        if GRAPH: graph(filename, analysis)
    # print some averages if there was more than one
    if len(analyses) > 1: print_averages(analyses)
    # show the graph if any
    if GRAPH:
        # totes stole this from stack overflow
        plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
        # show it
        plt.legend()
        plt.show()

if __name__ == '__main__':
    if len(sys.argv) > 1: bulk_analyse(sys.argv[1:])
    else: print(f'Usage: {sys.argv[0]} [text file]')
