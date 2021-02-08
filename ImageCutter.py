import os 

from PIL import Image
from resizeimage import resizeimage

try:
  os.mkdir("Image")
  os.mkdir("Output")

except:
  print("Image Cutter By Carlos_ V0.0.1")
  
  def imagecutter():
    
    # Image Directory
    
    _ImgDir = os.listdir("Image")
    
    # Cutter Multiple Images
    
    i = 0 
    if len(_ImgDir) == 0:
      print("\n" + "Error No Image Found")
      print("Please Try Again")
    
    if len(_ImgDir) > 0:
      Width = int(input("Width: "))
        
      Height = int(input("Height: "))
        
      while i < len(_ImgDir):
        
        # Image Name 
        
        ImageName = _ImgDir[i]
        
        i = i + 1
        
        OpenImage = Image.open("Image" + "/" + ImageName)
        
        # Image Size 
        
        _img_resize = resizeimage.resize_cover(OpenImage,[Width,Height])
        
        _img_resize.save("Output" + "/" + ImageName)
    
  imagecutter()
      
      