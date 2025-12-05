#import the required modules for image processing
import cv2
import numpy as np
#specify the image paths
PATH_IMG_1 = r"img1.jpg" 
PATH_IMG_2 = r"img2.jpg"
PATH_IMG_3 = r"img3.jpg"
PATH_IMG_4 = r"img4.jpg"

#reading the images
i1 = cv2.imread(PATH_IMG_1)
i2 = cv2.imread(PATH_IMG_2)
i3 = cv2.imread(PATH_IMG_3)
i4 = cv2.imread(PATH_IMG_4)

#checking the conditions is image os found successfully
if i1 is None or i2 is None or i3 is None or i4 is None:
    
    print("Error: Could not load one or more images. Check paths.")
    exit()
#function for 2 image collage
def two(img1,img2):
   TARGET_HEIGHT = 400 
   h1, w1 = img1.shape[:2] #geting the original heigth and width of the image
   h2, w2 = img2.shape[:2]

   new_w1 = int((TARGET_HEIGHT * (w1 / h1)))#changing the width while keeping the resolution constant
   new_w2 = int((TARGET_HEIGHT * (w2 / h2)))

   #resizing the image to new h and w
   resized_img1 = cv2.resize(img1, (new_w1, TARGET_HEIGHT), interpolation=cv2.INTER_AREA)
   resized_img2 = cv2.resize(img2, (new_w2, TARGET_HEIGHT), interpolation=cv2.INTER_AREA)

    #stacking the images
   final_collage=np.hstack([resized_img1, resized_img2])
   return final_collage

#function for 3 image collage
def three(img1,img2,img3):
  target_width = 5000 #specifying target width for verticle stack
  h1, w1 = img1.shape[:2]  #geting the original heigth and width of the image
  h2, w2 = img2.shape[:2]
  new_h1 = int(target_width * (h1 / w1))#changing the width while keeping the resolution constant
  new_h2 = int(target_width * (h2 / w2))

  #resizing the image to new h and w  
  resized_img1 =cv2.resize(img1, (target_width, new_h1), interpolation=cv2.INTER_AREA) 
  resized_img2 = cv2.resize(img2, (target_width, new_h2), interpolation=cv2.INTER_AREA) 

    #stacking the images
  coll = np.vstack([resized_img1, resized_img2]) 
  
  h_target_height = coll.shape[0]  #specifying target height for hstack

  h3, w3 = img3.shape[:2]
  new_w3 = int((h_target_height * (w3 / h3)))
#resizing the image to new h and w
  resized_img3 = cv2.resize(img3, (new_w3, h_target_height), interpolation=cv2.INTER_AREA)
  print(f"Image 3 Resized Shape: {resized_img3.shape}")
 #stacking the images
  final_collage = np.hstack([coll, resized_img3])
  return final_collage

#function for 4 image collage
def four(img1,img2,img3,img4):
     V_STACK_TARGET_WIDTH = 400 
    #setting the target width
     def new_h(img, target_w): #getting the height and width of the original image
        h, w = img.shape[:2]
        return int(target_w * (h / w))
        
    #resizing the images keeping the aspect ratio same
     resized_img1 = cv2.resize(img1, (V_STACK_TARGET_WIDTH,new_h(img1, V_STACK_TARGET_WIDTH)), interpolation=cv2.INTER_AREA) 
     resized_img2 = cv2.resize(img2, (V_STACK_TARGET_WIDTH,new_h(img2, V_STACK_TARGET_WIDTH)), interpolation=cv2.INTER_AREA) 
     resized_img3 = cv2.resize(img3, (V_STACK_TARGET_WIDTH,new_h(img3, V_STACK_TARGET_WIDTH)), interpolation=cv2.INTER_AREA) 
     resized_img4 = cv2.resize(img4, (V_STACK_TARGET_WIDTH,new_h(img4, V_STACK_TARGET_WIDTH)), interpolation=cv2.INTER_AREA) 

     #stacking the images verticle
     coll1 = np.vstack([resized_img1, resized_img2]) 
     coll2 = np.vstack([resized_img3, resized_img4]) 
    
    #stacking the images horizontally
     h_min = min(coll1.shape[0], coll2.shape[0])
     coll1 = cv2.resize(coll1, (coll1.shape[1], h_min), interpolation=cv2.INTER_AREA)
     coll2 = cv2.resize(coll2, (coll2.shape[1], h_min), interpolation=cv2.INTER_AREA)
    
   
     final_collage = np.hstack([coll1, coll2]) 
     return final_collage

#accepting input from the user
a=int(input("enter the number of images you want between 2 to 4 "))
if a == 2:
    
    final_collage = two(i1, i2) #calling the function
    WINDOW_NAME = '2-Image Horizontal Collage'
elif a == 3:
    
    final_collage = three(i1, i2, i3) #calling the function
    WINDOW_NAME = '3-Image collage'
elif a == 4:
    
    final_collage = four(i1, i2, i3, i4) #calling the function
    WINDOW_NAME = '4 image grid"'
else: 
    print("Invalid number  entered")
    exit()

WINDOW_NAME = 'collage'

collage_height, collage_width = final_collage.shape[:2]

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL) 
cv2.resizeWindow(WINDOW_NAME, collage_width, collage_height) 

#displaying the collage
cv2.imshow(WINDOW_NAME, final_collage)
#saving the image on the device
cv2.imwrite('compound_collage.jpg', final_collage)
print(f"Final Compound Collage successfully created, saved, and displayed.")

cv2.waitKey(0) 

cv2.destroyAllWindows()
