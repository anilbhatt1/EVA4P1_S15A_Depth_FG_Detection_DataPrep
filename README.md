## S15A - Data Preperation for Depth and FG Detection Network (Jointly Done by Anilkumar N Bhatt and Maruthi Srinivas)
Below are the images created as part of data preparation

###### Gdrive Location : https://drive.google.com/drive/folders/1raMnribL-gsa4FEpX8QIeyR6yP4XgmP-?usp=sharing
###### Total Size : 4.9 GB

-	100 BG and its corresponding 100 Flip Images, Shape : 192X192X3, Type : jpg, Folder Name : BG_and_Its Flip Images
- 100 FG images, Shape : 192x192x4, Type : png, transparent background, Folder Name : FG_Images
-	400K FG_BG images, Shape : 192x192x3, Type : jpg, Zip File Name : FG_BG_400K.zip

###### Mean 		: [0.56670278 0.49779153 0.43632878], Std-Dev 	: [0.38389994 0.30871084 0.25551239], Size 		:  3 GB

-	Corresponding 400K FG_BG_Masks, Shape : 192x192x1, Type : jpg, Zip File Name : FG_BG_Mask_400K.zip

###### Mean		:   [0.20249742], Std-Dev	: [0.39961225], Size		: 906 MB

-	400K Depth images of FG_BG, Shape : 200x200x1, Type : jpg, Zip File Name : FG_BG_Depth_400K.zip

###### Mean		: [0.32939295], Std-Dev		: [0.24930712], Size		: 1 GB

-	Log files corresponding to above three zip files which have file names, image size of BG, image size of FG and bounding box coordinates of overlaid FG image.
###### FG_BG_Filename_Logs.txt, FG_BG_Mask_Filename_Logs.txt, Log_FG_BG_Depth_400K.txt

Code for statistics calculation : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Statistics_FG_BG_Mask_Depth.ipynb


#### Data preperation details are as listed below

1.	This part deals with data preparation which will be later used by a network that will predict foreground from background and how far foreground is from camera w.r.to background (depth).
2.	Since data required for training this network is not publicly available & crowdsourcing is also not possible, data preparation strategy as follows was adopted.
3.	Downloaded 100 background images from web. Images of public places (mostly malls & shopping complexes) were selected for download. Resized them to 192x192.
4.	Downloaded 100 foreground images. Images of people were selected for download. Removed the background using Microsoft power point 'Remove Background' option thereby adding transparent layer. Cropped this image using 'Crop' option under 'Format' tab in PPT so that object only is retained. Then saved the image in 'png' format so that transparency (alpha channel) is retained.
5.	Flipped the 100 background images created in step 3. This makes total 200 background images (100 – Regular, 100 – Flipped) all in jpg format.

###### Sample BG images
![Sample_BG_Images](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/BG_Sample10.png)

###### Corresponding BG Flip images
![Sample_BG_Flip_Images](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/BG_Flip_Sample10.png)

###### Sample FG images
![Sample_FG_Images](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_Sample10.png)

#### FG_BG Preparation – Overlaying Foreground on Background Image. (400K images)

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DataPrep_V1.ipynb

6.	For each background image, each foreground image was overlaid in 20 random positions giving  1 BG * 100 FG * 20 Positions  = 20,000 images
7.	So each background with its flip generated 20000 + 20000 = 40000 images.
8.	In this manner, 100 background images with their corresponding flip in total generated 400K images.
9.	These 400K images were saved one-by-one with naming convention as Img_fg_bg_202217.jpg in a colab folder. 
10.	While overlaying, random positions were generated in such a way to ensure that foreground object remains within the background frame. We achieved this by calculating delta between width of BG & width of FG, delta between height of BG & height of FG and then generating random positions between lower range as 0 and higher range as delta values. This ensured FG images remain within BG canvas as shown below.

![Random_Positions](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/Random_Positions.png)

11.	Saved colab folder is zipped and copied to gdrive location.

###### Sample FG_BG

  ![Sample_FG_BG](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Sample10.png)

#### FG_BG Mask preparation – Preparing mask of FG from FG_BG images (400K images)

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DataPrep_V1.ipynb

12.	Mask of FG_BG was prepared along FG_BG but written in a separate colab folder.
13.	As followed for FG_BG, this colab folder was zipped at end and then copied to gdrive.
14.	Foreground image that we were going to overlay on top of background was converted to gray scale. FG image already has transparent background with object only retained.
15.	Hence only those pixels that represent object have pixel values greater than zero. We made these pixel values 255 so that they will be brighter compared to rest of the image pixels which were zeroes.
16.	Next we converted background image to gray scale. In this case, we made all those pixels that are > 0 as 0. Result was that entire background turned to be dark.
17.	Then we overlaid the converted foreground image from step 15 on top of converted background image from step 16. 
18.	Result was a white mask of foreground image on top of dark background image.

###### FG_BG Mask generated is as below

  ![FG_BG mask](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Mask_Sample10.png)

#### FG_BG Depth Creation

Code : https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection/blob/master/EVA4P1_S15_DepthCreation_V1.ipynb

19.	We used Dense Depth model that was pre-trained on NYU dataset. We opted for NYU dataset because this dataset is having similar background as the FG_BG images that we chosen.
20.	FG_BG images were passed on to DenseDepth model. Depth images generated were resized to Grayscale 200 x 200 and stored in colab folder.
21.	This colab folder was zipped at end and copied over to gdrive.

###### FG_BG Depth generated is as below

  ![FG_BG depth](https://github.com/anilbhatt1/EVA4P1_S15A_Depth_FG_Detection_DataPrep/blob/master/Images_For_ReadMe/FG_BG_Depth_Sample10.png)

