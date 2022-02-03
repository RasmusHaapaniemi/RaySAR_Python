'''
Created on 20 Jan 2022

@author: rhaapaniemi
'''




import numpy as np
import imageio as im
import matplotlib.pyplot as plt
from os import path
from contributions_data_class import Contributions_data
from simulation_parameters_class import Simulation_parameters





class Application:
    
    def __init__(self):
        self.data = Contributions_data()
        self.para = Simulation_parameters()
        self.save_file_path = ""
        self.visual_data = False
    
    
    def load_contributions(self, path):
               
        try:       
            data = np.genfromtxt(path, delimiter=" ")  
            # Data from contrubutions.txt
            Az_coordinate   = data[:,0]
            Ra_coordinate   = data[:,1]
            Intensity       = data[:,3]
            Ref_level       = data[:,4]
            print("Number of data rows %d" % Az_coordinate.size)    
                       
            # show data in plots
            if self.visual_data:
                '''max_index = np.argpartition(Intensity, -500)[-500:]
                plt.scatter(np.take(Az_coordinate, max_index), np.take(Ra_coordinate, max_index), marker='x')
                plt.ylabel("Range")
                plt.xlabel("Azimuth")
                plt.title("500 largest reflection points")
                plt.show()'''     
                plt.hist(Ra_coordinate, 1000)
                plt.title("Range data distribution")
                plt.ylabel("Number of data points")
                plt.xlabel("Range")
                plt.show()
                plt.hist(Az_coordinate, 1000)
                plt.title("Azimuth data distribution")
                plt.ylabel("Number of data points")
                plt.xlabel("Azimuth")
                plt.show()
                          
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
            
            
            
    def compute(self):
           
        # length of total coordinate system
        azimuth_len = self.para.az_max - self.para.az_min
        range_len = self.para.ra_max - self.para.ra_min
        # coordinate tics
        azimuth_tic = round(azimuth_len / self.para.az_spacing)
        range_tic = round(range_len / self.para.ra_spacing)
        # image matrix
        sensor_plane = np.zeros((range_tic, azimuth_tic), dtype=complex)
        

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
                noise = np.deg2rad(self.para.noise) * np.random.uniform(-1, 1)
                signal = amplitude*np.cos(angle + noise) + 1j*amplitude*np.sin(angle + noise)
                y = int(row_pixel[i]-1)
                x = int(col_pixel[i]-1)
                sensor_plane[y, x] = sensor_plane[y, x] + signal
            
            
        '''
        dB 10 scaling snesor_plane image to wanted range
        removing 0 amplitudes in load won't affect to final image!
        Adds star like shape due to sync overflow.
        '''
        # Take only length of complex pixel values
        sensor_plane = np.absolute(sensor_plane)     
        # Holds old pixel values for math function
        sensor_plane_temp = sensor_plane.copy()
        # maximum distance of star effect in pixels
        EFFECT_AREA = 100
        x = np.arange(0,EFFECT_AREA,1)
        thereshold = sensor_plane_temp.max()*self.para.response_th

        sensor_height = len(sensor_plane)
        sensor_width = len(sensor_plane[0])   
        for j in range(0, sensor_height, 1):
            for i in range(0, sensor_width, 1):
             
                if sensor_plane_temp[j,i] > thereshold:
                    x0 = i - EFFECT_AREA
                    x1 = i + EFFECT_AREA
                    if x0 < 0:
                        x0 = 0
                    if x1 > sensor_width:
                        x1 = sensor_width             
                    y0 = j - EFFECT_AREA
                    y1 = j + EFFECT_AREA
                    if y0 < 0:
                        y0 = 0
                    if y1 > sensor_height:
                        y1 = sensor_height
                        
                    values = sensor_plane_temp[j,i]/np.power((x/self.para.response_decay+1),2)   
                    sensor_plane[j,i:x1:1] += values[:x1-i]
                    sensor_plane[j:y1:1,i] += values[:y1-j]         
                    sensor_plane[j,x0:i:1] += np.flip(values[:i-x0])
                    sensor_plane[y0:j:1,i] += np.flip(values[:j-y0])
     
        with np.errstate(divide='ignore'):
            sensor_plane = np.log10(sensor_plane)*10 
            sensor_plane[sensor_plane < self.para.dB_min] = self.para.dB_min
            sensor_plane[sensor_plane > self.para.dB_max] = self.para.dB_max
            
            if self.visual_data:
                plt.hist(sensor_plane.ravel(), 1000)
                plt.title('Histogram for 10dB10')
                plt.show()
                  
           
        '''
        scale image to gray color of 255 bit
        '''
        amplitude_min = sensor_plane.min()
        amplitude_max = sensor_plane.max()
        interval = amplitude_max - amplitude_min
        step_width = 255 / interval
        sensor_plane -= amplitude_min
        sensor_plane = (sensor_plane * step_width).astype(np.uint8)
        
        if self.visual_data:
            plt.hist(sensor_plane.ravel(),256,[0,256])
            plt.title('Histogram for gray scale picture')
            plt.show()
        
        '''
        create name for image and save it to
        same folder as contributions data
        '''
        i = 1
        while i > 0:
            name = str(i) + "-Tr" + str(self.para.tr_level) + "dBmin" + str(self.para.dB_min) + \
                   "dBmax" + str(self.para.dB_max) + "N" + str(self.para.noise)
            name_string = ("/%s" % (name)) + ".jpeg"
            location = self.save_file_path + name_string
            
            if not path.exists(location):
                print("image saved to")
                print(location)
                im.imwrite(location, sensor_plane)
                i = -1
            else:
                i += 1
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    #################### SETTINGS ##########################
    
    def set_visual_data(self, value):
        self.visual_data = value
    
    def set_save_file(self, path):
        self.save_file_path = path
    
    def set_azimuth_spacing(self, value):
        self.para.az_spacing = float(value)
        
    def set_range_spacing(self, value):
        self.para.ra_spacing = float(value)
        
    def set_azimuth_min(self, value):
        self.para.az_min = float(value)
    
    def set_azimuth_max(self, value):
        self.para.az_max = float(value)
        
    def set_range_min(self, value):
        self.para.ra_min = float(value)
    
    def set_range_max(self, value):
        self.para.ra_max = float(value)
        
    def set_azimuth_res(self, value):
        self.para.az_res = float(value)
        
    def set_range_res(self, value):
        self.para.ra_res = float(value)
    
    def set_trace_level(self, value):
        self.para.tr_level = float(value)
    
    def set_dB_min(self, value):
        self.para.dB_min = float(value)
        
    def set_dB_max(self, value):
        self.para.dB_max = float(value)
    
    def set_noise_level(self, value):
        self.para.noise = float(value)

    def set_system_response_th(self, value):
        self.para.response_th = value
            
    def set_system_response_decay(self,value):
        self.para.response_decay = value
        
