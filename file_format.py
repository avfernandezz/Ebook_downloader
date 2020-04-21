import xlsxwriter


def read_file(file_name):
    file = open(file_name, 'r')
    list_books = []
    for line in file:
        if len(line.strip()) > 0:
            list_books.append(line)
    file.close()
    return list_books


def generate_worksheet(books):
    workbook = xlsxwriter.Workbook('ebooks_download.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    for book in books:
        name, url = book.split('http://', 1)
        worksheet.write(row, 0, name)
        worksheet.write(row, 1, 'http://'+url)
        row += 1
    workbook.close()


list_books = read_file('ebooks.txt')
generate_worksheet(list_books)
