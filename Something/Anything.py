class car:
    def __init__(self, marka, model, kolor, top_speed, paliwo):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.top_speed = top_speed
        self.paliwo = paliwo

    def __str__(self):
        return f'{self.kolor} {self.marka} {self.model}'
BMW = car(marka="śmietnik", model="5", kolor="red", top_speed="cały chuj", paliwo="diesel")        
print(BMW)

        