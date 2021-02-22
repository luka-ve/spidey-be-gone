import ebooklib
from ebooklib import epub

import bs4
from bs4 import BeautifulSoup

book = epub.read_epub('test/Itsy-Bitsy-Spider.epub')

chapters = [item.get_content()
            for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]

soup = BeautifulSoup(chapters[1], 'lxml')

strings = [child for child in soup.descendants if type(
    child) == bs4.element.NavigableString]


def replace_creature(string):
    pass


for string in strings:
    string.replace_with(replace_creature(string))
