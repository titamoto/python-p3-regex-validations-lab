import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo"
name_regex = re.compile(name)

phone_number = r"(?:[(| ]?5[)|-]?){10}"
phone_regex = re.compile(phone_number)

email_address = r"^\D[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-z]+"
email_regex = re.compile(email_address)
