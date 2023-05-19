from docx import Document
import exel_lh as data

# افتح مستند Word القائم لكل شخص
def open_word_document(file_path):
    return Document(file_path)

# البيانات التي تمتلكها
data = data.tableau
id=0;
# قم بوضع البيانات في مكان محدد في كل مستند
for person in data:
    doc = open_word_document('exel_lh.docx');
    for paragraph in doc.paragraphs:
        paragraph_text = paragraph.text
        paragraph_text = paragraph_text.replace(f"{{nom}}", person['nom'])
        paragraph_text = paragraph_text.replace(f"{{prenom}}", person['prenom'])
        paragraph.text = paragraph_text
    doc.save(f'{id}.docx')
    id=id+1

      
