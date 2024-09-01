# Python3 code to illustrate the conversion of
# "unknown format" strings to DateTime objects

# Importing parser from the dateutil.parser
import dateutil.parser as parser

# Initializing an unknown format date string
date_string = "19750503T080120"

# Calling the parser to parse the above
# specified unformatted date string
# into a datetime objects
date_time = parser.parse(date_string)

# Printing the converted datetime object
print(date_time)