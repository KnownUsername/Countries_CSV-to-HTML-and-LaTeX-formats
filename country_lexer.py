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
        r'[a-z A-Z-\'£Ã§]+'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

        #print(t.value)
        #print(self.current_country.country_name)

        #self.field_index += 1  # Index increment, to change column/field
        return t

    def t_QMFIELD(self, t):
        r'"[^"]+"'

        print(t.value)
        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.columns[self.column_index], t.value)

        return t

    def t_COMMA(self, t):
        r','
        #print(self.column_index)
        self.column_index += 1  # Index increment, to change column/field
        return t

    def t_NEWLINE(self, t):
        r'\n'
        #print(self.current_country.country_name)
        #print(t.value)
        # Restart index value
        self.column_index = 0

        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

        return t  # does it return?

    def t_EOF(self, t):
        r"/'"

        print("Olá!")
        # Store read country
        self.countries.append(copy.deepcopy(self.current_country))

        # Set all class's variables to None
        self.current_country.clean()

        #return t

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

###
# Provisory solution for last line
if file[-1] != '\n' and cl.current_country.country_namea:
    # Store read country
    cl.countries.append(copy.deepcopy(cl.current_country))

    # Set all class's variables to None
    cl.current_country.clean()
###

for country in cl.countries:
    country.present()

print("Finished processing")