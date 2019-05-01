class TaskTradeException(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__("This indicates a failure of the task trader to execute. ERROR STATE PRESENT", *args, **kwargs)
