class InvalidParamException(Exception):
    def __init__(self, func, keys):
        self.message = f'Function "{func}" missing required parameter(s): {str(keys)}.'
        super().__init__(self.message)
