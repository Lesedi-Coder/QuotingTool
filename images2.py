from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/LesediM/Desktop/New/LI.ico")


my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

# Creating all labels
label_type = Label(root,text = 'Type of quote: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_date = Label(root,text = 'Date of quote: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_insured = Label(root,text = 'Insured: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_pol_no = Label(root,text = 'Policy no: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_inception = Label(root,text = 'Policy inception: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_period = Label(root,text = 'Policy of insurance: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_pol_type = Label(root,text = 'Policy type: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_description = Label(root,text = 'Business description: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')
label_operation = Label(root,text = 'Key area of operation: ',font = 'times 12 bold',anchor = "w",width = 20,justify= 'left')

my_label.grid(row  = 0,column = 0)
label_type.grid(row = 1,column = 0)
label_date.grid(row = 2,column = 0)
label_insured.grid(row = 3,column = 0)
label_pol_no.grid(row = 4,column = 0)
label_inception.grid(row = 5,column = 0)
label_pol_type.grid(row = 6,column = 0)
label_description.grid(row = 7,column = 0)
label_operation.grid(row = 8,column = 0)

entry_dateofquote = Entry(root,width =20).grid(row = 2,column = 1)
entry_insured = Entry(root,width = 20).grid(row =3,column = 1)
entry_policyno = Entry(root,width = 20).grid(row =4,column = 1)
entry_policyinception = Entry(root,width = 20).grid(row =5,column = 1)
entry_description = Entry(root,width = 20).grid(row =7,column = 1)
entry_operation = Entry(root,width = 20).grid(row =8,column = 1)




clicked_insured = StringVar()
clicked_insured.set('1')
rbutton_renew = Radiobutton(root, text = 'Renewal',variable = clicked_insured,value = '1')
rbutton_newbusiness = Radiobutton(root, text = 'New Business',variable = clicked_insured,value = '2')
rbutton_renew.grid(row=1,column = 1)
rbutton_newbusiness.grid(row=1,column = 2)

clicked_ptype = StringVar()
clicked_ptype.set('1')
rbutton_annual = Radiobutton(root, text = 'Annual',variable = clicked_ptype,value = '1')
rbutton_monthly = Radiobutton(root, text = 'Monthly',variable = clicked_ptype,value = '2')
rbutton_annual.grid(row=6,column = 1)
rbutton_monthly.grid(row=6,column = 2)

button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()
