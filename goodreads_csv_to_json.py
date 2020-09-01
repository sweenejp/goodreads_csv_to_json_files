import csv
import json
from isbnlib import meta, desc, cover, classify, goom, isbn_from_words
import datetime

# service for looking up book data
SERVICE = 'goob'

#time stuff
current_time = datetime.datetime.now()
fmt = '%Y%m%d%H%M'

#how you want your text field to appear
TW_text_field = "{{!!long_title}} by {{!!book_author}}\n\n{{!!book_desc}}\n\n{{!!book_image}}"

csv_file_path = "/home/pi/Documents/Thonny/Goodreads converting to json/goodreads_library_export (3).csv"

#open csv file
with open(csv_file_path, "r") as file:
    book_dicts = csv.DictReader(file)
    for row in book_dicts:
        book = (dict(row))
        
        #write the other necessary fields for TW5
        book['created'] = book['date_added'].replace("/", "")+("000000000")
        book['modified'] = current_time.strftime(fmt)+"00001"
        
        #error handling on getting book description
        try:
            book['book_desc'] = isbn_from_words(book['isbn'])
        except:
            print("There appears to have been an error.")
            print(f"Attempting to get isbn from title: {book['title']}")
            try:
                possible_book_isbn = isbn_from_words(book['title'])
                book['book_desc'] = desc(possible_book_isbn)
            except:
                print("That didn't work either...")
                is_correct_book = "no"
                while is_correct_book != "Y":
                    possible_book_isbn = isbn_from_words(input("Type book title: "))
                    isbnlib_book = meta(possible_book_isbn, SERVICE)
                    print(isbnlib_book["Title"])
                    is_correct_book = input("Is this the correct book? y/n: ").upper()  
                
        book['type'] = "text/vnd.tiddlywiki"
        book['book_image'] = "[img[http://covers.openlibrary.org/b/isbn/" + book['isbn'] + "-L.jpg]]"
        book['text'] = TW_text_field
        
        #variable for a file name
        json_file_name = book["title"]
        
        json_string = json.dumps(book)
        print(json_string)
        #write the json file
        
        jsonfile = open(f"{json_file_name}.json", "w")
        jsonfile.write(json_string)
        jsonfile.close()
