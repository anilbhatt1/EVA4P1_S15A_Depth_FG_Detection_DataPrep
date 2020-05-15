## S15A - Data Preperation for Depth and FG Detection Network (Jointly Done by Anilkumar N Bhatt and Maruthi Srinivas)
Below are the images created as part of data preparation

###### Gdrive Location : https://drive.google.com/drive/folders/1raMnribL-gsa4FEpX8QIeyR6yP4XgmP-?usp=sharing

-	100 BG and its corresponding 100 Flip Images, 192X192X3, jpg 
- 100 FG images, 192x192x4, png, transparent background 
-	400K FG_BG images, 192x192x3, jpg 

###### Mean 		: [0.56670278 0.49779153 0.43632878], Std-Dev 	: [0.38389994 0.30871084 0.25551239], Size 		:  3 GB

-	Corresponding 400K FG_BG_Masks, 192x192x1, jpg

###### Mean		:   [0.20249742], Std-Dev	: [0.39961225], Size		: 906 MB

-	400K Depth images of FG_BG, 200x200x1, jpg

###### Mean		: [0.32939295], Std-Dev		: [0.24930712], Size		: 1 GB

-	Log files corresponding to above three zip files which have file names, image size of BG, image size of FG and bounding box coordinates of overlaid FG image.

Code for statistics calculation : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Statistics_FG_BG_Mask_Depth.ipynb


#### Data preperation details are as listed below

1.	This part deals with data preparation which will be later used by a network that will predict foreground from background and how far foreground is from camera w.r.to background (depth).
2.	Since data required for training this network is not publicly available & crowdsourcing is also not possible, data preparation strategy as follows were adopted.
3.	Downloaded 100 background images from web. Images of public places mostly malls & shopping complexes were downloaded. Resized them to 192x192
4.	Downloaded 100 foreground images. Images of people were selected. Removed the background using Microsoft power point using 'Remove Background' option thereby adding transparent layer. After that cropped this image using 'Crop' option under 'Format' tab in PPT to select object only. Then saved this image in 'png' format so that transparency (alpha channel) is retained.
5.	Flipped the 100 background images we created in step 3 and saved it. This makes total 200 background images (100 – Regular, 100 – Flipped) all in jpg format

###### Sample BG images
![Sample_BG_Images](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/BG_Sample10.png)

###### Corresponding BG Flip images
![Sample_BG_Flip_Images](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/BG_Flip_Sample10.png)

#### FG_BG Preparation – Overlaying Foreground on Background Image. (400K images)

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DataPrep_V1.ipynb

6.	For each background image, each foreground image is overlaid in 20 random positions giving  1 BG * 100 FG * 20 Positions  = 20000 images
7.	So each background with its flip is generating 20000 + 20000 = 40000 images.
8.	Similarly 100 background images with their corresponding flip will generate 400K images.
9.	These 400K images are saved one-by-one with naming convention like Img_fg_bg_20217.jpg in a colab folder. 
10.	While overlaying, random positions are generated in such a way to ensure that foreground object remains within the background frame. We achieved this by calculating delta between width of BG & width of FG, delta between height of BG & height of FG and generated random positions between low as 0 and high as delta values. This ensured FG images remain within BG canvas like below.

![Random_Positions](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/Random_Positions.png)

11.	Saved colab folder is zipped and then copied to gdrive location.

###### Sample FG_BG

  ![Sample_FG_BG](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Sample10.png)

#### FG_BG Mask preparation – Preparing mask of FG from FG_BG images (400K images)

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DataPrep_V1.ipynb

12.	Mask of FG_BG is prepared along FG_BG preparation and written in a separate colab folder.
13.	As followed for FG_BG, this colab folder is zipped and copied to gdrive.
14.	Foreground image that we are going to overlay over background is converted to gray scale. FG image already have a transparent background with object in it.
15.	Hence all those pixels which represent object will have a pixel value greater than zero. We will make these pixels 255 so they will be bright and rest all as zero.
16.	Next we will convert background image to gray scale. Here we will make all those pixels that are > 0 to 0. Result will be background turning dark.
17.	Next we will overlay converted foreground on top of converted background. 
18.	Result will be a white mask of foreground on top of dark background.

###### FG_BG Mask generated is as below

  ![FG_BG mask](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Mask_Sample10.png)

#### FG_BG Depth Creation

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DepthCreation_V1.ipynb

19.	We are taking Dense Depth model pre-trained on NYU dataset. This dataset is having similar background as chosen for FG_BG images.
20.	FG_BG images are passed on to DenseDepth model, resized to Grayscale 200x200 , stored in colab folder.
21.	This colab folder is zipped and copied to gdrive.

###### FG_BG Depth generated is as below

  ![FG_BG depth](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Depth_Sample10.png)

