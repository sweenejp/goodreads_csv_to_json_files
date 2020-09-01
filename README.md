# goodreads_csv_to_json_files

This script takes a csv exported from goodreads and turns it into individual json files compatible for importing TiddlyWikis.

First you need to change a few things in the csv file. Make sure that all the keys (items in the first row) only have lowercase letters and no special characters besides - (dash), _ (underscore) or . (period). The keys in the csv file will eventually be fields in your tiddlers.

You can update what your "text" field will look like by editing the script. Change the variable TW_text_field to however you wish your tiddler to appear.

Email any questions to sweenejp@gmail.com
