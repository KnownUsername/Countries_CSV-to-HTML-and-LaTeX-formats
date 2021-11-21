
class HTML_Generator:
    """ Generates HTML """

    def __init__(self, countries):
        self.countries = countries

    def initialize_doc(self):
        f = open('countries.html', 'w')
        f.write('')