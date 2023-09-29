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
        
movie = Movie('Mario', 2023, False, 5.0, 130)

print(movie)