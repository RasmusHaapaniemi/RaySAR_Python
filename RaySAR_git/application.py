'''
Created on 20 Jan 2022

@author: rhaapaniemi
'''




import numpy as np
import imageio as im
from contributions_data_class import Contributions_data
from simulation_parameters_class import Simulation_parameters





class Application:
    
    def __init__(self):
        self.data = Contributions_data()
        self.para = Simulation_parameters()
        self.save_file_path = ""
    
    
    def load_contributions(self, path):
               
        try:       
            data = np.genfromtxt(path, delimiter=" ")  
            # Data from contrubutions.txt
            Az_coordinate   = data[:,0]
            Ra_coordinate   = data[:,1]
            Intensity       = data[:,3]
            Ref_level       = data[:,4]
            print("Number of data rows %d" % Az_coordinate.size)    
                   
            # Remove all data that is out of selected range
            index_select = np.where((Az_coordinate > self.para.az_min)&
                                    (Az_coordinate < self.para.az_max)&
                                    (Ra_coordinate > self.para.ra_min)&
                                    (Ra_coordinate < self.para.ra_max))
            
            self.data.az_coordinate = (np.take(Az_coordinate, index_select)).ravel()
            self.data.ra_coordinate = (np.take(Ra_coordinate, index_select)).ravel()
            self.data.intensity     = (np.take(Intensity, index_select)).ravel()
            self.data.ref_level     = (np.take(Ref_level, index_select)).ravel()      
            print("Number of data rows after removing points outside of region %d" % len(self.data.az_coordinate))   
        except:
            print("Error occurred while downloading file !!!!!")
            
            
            
    def compute(self, progress_value=None):
           
        # length of total coordinate system
        azimuth_len = self.para.az_max - self.para.az_min
        range_len = self.para.ra_max - self.para.ra_min
        # coordinate tics
        azimuth_tic = round(azimuth_len / self.para.az_spacing)
        range_tic = round(range_len / self.para.ra_spacing)
        # image matrix
        sensor_plane = np.zeros((range_tic, azimuth_tic), dtype=complex)
        
        print("Sensor plane pixels")
        print(range_tic)
        print(azimuth_tic)

        # picture pixel location offsetted from min coordinate values and centered  
        row_pixel = np.true_divide((self.data.ra_coordinate - self.para.ra_min), self.para.ra_spacing) + 0.5
        col_pixel = np.true_divide((self.data.az_coordinate - self.para.az_min), self.para.az_spacing) + 0.5
        
        '''
        Adds amplitude values to correct places in sensor_plane
        Computes phase and adds noise
        range maximum 32bit is 2,147,000,000
        '''
        for i in range(len(self.data.az_coordinate)):   
            # use only wanted trace levels
            if self.data.ref_level[i] <= self.para.tr_level:
                # compute signal angle along the distance 
                temp_angle = (-4*np.pi)/0.031*self.data.ra_coordinate[i]
                cycles = round(temp_angle/(2*np.pi))
                angle = temp_angle - cycles*2*np.pi
                # complex amplitude
                amplitude = self.data.intensity[i]
                noise = np.deg2rad(self.para.noise) * np.random.rand()
                signal = amplitude*np.cos(angle + noise) + 1j*amplitude*np.sin(angle + noise)
                y = int(row_pixel[i]-1)
                x = int(col_pixel[i]-1)
                sensor_plane[y, x] = sensor_plane[y, x] + signal
            
            
        '''
        dB 10 scaling snesor_plane image to wanted range
        removing 0 amplitudes in load won't affect to final image!
        '''
        sensor_plane = np.absolute(sensor_plane)
        with np.errstate(divide='ignore'):
            sensor_plane = np.log10(sensor_plane)*10 
            sensor_plane[sensor_plane < self.para.dB_min] = self.para.dB_min
            sensor_plane[sensor_plane > self.para.dB_max] = self.para.dB_max
           
        '''
        scale image to gray color of 255 bit
        '''
        amplitude_min = sensor_plane.min()
        amplitude_max = sensor_plane.max()
        interval = amplitude_max - amplitude_min
        step_width = 255 / interval
        sensor_plane -= amplitude_min
        sensor_plane = (sensor_plane * step_width).astype(np.uint8)
        print("Min Max dB10 amplitude")
        print(amplitude_min)
        print(amplitude_max) 
        sensor_plane = np.flip(sensor_plane, 0)
        
        '''
        create name for image and save it to
        same folder as contributions data
        '''
        name = "Tr" + str(self.para.tr_level) + "dBmin" + str(self.para.dB_min) + \
               "dBmax" + str(self.para.dB_max) + "N" + str(self.para.noise)
        name_string = ("/%s" % (name)) + ".jpeg"
        location = self.save_file_path + name_string
        print("image saved to")
        print(location)
        im.imwrite(location, sensor_plane)
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    #################### SETTINGS ##########################
    
    def set_save_file(self, path):
        self.save_file_path = path
    
    def set_azimuth_spacing(self, value):
        self.para.az_spacing = value
        print(self.para.az_spacing)
        
    def set_range_spacing(self, value):
        self.para.ra_spacing = value
        print(self.para.ra_spacing)
        
    def set_azimuth_min(self, value):
        self.para.az_min = value
        print(self.para.az_min)
    
    def set_azimuth_max(self, value):
        self.para.az_min = value
        print(self.para.az_min)
        
    def set_range_min(self, value):
        self.para.ra_min = value
        print(self.para.ra_min)
    
    def set_range_max(self, value):
        self.para.ra_max = value
        print(self.para.ra_max)
        
    def set_azimuth_res(self, value):
        self.para.az_res = value
        print(self.para.az_res)
        
    def set_range_res(self, value):
        self.para.ra_res = value
        print(self.para.ra_res)
    
    def set_trace_level(self, value):
        self.para.tr_level = value
        print(self.para.tr_level)
    
    def set_dB_min(self, value):
        self.para.dB_min = value
        print(self.para.dB_min)
        
    def set_dB_max(self, value):
        self.para.dB_max = value
        print(self.para.dB_max)
    
    def set_noise_level(self, value):
        self.para.noise = value
        print(self.para.noise)
            
        
        
