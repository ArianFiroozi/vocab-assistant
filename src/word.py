class Word:
    def __init__(self, text, read=False):
        self.text=text
        self.read=read
        self.meaning=""
        self.show_again=True

    def set_meaning(self, meaning):
        self.meaning=meaning

    def __repr__(self):
        return self.text