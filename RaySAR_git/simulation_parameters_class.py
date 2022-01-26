'''
Created on 21 Jan 2022

@author: rhaapaniemi
'''




class Simulation_parameters():
    '''# step settings
    def __init__(self):
        self.az_spacing = 0.428
        self.ra_spacing = 0.22
        self.az_min     = -40
        self.az_max     = 40
        self.ra_min     = 75
        self.ra_max     = 135
        self.az_res     = 1
        self.ra_res     = 1
        self.noise      = 0
        self.tr_level   = 5
        self.dB_clip    = 100'''
    
    # ball settings
    def __init__(self):
        self.az_spacing = 0.2
        self.ra_spacing = 0.2
        self.az_min     = -15
        self.az_max     = 15
        self.ra_min     = 62
        self.ra_max     = 137
        self.az_res     = 1
        self.ra_res     = 1
        self.noise      = 20
        self.tr_level   = 2
        self.dB_min     = -20
        self.dB_max     = 100
    
    