# Assignment 4 - Word Spinner
# Author: Donghyun Lee (u1538647)
# GitHub Repo: https://github.com/DonghyunLee-2/A4_DonghyunLee

from Spinner import Spinner

def main():
    with open("essay.txt", "r") as f:
        original_text = f.read().lower()

    import string
    original_text = original_text.translate(str.maketrans('', '', string.punctuation))

    print("Original :", original_text)

    spinner = Spinner("synonyms-simplified.txt")

    for i in range(1, 4):
        spun_text = spinner.spin_text(original_text)
        print(f"Option {i} :", spun_text)

if __name__ == "__main__":
    main()
