# Idionalysis

Simple tool to measure word usage in text n stuff

Made to estimate the efficacy of various texts in learning new vocabulary via extensive reading. Efficacy correlates with heavy upfront concentration of the initial occurences of words because that means words are repeated more often throughout the rest of the text. The harder the text (more unique words) the longer it has to be in order to compensate evenly.

## Examples

Heavy upfront concentration of initial occurences of words correlate with low percentage of unique usage, which in turn correlates with both text length and text ease.

```bash
$ ./idionalysis.py texts/*
texts/alice.txt:
total words:                 26388
unique words:                2755
unique / total:              10.44%
initial occurence breakdown: 68.71% + 31.29% = 100.0%
initial occurence breakdown: 54.26% + 25.99% + 19.75% = 100.0%
initial occurence breakdown: 45.84% + 22.87% + 15.75% + 15.54% = 100.0%
initial occurence breakdown: 40.22% + 20.15% + 15.17% + 12.56% + 11.91% = 100.0%

texts/harry7.txt:
total words:                 197522
unique words:                12211
unique / total:              6.18%
initial occurence breakdown: 72.58% + 27.42% = 100.0%
initial occurence breakdown: 59.32% + 23.42% + 17.26% = 100.0%
initial occurence breakdown: 50.66% + 21.92% + 14.89% + 12.53% = 100.0%
initial occurence breakdown: 44.92% + 20.41% + 14.26% + 10.32% + 10.1% = 100.0%

texts/moby10b.txt:
total words:                 211805
unique words:                19761
unique / total:              9.33%
initial occurence breakdown: 67.51% + 32.49% = 100.0%
initial occurence breakdown: 53.12% + 25.66% + 21.22% = 100.0%
initial occurence breakdown: 43.5% + 24.01% + 17.12% + 15.37% = 100.0%
initial occurence breakdown: 36.68% + 22.91% + 14.65% + 13.89% + 11.87% = 100.0%

texts/siddhartha_de.txt:
total words:                 34367
unique words:                5069
unique / total:              14.75%
initial occurence breakdown: 66.27% + 33.73% = 100.0%
initial occurence breakdown: 50.33% + 29.1% + 20.58% = 100.0%
initial occurence breakdown: 40.34% + 25.92% + 18.37% + 15.37% = 100.0%
initial occurence breakdown: 35.43% + 20.38% + 19.23% + 12.57% + 12.39% = 100.0%

texts/siddhartha_en.txt:
total words:                 39139
unique words:                3638
unique / total:              9.3%
initial occurence breakdown: 72.73% + 27.27% = 100.0%
initial occurence breakdown: 56.29% + 26.97% + 16.74% = 100.0%
initial occurence breakdown: 46.15% + 26.58% + 14.49% + 12.78% = 100.0%
initial occurence breakdown: 41.23% + 20.81% + 17.67% + 10.36% + 9.92% = 100.0%

texts/the_elfin_hill.txt:
total words:                 2504
unique words:                820
unique / total:              32.75%
initial occurence breakdown: 64.15% + 35.85% = 100.0%
initial occurence breakdown: 48.05% + 30.61% + 21.34% = 100.0%
initial occurence breakdown: 36.71% + 27.44% + 20.37% + 15.49% = 100.0%
initial occurence breakdown: 31.34% + 24.15% + 19.39% + 13.05% + 12.07% = 100.0%
```
