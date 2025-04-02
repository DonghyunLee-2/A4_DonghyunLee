# Assignment 4 - Word Spinner
# Author: Donghyun Lee (u1538647)
# GitHub Repo: https://github.com/DonghyunLee-2/A4_DonghyunLee

import random

class Spinner:
    def __init__(self, synonym_filename):
        self.synonym_dict = {}
        with open(synonym_filename, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    word, synonyms = line.split(":", 1)
                    self.synonym_dict[word] = synonyms.split(",")

    def spin_text(self, text):
        words = text.split()
        spun_words = []
        for word in words:
            if word in self.synonym_dict and random.randint(1, 100) > 50:
                spun_words.append(random.choice(self.synonym_dict[word]))
            else:
                spun_words.append(word)
        return " ".join(spun_words)
