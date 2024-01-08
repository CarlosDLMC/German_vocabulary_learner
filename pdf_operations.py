# pip install reportlab PyPDF2
from PyPDF2 import PdfReader
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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


class PDFConstructor:

    def __init__(self, file_name, total_words):
        pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))
        self.doc = SimpleDocTemplate(f'./results_pdf/{file_name}.pdf',
                                pagesize=A4,
                                title=file_name
        )
        self.story = [Paragraph(file_name, self._styles_constructor('Heading1', 'center', font_size=20, bold=True))]
        self.total_words = total_words

    def _styles_constructor(self, base: str, alignment: str, bold: bool = False, font_size: int = 12):
        alignment_dict = {
            'left': 0,
            'center': 1,
            'right': 2
        }
        style = ParagraphStyle(
            'Style',
            parent=getSampleStyleSheet()[base],
            alignment=alignment_dict[alignment],  # 0=left, 1=center, 2=right
            fontName='Helvetica-Bold' if bold else 'DejaVuSerif',
            fontSize=font_size
        )
        return style

    def add_word(self, word_number, german_word, spanish_word, russian_word, english_word, sentences):
        word_story = []
        word_story.append(Paragraph(f"{german_word} ({word_number}/{self.total_words})", self._styles_constructor('Normal', 'left', font_size=14, bold=True)))
        word_story.append(Spacer(1, 15))
        word_story.append(Paragraph(spanish_word, self._styles_constructor('Normal', 'left')))
        word_story.append(Spacer(1, 5))
        word_story.append(Paragraph(russian_word, self._styles_constructor('Normal', 'left')))
        word_story.append(Spacer(1, 5))
        word_story.append(Paragraph(english_word, self._styles_constructor('Normal', 'left')))
        word_story.append(Spacer(1, 15))
        for sentence in sentences.split('\n'):
            word_story.append(Paragraph(sentence, self._styles_constructor('Normal', 'left')))
            word_story.append(Spacer(1, 5))

        self.story += word_story
        self.story.append(Spacer(1, 15))
        # doc.build(word_story)

    def save_file(self):
        self.doc.build(self.story)


