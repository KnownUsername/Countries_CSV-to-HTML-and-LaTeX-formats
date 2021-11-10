import copy

from country import Country
from my_utils import slurp
import ply.lex as plex

class CountryLexer:

    """ ! Check if the variables are kept in class, or outside !"""
    tokens = ("NEWLINE", "NFIELD", "QMFIELD", "COMMA", "EOF")

    # List of all countries
    column_index = 0

    current_country = Country()
    countries = []

    def t_NFIELD(self, t):
        r'[-\w \']+'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

        return t

    def t_QMFIELD(self, t):
        r'"[^"]+"'

        print(t.value)
        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

        return t

    def t_COMMA(self, t):
        r','

        self.column_index += 1  # Index increment, to change column/field
        return t

    def t_NEWLINE(self, t):
        r'\n'

        # Restart index value
        self.column_index = 0

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

        return t  # does it return?

    def t_eof(self, t):

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[0:10]}")
        exit(1)

    def __init__(self):
        self.lexer = None

    def initialize(self):
        self.lexer = plex.lex(module=self)


cl = CountryLexer()
file = slurp('small_text.csv')

cl.initialize()
cl.lexer.input(file)

for token in iter(cl.lexer.token, None):
    pass

# Show countries stored on list
for country in cl.countries:
    country.present()

print("Finished processing")