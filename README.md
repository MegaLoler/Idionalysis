# Idionalysis

Simple tool to measure word usage in text n stuff

Made to estimate the efficacy of various texts in learning new vocabulary via extensive reading. Efficacy correlates with heavy upfront concentration of the initial occurences of words because that means words are repeated more often throughout the rest of the text. The harder the text (more unique words) the longer it has to be in order to compensate evenly.

## Examples

Heavy upfront concentration of initial occurences of words correlate with low percentage of unique usage, which in turn correlates with both text length and text ease.

Moby Dick (Long and Hard)
```bash
$ ./idionalysis.py ~/text/moby10b.txt 
total words:                 212032
unique words:                31258
unique / total:              14.74%
initial occurence breakdown: 38.72% + 24.74% + 18.59% + 17.95% = 100.0%
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
total words:                 26449
unique words:                4944
unique / total:              18.69%
initial occurence breakdown: 37.54% + 23.89% + 19.3% + 19.28% = 100.0%
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
total words:                 34367
unique words:                7447
unique / total:              21.67%
initial occurence breakdown: 36.65% + 26.14% + 19.67% + 17.54% = 100.0%
```
Siddhartha (English)
```bash
$ ./idionalysis.py ~/text/siddhartha_en.txt 
total words:                 39139
unique words:                5898
unique / total:              15.07%
initial occurence breakdown: 40.34% + 26.94% + 17.11% + 15.62% = 100.0%
```
