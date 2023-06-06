from automobil_purchase.motor import Motor
from automobil_purchase.vehicul import Vehicul


class Automobil(Vehicul):
    # firma producătoare (string) şi de alte dotări:
    # -vopsea metalizată (boolean)
    # -aer condiţionat (boolean)
    def __init__(
        self,
        motor: Motor,
        numar_roti: int,
        numar_usi: int,
        numar_locuri: int,
        capacitate_rezervor: int,
        portbagaj: int,
        firma: str,
        vopsea_metalizata: bool,
        aer_conditionat: bool,
    ):
        super().__init__(
            motor, numar_roti, numar_usi, numar_locuri, capacitate_rezervor, portbagaj
        )

        self.firma = firma
        self.vopsea_metalizata = vopsea_metalizata
        self.aer_conditionat = aer_conditionat

    def afiseaza_carac(self):
        afisaj = super().afiseaza_caractersitici()
        afisaj += (
            "\nFirma/vopsea_metalizata: "
            + str(self.firma)
            + "/"
            + ("Da" if self.vopsea_metalizata else "Nu")
        )
        afisaj += "\nAer conditionat: " + ("Da" if self.aer_conditionat else "Nu")
        return afisaj
