import re
from pathlib import Path
import nltk
from nltk.corpus import stopwords

nltk_data_dir = Path(__file__).resolve().parents[3] / 'venv' / 'nltk_data'
nltk_data_dir.mkdir(parents=True, exist_ok=True)
nltk.data.path.append(str(nltk_data_dir))

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords', quiet=True, download_dir=str(nltk_data_dir))
    stop_words = set(stopwords.words('english'))

def utils(text):
     # 1. Lowercase
     text = text.lower()

     # 2. Remove newlines (\n)
     text = re.sub(r'\n', ' ', text)

     # 3. Remove all numbers
     text = re.sub(r'\d+', '', text)

     # 4. Remove punctuation
     text = re.sub(r'[^\w\s]', '', text)

     # 5. Remove Non-ASCII
     text = re.sub(r'[^\x00-\x7F]+', '', text)

     # 6. Remove extra multiple spaces
     text = re.sub(r'\s+', ' ', text).strip()

     # 7. Remove stopwords

     word_tokenize = text.split(' ')
     cleaned_text = []
     for i in word_tokenize:
          if not i in stop_words:
               cleaned_text.append(i)

     clean_txt = ' '.join(cleaned_text) 

     return clean_txt