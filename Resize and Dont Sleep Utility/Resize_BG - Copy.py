{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import cv2\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = 224\n",
    "Y = 224\n",
    "scaleFactor = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "new = 'BG_Images'\n",
    "new_path = os.path.join(os.getcwd(),new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.exists(new_path):\n",
    "    os.makedirs(new_path)\n",
    "    os.chdir(new_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def resize(path_to_file):\n",
    "    for file in os.listdir(path_to_file):\n",
    "        #print (file)\n",
    "        file_to_read = os.path.join(path_to_file,file)\n",
    "        img = cv2.imread(file_to_read)\n",
    "        y,x = img.shape[0],img.shape[1]\n",
    "        new_name = os.path.basename(os.path.join(path_to_file,file)).split('.')[0]\n",
    "        file_name = new_name + '.jpg'\n",
    "        print (file_name)        \n",
    "        if x < 224 and y > 224:  # Image size shouldn't go below 224x224, take larger among pixels & make it square image\n",
    "            x = y\n",
    "        elif x > 224 and y < 224:     \n",
    "            y = x\n",
    "        elif x > 224 and y > 224: # If image size greater than 224, take minimum of pixels and make it square image\n",
    "            temp = min(x,y)\n",
    "            x = temp\n",
    "            y = temp\n",
    "        elif x < 224 and y < 224: # if image size is less than 224*224 in both ht & width make it 224x224  \n",
    "            x, y = X * scaleFactor, Y * scaleFactor\n",
    "            \n",
    "        x = int(x)\n",
    "        y = int(y)\n",
    "        resized = cv2.resize(img, (x, y), interpolation=cv2.INTER_AREA)\n",
    "        cv2.imwrite(file_name, resized)         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Img1.jpg\n",
      "Img10.jpg\n",
      "Img100.jpg\n",
      "Img11.jpg\n",
      "Img12.jpg\n",
      "Img13.jpg\n",
      "Img14.jpg\n",
      "IMg15.jpg\n",
      "Img16.jpg\n",
      "Img17.jpg\n",
      "Img18.jpg\n",
      "Img19.jpg\n",
      "Img2.jpg\n",
      "Img20.jpg\n",
      "Img21.jpg\n",
      "Img22.jpg\n",
      "Img23.jpg\n",
      "Img24.jpg\n",
      "Img25.jpg\n",
      "Img26.jpg\n",
      "Img27.jpg\n",
      "Img28.jpg\n",
      "Img29.jpg\n",
      "Img3.jpg\n",
      "Img30.jpg\n",
      "Img31.jpg\n",
      "Img32.jpg\n",
      "Img33.jpg\n",
      "Img34.jpg\n",
      "Img35.jpg\n",
      "Img36.jpg\n",
      "Img37.jpg\n",
      "Img38.jpg\n",
      "Img39.jpg\n",
      "Img4.jpg\n",
      "Img40.jpg\n",
      "Img41.jpg\n",
      "Img42.jpg\n",
      "Img43.jpg\n",
      "Img44.jpg\n",
      "Img45.jpg\n",
      "Img46.jpg\n",
      "Img47.jpg\n",
      "Img48.jpg\n",
      "Img49.jpg\n",
      "Img5.jpg\n",
      "Img50.jpg\n",
      "Img51.jpg\n",
      "Img52.jpg\n",
      "Img53.jpg\n",
      "Img54.jpg\n",
      "Img55.jpg\n",
      "Img56.jpg\n",
      "Img57.jpg\n",
      "Img58.jpg\n",
      "Img59.jpg\n",
      "Img6.jpg\n",
      "Img60.jpg\n",
      "Img61.jpg\n",
      "Img62.jpg\n",
      "Img63.jpg\n",
      "Img64.jpg\n",
      "Img65.jpg\n",
      "Img66.jpg\n",
      "Img67.jpg\n",
      "Img68.jpg\n",
      "Img69.jpg\n",
      "Img7.jpg\n",
      "Img70.jpg\n",
      "Img71.jpg\n",
      "Img72.jpg\n",
      "Img73.jpg\n",
      "Img74.jpg\n",
      "Img75.jpg\n",
      "Img76.jpg\n",
      "Img77.jpg\n",
      "Img78.jpg\n",
      "Img79.jpg\n",
      "Img8.jpg\n",
      "Img80.jpg\n",
      "Img81.jpg\n",
      "Img82.jpg\n",
      "Img83.jpg\n",
      "Img84.jpg\n",
      "Img85.jpg\n",
      "Img86.jpg\n",
      "Img87.jpg\n",
      "Img88.jpg\n",
      "Img89.jpg\n",
      "Img9.jpg\n",
      "Img90.jpg\n",
      "Img91.jpg\n",
      "Img92.jpg\n",
      "Img93.jpg\n",
      "Img94.jpg\n",
      "Img95.jpg\n",
      "Img96.jpg\n",
      "Img97.jpg\n",
      "Img98.jpg\n",
      "Img99.jpg\n"
     ]
    }
   ],
   "source": [
    "path_to_file = r'C:\\Users\\annbhatt\\Desktop\\DS_AI\\S15A\\S15A_Scene Images'\n",
    "#path_to_file = r'C:\\Users\\annbhatt\\Desktop\\DS_AI\\S15A\\Test_Bg'\n",
    "resize(path_to_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
