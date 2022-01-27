'''
Created on 13 Dec 2021

@author: rasmus
'''




from application import Application




def main():
        
    app = Application()
    
    
    
    # Car settings
    app.set_azimuth_min(-30)
    app.set_azimuth_max(30)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(100)
    app.set_range_max(180)
    app.set_range_spacing(0.2)
    app.set_dB_min(-30)
    app.set_dB_max(100)
    app.set_noise_level(20)
    app.set_trace_level(4)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/car")
    app.set_visual_data(False)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/car/Contributions.txt")
    app.compute()
    
    
    '''# Airplane settings
    app.set_azimuth_min(-40)
    app.set_azimuth_max(30)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(100)
    app.set_range_max(180)
    app.set_range_spacing(0.2)
    app.set_dB_min(-30)
    app.set_dB_max(100)
    app.set_noise_level(20)
    app.set_trace_level(4)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane")
    app.set_visual_data(False)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/Contributions.txt")
    app.compute()'''
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    