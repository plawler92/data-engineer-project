The main application loop is located in app.py. It is setup to be easy to add additional transformations or load the data to different target types (JSON, db, etc) or locations. The file movies_metadata.csv has some issues relating to it's syntax (described below). The app will log these rows as errors but continute to parse the rest of the document.

 - Malformed data in the genres field ```"[{'id': 35, 'name': 'Comedy'} GATORADE"``` Movie Id = 10663
 
 - Overview field has a line break that causes the record to split into two rows improperly which cause problems with CSV readers. Movie Id = 82663, 122662, 249260
