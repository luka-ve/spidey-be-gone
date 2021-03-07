import zipfile
import glob
import shutil
import os

import bs4
from bs4 import BeautifulSoup

import re


def main():
    old_creature = 'spider'
    new_creature = 'unicorn'

    # Unzip epub

    epub_location = r'test/Itsy-Bitsy-Spider.epub'
    extraction_location = r'test/current_book/'

    book_zip = zipfile.ZipFile(epub_location, 'r')
    book_zip.extractall(path=extraction_location)

    # Find HTML files

    html_files = glob.glob(extraction_location + '**/*.html', recursive=True)

    # Read HTML files
    for html_f in html_files:
        with open(html_f, 'r', encoding='utf8') as f:
            chapter_text = f.read()

        soup = BeautifulSoup(chapter_text, 'lxml')

        lines = [child for child in soup.descendants if type(
            child) == bs4.element.NavigableString]

        # Replace creatures
        for line in lines:
            line.replace_with(replace_creature_in_string(
                line, old_creature, new_creature))

        # Write back to HTML files
        with open(html_f, 'wb') as f:
            f.seek(0)
            f.write(soup.encode('utf8'))
            f.truncate()

    # Zip back up into .epub
    new_epub_path = 'test/out/book-out'
    write_to_epub(extraction_location, new_epub_path)

    # Clean up temp folders
    shutil.rmtree(extraction_location)


def replace_creature_in_string(string, old_creature, new_creature):
    return re.sub(old_creature, new_creature, string)


def write_to_epub(source_location, target_folder):
    target_file_path = target_folder + '.zip'
    target_file_path_epub = target_folder + '.epub'

    if os.path.isfile(target_file_path):
        os.remove(target_file_path)

    if os.path.isfile(target_file_path_epub):
        os.remove(target_file_path_epub)

    shutil.make_archive(target_folder, 'zip', source_location)

    os.rename(target_file_path, re.sub('.zip', '.epub', target_file_path))


if __name__ == '__main__':
    main()
