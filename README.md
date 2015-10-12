# ProjectMUSE_SearchForNewRecords

This project will check the Project MUSE Marc Updates page for updates 
http://muse.jhu.edu/cgi-bin/book_marc_html.cgi

It essentially automates the entering of a date and checking for updates of a given collection set

local procedures:
https://sites.google.com/a/fau.edu/technical-services-process-documentation/procedures/cataloging/vendor-specific-procedures/project-muse-upcc-ebook-updates

to use this, you'll need a CSV File (with no headers)
the first column should be the the collection ID
the second column should be the collection name (which will be used to name the file)

To get the collection ID, go to the collection set, and check for updates so that you return no results (eg use a date range of today to today)
go to your browsing history and you'll find the URL for the collection.
eg:
http://muse.jhu.edu/cgi-bin/book_marc_html.cgi?action=marcRecord&type=customUpdate&fromDate=2015-09-01&toDate=2015-10-12&collectionID=213&collectionName=2013%20American%20Studies

you would extract:
collectionID=213
collectionName=2013%20American%20Studies

