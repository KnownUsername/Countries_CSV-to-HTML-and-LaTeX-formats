from country import Country

class CountryLexer:

    """ ! Check if the variables are kept in class, or outside !"""

    # List of all countries
    fields = Country.fields
    field_index = 0

    current_country = Country()
    countries = []


    def t_NEWLINE(self, t):
        r'\n'

        # Restart index value
        self.field_index = 0

        # Store read country


        return t

    def t_FIELD(self, t):
        r'[^,]'

        # Set value of a class attribute ( Something close to this -> current_country.fields[field_index] = t.value )
        setattr(self.current_country, self.fields[self.field_index], t.value)

        self.field_index += 1  # Index increment, to change column/field
        return t

