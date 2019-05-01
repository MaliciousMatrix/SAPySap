from has_unique_identifer import HasUniqueIdentifer

class NamedWithId(HasUniqueIdentifer):
    def __init__(self, id, name, *args, **kwargs):
        self.name = name
        return super().__init__(id, *args, **kwargs)

    def set_name(self, value):
        assert value is not None, 'Name cannot be None'

        formatted_value = value.strip()
        assert formatted_value, 'Name cannot be whitespace or empty.'
        self._name = formatted_value

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def __eq__(self, value):
        return self.name == value.name and super().__eq__(value)