'''
Created on 13 Dec 2021

@author: rasmus
'''




from application import Application




def main():
        
    app = Application()
    
    
    
    '''# Car settings
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
    app.set_visual_data(True)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/car/Contributions.txt")
    app.compute()'''
    
    
    '''# Airplane settings for /rotation/6Contributions.txt
    app.set_azimuth_min(-40)
    app.set_azimuth_max(30)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(100)
    app.set_range_max(180)
    app.set_range_spacing(0.2)
    app.set_dB_min(-20)
    app.set_dB_max(-3)
    app.set_noise_level(20)
    app.set_trace_level(4)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/rotation")
    app.set_visual_data(True)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/rotation/6Contributions.txt")
    app.compute()'''
    
    '''# Airplane settings for iceye colorado airport
    app.set_azimuth_min(-6)
    app.set_azimuth_max(8)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(135)
    app.set_range_max(150)
    app.set_range_spacing(0.2)
    app.set_dB_min(-16)
    app.set_dB_max(-7)
    app.set_noise_level(15)
    app.set_trace_level(4)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane")
    app.set_visual_data(True)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/Contributions.txt")
    app.compute()'''
    
    '''# Airplane settings for airport_2
    app.set_azimuth_min(-14)
    app.set_azimuth_max(14)
    app.set_azimuth_spacing(0.4)
    app.set_range_min(130)
    app.set_range_max(150)
    app.set_range_spacing(0.4)
    app.set_dB_min(-19)
    app.set_dB_max(-11)
    app.set_noise_level(10)
    app.set_trace_level(4)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/airport_2")
    app.set_visual_data(True)
    app.set_system_response(False)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Airplane/airport_2/Contributions.txt")
    app.compute()'''
    
    '''# T62
    app.set_azimuth_min(-20)
    app.set_azimuth_max(20)
    app.set_azimuth_spacing(0.18)
    app.set_range_min(120)
    app.set_range_max(170)
    app.set_range_spacing(0.1833)
    app.set_dB_min(-16)
    app.set_dB_max(-10)
    app.set_noise_level(40)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62")
    app.set_visual_data(True)
    app.set_system_response_th(0.9)
    app.set_system_response_decay(1.0)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/Contributions.txt")
    app.compute()'''
    
    # Ground scene
    app.set_azimuth_min(-50)
    app.set_azimuth_max(50)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(100)
    app.set_range_max(200)
    app.set_range_spacing(0.2)
    app.set_dB_min(-25)
    app.set_dB_max(-17)
    app.set_noise_level(30)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ground")
    app.set_visual_data(True)
    app.set_system_response_th(1.1)
    app.set_system_response_decay(0.7)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ground/Contributions.txt")
    app.compute()
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    