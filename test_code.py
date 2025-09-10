import pytest
from simon_says import simon_says
from calculator_practice import run_total_seconds 
from io import StringIO
import sys

def test_simon_says():
    captured_output = StringIO()
    sys.stdout = captured_output
    
    simon_says()
    
    sys.stdout = sys.__stdout__
    
    expected_outputs = [
        "10",                
        "Hello, World!", 
        "13.14",      
        "21.0"  
    ]
    

    output_lines = captured_output.getvalue().splitlines()
    assert output_lines == expected_outputs, f"Expected {expected_outputs}, but got {output_lines}"
    
def test_calc():
    assert (run_total_seconds(3, 2) == 2349)
    assert (run_total_seconds(5, 3) == 3771)
    assert (run_total_seconds(10, 5) == 7110)

if __name__ == "__main__":
    pytest.main()
