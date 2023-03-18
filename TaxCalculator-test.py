import inspect
# from main import TaxCalculator
from main__ import TaxCalculator

class TaxCalculator_Test():

    @classmethod
    def individual_assessment(
        cls,
        mine: int,
        expected: int):

        cal = TaxCalculator(mine)
        result = cal.calculate_tax()
        output = expected
        # On failure

        assert int(result) == int(expected), cls.failed(
             unit=inspect.currentframe().f_code.co_name,
             mine=mine,
             output=output,
             result=result)
        
        # On Success
        cls.passed(inspect.currentframe().f_code.co_name,
                        mine=mine)

    @classmethod    
    def joint_assessment(
            cls,
            mine: int,
            spouse: int,
            expected: int):
            
            cal = TaxCalculator(mine, is_married=True)
            result = cal.calculate_joint_tax(spouse_income=spouse)
            output = expected

            #On failure
            assert int(result) == int(expected), cls.failed(
             unit=inspect.currentframe().f_code.co_name.replace("_", " ").capitalize(),
             mine=mine,
             spouse=spouse,
             output=output,
             result=result)
            
            #On success
            cls.passed(inspect.currentframe().f_code.co_name.replace("_", " ").capitalize(),
                        mine=mine,
                        spouse=spouse,)

    @staticmethod
    def failed(unit: str, output: int, result: int, mine:int, spouse: int=None,) -> str:
        return f"\nMine: {mine}\nSpouse: {spouse}\n❌ {unit} failed!!!\nExpected result is: {int(output)}, actual result is: {int(result)}"
    @staticmethod
    def passed(unit: str, mine:int, spouse: int=None,):
        print(f"Mine: {mine}\nSpouse: {spouse}\n✅ {unit} passed\n")

        
if __name__ == "__main__":
    TaxCalculator_Test.individual_assessment(mine=50000, expected=0)
    TaxCalculator_Test.individual_assessment(mine=500000, expected=41500)
    TaxCalculator_Test.individual_assessment(mine="500000", expected="41500")
    TaxCalculator_Test.individual_assessment(mine="dsfasdf", expected=0)

    TaxCalculator_Test.joint_assessment(mine=500000, spouse=100000, expected=35210)
    TaxCalculator_Test.joint_assessment(mine=1000000, spouse="dsfasdf", expected=0)
    TaxCalculator_Test.joint_assessment(mine=1000000, spouse=-1000, expected=104060)
    TaxCalculator_Test.joint_assessment(mine=1000000, spouse=0, expected=104060)
    TaxCalculator_Test.joint_assessment(mine=-1000000, spouse=0, expected=0)