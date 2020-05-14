# S15A - Data Preperation for Depth and FG Detection Network
Below are the images created as part of data preparation

Gdrive Location : https://drive.google.com/drive/folders/1raMnribL-gsa4FEpX8QIeyR6yP4XgmP-?usp=sharing

A)	100 BG and its corresponding 100 Flip Images 
B)	400K FG_BG images and its corresponding 400K mask 
C)	400K Depth images of FG_BG
D)	Log files corresponding to above three zip files which have file names, image size of BG, image size of FG and bounding box coordinates of overlaid FG image.


# Details are as listed below

1.	This part deals with data preparation which will be later used by a network that will predict foreground from background and how far foreground is from camera w.r.to background (depth).
2.	Since data required for training this network is not publicly available & crowdsourcing is also not possible, data preparation strategy as follows were adopted.
3.	Downloaded 100 background images from web. Images of public places mostly malls & shopping complexes were downloaded. Resized them to 192x192
4.	Downloaded 100 foreground images. Images of people were selected. Removed the background using Microsoft power point, added transparent layer, cropped the image to select object only and saved the image.
5.	Flip the 100 background images we created in step 3 and save it. This makes total 200 background images (100 – Regular, 100 – Flipped)

# FG_BG Preparation – Overlaying Foreground on Background Image. (400K images)

6.	For each background image, each foreground image is overlaid in 20 random positions giving     1 BG * 100 FG * 20 Positions  = 20000 images
7.	So each background with its flip is generating 20000 + 20000 = 40000 images.
8.	Similarly 100 background images with their corresponding flip will generate 400K images.
9.	These 400K images are saved one-by-one with naming convention like Img_fg_bg_20217.jpg in a colab folder. 
10.	While overlaying, random positions are generated in such a way to ensure that foreground object remains within the background frame.
11.	This saved colab folder is zipped and then copied to gdrive location.

# FG_BG Mask preparation – Preparing mask of FG from FG_BG images (400K images)

12.	Mask of FG_BG is prepared along FG_BG preparation and written in a separate colab folder.
13.	As followed for FG_BG, this colab folder is zipped and copied to gdrive.
14.	Foreground image that we are going to overlay over background is converted to gray scale. FG image already have a transparent background with object in it.
15.	Hence all those pixels which represent object will have a pixel value greater than zero. We will make these pixels 255 so they will be bright and rest all as zero.
16.	Next we will convert background image to gray scale. Here we will make all those pixels that are > 0 to 0. Result will be background turning dark.
17.	Next we will overlay converted foreground on top of converted background. 
18.	Result will be a white mask of foreground on top of dark background.

# FG_BG Depth Creation

19.	We are taking Dense Depth model pre-trained on NYU dataset. This dataset is having similar background as chosen for FG_BG images.
20.	FG_BG images are passed on to DenseDepth model, resized to Grayscale 200x200 , stored in colab folder.
21.	This colab folder is zipped and copied to gdrive.

