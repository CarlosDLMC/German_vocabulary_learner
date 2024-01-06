from pdf_operations import get_words_by_subject

words_by_subject = get_words_by_subject("Der-deutsche-Wortschatz-von-A1-bis-B2-Lingster-Academy.pdf")

print("total number of words: ", sum(len(words_list) for words_list in words_by_subject.values()))