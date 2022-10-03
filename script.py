import cv2
import os
import glob

'''
img = cv2.imread("/Users/hemantb/workspace/python_projects/image_video_processing/sample_images/galaxy.jpg", 0)
print(img.shape)
'''

src_directory = r'/Users/hemantb/workspace/python_projects/image_video_processing/sample_images/'
dest_directory = r'/Users/hemantb/workspace/python_projects/image_video_processing/resized_images/'

print("Before saving image:")
print(os.listdir(dest_directory))

for img in glob.glob(src_directory+"*.jpg"):                      #glob.glob method to make list of files name
    fileName = os.path.basename(img)                              #Fetch abssolute file name form the path
    imgage = cv2.imread(img, 1)                                   #Read image with RGB

    resize_img = cv2.resize(imgage, (int(imgage.shape[1] / 2), int(imgage.shape[0] / 2)))
    cv2.imshow("Galaxy", resize_img)
    cv2.imwrite(os.path.join(dest_directory, "resized_"+ fileName), resize_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

print("After saving image:")
print(os.listdir(dest_directory))









