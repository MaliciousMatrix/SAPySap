class BadTaskAssignmentException(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)