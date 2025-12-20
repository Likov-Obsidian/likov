from typing import List, Dict, Union

def calc_avg(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def fmt_fio(parts: List[str], capitalize: bool = True) -> str:
    fio = " ".join(parts)
    return fio.title() if capitalize else fio

def filter_scores(data_dict: Dict[str, Union[int, float]], 
                  min_value: Union[int, float]) -> Dict[str, Union[int, float]]:
    return {k: v for k, v in data_dict.items() if v >= min_value}

if __name__ == "__main__":
    print("calc_avg([10, 20, 30, 40]) =", calc_avg([10, 20, 30, 40]))
    print()
    
    print('fmt_fio(["Арсений", "иван", "Яковенко"]) =', 
          fmt_fio(["Арсений", "иван", "Яковенко"]))
    print('fmt_fio(["Антон", "анна", "Макс"], capitalize=False) =',
          fmt_fio(["Антон", "анна", "Макс"], capitalize=False))
    print()
    
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    print(filter_scores(scores, 90))