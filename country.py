""" Defines a country structure, from the csv file.
    Each field represents a column. """
class Country:

    # Contains all fields' name (each column name)
    fields = ['country_name', 'capital', 'currency', 'official_languages', 'head_of_government']

    def __init__(self, country_name = None, capital = None, currency = None, official_languages = None, head_of_government = None):
        self.country_name = country_name
        self.capital = capital
        self.currency = currency
        self.official_languages = official_languages
        self.head_of_government = head_of_government

    """  Changes the value of every field into None. 
    This can be used, in order to reutilize a variable"""
    def clean(self):
        self.country_name = None
        self.capital = None
        self.currency = None
        self.official_languages = None
        self.head_of_government = None
