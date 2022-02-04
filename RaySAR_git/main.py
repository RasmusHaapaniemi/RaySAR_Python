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
    app.set_azimuth_min(-17)
    app.set_azimuth_max(17)
    app.set_azimuth_spacing(0.35)#(0.24)
    app.set_range_min(368)
    app.set_range_max(402)
    app.set_range_spacing(0.35)#(0.4354)
    app.set_dB_min(-36.0)
    app.set_dB_max(-15.3)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/15-rotation")
    app.set_visual_data(False)
    app.set_system_response_th(0.47)#(0.47)
    app.set_system_response_decay(0.08)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/15-rotation/12Contributions.txt")
    app.compute()'''
    
    # Ground scene
    app.set_azimuth_min(-42)
    app.set_azimuth_max(42)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(200)
    app.set_range_max(284)
    app.set_range_spacing(0.2)
    app.set_dB_min(-37)
    app.set_dB_max(10)
    app.set_noise_level(30)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ground")
    app.set_visual_data(True)
    app.set_system_response_th(1.1)
    app.set_system_response_decay(0.7)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ground/Contributions.txt")
    app.compute()
    
    '''# steps
    app.set_azimuth_min(-15)
    app.set_azimuth_max(15)
    app.set_azimuth_spacing(0.2)
    app.set_range_min(330)
    app.set_range_max(400)
    app.set_range_spacing(0.54)
    app.set_dB_min(-20)
    app.set_dB_max(100)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/step")
    app.set_visual_data(True)
    app.set_system_response_th(1.1)
    app.set_system_response_decay(0.18)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/step/Contributions.txt")
    app.compute()'''
    
    ''' # Ship
    app.set_azimuth_min(-30)
    app.set_azimuth_max(30)
    app.set_azimuth_spacing(0.2)#(0.24)
    app.set_range_min(105)
    app.set_range_max(180)
    app.set_range_spacing(0.2)#(0.4354)
    app.set_dB_min(-37.0)
    app.set_dB_max(-13)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_save_file("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ship")
    app.set_visual_data(True)
    app.set_system_response_th(1.1)#(0.47)
    app.set_system_response_decay(0.08)
    app.load_contributions("C:/Users/rhaapaniemi/Desktop/Testing_Folder/Ship/Contributions.txt")
    app.compute()'''
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    