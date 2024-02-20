class base_item:
    def __init__(self, data):
        # Initialize the description attribute based on the provided data
        print("test")
        print(data)
        self.description = data.get("description", "")