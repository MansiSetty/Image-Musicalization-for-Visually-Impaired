from __future__ import print_function, division, absolute_import

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style

import numpy as np
import numpy.core.multiarray
import warnings
import tkinter as tk
from tkinter import ttk
import cv2
from skimage import io
 
import cv2
from keras.preprocessing.image import img_to_array
import pandas as pd
import os,random,time,sys,webbrowser
import pickle 
file_object = open('cnn_model.pkl', 'rb')
 
model=pickle.load(file_object)
style.use('ggplot')
warnings.simplefilter('ignore')

from tkinter import filedialog
global custom
custom=[]
global_filename = ""
# ===========================================================================================
def get_input(inp):
    print(inp)


# function to browse files
def browsefunc():
    global global_filename
    filename = filedialog.askopenfilename()
    global_filename = filename
    pathlabel.config(text=filename)


# given the path to image, returns its name
def get_img_name(path):
    path_split = path.split("/")
    return path_split[-1]


# save the genrated image
def save_file(image, img_path, scale):
    img_name = get_img_name(img_path)
    save_img_name = img_name[:-4] + "_SR_x{0}".format(scale) + img_name[-4:]

    save_folder =  filedialog.askdirectory()
    save_file = save_folder + "/" + save_img_name

    io.imsave(save_file, image)


# function to Show low resolution image on a new pop up window
def show_lr(path):
    global custom
    img = io.imread(path)
    if img is None:
        print(path)
        print(type(path))
        print("IMG IS NONE")
    plt.figure()    
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.grid("off")
    plt.axis("off")
    plt.title('Original Image')
    default_image_size = tuple((256, 256))
    image = cv2.resize(img, default_image_size)
    x=img_to_array(image)
    x = np.expand_dims(x, axis = 0)
    x /= 255
    custom_out = model.predict(x)
    custom=custom_out 
    emotions=custom[0]
    objects = ('angry', 'disgust', 'fear', 'JOY', 'sad', 'surprise')
    y_pos = np.arange(len(objects))
    plt.figure()
    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')
    plt.show()    
    #custom=[[0.14946249, 0.1587524 , 0.18512616, 0.10543171, 0.05575599, 0.34547135]]
    return custom
def show_exit():
    import sys
    sys.exit('Stopped')

# function to Show super resolved image on a new pop up window
def show_sr(custom):
    directory='C:/Users/soso/Desktop/WORK/project/Recognition/music classified/'
    
    percentage=pd.DataFrame(np.round([custom[0]*100])).T
    pos=pd.DataFrame(percentage[0].nlargest(2))
    pos[pos[0] >30]
    Categories = pd.DataFrame(['angry', 'disgust', 'fear', 'JOY', 'sad', 'surprise'])
    req_val=pos[pos[0] >30]
    if len(req_val)>1:
       combination=2
    else:
       combination=1
    while (combination==2):   
          out=pd.Series(req_val.index.astype(int))
          decision=Categories[0][out[0]]
          decision1=Categories[0][out[1]]
          print("emotion detected:"+Categories[0][out[0]])
          print("emotion detected:"+Categories[0][out[1]])
          if decision=='fear' and decision1=='angry':
             folder =directory+'fear+anger'
          elif decision=='angry' and decision1=='fear':
             folder =directory+'fear+anger'
          elif decision=='fear' and decision1=='sad':
             folder =directory+'fear+sad'
          elif decision=='sad' and decision1=='fear':
             folder =directory+'fear+sad'
          elif decision=='angry' and decision1=='sad':
             folder =directory+'anger+sad'
          elif decision=='sad' and decision1=='angry':
             folder =directory+'anger+sad'
          elif decision=='disgust' and decision1=='angry':
             folder =directory+'disgust+anger'
          elif decision=='angry' and decision1=='disgust':
             folder =directory+'disgust+anger'
          elif decision=='JOY' and decision1=='surprise':
             folder =directory+'joy+surprise'  
          elif decision=='surprise' and decision1=='JOY':
             folder =directory+'joy+surprise'
          combination=0
    while (combination==1):
         out=pd.Series(req_val.index.astype(int))
         decision=Categories[0][out[0]]
         print(Categories[0][out[0]])
         if decision=='fear':
             folder =directory+'Fear'
         elif decision=='disgust':  
              folder =directory+'Disgust'   
         elif decision=='angry':  
              folder =directory+'Angry'       
         elif decision=='JOY':  
              folder =directory+'JOY'   
         elif decision=='sad':  
              folder =directory+'sad' 
         elif decision=='surprise':  
              folder =directory+'surprise'  
         else:     
              folder =directory+'Neutral'
         combination=0    
    print(folder) 
    path = folder
    files=os. listdir(path)
    d=random.choice(files)
    print(path+'/'+d)
    from playsound import playsound
    playsound(path+'/'+d) 
       
      
     
# ============================================================================================

root = tk.Tk()
tk.Tk.wm_title(root, "IMAGE MUSICALIZATION")
label = ttk.Label(root, text="Image Musicalization", font=("Courier", 26, "bold"),background='#000000',foreground='#39FF14')
label.pack(side="top", pady=30, padx=50)
root.configure(background='#000000')
desc = '''In a land far far away, you can hear music according to the view you're looking at...\n Wait that's not a fairyland! That's exactly what this application does. \n Try uploading an image and get to hear music out of it!'''
label = ttk.Label(root, justify=tk.CENTER, text=desc, font=("Lucida handwriting", 12),background='#000000',foreground='#39FF14')
label.pack(side="top", pady=30, padx=30)

label = ttk.Label(root, justify=tk.CENTER,
                  text="Click the browse button below to select the image file", font=("Courier", 11),background='#000000',foreground='#39FF14')
label.pack(side="top", pady=5, padx=30)


button1 = ttk.Button(root, text="BROWSE", command=lambda: browsefunc())
button1.pack()

label = ttk.Label(root, justify=tk.CENTER, text="Path of the selected image file", font=("Courier", 12),background='#000000',foreground='#39FF14')
label.pack(side="top", pady=3, padx=30)

pathlabel = ttk.Label(root, font=("Courier", 12, "bold"),background='#000000',foreground='#39FF14')
pathlabel.pack(side="top", pady=3, padx=30)

label = ttk.Label(root, justify=tk.CENTER, text="",background='#000000',foreground='#39FF14')
label.pack(side="top", pady=1, padx=30)

button1 = ttk.Button(root, text="SHOW ORIGINAL IMAGE & PREDICT EMOTION", command=lambda: show_lr(global_filename))
button1.pack()
#print(custom)
label = ttk.Label(root, justify=tk.CENTER, text="",background='#000000',foreground='#39FF14')
label.pack(side="top", pady=2, padx=30)

button2 = ttk.Button(root, text="PLAY MUSIC", command=lambda: show_sr(custom))
button2.pack()

label = ttk.Label(root, justify=tk.CENTER, text="",background='#000000',foreground='#39FF14')
label.pack(side="top", pady=2, padx=30)

#button3 = ttk.Button(root, text="SUPER RESOLOVE X4", command=lambda: show_sr(global_filename, scale=4))
#button3.pack()

label = ttk.Label(root, justify=tk.CENTER, text="",background='#000000',foreground='#39FF14')
label.pack(side="top", pady=2, padx=30)


button3 = ttk.Button(root, text="QUIT", command=lambda: show_exit())
button3.pack()

label = ttk.Label(root, justify=tk.CENTER, text="",background='#000000',foreground='#39FF14')
label.pack(side="top", pady=5, padx=30)

if __name__ == "__main__":
    root.mainloop()
