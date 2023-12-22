import g4f


class Message:
    def __init__(self, sender, content, hour):
        self.sender = sender
        self.content = content
        self.hour = hour

    def answer_bot(self):
        return g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": self.content}],
        )

    def to_json(self):
        return {
            'sender': self.sender,
            'content': self.content,
            'hour': self.hour
        }
