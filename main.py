from country_lexer import CountryLexer
from latex_generator import Latex_Generator

# Instance of class to apply Language Processing
cl = CountryLexer('list1_new.csv')
# Apply lex processes on file
cl.process()

# Instance of class to build LaTeX file
lg = Latex_Generator('countries.tex', countries = cl.countries)
# Writes info into a file with given name on class builder
lg.auto_fill_file()