import pandas as pd
import numpy as np


chat_id = 230790372 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 85
    acceleration = 2 * x / time**2
    return acceleration.mean()
