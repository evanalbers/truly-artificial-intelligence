import pytest
from dataset.syntax import Syntax

"""
TESTING NOTE
- test addition and subtraction, operands 
- can a model that knows 1 + 9 = 10 arrive at -10 from -9 - 1?

"""

def addition(a, b):
    """ basic addition function """
    return a + b

def subtraction(a, b):
    """ basic subtraction function """
    return a - b

def multiplication(a, b):
    """ basic multiplication function """
    return a * b

def floor_division(a, b):
    """ basic floor division operation"""
    return a // b

@pytest.fixture
def example_syntax_one():
    """ sets up an example syntax 
    Operators
    ---------
    addition : '+'
        traditional addition operation.
        5 + 5 -> 10

    subtraction : '-'
        traditional subtraction operation.
        5 - 5 -> 0

    Operands 
    --------

    all real numbers using digits 0-9.
    """

    syntax_dict = {}
    syntax_dict['+'] = addition
    syntax_dict['-'] = subtraction

    for num in range(10):
         syntax_dict[str(num)] = str(num)
    return Syntax(syntax_dict)

@pytest.fixture
def example_syntax_two():
    """ example context that supports the following: 
    Operators
    ---------
    addition : '+'
        traditional addition operation.
        5 + 5 -> 10

    subtraction : '-'
        traditional subtraction operation.
        5 - 5 -> 0

    multiplication : "*"
        traditional multiplication operation.
        5 * 5 -> 25

    divison : "/"
        floor division operation.
        10 / 2 -> 5
        10 / 3 -> 3

    Operands 
    --------

    all real numbers using digits 0-9.
     
     """

    syntax_dict = {}
    syntax_dict['+'] = addition
    syntax_dict['-'] = subtraction
    syntax_dict['*'] = multiplication
    syntax_dict['/'] = floor_division

    for num in range(10):
         syntax_dict[str(num)] = str(num)

    return Syntax(syntax_dict)

class TestSyntax:
    """ a unit test class for the Syntax class """
    
    @pytest.mark.parametrize(
                "syntax, input, expected",
                [
                    (example_syntax_one, "5 + 4", "9"),
                    (example_syntax_one, "5 + 3 - 2 + 6 - 9 + 1", "4"),
                    (example_syntax_two, "5 / 4", "0"),
                    (example_syntax_two, "5 * 4",  "20"),
                ],
                indirect=['syntax']
    )
    def test_exp_eval(self, syntax, input, expected):
        """ tests expression evalutation using syntax """
        s = syntax
        output = s.evaluate(input)
        assert output == expected

    
    @pytest.mark.parametrize(
                "syntax, input, expected_error",
                [
                    (example_syntax_one, "5 * 4", "NoSuchOperator"),
                    (example_syntax_two, "5 % 5", "NoSuchOperator"),
                    (example_syntax_two, "5 & 5", "NoSuchOperator"),
                    (example_syntax_one, "5 a 5", "NoSuchOperator"),
                    (example_syntax_two, "a + 5", "NoSuchOperand")
                ],
                indirect=['syntax']
    )
    def test_runtime_exceptions(self, syntax, input, expected_error):
        """ tests that correct runtime exceptions are being thrown for incorrect input """

        s = syntax
        with pytest.raises(RuntimeError) as excinfo:
            s.evaluate(input)
            assert expected_error in str(excinfo.value)






    

