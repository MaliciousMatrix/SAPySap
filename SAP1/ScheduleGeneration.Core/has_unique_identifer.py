class HasUniqueIdentifer:
    def __init__(self, id, *args, **kwargs):
        self.id = id
        return super().__init__(*args, **kwargs)

    def set_id(self, value):
        assert isinstance(value, int) and value >= 0, 'id must be a positive integer. cannot be: ' + str(value)
        self._id = value

    def get_id(self):
        return self._id

    def __eq__(self, value):
        return self.id == value.id and type(self) == type(value)

    id = property(get_id, set_id)