class Tax:
    brackets = [0, 100000, 250000, 1000000]
    taxRates = [0, 0.05, 0.10, 0.20]

    def tax (self, income):
        result = 0

        if(income < 0):
            raise ValueError('Negative income')
        
        if(type(income) not in [float, int]):
            raise TypeError('Income must be a number')

        for i in range(1, len(self.brackets)):
            if income > self.brackets[i]:
                result += (self.brackets[i] - self.brackets[i - 1]) * self.taxRates[i - 1]
            else:
                result += (income - self.brackets[i - 1]) * self.taxRates[i - 1]
                break
        
        if income > 1000000:
            result += (income - 1000000) * self.taxRates[3]

        return result