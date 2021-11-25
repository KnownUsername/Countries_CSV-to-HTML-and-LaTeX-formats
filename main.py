"""
    Project: Countries_CSV-to-HTML-and-LaTeX-formats
    Purpose: Academical
    Description: Runs all program, by filtering values and
                 generating an HTML and LaTeX file

    Author: João Rodrigues
    Student No.: 16928

    Course: LESI
    Subject: Languages Processing
    College: IPCA
    Academic year: 2021/2022
"""

from country_lexer import CountryLexer
from latex_generator import Latex_Generator
from html_generator import HTML_Generator

# Instance of class to apply Language Processing
cl = CountryLexer('small_text.csv')
# Apply lex processes on file
cl.process()

print("Choose columns you want to be seen on both documents.\n"
      "Each desired column should be inputted individually, per line.\n"
      "1st column is enabled by default, for visualization purposes.\n"
      "To end the choice of columns, it's sent an space string")
# Show columns present on csv
for column in cl.countries[0].columns:
    print('-'+ column)

# Read input from user

chosen_columns = []
    # -> Columns to be shown
for line in iter(lambda: input(">> "), " "):

    if line in cl.countries[0].columns[1:]:
        chosen_columns.append(line)

    elif line == cl.countries[0].columns[0]:
        print("This column is chosen by default and cannot be excluded.")
    else:
        print("Column doesn't exist")

# Instance of class to build LaTeX file
lg = Latex_Generator('countries.tex', countries = cl.countries, columns_enabled = chosen_columns)
# Writes info into a file with given name on class builder
lg.auto_fill_file()

# Instance of class to build HTML file
html = HTML_Generator('countries.html', countries = cl.countries, columns_enabled= chosen_columns)
# Writes info into a file with given name on class builder
html.auto_fill_file()
