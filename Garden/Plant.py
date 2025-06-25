class Plant():
    def __init__(self, pavadinimas = "", lotyniskas_pavadinimas = "", vienmetis = False, zemynas = "", aukstis = 0.0, valgomas = False ):
        self.pavadinimas = pavadinimas
        self.lotyniskas_pavadinimas = lotyniskas_pavadinimas
        self.vienmetis = vienmetis
        self.zemynas = zemynas
        self.aukstis = aukstis
        self.valgomas = valgomas

    def __str__(self):
        return (f"{self.pavadinimas} ({self.lotyniskas_pavadinimas}) , "
                f"{'Vienmetis' if self.vienmetis else 'Daugiametis'} , "
                f"Auga žemyne: {self.zemynas} , "
                f"Aukštis: {self.aukstis} m , "
                f"{'Valgomas' if self.valgomas else 'Nevalgomas'}")