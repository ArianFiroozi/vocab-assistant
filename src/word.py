class Word:
    def __init__(self, text, read=False):
        self.text=text
        self.read=read
        self.meaning=""
        self.show_again=True

    def set_show_again(self, show_again):
        self.show_again=show_again

    def set_read(self, read):
        self.read=read

    def set_meaning(self, meaning):
        self.meaning=meaning

    def __repr__(self):
        return self.text