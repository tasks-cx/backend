class Host:
    def __init__(self, raw_str):
        self.host = raw_str

    def __str__(self):
        return f"{self.host}"

