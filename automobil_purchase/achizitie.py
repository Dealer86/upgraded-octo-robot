from automobil_purchase.automobil import Automobil
from automobil_purchase.motor import Motor


class Achizitie:
    def __init__(self, automobile: list[Automobil]):
        self.automobile = automobile

    def cautare_optiuni(self):
        cai_putere = input("Intre ce valori min si max doriti: ").split(" ")
        cai_putere_min = int(cai_putere[0])
        cai_putere_max = int(cai_putere[1])
        vopsea_input = input("Doriti vopsea metalizata, da sau nu?: ").lower()
        vopsea = vopsea_input == "da"

        optiuni = []
        for automobil in self.automobile:
            if (
                (cai_putere_min <= automobil.motor.putere_maxima)
                and (cai_putere_max >= automobil.motor.putere_maxima)
                and (vopsea == automobil.vopsea_metalizata)
            ):
                optiuni.append(automobil)
        if len(optiuni) == 0:
            print("Nu am gasit masini")
        lista_de_optiuni = [a.afiseaza_carac() for a in optiuni]
        return " ".join(lista_de_optiuni)


motor1 = Motor(1, 1, 100)
auto1 = Automobil(motor1, 1, 1, 1, 1, 1, "Dacia", False, False)

motor2 = Motor(1, 1, 300)
auto2 = Automobil(motor2, 1, 1, 1, 1, 1, "Ferrari", True, True)

ac = Achizitie([auto1, auto2])
print(ac.cautare_optiuni())
