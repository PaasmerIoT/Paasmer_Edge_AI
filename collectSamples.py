import urllib.request
import cv2 
import numpy as  np
import os
import shutil
os.system("sudo chmod 777 install.sh")
os.system("sudo ./install.sh")
if os.path.exists('samples'):
	shutil.rmtree('samples')

def store_raw_images():
	neg_images_link = input("Enter the link to download the sample image set obtined from http://www.image-net.org/")
	neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
	
	if not os.path.exists('samples'):
		os.makedirs('samples')
	pic_num = 1

	for i in neg_image_urls.split('\n'):
		try:
			print(i)
			print("pic_num"+str(pic_num))
			urllib.request.urlretrieve(i,"samples/"+str(pic_num)+'.jpg')
			img = cv2.imread("samples/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
			resized_image = cv2.resize(img, (100,100))
			cv2.imwrite("samples/"+str(pic_num)+'.jpg', resized_image)
			pic_num = pic_num + 1
					
	
		except Exception as e:
			print(str(e))
store_raw_images()
def find_junk():
	for file_type in ['samples']:
		for img in os.listdir(file_type):
			for ugly in os.listdir('junk'):
				try:
					current_image_path = str(file_type) + '/'+str(img)
					junk = cv2.imread('junk/'+str(ugly))
					discard = cv2.imread(current_image_path)
					if junk.shape == discard.shape and not (np.bitwise_xor(junk,discard).any()):
						print( 'damyyy girl u ugly')
						print(current_image_path)
						os.remove(current_image_path)
				
				except Exception as e :
					print(str(e))
find_junk()

def create_samples():
    for file_type in ['samples']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'samples':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
					
create_samples()
