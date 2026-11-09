import csv
import sys


def main():
    # Require exactly two command-line arguments: database CSV and DNA text file
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE.csv SEQUENCE.txt")
        sys.exit(1)

    database_path = sys.argv[1]
    sequence_path = sys.argv[2]

    # Read the database with DictReader; the header tells us which STRs to count
    with open(database_path, newline="") as file:
        reader = csv.DictReader(file)
        strs = reader.fieldnames[1:]  # everything after the "name" column
        people = list(reader)

    # Read the whole DNA sequence as a single string
    with open(sequence_path) as file:
        dna = file.read().strip()

    # Longest run of consecutive repeats for every STR in the header
    counts = {s: longest_match(dna, s) for s in strs}

    # Compare against every person; all STR counts must match
    for person in people:
        if all(int(person[s]) == counts[s] for s in strs):
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Return the longest run of consecutive repeats of subsequence in sequence."""
    longest = 0
    length = len(subsequence)

    # Try every position in the sequence as the start of a possible run
    for start in range(len(sequence)):
        run = 0
        position = start

        # Keep stepping forward one full copy at a time while the copies
        # are back-to-back (consecutive) with no gap between them
        while sequence[position:position + length] == subsequence:
            run += 1
            position += length

        # Remember the best run seen so far
        longest = max(longest, run)

    return longest


main()
