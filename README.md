This is our Final Year Project called IMAGE MUSICALIZATION- USING IMAGE EMOTION ANALYSIS.
The project achieves two goals-
- Finding the emotion label of an input image.
- Mapping the input image to an appropriate music based on the emotions.

The project files hierarchy is as follows:

Project:
1. Python Code-
-cnn.py( This is the training code)
-gui.py( This is the testing code with GUI)
-cnn_model.pkl
-label_transform.pkl
2. DATABASE-
This is the image dataset with 6 folders(angry, disgust, fear, joy, surprise, sadness). Each of the folders contain 400 images. Unzip the 'database.zip' file and extract the folder here.
3. Music clasified-
This is the music dataset with 6 emotions folders + 1 neutral folder + 5 combination folders. Each folder contains MP3 music files.

=================================================================================================

System and software Pre-requisites to run the project:

- Any desktop/laptop with the following software packages installed-

1. Anaconda Navigator( latest version)
2. Spyder IDE ( normally installed with anaconda) 
3. Tensorflow
4. Keras
5. OpenCV

====================================================================================================

Since the databases are stored locally in directories, the file path needs to be changed :

in the file 'cnn.py' at the following line of code:

	at line 28: 	directory_root = 'C:/Users/soso/Desktop/WORK/project/Recognition/DATABASE'

in the file 'gui.py' at the following line of code:

	at line 100 :   directory='C:/Users/soso/Desktop/WORK/project/Recognition/music classified/'

================================================================================================

-The file cnn.py was used to train the CNN model.

- The file gui.py gives the actual output on a python gui rendered by tkinter.

With the above packages installed and modifications done, run the gui.py file in Spyder IDE. Upload a photo and experience Image Musicalization.

If you wish to retrain the Network with a different dataset, run the cnn.py file.
