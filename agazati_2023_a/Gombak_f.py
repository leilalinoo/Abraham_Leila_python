class Gombak:
    #gomba neve@nemzettség@évszak
    def __init__(self, sor: str):
        darabok = sor.strip().split("@")
        self.nev = sor[0]
        self.nemzettseg = darabok[1]
        self.orszag = darabok[2]