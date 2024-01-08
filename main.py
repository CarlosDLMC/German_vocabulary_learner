from pdf_operations import get_words_by_subject, PDFConstructor
from chatgpt_operations import get_translation

import os


RESULTS_PATH = "results_txt"

# Getting all the words, separated by subject
words_by_subject = get_words_by_subject("Der-deutsche-Wortschatz-von-A1-bis-B2-Lingster-Academy.pdf")

print("total number of words: ", sum(len(words_list) for words_list in words_by_subject.values()))

# Writing all the words into a .txt for every subject
for subject in list(words_by_subject):
    file_name = subject.strip().replace(" ", "_") + ".txt"
    for i, word in enumerate(words_by_subject[subject]):
        if word.strip().isdigit():
            print(f"{word} is a digit, skipping")
            continue
        translation = get_translation(word)
        print(f"Got translation for word {word}! ({i+1}/{len(words_by_subject[subject])}). Writing into {file_name}...")
        with open(f"{RESULTS_PATH}/{file_name}", "a") as file:
            file.write(f"'''\n{translation}\n")

# Reading the .txt files and converting them to pdf
for file in os.listdir(RESULTS_PATH):

    with open(f"{RESULTS_PATH}/{file}", 'r') as f:
        text = f.read()

    words_with_info = text.split("'''\n")

    file_name = file.replace(".txt", "")

    constructor = PDFConstructor(file_name)
    for word_with_info in words_with_info:
        lines = word_with_info.split("\n", 4)
        if len(lines) < 5:
            print_lines = '\n'.join(lines)
            print(f"This word has less than 5 lines: {print_lines}")
            continue
        german_word = lines[0].strip()
        spanish_translation = lines[1].strip()
        russian_translation = lines[2].strip()
        english_translation = lines[3].strip()
        sentences = lines[4]
        constructor.add_word(german_word, spanish_translation, russian_translation, english_translation, sentences)
    constructor.save_file()