# tests/test_env.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # añade la raíz al PYTHONPATH

from utils import *                 # en lugar de mva_tda.utils
from model import Model1, Model2    # en lugar de mva_tda.models
