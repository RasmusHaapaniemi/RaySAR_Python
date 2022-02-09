'''
Created on 13 Dec 2021

@author: rasmus
'''




import sys
import json
import pprint
from application import Application


def main(argv):
        
    app = Application()
    
    if len(argv) != 3:
        print("\nArgiments are not correct!!!\nExiting program...\n\n")
  
    with open(argv[1]) as json_file:
        data = json.load(json_file)
        
    for settings in data:
        if settings['fileName'] ==  argv[2]:
            print("\nParameters from:\n" + settings['fileName'] + " selected\n")
            pprint.pprint(settings)
            
            app.set_azimuth_min(settings['azimuthMin'])
            app.set_azimuth_max(settings['azimuthMax'])
            app.set_azimuth_spacing(settings['azimuthSpacing'])
            app.set_range_min(settings['rangeMin'])
            app.set_range_max(settings['rangeMax'])
            app.set_range_spacing(settings['rangeSpacing'])
            app.set_dB_min(settings['dBmin'])
            app.set_dB_max(settings['dBmax'])
            app.set_dB_rng(settings['dBrng'])
            app.set_noise_level(settings['noise'])
            app.set_trace_level(settings['traceLevel'])
            app.set_system_response_th(settings['responseTh'])
            app.set_system_response_decay(settings['responseDecey'])
            app.set_visual_data(settings['visualData'])
            app.set_sar_image_rescale(settings['imageRescale'])
            app.set_folder_path(settings['path'])
            app.run()
         
    print("\n\nAll selected data is processed\nExiting program...")
    
    
    
    
    
    
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
    
    '''# T62 15
    app.set_azimuth_min(-17)
    app.set_azimuth_max(17)
    app.set_azimuth_spacing(0.30)
    app.set_range_min(366)
    app.set_range_max(400)
    app.set_range_spacing(0.30)
    app.set_dB_min(-36.0)
    app.set_dB_max(-15.0)
    app.set_dB_rng(0.01)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_visual_data(False)
    app.set_system_response_th(0.54)
    app.set_system_response_decay(0.03)
    app.set_folder_path("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/Training/15")
    app.run()'''
    
    '''# T62 17
    app.set_azimuth_min(-21)
    app.set_azimuth_max(13)
    app.set_azimuth_spacing(0.30)
    app.set_range_min(327)
    app.set_range_max(361)
    app.set_range_spacing(0.30)
    app.set_dB_min(-36.0)
    app.set_dB_max(-15.0)
    app.set_dB_rng(0.01)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_visual_data(False)
    app.set_system_response_th(0.57)
    app.set_system_response_decay(0.03)
    app.set_folder_path("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/Training/17")
    app.run()'''
    
    '''# T62 20
    app.set_azimuth_min(-17)
    app.set_azimuth_max(17)
    app.set_azimuth_spacing(0.30)
    app.set_range_min(275)
    app.set_range_max(309)
    app.set_range_spacing(0.305)
    app.set_dB_min(-36.0)
    app.set_dB_max(-15.0)
    app.set_dB_rng(0.01)
    app.set_noise_level(0)
    app.set_trace_level(5)
    app.set_visual_data(False)
    app.set_system_response_th(0.54)
    app.set_system_response_decay(0.03)
    app.set_folder_path("C:/Users/rhaapaniemi/Desktop/Testing_Folder/t-62/Training/20")
    app.run()'''
    
    '''# Ground scene
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
    app.compute()'''
    
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
    main(sys.argv)
    
    
    
    
    
    