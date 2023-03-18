class TaxCalculator:
    def __init__(self, income, is_married=False):
        self._validate_is_number(income)
        income = max(0, int(income))
        self.income = income
        self.is_married = is_married
        self.allowance = 132000 if not is_married else 264000
        self.mpf = min(income * 0.05, 18000)
        self.taxable_income = self.income - self.allowance - self.mpf
        self.tax_brackets = [(50000, 0.02), (50000, 0.06), (50000, 0.1), (50000, 0.14), (None, 0.17)]

    def calculate_tax(self):
        taxable_income = self.taxable_income
        total_tax = 0
        for (limit, rate) in self.tax_brackets:
            if taxable_income > 0:
                if limit is None:
                    tax = taxable_income * rate
                else:
                    tax = min(taxable_income, limit) * rate
                total_tax += tax
                taxable_income -= (limit if limit else 0)
            else:
                break
        return total_tax

    def print_tax(self, total_tax, income_type):
        print(f"{income_type} Total payable tax amount:", int(total_tax))

    def calculate_joint_tax(self, spouse_income):
        self._validate_is_number(spouse_income)
        spouse_income = max(0, int(spouse_income))
        joint_calculator = TaxCalculator(self.income + spouse_income, is_married=True)
        joint_calculator.mpf = min(self.income * 0.05, 18000) + min(spouse_income * 0.05, 18000)
        joint_calculator.taxable_income = joint_calculator.income - joint_calculator.allowance - joint_calculator.mpf
        return joint_calculator.calculate_tax()

    def joint_tax_saving(self, spouse_income):
        self._validate_is_number(spouse_income)
        spouse_income = max(0, int(spouse_income))
        joint_tax = self.calculate_joint_tax(spouse_income)
        calculator_spouse = TaxCalculator(spouse_income, is_married=False)
        return (self.calculate_tax() + calculator_spouse.calculate_tax()) - joint_tax

    def _validate_is_number(self, input):
        try_number = float(input) if str(input).isdigit() else None
        assert try_number is not None, f"\n❌ input -> \"{input}\" isn't a number"

def input_income(prompt):
    while True:
        try:
            income = int(input(prompt))
            if income < 0:
                raise ValueError("Income must be a non-negative number.")
            return income
        except ValueError as e:
            print(str(e))


if __name__ == "__main__":
    while True:
        try:
            is_married = input('Married(y/n)').lower()
            if is_married not in ['y', 'n']:
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
            is_married = is_married == 'y'
            break
        except ValueError as e:
            print(str(e))

    if is_married:
        income1 = input_income('Your yearly income: ')
        income2 = input_income("Spouse's yearly income: ")

        calculator1 = TaxCalculator(income1, is_married=False)
        tax1 = calculator1.calculate_tax()
        calculator1.print_tax(tax1, "For yourself - ")

        calculator2 = TaxCalculator(income2, is_married=False)
        tax2 = calculator2.calculate_tax()
        calculator2.print_tax(tax2, "For your spouse - ")

        print("Total tax payable by you and your spouse ", int(tax1 + tax2))
        joint_tax = calculator1.calculate_joint_tax(income2)
        calculator1.print_tax(joint_tax, "Jont Assessment - ")

        tax_saving = calculator1.joint_tax_saving(income2)
        if tax_saving > 0 and int(tax1 + tax2) > joint_tax:
            print('Filing jointly is better. You can save:', int(tax_saving))
        elif tax_saving ==0 and int(tax1 + tax2) == 0 or joint_tax == 0:
            print('None')
        else:
            print('Filing separately is better.')
    else:
        income = input_income('Your yearly income: ')
        calculator = TaxCalculator(income)
        tax = calculator.calculate_tax()
        calculator.print_tax(tax, "Total payable tax amount")