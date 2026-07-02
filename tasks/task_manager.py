# Açıklama: Liste olarak verilen sayıların ortalamasını hesapla.
# 📥 Input: [5, 10, 15]
# 📤 Output: 10.0
from scipy.stats import ttest_ind
import math
def calculate_mean(data: list[float]) -> float:
    return sum(data) / len(data)
    pass

# Açıklama: Liste olarak verilen sayıların standart sapmasını hesapla.
# 📥 Input: [5, 10, 15]
# 📤 Output: 5.0
def calculate_std(data: list[float]) -> float:
    ort = calculate_mean(data)
    n = len(data)
    toplam = sum((x - ort) ** 2 for x in data)
    return math.sqrt(toplam / (n - 1))
    pass

# Açıklama: Z testinin z skorunu hesapla.
# 📥 Input: sample_mean=110, population_mean=100, std_dev=15, sample_size=30
# 📤 Output: 3.65
def perform_z_test(sample_mean: float, population_mean: float, std_dev: float, sample_size: int) -> float:
    return (sample_mean - population_mean) / (std_dev / math.sqrt(sample_size))
    pass

# Açıklama: İki örneklemli T-Testi yap ve p-değerini döndür.
# 📥 Input: [23, 25, 21], [20, 19, 22]
# 📤 Output: 0.189 (örnek)
def perform_t_test(sample1: list[float], sample2: list[float]) -> float:
    t_stat, p_value = ttest_ind(sample1, sample2)
    return round(p_value, 3)
    pass

# Açıklama: p-değerini anlamlılık seviyesine göre yorumla.
# 📥 Input: p_value=0.03, alpha=0.05
# 📤 Output: "Sonuç anlamlıdır."
def interpret_p_value(p_value: float, alpha: float = 0.05) -> str:
    if p_value < alpha:
        return "Sonuç anlamlıdır."
    else:
        return "Sonuc anlamlı degildir."
    pass

# Açıklama: Karakterin her bölümdeki öldürme sayılarını liste olarak çıkar.
# 📥 Input: {"Jesse": [2, 0, 1], "Walter": [5, 3, 6]}, character="Walter"
# 📤 Output: [5, 3, 6]
def extract_character_kill_counts(data: dict, character: str) -> list[int]:
    return data[character]
    pass

# Açıklama: İstenen sezonun laboratuvar üretim verilerini döndür.
# 📥 Input: {"S1": [100, 110], "S2": [95, 98]}, season="S2"
# 📤 Output: [95, 98]
def season_wise_lab_output(data: dict[str, list[float]], season: str) -> list[float]:
    return data[season]
    pass

# Açıklama: İki sezonun üretim verilerini karşılaştırmak için t-testi uygula ve p-değeri döndür.
# 📥 Input:
# data = {
#     "S1": [100, 110, 105],
#     "S2": [90, 88, 92]
# }
# 📤 Output: 0.027
def compare_lab_output_between_seasons(data: dict[str, list[float]], season1: str, season2: str) -> float:
    grup1 = data[season1]
    grup2 = data[season2]
    return perform_t_test(grup1, grup2)
    pass

    