import os
import requests
import sys
import xlrd


def create_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)
    directory = os.getcwd() + "\\" + name
    os.chdir(directory)
    if not os.path.exists("PDF"):
        os.mkdir("PDF")
    if not os.path.exists("Epub"):
        os.mkdir("Epub")
    return directory


def open_worksheet(file_name):
    try:
        workbook = xlrd.open_workbook(file_name)
        sheet = workbook.sheet_by_index(0)
    except FileNotFoundError:
        print(
            "File not found. Verify file exists and contains information within. Please run first: 'file_format.py'")
        sys.exit(1)
    return sheet


def download_ebooks(books_path, worksheet):
    # Used for Springer Books. Available til June 2020
    for row_idx in range(worksheet.nrows):
        book_name = worksheet.cell_value(row_idx, 0)
        book_file_name = book_name.strip() + '.pdf'
        url = worksheet.cell_value(row_idx, 1)

        print("Requesting: ", book_file_name, )
        response = requests.get(url)
        actual_url = response.url
        actual_url = actual_url.replace('/book/', '/content/pdf/')
        actual_url = actual_url.replace('%2F', '/')

        book_file = books_path + '\\PDF\\' + book_file_name
        print("Downloading file...")
        if not os.path.exists(book_file):
            file_content = requests.get(actual_url, allow_redirects=True)
            try:
                open(book_file, 'wb').write(file_content.content)
            except OSError:
                print('FileName appears to be incorrect')
            print("Downloaded PDF Version of: ", book_name, "\n")
        else:
            print("File: ", book_name, "|| Already exists. Download cancelled\n")

        print("Attempting to Download Epub version")
        actual_url = response.url
        actual_url = actual_url.replace('/book/', '/download/epub/')
        actual_url = actual_url.replace('%2F', '/')
        actual_url = actual_url + '.epub'

        book_file_name = book_name.strip() + '.epub'

        epub_request = requests.get(actual_url, allow_redirects=True)
        if epub_request.status_code == 200:
            print("Epub Exists: Downloading...")
            book_file = books_path + '\\Epub\\' + book_file_name
            if not os.path.exists(book_file):
                try:
                    open(book_file, 'wb').write(epub_request.content)
                except OSError:
                    print('FileName appears to be incorrect')
                print("Downloaded Epub Version of: ", book_file_name, "\n")
            else:
                print("File: ", book_file_name,
                      "|| Already exists. Download cancelled\n")
        else:
            print("Epub Version doesn't exist\n")


oldpwd = os.getcwd()
books_path = create_directory("Springer_Books")
os.chdir(oldpwd)
sheet = open_worksheet('ebooks_download.xlsx')
download_ebooks(books_path, sheet)
