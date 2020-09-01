# goodreads_csv_to_json_files

This script takes a csv exported from Goodreads and turns it into individual json files compatible for importing TiddlyWikis. If you have a Goodreads account, you can export a csv file of all your books. See: https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590

First you need to change a few things in the csv file. Make sure that all the keys (items in the first row) only have lowercase letters and no special characters besides - (dash), _ (underscore) or . (period). The keys in the csv file will eventually be fields in your tiddlers.

You can update what your "text" field will look like by editing the script. Change the variable TW_text_field to however you wish your tiddler to appear.

After you run the script, simply drag and drop the json files into your TiddlyWiki :)

Email any questions to sweenejp@gmail.com
