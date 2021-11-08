""" Defines a country structure, from the csv file.
    Each field represents a column. """
class Country:

    def __init__(self, country_name, capital, currency, official_languages, head_of_government):
        self.country_name = country_name
        self.capital = capital
        self.currency = currency
        self.official_languages = official_languages
        self.head_of_government = head_of_government

    # Contains all fields' name (each column name)
    fields = ['country_name', 'capital', 'currency', 'official_languages', 'head_of_government']
