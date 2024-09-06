class Word:
    def __init__(self, text, read=False):
        self.text=text
        self.read=read
        self.meaning=""
        self.show_again=True

    def do_not_show(self):
        self.show_again=False

    def set_read(self, read):
        self.read=read

    def set_meaning(self, meaning):
        self.meaning=meaning

    def __repr__(self):
        return self.text