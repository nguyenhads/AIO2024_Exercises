# Function to read a txt file and count a number of an appearance of a word
# Output is a dictionary in which key is a word and value is the appearance of the word
from pathlib import Path
from typing import Dict, Union


def word_count(file_path: Union[Path, str]) -> Dict[str, int]:

    res = {}
    with open(file_path, 'r') as f:
        for sentence in f.readlines():
            cleaned_sentence = sentence.strip().replace('\n', '')
            for word in cleaned_sentence.split(' '):
                key = word.lower()
                if key not in res.keys():
                    res[key] = 1
                else:
                    res[key] += 1

    return res


if __name__ == "__main__":
    file_path = "./P1_data.txt"
    res = word_count(file_path)
    print(res)
