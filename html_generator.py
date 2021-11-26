"""
    Project: Countries_CSV-to-HTML-and-LaTeX-formats
    Purpose: Academical
    Description: Generates HTML a file, based on a list of objects

    Author: João Rodrigues
    Student No.: 16928

    Course: LESI
    Subject: Languages Processing
    College: IPCA
    Academic year: 2021/2022
"""

class HTML_Generator:
    """ Generates HTML """

    def __init__(self, filename, countries, columns_enabled = None):

        self.countries = countries
        self.filename = filename
        self.columns_enabled = columns_enabled

        # In case no columns passed, it's assumed all columns
        if not columns_enabled:
            self.columns_enabled = self.countries[0].columns[1:]

    def initialize_doc(self):
        """ Writes on file default notation """

        f = open(self.filename, 'w')
        f.write(
        '<!DOCTYPE html>\n'
        '<html lang = "en">\n'
            '\t<head>\n'
                '\t\t<meta charset="utf-8">\n'
                '\t\t<meta name = "description" content="HTML representation of a CSV file">\n'
                '\t\t<title> HTML representation of a CSV file</title>\n'
            '\t</head>\n'
            '\t<body>\n'
                '\t\t<h1> Countries Information </h1>\n'
                '\t\t<br><br>\n')
        f.close()

    def datafile_fill(self):
        """ Writes data on file """

        f = open(self.filename, 'a')

        for country in self.countries:
            f.write('\t\t<h2>' + getattr(country, country.columns[0]) +'</h2>\n')
            f.write('\t\t<ul>\n')
            for column in self.columns_enabled:
                f.write('\t\t\t<li><strong>'+ column +':</strong> ' + getattr(country, column) + '</li>\n')
            f.write('\t\t</ul>\n\n')
        f.close()

    def auto_fill_file(self):
        """ Joins both write files and ends body and html tag """

        self.initialize_doc()
        self.datafile_fill()

        f = open(self.filename, 'a')
        # Close body tag
        f.write('\t</body>\n')
        # Close html tag
        f.write('</html>')

        f.close()
