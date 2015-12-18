# Poster generator for the Dropbox Hack Week Haxpo


Requires:

- `pip install flask`
- Install the font "Founders Grotesk".  Ask a designer for access to it since sadly it's not free.  (or find it on the internet)

Just run `python haxpo-poster-maker.py` to see an example.  The data comes from data.tsv which is an export from the haxpo spreadsheet.  The webpage doesn't look very nice in a browser, but the css it uses should make the print previews look correct.  My workflow was to run this, try to print it but export it to a PDF.  Do a test print of one page of the PDF, then print the full PDF.