from typing import List 

def total(xs: List[float]) -> float:
    # Total returns the sum of xs
    result: float = 0.0
    #for each x float in xs, add it to result
    for x in xs:
        result += x
    return result