# Idionalysis

Simple tool to measure word usage in text n stuff

Made to estimate the efficacy of various texts in learning new vocabulary via extensive reading. Efficacy correlates with heavy upfront concentration of the initial occurences of words because that means words are repeated more often. The harder the text the longer it must be in order to compensate evenly.

## Examples

Heavy upfront concentration of initial occurences of words correlate with percentage of low percentage of unique usage, which in turn correlates with both text length and text ease.

Moby Dick (Long and Hard)
```bash
$ ./idionalysis.py ~/text/moby10b.txt 
total words:                 214112
unique words:                31641
unique / total:              14.78%
initial occurence breakdown: 38.96% + 24.76% + 18.49% + 17.79% = 100.0%
```
Harry Potter and the Deathly Hallows (Long and Easy)
```bash
$ ./idionalysis.py ~/text/harry7.txt
total words:                 200119
unique words:                22538
unique / total:              11.26%
initial occurence breakdown: 43.13% + 22.82% + 18.5% + 15.56% = 100.0%
```
Alice in Wonderland
```bash
$ ./idionalysis.py ~/text/alice.txt 
total words:                 29465
unique words:                5583
unique / total:              18.95%
initial occurence breakdown: 36.29% + 22.68% + 19.15% + 21.89% = 100.0%
```
The Elfin Hill
```bash
$ ./idionalysis.py ~/text/the_elfin_hill.txt 
total words:                 2505
unique words:                955
unique / total:              38.12%
initial occurence breakdown: 33.72% + 26.6% + 22.2% + 17.49% = 100.0%
```
Siddhartha (German)
```bash
$ ./idionalysis.py ~/text/siddhartha.txt 
total words:                 37428
unique words:                8307
unique / total:              22.19%
initial occurence breakdown: 35.45% + 25.15% + 18.41% + 20.99% = 100.0%
```
Siddhartha (English)
```bash
$ ./idionalysis.py ~/text/siddhartha_en.txt 
total words:                 42166
unique words:                6512
unique / total:              15.44%
initial occurence breakdown: 38.93% + 25.35% + 16.32% + 19.39% = 100.0%
```
