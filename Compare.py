class Compare:

    def compare(self, value1: str, value2: str):
        if value1 == value2:
            self.strength = 100
        else:
            self.strength = 0


    def get_strength(self) -> float:
        return self.strength
