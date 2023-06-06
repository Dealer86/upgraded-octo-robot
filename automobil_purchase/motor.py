class Motor:
    # -număr cilindri (int)
    # -număr supape (int)
    # -putere maximă - cp (int)

    def __init__(self, cilindri: int, supape: int, putere_maxima: int):
        self.cilindri = cilindri
        self.supape = supape
        self.putere_maxima = putere_maxima

    def afiseaza_caractersistici(self) -> str:
        afisaj = "Cilindri: " + str(self.cilindri)
        afisaj += "\nSupape: " + str(self.supape)
        afisaj += "\nPutere maxima: " + str(self.putere_maxima) + "\n"
        return afisaj
