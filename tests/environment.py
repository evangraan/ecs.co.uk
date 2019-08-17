import sys, os

current = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, current)
sys.path.insert(0, current + "/shopping")
