import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string




pdf_file = open(r'C:\Users\ddnfn\OneDrive\Masaüstü\10030015.pdf', mode='rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
content = ""

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    content += page.extract_text()

pdf_file.close()
print(content)
print('******************************')
# Metin verilerini token'lar halinde ayırın
tokens = word_tokenize(content)
# Stop words'leri kaldırın
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token.lower() not in stop_words]

# Noktalama işaretlerini kaldırın
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# Kelimeleri köklerine indirin
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in stripped]
print(stemmed)