class Pet:
    def __init__(self, id, status, name, category, photo_url, tags):
        self.id = id
        self.name = name
        self.tags = tags
        self.photo_url = photo_url
        self.category = category
        self.status = status