from country_lexer import CountryLexer
from latex_generator import Latex_Generator

# Instance of class
cl = CountryLexer('list1.csv')

# Apply processes on file
cl.process()

# Show countries stored on list
for country in cl.countries:
    country.present()

print("Finished processing")

lg = Latex_Generator('countries.tex', countries = cl.countries)
lg.initialize_doc()
lg.datafile_fill()