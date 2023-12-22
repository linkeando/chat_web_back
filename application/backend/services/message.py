class Message:
    def __init__(self, sender, content, hour):
        self.sender = sender
        self.content = content
        self.hour = hour

    def to_json(self):
        return {
            'sender': self.sender,
            'content': self.content,
            'hour': self.hour
        }
