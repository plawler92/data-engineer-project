Outstanding Issues:
Currently several rows trhow errors while being parsed. The app will log the isse with the row data, skip parsing that row, but continue parsing the rest
of the document.

1: Malformed data in the genres field ("[{'id': 35, 'name': 'Comedy'} GATORADE") Movie Id = 10663

2: Overview field has a line break that causes the record to split into two rows improperly which cause problems with CSV readers. Movie Id = 82663, 122662, 249260
