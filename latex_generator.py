"""
    Project: Countries_CSV-to-HTML-and-LaTeX-formats
    Purpose: Academical
    Description: Generates a LaTeX file, based on a list of objects

    Author: João Rodrigues
    Student No.: 16928

    Course: LESI
    Subject: Languages Processing
    College: IPCA
    Academic year: 2021/2022
"""

from country import Country

class Latex_Generator:
    """ Generates LaTeX """

    def __init__(self, filename, countries):

        self.countries = countries
        self.filename = filename

    def initialize_doc(self):
        """ Writes on file default notation """

        f = open(self.filename, 'w')
        f.write('\\documentclass[a4paper,100pt,twoside]{book} \n'
                '\\usepackage{tabularx}\n'
                '\\font\\titlefont=cmr12 at 60pt \n'
                '\\title{\\titlefont Countries Information}\n'
                '\\begin{document}\n'
                '\n\\maketitle\n')
        f.close()

    def datafile_fill(self):
        """ Writes data on file """

        f = open(self.filename, 'a')

        for country in self.countries:
            field = getattr(country, country.columns[0])
            # Representation of & on LaTeX
            field = field.replace('&', '\\&')

            f.write('\\section*{\\Huge ' + field + '}\n')
            f.write('\\vspace{5mm} %5mm vertical space)\n')
            f.write('\\begin{itemize}\n')
            for column in country.columns[1:]:
                # Representation of # on LaTeX
                field = getattr(country, column).replace('#','\\#')
                f.write('\t\\item \\textbf{' + column.replace('#','\\#') + ':} ' + field + '\n')
            f.write('\\end{itemize}\n\n')
        f.close()

    def auto_fill_file(self):
        """ Joins both write files and ends document tag """

        self.initialize_doc()
        self.datafile_fill()

        f = open(self.filename, 'a')
        f.write('\\end{document}')
