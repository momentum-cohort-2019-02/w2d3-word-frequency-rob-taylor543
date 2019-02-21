STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import string

def clean(file):
    """Read in a string and remove special characters and stop words (keep spaces). Return the result as a string."""
    file = file.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    new_file = ""
    for char in file:
        if char in valid_chars:
            new_file += char

    file = new_file
    file = file.replace("\n", " ")
    return file

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file, "r") as open_file:
        file_string = open_file.read()
        
    clean_file = clean(file_string)

    word_freq = {}
    words = []

    for word in clean_file.split(" "):
        if word and word not in STOP_WORDS:
            words.append(word)

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    sorted_keys = sorted(word_freq, key = word_freq.__getitem__, reverse = True)

    for word in sorted_keys:
        freq = word_freq[word]
        asterisk = "*" * freq
        print (f"{word:>20} | {freq:<3} {asterisk}")
    
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
