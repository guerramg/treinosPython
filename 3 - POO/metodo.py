class Movie:
    # METODO CONSTRUTOR
    def __init__(self, name, yearLaunch, includedPlan, note, duration):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.duration = duration
        
    # METODO STR
    def __str__(self) -> str:
        return f"Filme: {self.name}"

    # METODO INTERNO
    def ficha(self):
        print('#Dados do Filme')
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está no Plano: {self.includedPlan}")
        print(f"Nota do Filme: {self.note}")
        print(f"Duração do Filme: {self.duration}\n")


mario = Movie('Mario', 2023, True, 5.0, 120)
topGun = Movie('Top Gun', 2022, False, 4.5, 160)

mario.ficha()
topGun.ficha()