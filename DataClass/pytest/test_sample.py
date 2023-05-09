from sample import add,validate_age
import pytest     
class TestSample:
    def test_add_num(self):
        assert add(1,2) == 3
    
    def test_add_str(self): 
        assert add("1","2") == "12"
        
    def test_validate_age(self):
        validate_age(10)
        
    def test_validate_age_invalid(self):
        with pytest.raises(ValueError,match='Age can not be less than 0.'):
            validate_age(-3)