import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sys.path.append('src')
from analysis_visualizations import visualize_classification

def test_data():
    return pd.DataFrame({
        'age':[41,23,46,70],
        'TSH':[1.3, 4.1, 0.98, 0.16],
        'TT4':[125,102,109,175],
        'T4U':[1.14,0.91,0.87,1.3],
        'FTI':[109,120,70,141]
    })

def test_visualize_classification_returns_none():
    result = visualize_classification(test_data(), np.random.randint(low=0, high = 2, size = (4,)))
    assert result is None

def test_visualize_classification_calls_show(monkeypatch):
    #list so it's global
    called = [False] 
    #runs if .show() is ran
    def test_show(test):
        called[0] = True
    monkeypatch.setattr(plt, "show", test_show)
    visualize_classification(test_data(), np.random.randint(low=0, high = 2, size = (4,)))
    assert called[0] == True