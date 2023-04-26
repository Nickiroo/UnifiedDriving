""" This is the grading system for the UnifiedDriving autonomous driving AI. """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

""" Algo for grading that will take into account the following:
    
    Steering related:
    - How much time the car was in the center of the lane
    - How many times the car went out of the lane when it was not trying to change lanes, turn, merge, etc.
    - How many times a collision was detected
    
    Speed related:
    - How much time the car was below the speed limit
    - How much time the car was above the speed limit
    - How much time the car was at the speed limit
        
"""