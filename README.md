# CS50 Problem Set 6: DNA

A Python program that identifies a person from a DNA sequence by counting
Short Tandem Repeats (STRs) and matching the counts against a database.

Spec: https://cs50.harvard.edu/x/psets/6/dna/

## Usage

    python dna.py databases/large.csv sequences/5.txt
    Lavender

Prints the matching person's name, or `No match`. With the wrong number of
command-line arguments it prints a usage message and exits with status 1.

## How it works

1. Read the CSV with `csv.DictReader`. The header row gives the STRs to count,
   so nothing is hard-coded and both `small.csv` and `large.csv` work.
2. Read the DNA text file into one string.
3. For each STR, `longest_match(sequence, subsequence)` finds the longest run
   of *consecutive* repeats: `AGATAGAT` is a run of 2, `AGATCAGAT` is a run of 1.
4. Compare the counts with every person. A person matches only if all
   STR counts are equal.

## Testing

`longest_match` was tested on its own with hand-made strings before being
wired into the rest of the program. Then all five small-database sequences
were checked, then the large database, and finally `check50`.
