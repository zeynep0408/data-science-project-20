import pytest
import pandas as pd
import numpy as np
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import *

def test_calculate_mean():
    assert calculate_mean([10, 20, 30]) == 20.0

def test_calculate_std():
    assert round(calculate_std([5, 10, 15]), 2) == 5.0

def test_perform_z_test():
    z = perform_z_test(110, 100, 15, 30)
    assert round(z, 2) == 3.65

def test_perform_t_test():
    p = perform_t_test([23, 25, 21], [20, 19, 22])
    assert 0 <= p <= 1

def test_interpret_p_value():
    assert interpret_p_value(0.03) == "Sonuç anlamlıdır."

def test_extract_character_kill_counts():
    data = {"Walter": [5, 6], "Jesse": [1, 2]}
    assert extract_character_kill_counts(data, "Jesse") == [1, 2]

def test_season_wise_lab_output():
    data = {"S1": [100], "S2": [90]}
    assert season_wise_lab_output(data, "S2") == [90]

def test_compare_lab_output_between_seasons():
    data = {"S1": [100, 110, 105], "S2": [90, 88, 92]}
    p = compare_lab_output_between_seasons(data, "S1", "S2")
    assert 0 <= p <= 1

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://kaizu-api-8cd10af40cb3.herokuapp.com/projectLog"
    payload = {
        "user_id": 34,
        "project_id": 668,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()
