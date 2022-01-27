'''
Created on 21 Jan 2022

@author: rhaapaniemi
'''




class Simulation_parameters():
     
    '''
    az and ra spacing needs to be at least 2x
    to POVray samplings == resolution pixels / view range!!!
    '''
    
    def __init__(self):
        self.az_spacing = 0.2
        self.ra_spacing = 0.2
        self.az_min     = -30
        self.az_max     =  30
        self.ra_min     = 100
        self.ra_max     = 180
        self.az_res     = 1
        self.ra_res     = 1
        self.noise      = 20
        self.tr_level   = 3
        self.dB_min     = -30
        self.dB_max     = 100
    
    