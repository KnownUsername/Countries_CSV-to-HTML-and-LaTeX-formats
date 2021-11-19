""" Defines a country structure, from the csv file.
    Each field represents a column. """
class Country:

    # Contains all fields' name (each column name)
    columns = []

    """  Changes the value of every field into None. 
    This can be used, in order to reutilize a variable"""
    def clean(self):
        for column in self.columns:
            setattr(self, column, None)

    def present(self):
        for column in self.columns:
            print(f'{column}: {getattr(self, column)}\t')


