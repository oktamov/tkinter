class Trans:
    def __init__(self, trans_word, DOJ):
        self.trans_word = trans_word
        self.DOJ = DOJ

    def get_attrs(self):
        return {
            "Trans_word": self.trans_word,
            "DOJ": self.DOJ
        }
