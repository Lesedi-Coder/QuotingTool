from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import fpdf
from fpdf import FPDF

HEIGHT = 1000
WIDTH = 1000


root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/LesediM/Desktop/New/LI.ico")
 
frame = Frame(root)
frame.pack(fill = BOTH,expand = 1)

my_canvas = Canvas(frame, height = HEIGHT,width = WIDTH)
my_canvas.pack(side = LEFT,fill = BOTH, expand = 1)

my_yscrollbar = ttk.Scrollbar(frame, orient = VERTICAL,command = my_canvas.yview)
my_xscrollbar = ttk.Scrollbar(frame, orient = HORIZONTAL,command = my_canvas.xview)

my_yscrollbar.pack(side = RIGHT, fill = Y)
my_xscrollbar.pack(side = BOTTOM, fill = X)


my_canvas.configure(yscrollcommand=my_yscrollbar.set)
my_canvas.configure(xscrollcommand=my_xscrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


main_frame = Frame(my_canvas)
policyinfo_frame = LabelFrame(main_frame,text = 'Policy Information')
policyinfo_frame.grid(row = 0,column = 0,sticky = W)

pol_frame = ttk.Frame(policyinfo_frame)
fleet_frame = ttk.Frame(policyinfo_frame)
cover_frame = ttk.Frame(policyinfo_frame)
specified_frame = ttk.Frame(policyinfo_frame)

pol_frame.grid(row = 0, column =0,sticky = W)
fleet_frame.grid(row = 1, column =0,sticky = W)
cover_frame.grid(row = 2, column =0,sticky = W)
specified_frame.grid(row = 3, column =0,sticky = W)



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

 


# button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()

