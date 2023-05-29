from ebooklib import epub
import bs4
import re

epub_path = 'Inspired_ How to Create Tech Products Customers Love by Marty Cagan.epub'

# Open the EPUB file
book = epub.read_epub(epub_path)

# Extract text from each chapter
text = ''
for item in book.get_items():
    if isinstance(item, epub.EpubHtml):
        soup = bs4.BeautifulSoup(item.get_content(), 'html.parser')
        extracted_text = soup.get_text()
        # Remove non-word characters and count words
        words = re.findall(r'\b\w+\b', extracted_text)
        text += ' '.join(words) + ' '

word_count = len(text.split())
print(f"Estimated word count: {word_count}")
