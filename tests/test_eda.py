import pytest
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('src')
from EDA import plot_correlations

#called = False
def test_data():
    return pd.DataFrame({
        'age':[41,23,46,70],
        'TSH':[1.3, 4.1, 0.98, 0.16],
        'TT4':[125,102,109,175],
        'T4U':[1.14,0.91,0.87,1.3],
        'FTI':[109,120,70,141]
    })

def test_return_none():
    result = plot_correlations(test_data())
    assert result is None
    
def test_invalid_input():
    with pytest.raises(TypeError):
        plot_correlations("invalid input")

def test_calls_show(monkeypatch):
    #list so it's global
    called = [False] 
    #runs if .show() is ran
    def test_show(test):
        called[0] = True
    monkeypatch.setattr(plt, "show", test_show)
    plot_correlations(test_data())
    assert called[0] == True
