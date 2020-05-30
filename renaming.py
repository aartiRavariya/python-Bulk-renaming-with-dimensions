from tkinter import messagebox
import cv2
import os
from tkinter import filedialog
from tkinter import *


height1 = 0
width1 = 0


def get_folder_path():
    
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


# Function to rename multiple files
def submit():
    source = src_dir.get()

    src_dir.set("")

    global width1
    global height1
    input_folder = get_folder_path()
    i = 0
    for img_file in os.listdir(input_folder):

        file_name = os.path.splitext(img_file)[0]
        extension = os.path.splitext(img_file)[1]

        if extension == '.jpg':

            src = os.path.join(input_folder,img_file)
            img = cv2.imread(src)
            h,w,c = img.shape
            dst = source + '-' + str(i) + '-' + str(w) + "x" + str(h) + ".jpg"
            dst = os.path.join(input_folder, dst)

            # rename() function will rename all the files
            os.rename(src, dst)
            i += 1
    messagebox.showinfo("Done", "All files renamed successfully!!")


# Driver Code
if __name__ == '__main__':
    top = Tk()
    top.geometry("450x300")
    top.title("Image Files Renamer")
    top.configure(background="Dark grey")

    input_path = Label(top, text="Enter Name to Rename files:", bg="Dark grey").place(x=40, y=60)

    src_dir = StringVar()
    input_path_entry_area = Entry(top, textvariable=src_dir, width=50).place(x=40, y=100)


    submit_button = Button(top, text="Submit", command=submit).place(x=200, y=150)

    top.mainloop()