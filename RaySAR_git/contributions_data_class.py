'''
Created on 21 Jan 2022

@author: rhaapaniemi
'''




import numpy as np

class Contributions_data:
    def __init__(self):
        self.az_coordinate   = np.array(0)
        self.ra_coordinate   = np.array(0)
        self.el_coordinate   = np.array(0)
        self.int_value       = np.array(0)
        self.ref_level       = np.array(0)
        self.sp_flag         = np.array(0)  