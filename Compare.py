from CharCoverage import CharCoverage
from WordCoverage import WordCoverage

class Compare:

    def compare(self, value1: str, value2: str):
        char_coverage = CharCoverage()
        word_coverage = WordCoverage()

        index_char_coverage = char_coverage.get_index(value1, value2)
        index_word_coverage = word_coverage.get_index(value1, value2)

        self.strength = self.__calculate_general_index__(index_char_coverage, index_word_coverage)


    def get_strength(self) -> float:
        return self.strength


    def __calculate_general_index__(self, index_char_coverage, index_word_coverage):
        return 100
