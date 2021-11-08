from country import Country
from my_utils import slurp
import ply.lex as plex

class CountryLexer:

    """ ! Check if the variables are kept in class, or outside !"""
    tokens = ("NEWLINE", "FIELD")

    # List of all countries
    field_index = 0

    current_country = Country()
    countries = []


    def t_NEWLINE(self, t):
        r'\n'

        # Restart index value
        self.field_index = 0

        # Store read country
        self.countries.append(self.current_country)

        # Set all class's variables to None
        self.countries.clear()

        return t  # does it return?

    def t_FIELD(self, t):
        r'[^,]'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, Country.fields[self.field_index], t.value)

        self.field_index += 1  # Index increment, to change column/field
        return t

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[0:10]}")
        exit(1)

    def __init__(self):
        self.lexer = None


cl = CountryLexer()
file = slurp('small_text.csv')
#Ola = CalcLexer()
#lexer = plex.lex()
cl.lexer = plex.lex()
cl.lexer.input(file)
for token in iter(cl.lexer.token, None):
    pass
print("Finished processing")
