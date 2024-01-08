from PyPDF2 import PdfReader


def get_words_by_subject(pdf_file_name):
    reader = PdfReader(pdf_file_name)

    current_subject_index = 0
    current_subject = list()
    words_by_subject = dict()
    subject_name = None
    for page in reader.pages[2:]: # nos saltamos la portada y el índice
        words = page.extract_text().split("\n")
        for word in words:
            if f"{current_subject_index + 1}." in word:
                if not subject_name:
                    subject_name = word
                    current_subject = list()
                    current_subject_index += 1
                    continue
                words_by_subject[subject_name] = current_subject.copy()
                current_subject_index += 1
                subject_name = word
                current_subject = list()
                continue
            current_subject.append(word)
    words_by_subject[subject_name] = current_subject.copy()
    return words_by_subject


