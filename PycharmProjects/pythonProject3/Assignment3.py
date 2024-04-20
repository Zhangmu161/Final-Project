class EuclideanAlgorithm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_gcd(self):
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b
        return a

# Example usage:
gcd_calculator = EuclideanAlgorithm(48, 18)
print(gcd_calculator.calculate_gcd())  # Output: 6
