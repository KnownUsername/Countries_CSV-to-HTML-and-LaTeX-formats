from country import Country

class Latex_Generator:
    """ Generates HTML """

    def __init__(self, filename, countries):
        if countries is None:
            print("Countries are null")

        else: print("Not None")

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
        f = open(self.filename, 'a')
        for country in self.countries:
            country_obj = country
            f.write('\\section*{\\Huge '+ getattr(country, country.columns[0]) + '}\n')
            f.write('\\vspace{5mm} %5mm vertical space)\n\n')
            #f.write(''country.)
        f.close()

