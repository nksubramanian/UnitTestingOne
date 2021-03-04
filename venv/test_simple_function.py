import simple_function

def test_add():
    assert simple_function.addition(3,4)==7
    assert simple_function.addition(2,3)==5
    assert simple_function.addition(3,1)==4


def test_product():
    assert simple_function.multiplication(3,4)==12
    assert simple_function.multiplication(2,4)==8
    assert simple_function.multiplication(5,4)==20