# swap/test_chunks.py
from chunks import pairs
 
 
def test_pairs_with_odd_student_out():
    assert pairs(["Ada", "Alan", "Grace"]) == [["Ada", "Alan"], ["Grace"]]