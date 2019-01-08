## Paasmer Artificial Intelligence
Paasmer has built the capability to build AI applications at Edge, the AI feature released with the Paasmer version 3.0 demonstrates the same by offering a use case to identify a pre-selected object on the input live image from a camera.

## Instructions on how to use the Paasmer AI to identify an object on a live image

## Pre-requisites
### Software 
* Python3
* python-pip3 
* OpenCV
* Numpy

**AI installation script comes along with the Paasmer  AI module takes care of installing the dependencies.**

### Hardware
* Camera compatible with the device  
* Minimum 2gb RAM on the device 

* The module already has the capability to identify the human faces on the live image. The user can add any object of their choice by training the module with sample images of the desired object for identification.

### Train, Test and Deploy
* Once the user has decided on the object to run training, the sample files of that image need to be provided for training. This version of Paasmer AI module supports the sample images from the website  http://www.image-net.org/ and it can download the images automatically once the URL for the master file is provided as an input to a script.

Here is the step by step instructions on the same.

* Get a sample image of the object with a resolution of 50x50 pixels. 
* Open the [website](http://www.image-net.org/) and type the name of the similar desired object and enter.
* It will display the links of the image collections. Click the link, once open, click on Download tab and Click URL’s option, that will open a page with a list of URLs for the desired object. 
* Copy the link of this page, and give as an input to the script  `python3 collectSamples.py` 
* This script will download all the images to the local folder and run the training using `python3 train.py sampleimage.jpeg` command. The sample image here is the first ever collected image having 50x50 pixels. 
* This process will talk a long time to complete the download and training, 2-4 hrs depending on your RAM speed. 
* Once the training is completed, `test.py` file should be edited to enter the trained input file name

### Editing instructions on test.py
* The output file of the training is created as `cascade.xml`.
* Locate the `cascade.xml` file on the current folder, rename it to the object name as this will be overwritten when training is done again for the same or different object
* On `test.py`,  replace the `cascade.xml` name with the name it was renamed when calling the `cv2.CascadeClassifier()` function.
* On the `cv2.VideoCapture(0)`  function call, replace the number with the port number on the device where the camera is connected
* Edit the detection representation methods rectangle frame/ Text. or both can be used.
* For text : 
```
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Watch',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA). 
```
* For rectangle: 
```
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
```
* Save the changes and run the `test.py` using `python3 test.py`. 
* AI application is running on the edge now and it can detect the human face and the object user has trained on the live image  

## Support

The support forum is hosted on the GitHub, issues can be identified by users and the Team from Paasmer would be taking up requests and resolving them. You could also send a mail to support@paasmer.co with the issue details for a quick resolution.

## Note

* The Paasmer AI utilizes the features and libaries from Python.org
