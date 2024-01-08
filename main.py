from pdf_operations import get_words_by_subject
from chatgpt_operations import get_translation


RESULTS_PATH = "results_txt"

words_by_subject = get_words_by_subject("Der-deutsche-Wortschatz-von-A1-bis-B2-Lingster-Academy.pdf")

print("total number of words: ", sum(len(words_list) for words_list in words_by_subject.values()))

for subject in list(words_by_subject)[11:]:
    file_name = subject.strip().replace(" ", "_") + ".txt"
    for i, word in enumerate(words_by_subject[subject]):
        if word.strip().isdigit():
            print(f"{word} is a digit, skipping")
            continue
        translation = get_translation(word)
        print(f"Got translation for word {word}! ({i+1}/{len(words_by_subject[subject])}). Writing into {file_name}...")
        with open(f"{RESULTS_PATH}/{file_name}", "a") as file:
            file.write(f"'''\n{translation}\n")