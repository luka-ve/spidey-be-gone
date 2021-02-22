import ebooklib
from ebooklib import epub

book = epub.read_epub('test/Itsy-Bitsy-Spider.epub')

chapters = [item.get_content()
            for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
