"""
    Project: Countries_CSV-to-HTML-and-LaTeX-formats
    Purpose: Academical
    Description: Contains a class using lexer, to find fields on a csv file.

    Author: João Rodrigues
    Student No.: 16928

    Course: LESI
    Subject: Languages Processing
    College: IPCA
    Academic year: 2021/2022
"""

# Imports
from country import Country
from my_utils import slurp
import ply.lex as plex
import copy


class CountryLexer:
    """ Uses lexer, to find fields on a csv file. """

    # Tokens - defines different rules for regular expressions
    tokens = ("NEWLINE", "NFIELD", "QMFIELD", "COMMA", "EOF")

    # List of all countries
    column_index = 0

    # Current country being read
    current_country = Country()

    # All countries read
    countries = []

    #   --- Token Rules ---   #

    # Normal fields - No quotation marks
    def t_NFIELD(self, t):
        r'[-\w \']+'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

    # Fields containing quotation marks
    def t_QMFIELD(self, t):
        r'"[^"]+"'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

    # Commas
    def t_COMMA(self, t):
        r','
        self.column_index += 1  # Index increment, to change column/field

    # New lines
    def t_NEWLINE(self, t):
        r'\n'

        # Restart index value
        self.column_index = 0

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

    # End Of File
    def t_eof(self, t):

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

    # Error manager
    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[0:10]}")
        exit(1)

    #   ###################   #


    def __init__(self, filename):
        """ Class constructor.

            It's assigned it filename and initialized lexer variable with None value.

        """

        self.lexer = None
        self.filename = filename

    def process(self):
        """ Processes a csv file.
                - Reads it
                - Applies tokens' rules
                - Saves elements on a list (each line is an element)
        """

        # Reads a file content and saves it as string
        file = slurp(self.filename)
        # Initializes lexer variable
        self.lexer = plex.lex(module=self)
        # Introduces file's content on lexer
        self.lexer.input(file)

        # Tokens' processing
        for token in iter(cl.lexer.token, None):
            pass


# Code to run

# Instance of class
cl = CountryLexer('small_text.csv')

# Apply processes on file
cl.process()

# Show countries stored on list
for country in cl.countries:
    country.present()

print("Finished processing")