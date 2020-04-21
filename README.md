# Ebook Downloader

Download e-books from a Text file with a "Name Link" Format. 
Code generates an .xlsx with the values for downloading all the books in the list verifying it doesn't already exists in the file system.

## Built With

* [Requests](https://requests.readthedocs.io/en/master/) - Make the request of the book at the specified url.
* [Xlrd](https://xlrd.readthedocs.io/en/latest/) - Read Xlsx files
* [Xlswriter](https://xlsxwriter.readthedocs.io/) - Create and append content to Xlsx files
 
 ## Usage
 
 * Run first the [File Format](https://github.com/avfernandezz/Ebook_downloader/blob/master/file_format.py) file to process the Text file. 
 * Execute [Bulk Download](https://github.com/avfernandezz/Ebook_downloader/blob/master/bulk_download.py) to download the provided list of books.
 * #Note: Currently pointing to Springer Ebooks Url Format. File format available in repository.
 
 
 ## License

This project is licensed under the GNU v3 License - see the [LICENSE.md](LICENSE.md) file for details
