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
from my_utils import slurp, split_columns_values
import ply.lex as plex
import copy


class CountryLexer:
    """ Uses lexer, to find fields on a csv file. """

    # Tokens - defines different rules for regular expressions
    tokens = ("NEWLINE", "NFIELD", "QMFIELD", "COMMA", "EOF", "DUMMY")

    # States - Environment where tokens will be applied
    states = (
        ("header", "exclusive"),
        ("body", "exclusive"),
        ("comment", "exclusive")
    )

    # List of all countries
    column_index = 0

    # Current country being read
    current_country = Country()

    # All countries read
    countries = []

    #   --- Token Rules ---   #
    def t_DUMMY(self, t):
        """ It's only defined, so that state INITIAL has a method associated to it.

            If this method is removed, the program won't run, because INITIAL needs to be defined.
            Being defined, means having any rule to work it, in this case, it's being used a method,
            where the regular expression doesn't matter, as this state is never used.

        """
        r'[-\w \']+'
        pass

    def t_header_HASHTAG(self, t):
        r"\#[^,^\n]+"

        if self.column_index == 0:
            print(t.value + "\n")
            self.comments.append(t.value)
            self.previous_state = 'header'
            self.lexer.begin('comment')

        else:
            print("Viva " + t.value)
            self.current_country.columns.append(t.value)


    def t_header_NFIELD(self, t):
        r'[-\w ()\'#]+'
        self.current_country.columns.append(t.value)


    # Fields containing quotation marks
    def t_header_QMFIELD(self, t):
        r'"[^"]+"'
        self.current_country.columns.append(t.value)

    # Commas
    def t_header_COMMA(self, t):
        r','
        self.column_index += 1  # Index increment, to change column/field

    # New lines
    def t_header_NEWLINE(self, t):
        r'\n'
        self.column_index = 0
        self.lexer.begin('body')


    # Normal fields - No quotation marks

    def t_body_HASHTAG(self, t):
        r"\#[^,^\n]+"

        if self.column_index == 0:
            self.comments.append(t.value)
            self.previous_state = 'body'
            self.lexer.begin('comment')

        else:
            # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
            setattr(self.current_country, Country.columns[self.column_index], t.value)

    def t_body_NFIELD(self, t):
        r'[-\w &()\'\.#]+'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)


    def t_comment_FILL(self, t):
        r"[^\n]+"

        self.comments[-1] = self.comments[-1] + t.value

    def t_comment_NEWLINE(self, t):
        r"\n"
        print("Opo")
        # returns to previous state
        self.lexer.begin(self.previous_state)



    # Fields containing quotation marks
    def t_body_QMFIELD(self, t):
        r'"[^"]+"'
        modified_token = t.value
        modified_token = modified_token[1:-1]
        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], modified_token)

    # Commas
    def t_body_COMMA(self, t):
        r','

        self.column_index += 1  # Index increment, to change column/field

    # New lines
    def t_body_NEWLINE(self, t):
        r'\n'

        # Restart index value
        self.column_index = 0

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

    # End Of File
    def t_body_eof(self, t):

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

    # Error manager
    def t_ANY_error(self, t):
        print(f"Unexpected tokens: {t.value[0:10]}")
        exit(1)

    #   ###################   #


    def __init__(self, filename):
        """ Class constructor.

            It's assigned it filename and initialized lexer variable with None value.

        """

        self.lexer = None
        self.filename = filename
        self.previous_state = None
        self.comments = []

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
        # Start lexer on header state
        self.lexer.begin('header')

        # Tokens' processing
        for token in iter(self.lexer.token, None):
            pass