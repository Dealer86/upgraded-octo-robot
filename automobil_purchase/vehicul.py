from automobil_purchase.motor import Motor


class Vehicul:
    # număr roţi (int), număr uşi (int), număr locuri (int);
    # capacitate rezervor (int) /portbagaj (int) u.m. : litru;
    def __init__(
        self,
        motor: Motor,
        numar_roti: int,
        numar_usi: int,
        numar_locuri: int,
        capacitate_rezervor: int,
        portbagaj: int,
    ):
        self.numar_roti = numar_roti
        self.numar_usi = numar_usi
        self.numar_locuri = numar_locuri
        self.capacitate_rezervor = capacitate_rezervor
        self.portbagaj = portbagaj
        self.motor = motor

    def afiseaza_caractersitici(self):
        afisaj = (
            "\nMotor: Putere/Cilindri/Supape: " + self.motor.afiseaza_caractersistici()
        )
        afisaj += (
            "Numar roti/usi/locuri: "
            + str(self.numar_roti)
            + "/"
            + str(self.numar_usi)
            + "/"
            + str(self.numar_locuri)
        )
        afisaj += (
            "\nCapacitate rezervor/portbagaj: "
            + str(self.capacitate_rezervor)
            + "/"
            + str(self.portbagaj)
        )

        return afisaj
