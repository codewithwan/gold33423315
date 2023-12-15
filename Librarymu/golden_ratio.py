import math

class GoldenRatioCalculator:
    def hitung_golden_ratio(self, nilai):
        phi = nilai * ((1 + math.sqrt(5)) / 2)
        return phi

    def hitung_golden_ratio_fibonacci(self, iterations=10):
        a, b = 1, 1
        for _ in range(iterations):
            a, b = b, a + b
        return b / a

    def hitung_golden_ratio_polinomial(self, nilai):
        phi = nilai * ((1 + math.sqrt(1 + 4 * (1))) / 2)
        return phi
    # Fungsi lain yang menghitung Golden Ratio berdasarkan pendekatan polinomial
