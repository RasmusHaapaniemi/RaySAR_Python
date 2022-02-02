// File produced by AccuTrans 3D

#version 3.5;

global_settings { assumed_gamma 2.2 } 


global_settings{SAR_Output_Data 1 SAR_Intersection 0}  // activate line only for adapted POV-Ray!
                                    
                                    
#declare Cam = camera {
  orthographic
  location <100, 100, 0>  // location of virtual SAR, far field -> orthographic projection
  look_at <0,0,0>
  right 100*x            // horizontal size of view
  up 120*y               // vertical size of view
}     

// Insert camera
camera{Cam} 


#declare Runway = box{
  <100,0, 100>,
  <-100,0, 0>   
}  

#declare Grass = box{
  <100,0, 0>,
  <-100,0, -100>   
}     

  
#declare Object = sphere{
  <0,10, 0>,
  6   
}     




// Signal source
light_source {
  <100, 100, 0>
  color rgb<1, 1, 1>
  parallel
  point_at <0, 0, 0>
} 



          
object {Object 
rotate < 0,0,0>  
translate <0,0 ,0>           
texture {
pigment { color rgb<1, 1, 1> }
finish {reflection {0.8} ambient 0 diffuse 0.01 specular 0.8 roughness 0.00085}           
} }   

object {Runway 
rotate < 0,0,0>  
translate <0,0 , 0>           
texture {
pigment { color rgb<1, 1, 1> } 
//normal { granite 0.5  scale 2} 
finish {reflection {0.5} ambient 0 diffuse 0.01 specular 0.5 roughness 0.0033}           
} }    

      
object {Grass  
rotate < 0,0,0>  
translate <0,0,0>           
texture {
pigment { color rgb<1, 1, 1> }      
//normal { granite 1  scale 5}
finish {reflection {0.5} ambient 0 diffuse 0.01 specular 0.5 roughness 0.0033}           
} }      




