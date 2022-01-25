'''
Created on 20 Jan 2022

@author: rhaapaniemi
'''




import numpy as np
from PIL import Image
from contributions_data_class import Contributions_data
from simulation_parameters_class import Simulation_parameters



class Application:
    
    def __init__(self):
        self.data = Contributions_data()
        self.para = Simulation_parameters()
        self.save_file_path = ""
    
    
    
    
    
    def load_contributions(self, path):
        
        data = np.genfromtxt(path, delimiter=" ")    
        try:       
            # Data from contrubutions.txt
            Az_coordinate   = data[:,0]
            Ra_coordinate   = data[:,1]
            El_coordinate   = data[:,2]
            Int_value       = data[:,3]
            Ref_level       = data[:,4]
            Sp_flag         = data[:,5]  
            print("Number of data rows %d" % Az_coordinate.size)    
            
            # Remove all rows with 0 amplitude
            TH_LEVEL = 0.01
            Az_coordinate = Az_coordinate[Int_value > TH_LEVEL]
            Ra_coordinate = Ra_coordinate[Int_value > TH_LEVEL]
            El_coordinate = El_coordinate[Int_value > TH_LEVEL]
            Ref_level     = Ref_level[Int_value > TH_LEVEL]
            Sp_flag       = Sp_flag[Int_value > TH_LEVEL]
            Int_value     = Int_value[Int_value > TH_LEVEL]
            print("Number of data rows after removing 0 amplitudes %d" % Az_coordinate.size)
            
            
            self.data.az_coordinate = Az_coordinate[Ref_level <= self.para.tr_level]
            self.data.ra_coordinate = Ra_coordinate[Ref_level <= self.para.tr_level]
            self.data.el_coordinate = El_coordinate[Ref_level <= self.para.tr_level]
            self.data.ref_level     = Ref_level[Ref_level <= self.para.tr_level]
            self.data.sp_flag       = Sp_flag[Ref_level <= self.para.tr_level]
            self.data.int_value     = Int_value[Ref_level <= self.para.tr_level]
            print("Number of data rows after removing secondary reflections %d" % len(self.data.az_coordinate))
            
        except:
            print("Error occurred!")
            
            
            
    def compute(self, progress_value=None):
        
        
        # range coordiantes....
        #self.data.ra_coordinate = self.data.ra_coordinate * (1/np.sin(np.deg2rad(22.62)))
        
        # length of total coordinate system
        azimuth_len = self.para.az_max - self.para.az_min
        range_len = self.para.ra_max - self.para.ra_min
        # coordinate tics
        azimuth_tic = round(azimuth_len / self.para.az_spacing)
        range_tic = round(range_len / self.para.ra_spacing)
        
        sensor_plane = np.zeros((range_tic, azimuth_tic))
        
        print("Sensor plane")
        print("Size m")
        print(range_tic)
        print(azimuth_tic)
        
        # Remove all data that is out of selected range
        index_select = np.where((self.data.az_coordinate > self.para.az_min)&
                                (self.data.az_coordinate < self.para.az_max)&
                                (self.data.ra_coordinate > self.para.ra_min)&
                                (self.data.ra_coordinate < self.para.ra_max))
        
        self.data.az_coordinate = np.take(self.data.az_coordinate, index_select)
        self.data.ra_coordinate = np.take(self.data.ra_coordinate, index_select)
        self.data.el_coordinate = np.take(self.data.el_coordinate, index_select)
        self.data.int_value     = np.take(self.data.int_value, index_select)
        self.data.ref_level     = np.take(self.data.ref_level, index_select)
        
        print("In range")
        print(len(index_select[0]))
        print(index_select)
        
        # picture pixel location offsetted from min coordinate values and centered  
        row_pixel = np.true_divide(self.data.ra_coordinate - self.para.ra_min, self.para.ra_spacing) + 0.5
        col_pixel = np.true_divide(self.data.az_coordinate - self.para.az_min, self.para.az_spacing) + 0.5
        
        
        '''
        wave lenght and trace level comes here
        '''
        #Iterate over data and signal amplitude to correct place in sensor plane
        '''
        range maximum 32bit is 2,147,000,000
        '''
        for i in range(len(self.data.az_coordinate[0])):   
            signal = self.data.int_value[0,i]
            y = int(row_pixel[0,i]-1)
            x = int(col_pixel[0,i]-1)
            sensor_plane[y, x] = sensor_plane[y, x] + signal
            
            '''
            imaginary ampllitude -> noise -> absolut -> clip
            '''
        
        
        '''
        scale image to gray color of 255 bit
        '''
        amplitude_min = self.data.int_value.min()
        amplitude_max = self.data.int_value.max()
        interval = amplitude_max - amplitude_min
        step_width = 255 / interval
        # smallest is zero amplitude
        sensor_plane[sensor_plane > 0] -= amplitude_min
        sensor_plane = (sensor_plane * step_width).astype(int)
        print("Min Max amplitude")
        print(amplitude_min)
        print(amplitude_max) 
        
        
        image = Image.fromarray(sensor_plane)
        image.show()
        '''name = "test_image"
        name_string = ("/%s" % (name)) + ".jpeg"
        location = self.save_file_path + name_string
        print("image saved to")
        print(location)
        image.save(location)'''
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
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
    
    def set_dBcliping(self, value):
        self.para.dB_clip = value
        print(self.para.dB_clip)
    
    def set_noise_level(self, value):
        self.para.noise = value
        print(self.para.noise)
            
        
        
