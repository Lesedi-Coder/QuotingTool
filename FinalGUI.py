from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import fpdf
from fpdf import FPDF
from tkinter import ttk
import numpy as np


root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/LesediM/Desktop/New/LI.ico")
 
frame = Frame(root)
frame.pack(fill = BOTH,expand = 1)

my_canvas = Canvas(frame)
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

pol_frame.grid(sticky = 'W')
fleet_frame.grid(sticky = 'W')
cover_frame.grid(sticky = 'W')
specified_frame.grid(sticky = 'W')



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')
user_inputinsured = StringVar(pol_frame)
user_inputpolno = StringVar(pol_frame)
user_inputdesc = StringVar(pol_frame)
user_inputoper = StringVar(pol_frame)
user_units = IntVar(pol_frame)
user_value = DoubleVar(pol_frame)

user_f11 = IntVar(pol_frame)
user_f21 = IntVar(pol_frame)
user_f31 = IntVar(pol_frame)
user_f41 = IntVar(pol_frame)
user_f51 = IntVar(pol_frame)
user_f61 = IntVar(pol_frame)
user_f71 = IntVar(pol_frame)
user_f81 = IntVar(pol_frame)

user_f12 = DoubleVar(pol_frame)
user_f22 = DoubleVar(pol_frame)
user_f32 = DoubleVar(pol_frame)
user_f42 = DoubleVar(pol_frame)
user_f52 = DoubleVar(pol_frame)
user_f62 = DoubleVar(pol_frame)
user_f72 = DoubleVar(pol_frame)
user_f82 = DoubleVar(pol_frame)

user_f13 = DoubleVar(pol_frame)
user_f23 = DoubleVar(pol_frame)
user_f33 = DoubleVar(pol_frame)
user_f43 = DoubleVar(pol_frame)
user_f53 = DoubleVar(pol_frame)
user_f63 = DoubleVar(pol_frame)
user_f73 = DoubleVar(pol_frame)
user_f83 = DoubleVar(pol_frame)

user_f15 = DoubleVar(pol_frame)
user_f25 = DoubleVar(pol_frame)
user_f35 = DoubleVar(pol_frame)
user_f45 = DoubleVar(pol_frame)
user_f55 = DoubleVar(pol_frame)
user_f65 = DoubleVar(pol_frame)
user_f75 = DoubleVar(pol_frame)
user_f85 = DoubleVar(pol_frame)

# ------------------Specified Entries-------------------
user_s13 = DoubleVar(specified_frame)
user_s23 = DoubleVar(specified_frame)
user_s33 = DoubleVar(specified_frame)
user_s43 = DoubleVar(specified_frame)
user_s53 = DoubleVar(specified_frame)

user_s14 = DoubleVar(specified_frame)
user_s24 = DoubleVar(specified_frame)
user_s34 = DoubleVar(specified_frame)
user_s44 = DoubleVar(specified_frame)
user_s54 = DoubleVar(specified_frame)

user_s15 = DoubleVar(specified_frame)
user_s25 = DoubleVar(specified_frame)
user_s35 = DoubleVar(specified_frame)
user_s45 = DoubleVar(specified_frame)
user_s55 = DoubleVar(specified_frame)
user_s65 = DoubleVar(specified_frame)

user_s16 = DoubleVar(specified_frame)
user_s26 = DoubleVar(specified_frame)
user_s36 = DoubleVar(specified_frame)
user_s46 = DoubleVar(specified_frame)
user_s56 = DoubleVar(specified_frame)
user_s66 = DoubleVar(specified_frame)
def add_spec():

	annprem_s15 = ((user_s13.get()
		           *user_s14.get())/100)
	annprem_s25 = ((user_s23.get()
		           *user_s24.get())/100)
	annprem_s35 = ((user_s33.get()
		           *user_s34.get())/100)
	annprem_s45 = ((user_s43.get()
		           *user_s44.get())/100)
	annprem_s55 = ((user_s53.get()
		           *user_s54.get())/100)		           	
	total_annprem = (annprem_s15 +
		             annprem_s25 +
		             annprem_s35 + 
	                 annprem_s45 +
	                 annprem_s55)
	total_sasprem = (user_s16.get()+
	                 user_s26.get()+
	                 user_s36.get()+
	                 user_s46.get()+
	                 user_s56.get())
	user_s15.set(annprem_s15)
	user_s25.set(annprem_s25)
	user_s35.set(annprem_s35)
	user_s45.set(annprem_s45)
	user_s55.set(annprem_s55)
	user_s65.set(total_annprem)
	user_s66.set(total_sasprem)              

def add_fleet():
	total_units = (user_f11.get()+
	              user_f21.get()+
	              user_f31.get()+
	              user_f41.get()+
	              user_f51.get()+
	              user_f61.get()+
	              user_f71.get()+
	              user_f81.get())

	total_values = (user_f12.get()+
	                user_f22.get()+
	                user_f32.get()+
	                user_f42.get()+
	                user_f52.get()+
	                user_f62.get()+
	                user_f72.get()+
	                user_f82.get())	
	txt_fleet91.configure(state = NORMAL)
	txt_fleet91.delete(1.0,END)
	txt_fleet91.insert(END,f"{total_units}")
	txt_fleet91.configure(state = DISABLED)

	txt_fleet92.configure(state = NORMAL)
	txt_fleet92.delete(1.0,END)
	txt_fleet92.insert(END,f"R{np.round(total_values,2)}")
	txt_fleet92.configure(state = DISABLED)

	M1 = 0.0
	M2 = 0.0
	M3 = 0.0
	M4 = 0.0
	M5 = 0.0
	M6 = 0.0
	M7 = 0.0
	M8 = 0.0



	if(clicked_poltype.get()=="Annual"):
		M1  = 20.18
		M2 = 45.39
		M3 = 45.39
		if(user_f41.get()!=0 and user_f42.get() !=0):
			if (M4 < 100 and M4 >0):
				M4 = 100
			else:
				M4 = (total_values*0.00868)/100
		if(user_f51.get()!=0 and user_f52.get() !=0):
			if(M5 < 2000 and M5 > 0):
				M5 = 2000
			else:
				M5 = (total_values*0.504)/100
		if(user_f61.get()!=0 and user_f62.get() !=0):
			if(M6 < 200 and M5 > 0):
				M6 = 200 
			else:
				M6 = (total_values*0.0363)/100 
		if(user_f81.get()!=0 and user_f82 !=0):
			if(M8 < 54.47 and M4 > 0):
				M8 = 54.47 
			else:
				M8 = (total_values*0.01879)/100

	if (clicked_poltype.get() =="Monthly"):
		M1  = 2.02
		M2 = 4.54
		M3 = 4.54

		if (M4 < 10 and M4 >0):
			M4 = 10

		if(M5 < 200 and M5 > 0):
			M5 = 200

		if(M6 < 200 and M6 > 0):
			M6 = 200 

		if(M8 < 5.45 and M8 >0):
			M8 = 5.45 
	R1 = M1 *user_f11.get()
	R2 = M2 * user_f21.get()
	R3 = M3 *user_f31.get()
	R4 = M4
	R5 = M5
	R6 = M6
	R7 = M7
	R8 = M8		
			
	txt_fleet15.configure(state = NORMAL)
	txt_fleet15.delete(1.0,END)
	txt_fleet15.insert(END,f"R{np.round(R1,2)}")
	txt_fleet15.configure(state = DISABLED)

	txt_fleet25.configure(state = NORMAL)
	txt_fleet25.delete(1.0,END)
	txt_fleet25.insert(END,f"R{np.round(R2,2)}")
	txt_fleet25.configure(state = DISABLED)

	txt_fleet35.configure(state = NORMAL)
	txt_fleet35.delete(1.0,END)
	txt_fleet35.insert(END,f"R{np.round(R3,2)}")
	txt_fleet35.configure(state = DISABLED)

	if (total_values == "R0.0"):
		if(user_f41.get() == 0 and user_f42.get() ==0):
			R4 = 0
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R4,2)}")
			txt_fleet45.configure(state = DISABLED)
		else:
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R4,2)}")
			txt_fleet45.configure(state = DISABLED)

		if (user_f51.get() == 0 and user_f52.get() ==0):
			R5 = 0
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R5,2)}")
			txt_fleet45.configure(state = DISABLED)
		else:
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R5,2)}")
			txt_fleet45.configure(state = DISABLED)	

		if (user_f61.get() == 0 and user_f62.get() ==0):
			R6 = 0
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R6,2)}")
			txt_fleet45.configure(state = DISABLED)
		else:
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R6,2)}")
			txt_fleet45.configure(state = DISABLED)

		if (user_f81.get() == 0 and user_f82.get() ==0):
			R8 = 0
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R8,2)}")
			txt_fleet45.configure(state = DISABLED)
		else:
			txt_fleet45.configure(state = NORMAL)
			txt_fleet45.delete(1.0,END)
			txt_fleet45.insert(END,f"R{np.round(R8,2)}")
			txt_fleet45.configure(state = DISABLED)		

	else:
		txt_fleet45.configure(state = NORMAL)
		txt_fleet45.delete(1.0,END)
		txt_fleet45.insert(END,f"R{np.round(R4,2)}")
		txt_fleet45.configure(state = DISABLED)

		txt_fleet55.configure(state = NORMAL)
		txt_fleet55.delete(1.0,END)
		txt_fleet55.insert(END,f"R{np.round(R5,2)}")
		txt_fleet55.configure(state = DISABLED)

		txt_fleet65.configure(state = NORMAL)
		txt_fleet65.delete(1.0,END)
		txt_fleet65.insert(END,f"R{np.round(R6,2)}")
		txt_fleet65.configure(state = DISABLED)

		txt_fleet75.configure(state = NORMAL)
		txt_fleet75.delete(1.0,END)
		txt_fleet75.insert(END,f"R{np.round(R7,2)}")
		txt_fleet75.configure(state = DISABLED)

		txt_fleet85.configure(state = NORMAL)
		txt_fleet85.delete(1.0,END)
		txt_fleet85.insert(END,f"R{np.round(R8,2)}")
		txt_fleet85.configure(state = DISABLED)	


def validation():
	dictionary = []

	if (user_inputinsured.get() == "" or
	    user_inputpolno.get()==""):
		messagebox.showwarning('Missng Entries','Please enter missing entries')
	elif(clicked_type.get() == 'Select Option'):
			messagebox.showwarning('Date correlation','Please select the type of quote')

	elif(clicked_poltype.get() == 'Select Option'):
		messagebox.showwarning('Date correlation','Please select the type of policy')			

	elif(e_policyinception.get_date() > e_periodfrom.get_date()):
		messagebox.showwarning('Date correlation',
			                   'Policy inception date cannot be after starting period date. Please correct it')
	elif(e_periodfrom.get_date() > e_periodto.get_date()):
		messagebox.showwarning('Date correlation',
			                   'Starting period date cannot be after the ending period date. Please correct it')

	elif (user_inputpolno.get().isdigit()):
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font('Arial','B',11)
		# pdf.cell(20,20,my_img,0,1,'C')
		pdf.cell(10,
			     10,
			     f"Type of quote:\t           {clicked_type.get()}",0,1,'L')
		pdf.cell(10,
			     10,
			     f"Date of quote:\t            {e_dateofquote.get_date()}",0,1,'L')
		pdf.cell(10,
			     10,
			     f"Insured:\t                      {user_inputinsured.get()}",0,1,'L')
		pdf.cell(10,
			     10,
			     f"Policy No:\t                   {user_inputpolno.get()}",0,1,'L')
		pdf.cell(10,
			     10,
			     f"Policy Inception:\t        {e_policyinception.get_date()}",
			     0,1,'L')
		pdf.cell(10,
			     10,
			     f"Period Of Insurance:\t  {e_periodfrom.get_date()}\
				 to {e_periodto.get_date()}",
			     0,1,'L')
		pdf.cell(10,
			     10,
			     f"Policy Type:\t               {clicked_poltype.get()}",0,1,'L')
		if(user_inputdesc.get()!=""):
			pdf.cell(10,10,f"Business Description:\t            \
				    {user_inputdesc.get()}",0,1,'L')	
		if( user_inputoper.get()!=""):
			pdf.cell(10,
				     10,
				     f"Key Area Of Operation:\t            \
				     {user_inputoper.get()}",0,1,'L')			

		pdf.output('Quote.pdf','F')


	else:	
	    messagebox.showwarning('Non Numeric Values',
		    	              ' "Policy no" accepts numeric values only')

	


#------------------Policy Holder Infromation-------------------------------------------

label_pholder = Label(pol_frame,text = 'Policy Holder Information' , font = 'times 20 bold underline')
label_date = Label(pol_frame,text = 'Date of quote: ' ,font = 'times 12 bold')
label_type = Label(pol_frame,text = 'Type of quote: ' ,font = 'times 12 bold')
label_insured = Label(pol_frame,text = 'Insured: ',font = 'times 12 bold')
label_pol_no = Label(pol_frame,text = 'Policy no: ' ,font = 'times 12 bold')
label_inception = Label(pol_frame,text = 'Policy inception: ',font = 'times 12 bold')
label_period = Label(pol_frame,text = 'Period of insurance(From--To): ',font = 'times 12 bold')
label_to = Label(pol_frame,text = 'to ',font = 'times 12  bold')
label_pol_type = Label(pol_frame,text = 'Policy type: ',font = 'times 12 bold')
label_description = Label(pol_frame,text = 'Business description: ' ,font = 'times 12 bold')
label_operation = Label(pol_frame,text = 'Key area of operation: ' ,font = 'times 12 bold')

#Placing labels on grib for policy holder
label_pholder.grid(row  = 0,column = 0,sticky = E)
label_type.grid(row = 2,column = 0,sticky = W)
label_date.grid(row = 3,column = 0,sticky = W)
label_insured.grid(row = 4,column = 0,sticky = W)
label_pol_no.grid(row = 5,column = 0,sticky = W)
label_inception.grid(row = 6,column = 0,sticky = W)
label_period.grid(row = 7,column = 0,sticky = W)
label_to.grid(row = 7, column = 2,sticky = W)
label_pol_type.grid(row = 8,column = 0,sticky = W)
label_description.grid(row = 9,column = 0,sticky = W)
label_operation.grid(row = 10,column = 0,sticky = W)

#Text boxes for policyholder information
e_dateofquote = DateEntry(pol_frame)
e_dateofquote.grid(row = 3,column = 1) 

e_insured = Entry(pol_frame,textvariable = user_inputinsured,bg = 'light blue')
e_insured.grid(row =4,column = 1)

e_policyno = Entry(pol_frame,
	               textvariable = user_inputpolno,
	               bg = 'light blue')
e_policyno.grid(row =5,column = 1)

e_policyinception = DateEntry(pol_frame)
e_policyinception.grid(row =6,column = 1)


e_periodfrom = DateEntry(pol_frame)
e_periodfrom.grid(row = 7,column =1)

e_periodto = DateEntry(pol_frame)
e_periodto.grid(row = 7,column = 3)

e_description = Entry(pol_frame,
	                  textvariable = user_inputdesc,
	                  bg = 'light blue')
e_description.grid(row = 9,column = 1)

e_operation = Entry(pol_frame,
	                textvariable = user_inputoper,
	                bg = 'light blue')
e_operation.grid(row =10,column = 1)

#Dropdown menus for policy information
clicked_type = StringVar(pol_frame)
clicked_type.set('Select Option')
menu_type = OptionMenu(pol_frame, clicked_type,'Renewal','New Business')
menu_type.grid(row=2,column = 1)

clicked_poltype = StringVar(pol_frame)
clicked_poltype.set('Select Option')
menu_poltype = OptionMenu(pol_frame, clicked_poltype,'Annual','Monthly')
menu_poltype.grid(row=8,column = 1)

button_save = Button(pol_frame, text="Save", command=validation)
button_save.grid(row = 11,column =0)


#--------------------Fleet Information---------------------------------------------------

label_fleet = Label(fleet_frame,text = 'Fleet Information',
	                font = 'times 20 bold underline',
	                anchor = 'w')
label_fleet.grid(row = 0,column = 0,sticky = W)

#Labels for fleet information
label_vcategory = Label(fleet_frame,text ='Vehicle Category',
	                    font = 'times 12 bold underline')
label_cars = Label(fleet_frame,text ='Cars- Single Vehicles',
	               font = 'times 12')
label_motorcycles = Label(fleet_frame,text ='Motorcycles',
	                      font = 'times 12')
label_ldvs = Label(fleet_frame,text ='LDVs',font = 'times 12')
label_commercial = Label(fleet_frame,
	                     text ='Commercial Vehicles(Mass ≥ 3500kg)',
	                     font = 'times 12')
label_busses = Label(fleet_frame,text ='Busses',
	                 font = 'times 12')
label_mobile = Label(fleet_frame,text ='Mobile Plants ',font = 'times 12')
label_specialless = Label(fleet_frame,
	                      text ='Special Types < 3500kg(incl Trailers and Forklifts)',
	                      font = 'times 12')
label_specialmore = Label(fleet_frame,
	                      text ='Special Types > 3500kg(incl Trailers and Forklifts)',
	                      font = 'times 12')
label_total = Label(fleet_frame,text ='Total',
	                font = 'times 12 bold underline')


#Place labels on grid for fleet information
label_vcategory.grid(row = 1,column = 0,sticky = W)
label_cars.grid(row = 2,column = 0,sticky = W)
label_motorcycles.grid(row = 3,column = 0,sticky = W)
label_ldvs.grid(row = 4,column = 0,sticky = W)
label_commercial.grid(row = 5,column = 0,sticky = W)
label_busses.grid(row = 6,column = 0,sticky = W)
label_mobile.grid(row = 7,column = 0,sticky = W)
label_specialless.grid(row = 8,column = 0,sticky = W)
label_specialmore.grid(row = 9,column = 0,sticky = W)
label_total.grid(row = 10,column = 0,sticky = W)

label_units = Label(fleet_frame,text = 'No. of units',font = 'times 12 bold ')
label_value = Label(fleet_frame,text = 'Value',font = 'times 12 bold ')
label_damage = Label(fleet_frame,text = 'Own Damage Limit',font = 'times 12 bold ')
label_sasria_des = Label(fleet_frame,text = 'SASRIA Description',font = 'times 12 bold ')
label_sasria_prem = Label(fleet_frame,text = 'SASRIA Premium',font = 'times 12 bold ')

label_units.grid(row = 1,column = 1)
label_value.grid(row = 1,column = 2)
label_damage.grid(row = 1,column = 3)
label_sasria_des.grid(row = 1,column = 4)
label_sasria_prem.grid(row = 1,column = 5)


txt_fleet11 = Entry(fleet_frame,
	                  textvariable = user_f11,
	                  width = 10,
	                  bg = 'light blue').grid(row = 2,column=1)
txt_fleet12 = Entry(fleet_frame,
	                  textvariable = user_f12,
	                  bg = 'light blue').grid(row = 2,column=2)
txt_fleet13 = Entry(fleet_frame,
	              textvariable = user_f13,
	              bg = 'light blue').grid(row = 2,column=3)
txt_fleet14 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet14.insert(INSERT,"Cars(Primary use: Domestic/ private)")
txt_fleet14.configure(state = 'disabled')
txt_fleet14.grid(row = 2,column=4)

txt_fleet15 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet15.grid(row = 2,column=5)

txt_fleet21 = Entry(fleet_frame,
	              textvariable = user_f21,
	              width = 10,
	              bg = 'light blue').grid(row = 3,column=1)
txt_fleet22 = Entry(fleet_frame,
	              textvariable = user_f22,
	              bg = 'light blue').grid(row = 3,column=2)
txt_fleet23 = Entry(fleet_frame,
	              textvariable = user_f23,
	              bg = 'light blue').grid(row = 3,column=3)
txt_fleet24 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet24.insert(INSERT,"LDV(Commercial use")
txt_fleet24.configure(state = 'disabled')
txt_fleet24.grid(row = 3,column=4)

txt_fleet25 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet25.grid(row = 3,column=5)

txt_fleet31 = Entry(fleet_frame,
	              textvariable = user_f31,
	              width = 10,
	              bg = 'light blue').grid(row = 4,column=1)
txt_fleet32 = Entry(fleet_frame,
	              textvariable = user_f32,
	              bg = 'light blue').grid(row = 4,column=2)
txt_fleet33 = Entry(fleet_frame,
	              textvariable = user_f33,
	              bg = 'light blue').grid(row = 4,column=3)
txt_fleet34 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet34.insert(END,"LDV(Commercial use)")
txt_fleet34.configure(state = 'disabled')
txt_fleet34.grid(row = 4,column=4)

txt_fleet35 =Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet35.grid(row = 4,column=5)

txt_fleet41 = Entry(fleet_frame,
	              textvariable = user_f41,
	              width = 10,
	              bg = 'light blue').grid(row = 5,column=1)
txt_fleet42 = Entry(fleet_frame,
	               textvariable = user_f42,
	               bg = 'light blue').grid(row = 5,column=2)
txt_fleet43 = Entry(fleet_frame,
	              textvariable = user_f43,
	              bg = 'light blue').grid(row = 5,column=3)
txt_fleet44 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet44.insert(INSERT,"Heavy Commercial Vehicles (>3,500kg)")
txt_fleet44.configure(state = 'disabled')
txt_fleet44.grid(row = 5,column=4)

txt_fleet45 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet45.grid(row = 5,column=5)

txt_fleet51 = Entry(fleet_frame,
	               textvariable = user_f51,
	               	bg = 'light blue',width = 10).grid(row = 6,column=1)
txt_fleet52 = Entry(fleet_frame,
	              textvariable = user_f52,
	              bg = 'light blue').grid(row = 6,column=2)
txt_fleet53 = Entry(fleet_frame,
	              textvariable = user_f53,
	              bg = 'light blue').grid(row = 6,column=3)
txt_fleet54 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet54.insert(INSERT,"Buses")
txt_fleet54.configure(state = 'disabled')
txt_fleet54.grid(row = 6,column=4)
txt_fleet55 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet55.grid(row = 6,column=5)

txt_fleet61 = Entry(fleet_frame,
	              textvariable = user_f61,
	              width = 10,
	              bg = 'light blue').grid(row = 7,column=1)
txt_fleet62 = Entry(fleet_frame,
	              textvariable = user_f62,
	              bg = 'light blue').grid(row = 7,column=2)
txt_fleet63 = Entry(fleet_frame,
	              textvariable = user_f63,
	              bg = 'light blue').grid(row = 7,column=3)
txt_fleet64 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet64.insert(INSERT,"Mobile Plant")
txt_fleet64.configure(state = 'disabled')
txt_fleet64.grid(row = 7,column=4)
txt_fleet65 =Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet65.grid(row = 7,column=5)

txt_fleet71 = Entry(fleet_frame,
	              textvariable = user_f71,
	              bg = 'light blue',width = 10).grid(row = 8,column=1)
txt_fleet72 = Entry(fleet_frame,
	              textvariable = user_f72,
	              bg = 'light blue').grid(row = 8,column=2)
txt_fleet73 = Entry(fleet_frame,
	              textvariable = user_f73,
	              bg = 'light blue').grid(row = 8,column=3)
txt_fleet74 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet74.insert(INSERT,"LDV(Commercial use)")
txt_fleet74.configure(state = 'disabled')
txt_fleet74.grid(row = 8,column=4)
txt_fleet75 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet75.grid(row = 8,column=5)

txt_fleet81 = Entry(fleet_frame,
	              textvariable = user_f81,
	              width = 10,
	              bg = 'light blue').grid(row = 9,column=1)
txt_fleet82 = Entry(fleet_frame,
	              textvariable = user_f82,
	              bg = 'light blue').grid(row = 9,column=2)
txt_fleet83 = Entry(fleet_frame,
	              textvariable = user_f83,
	              bg = 'light blue').grid(row = 9,column=3)
txt_fleet84 = Text(fleet_frame,
	               height = 0.1,
	               width = 36)
txt_fleet84.insert(INSERT,"Heavy Commercial(>3,500kg)")
txt_fleet84.configure(state = 'disabled')
txt_fleet84.grid(row = 9,column=4)
txt_fleet85 = Text(fleet_frame,
	              width = 18,
	              height = 0.1)
txt_fleet85
txt_fleet85.grid(row = 9,column=5)

txt_fleet91 = Text(fleet_frame,
	              width = 8,
	              height = 0.1)
txt_fleet91.grid(row = 10,column=1)
txt_fleet92 = Text(fleet_frame,
	               width =15,
	               height = 0.1)
txt_fleet92.grid(row = 10,column=2)

button_totfleet = Button(fleet_frame, text="Total", command=add_fleet)
button_totfleet.grid(row = 10, column = 3)


#----------------Cover Information----------------------------

label_coverinfo = Label(cover_frame, text ='Cover Information',font = 'times 20 bold underline',anchor = 'w')
label_coverinfo.grid(row = 0, column = 0,sticky = W)

label_covertype = Label(cover_frame,anchor = "w",text = 'Cover Type: ',font = 'times 12 bold')
label_liability = Label(cover_frame,anchor = 'w',text = 'Third Party Liability: ',font ='times 12 bold')

label_covertype.grid(row = 1, column = 0,sticky = W)
label_liability.grid(row = 2,column = 0,sticky = W)

clicked_covertype = StringVar(cover_frame)
clicked_covertype.set('Comprehensive')
menu_cover = OptionMenu(cover_frame,clicked_covertype,'Comprehensive'
											  ,'Third Party, Fire and Theft'
											  ,'Third Party Only'
											  ,'Own Damage Only')
menu_cover.grid(row = 1,column = 1,sticky = W)
entry_liabilty = Entry(cover_frame,
	                   bg = 'light blue').grid(row=2,column = 1,sticky = W)

label_excess = Label(cover_frame,text = 'Excess',font = 'times 12 bold',anchor = "w")
label_excess.grid(row = 3,column = 0,sticky = W)

label_basicexcess = Label(cover_frame, text = '-Basic Excess',font = 'times 11',justify = 'left',anchor = 'w')
label_theft = Label(cover_frame, text = '-Theft/Hijack',font = 'times 11',justify = 'left',anchor = 'w')
label_windscreen = Label(cover_frame, text = '-Windscreen',font = 'times 11',justify = 'left',anchor = 'w')
label_thirdparty = Label(cover_frame, text = '-Third Party Liability',font = 'times 11',justify = 'left',anchor = 'w')
label_section2 = Label(cover_frame, text = '-Section 2 only Excess',font = 'times 11',justify = 'left',anchor = 'w')
label_lossofkeys = Label(cover_frame, text = '-Loss of Keys',font = 'times 11',justify = 'left',anchor = 'w')
label_audiosystem = Label(cover_frame, text = '-Audio System',font = 'times 11',justify = 'left',anchor = 'w')

label_basicexcess.grid(row = 4,column =0 ,sticky = W)
label_theft.grid(row = 5,column = 0,sticky = W)
label_windscreen.grid(row = 6,column = 0,sticky = W)
label_thirdparty.grid(row = 7,column = 0,sticky = W)
label_section2.grid(row =8 ,column = 0,sticky = W)
label_lossofkeys.grid(row = 9,column = 0,sticky = W)

entry_excess = Entry(cover_frame,
	                 bg = 'light blue').grid(row = 4, column =1)
entry_theft = Entry(cover_frame,
	                bg = 'light blue').grid(row = 5, column =1)
entry_windscreen = Entry(cover_frame,
	                     bg = 'light blue').grid(row = 6, column =1)
entry_thirdparty = Entry(cover_frame,
	                     bg = 'light blue').grid(row = 7, column =1)
entry_section2 = Entry(cover_frame,
	                   bg = 'light blue').grid(row = 8, column =1)
entry_lossofkeys = Entry(cover_frame,
	                     bg = 'light blue').grid(row = 9, column =1)

#-----------------Specified Vehicles-----------------------------
label_specified = Label(specified_frame,text = 'Specified Vehicles',font = 'times 20 bold underline' )
label_specified.grid(row = 0,column = 0,sticky = W)

label_showquote = Label(specified_frame,text = 'Show On Quote',font = 'times 11 bold ')
label_showquote.grid(row =1, column =0,sticky = W)
clicked_showquote = IntVar()
check_poltype = Checkbutton(specified_frame,variable=clicked_showquote)
check_poltype.grid(row=1,column =1 ,sticky = W)

label_vdescription = Label(specified_frame,text = 'Vehicle Description',font = 'times 11 bold ')
label_sasriacat = Label(specified_frame,text = 'SASRIA Category',font = 'times 11 bold ')
label_suminsured = Label(specified_frame,text = 'Sum Insured',font = 'times 11 bold ')
label_rate = Label(specified_frame,text = 'Rate',font = 'times 11 bold ')
label_annpremium = Label(specified_frame,text = 'Annual Premium',font = 'times 11 bold ')
label_sasria_prem2 = Label(specified_frame,text = 'SASRIA Premium',font = 'times 11 bold ')

label_vdescription.grid(row = 2, column =1,sticky = W)
label_sasriacat.grid(row = 2, column =2,sticky = W)
label_suminsured.grid(row = 2, column =3,sticky = W)
label_rate.grid(row = 2, column =4,sticky = W)
label_annpremium.grid(row = 2, column =5,sticky = W)
label_sasria_prem2.grid(row = 2, column =6,sticky = W)


e_spec11 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 1,sticky = W)
clicked_cat1 = StringVar(specified_frame)
clicked_cat1.set('Select Option           ')
menu_cat1 = OptionMenu(specified_frame,
                       clicked_cat1,
                       'Cars)Primary use:Domestic/private)',
                       'LDV(Commercial use)',
                       'Taxi(7-24)',
                       'Motor Traders',
                       'Buses',
                       'Mobile Plant',
                       'BRT',
                       'Heavy Vehichles(>3,500kg)').grid(row=3,column = 2)

e_spec13 = Entry(specified_frame,
	             textvariable = user_s13,
	             bg = 'light blue').grid(row = 3, column = 3,sticky = W)
e_spec14 = Entry(specified_frame,
	             textvariable = user_s14,
	             bg = 'light blue').grid(row = 3, column = 4,sticky = W)
e_spec15 = Entry(specified_frame,
	             textvariable = user_s15).grid(row = 3, column = 5,sticky = W)
e_spec16 = Entry(specified_frame,
	             textvariable = user_s16).grid(row = 3, column = 6,sticky = W)

e_spec21 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 1,sticky = W)
clicked_cat2 = StringVar(specified_frame)
clicked_cat2.set('Select Option           ')
menu_cat2 = OptionMenu(specified_frame,
                       clicked_cat2,
                       'Cars)Primary use:Domestic/private)',
                       'LDV(Commercial use)',
                       'Taxi(7-24)',
                       'Motor Traders',
                       'Buses',
                       'Mobile Plant',
                       'BRT',
                       'Heavy Vehichles(>3,500kg)').grid(row=4,column = 2)
e_spec23 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s23).grid(row = 4, column = 3,sticky = W)
e_spec24 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s24).grid(row = 4, column = 4,sticky = W)
e_spec25 = Entry(specified_frame,
	             textvariable = user_s25).grid(row = 4, column = 5,sticky = W)
e_spec26 = Entry(specified_frame,
	             textvariable = user_s26).grid(row = 4, column = 6,sticky = W)

e_spec31 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 1,sticky = W)
clicked_cat3 = StringVar(specified_frame)
clicked_cat3.set('Select Option           ')
menu_cat3 = OptionMenu(specified_frame,
                       clicked_cat3,
                       'Cars)Primary use:Domestic/private)',
                       'LDV(Commercial use)',
                       'Taxi(7-24)',
                       'Motor Traders',
                       'Buses',
                       'Mobile Plant',
                       'BRT',
                       'Heavy Vehichles(>3,500kg)').grid(row=5,column = 2)
e_spec33 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s33).grid(row = 5, column = 3,sticky = W)
e_spec34 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s34).grid(row = 5, column = 4,sticky = W)
e_spec35 = Entry(specified_frame,
	             textvariable = user_s35).grid(row = 5, column = 5,sticky = W)
e_spec36 = Entry(specified_frame,
	             textvariable = user_s36).grid(row = 5, column = 6,sticky = W)

e_spec41 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 1,sticky = W)
clicked_cat4 = StringVar(specified_frame)
clicked_cat4.set('Select Option           ')
menu_cat4 = OptionMenu(specified_frame,
                       clicked_cat4,
                       'Cars)Primary use:Domestic/private)',
                       'LDV(Commercial use)',
                       'Taxi(7-24)',
                       'Motor Traders',
                       'Buses',
                       'Mobile Plant',
                       'BRT',
                       'Heavy Vehichles(>3,500kg)').grid(row=6,column = 2)
e_spec43 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s43).grid(row = 6, column = 3,sticky = W)
e_spec44 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s44).grid(row = 6, column = 4,sticky = W)
e_spec45 = Entry(specified_frame,
	             textvariable =user_s45).grid(row = 6, column = 5,sticky = W)
e_spec46 = Entry(specified_frame,
	             textvariable = user_s46).grid(row = 6, column = 6,sticky = W)

e_spec51 = Entry(specified_frame,

	             bg = 'light blue').grid(row = 7, column = 1,sticky = W)
clicked_cat5 = StringVar(specified_frame)
clicked_cat5.set('Select Option           ')
menu_cat5 = OptionMenu(specified_frame,
                       clicked_cat5,
                       'Cars)Primary use:Domestic/private)',
                       'LDV(Commercial use)',
                       'Taxi(7-24)',
                       'Motor Traders',
                       'Buses',
                       'Mobile Plant',
                       'BRT',
                       'Heavy Vehichles(>3,500kg)').grid(row=7,column = 2)
e_spec53 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s53).grid(row = 7, column = 3,sticky = W)
e_spec54 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s54).grid(row = 7, column = 4,sticky = W)
e_spec55 = Entry(specified_frame,
	             textvariable = user_s55).grid(row = 7, column = 5,sticky = W)
e_spec56 = Entry(specified_frame,
	             textvariable = user_s56).grid(row = 7, column = 6,sticky = W)

button_totfleet = Button(specified_frame, text=
	"Total", command=add_spec)
button_totfleet.grid(row = 8,column = 4)

e_spec65 = Entry(specified_frame,
	             textvariable = user_s65).grid(row = 8,column = 5)
e_spec66 = Entry(specified_frame,
	             textvariable = user_s66).grid(row = 8,column = 6)

label_excess2 = Label(specified_frame,text = 'Excess',font = 'times 12 bold',anchor = "w")
label_excess2.grid(row = 9,column = 0,sticky = W)

label_basicexcess2 = Label(specified_frame, text = '-Basic Excess',font = 'times 11',justify = 'left',anchor = 'w')
label_theft2 = Label(specified_frame, text = '-Theft/Hijack',font = 'times 11',justify = 'left',anchor = 'w')
label_windscreen2 = Label(specified_frame, text = '-Windscreen',font = 'times 11',justify = 'left',anchor = 'w')
label_thirdparty2 = Label(specified_frame, text = '-Third Party Liability',font = 'times 11',justify = 'left',anchor = 'w')
label_section22 = Label(specified_frame, text = '-Section 2 only Excess',font = 'times 11',justify = 'left',anchor = 'w')
label_lossofkeys2 = Label(specified_frame, text = '-Loss of Keys',font = 'times 11',justify = 'left',anchor = 'w')
label_audiosystem2 = Label(specified_frame, text = '-Audio System',font = 'times 11',justify = 'left',anchor = 'w')

label_basicexcess2.grid(row = 10,column =0 ,sticky = W)
label_theft2.grid(row = 11,column = 0,sticky = W)
label_windscreen2.grid(row = 12,column = 0,sticky = W)
label_thirdparty2.grid(row = 13,column = 0,sticky = W)
label_section22.grid(row =14 ,column = 0,sticky = W)
label_lossofkeys2.grid(row = 15,column = 0,sticky = W)

e_excess2 = Entry(specified_frame,
	              bg = 'light blue').grid(row = 10, column =1)
e_theft2 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 11, column =1)
e_windscreen2 = Entry(specified_frame,
	                  bg = 'light blue').grid(row = 12, column =1)
e_thirdparty2 = Entry(specified_frame,
	                  bg = 'light blue').grid(row = 13, column =1)
e_section22 = Entry(specified_frame,
	                bg = 'light blue').grid(row = 14, column =1)
e_lossofkeys2 = Entry(specified_frame,
	                  bg = 'light blue').grid(row = 15, column =1)


#---------------------------Rating Info------------------------------
rating_frame = LabelFrame(main_frame,text = 'Rating Information')
rating_frame.grid(row = 1, column =0,sticky = W)

option1_frame = LabelFrame(rating_frame,text = 'Option 1')
option2_frame = LabelFrame(rating_frame,text = 'Option 2')
option3_frame = LabelFrame(rating_frame,text = 'Option 3')
option4_frame = LabelFrame(rating_frame,text = 'Option 4')




label_ratinginfo = Label(rating_frame,text = 'Rating Information',font = 'times 18 bold underline')
label_fleetvalue = Label(rating_frame,text = 'Fleet value: ',font = 'times 12 bold')
label_priorclaims = Label(rating_frame,text = 'Prior year claims: ',font = 'times 12 bold')
label_totalclaims = Label(rating_frame,text = 'Total claims YTD: ',font = 'times 12 bold')
label_numofmonths = Label(rating_frame,text = 'No. of months remaining before renewal: ',font = 'times 12 bold')
label_annclaims = Label(rating_frame,text = 'Annualised Claims: ',font = 'times 12 bold')

label_ratinginfo.grid(row =0,column = 0,sticky = W)
label_fleetvalue.grid(row = 1,column = 0,sticky = W)
label_priorclaims.grid(row = 2,column = 0,sticky = W)
label_totalclaims.grid(row = 3,column = 0,sticky = W)
label_numofmonths.grid(row = 4,column = 0,sticky = W)
label_annclaims.grid(row = 5,column = 0,sticky = W)
option1_frame.grid(row = 7, column =0,sticky = W)
option2_frame.grid(row = 8, column =0,sticky = W)
option3_frame.grid(row = 9, column =0,sticky = W)
option4_frame.grid(row = 10, column =0,sticky = W)

entry_fleetvalue= Entry(rating_frame).grid(row = 1,column = 1,sticky = W)
entry_proirclaims = Entry(rating_frame).grid(row = 2,column = 1,sticky = W)
entry_totalclaims= Entry(rating_frame).grid(row = 3,column = 1,sticky = W)
entry_numofmonths = Entry(rating_frame).grid(row = 4,column = 1,sticky = W)
entry_annclaims = Entry(rating_frame).grid(row = 5,column = 1,sticky = W)

label_premcalcs = Label(rating_frame,text = 'Premium Calcuations',font = 'times 18 bold underline')
label_premcalcs.grid(row = 6,column = 0,sticky ='W')
#------------------------Option 1 ---------------------------------
label_opt1 = Label(option1_frame,text = 'Option 1- Conventional',font = 'times 15 bold underline')
label_showqoteopt1 = Label(option1_frame,text = 'Show on Quote:' ,font = 'times 12 bold')
label_premfleetopt1 = Label(option1_frame,text = 'Premiunm based on fleet value:',font = 'times 12 bold')
label_ratioapplied = Label(option1_frame,text = 'Rate/Ratio applied: ')
label_premiumopt1 = Label(option1_frame,text = 'Premium: ')
label_premlossopt1 = Label(option1_frame,text = 'Premiunm based on loss value:',font = 'times 12 bold')
label_roundupeopt1 = Label(option1_frame,text = 'Round-up/-down',font = 'times 12 bold')
label_roundnearopt1 = Label(option1_frame,text = 'Round to nearest:',font = 'times 12 bold')
label_premquoteopt1 = Label(option1_frame,text = 'Premium on Quote:',font = 'times 12 bold')
label_overrideopt1 = Label(option1_frame,text = 'Override?',font = 'times 12 bold')
label_premquote2opt1 = Label(option1_frame,text = 'Premium on Quote:',font = 'times 12 bold')

clicked_typerating = StringVar(option1_frame)
clicked_typerating.set('No')
menu_type = OptionMenu(option1_frame, clicked_typerating,'No','Yes')
menu_type.grid(row = 1,column = 1)

label_opt1.grid(row =0,column = 0)
label_showqoteopt1.grid(row = 1, column = 0,sticky = W)
label_ratioapplied.grid(row = 2,column = 1)
label_premiumopt1.grid(row = 2,column = 2)
label_premfleetopt1.grid(row =3,column = 0,sticky = W)
label_premlossopt1.grid(row =4,column = 0,sticky = W)
label_roundupeopt1.grid(row =5,column = 0,sticky = W)
label_roundnearopt1.grid(row =6,column = 0,sticky = W)
label_premquoteopt1.grid(row =7,column = 0,sticky = W)
label_overrideopt1.grid(row =8,column = 0,sticky = W)
label_premquote2opt1.grid(row =9,column = 0,sticky = W)

entry_fleetpremopt1 = Entry(option1_frame).grid(row = 3,column = 1,sticky = 'W')
entry_fleetpercopt1 = Entry(option1_frame).grid(row = 3,column = 2,sticky = 'W')

entry_losspremopt1 = Entry(option1_frame).grid(row = 4,column = 1)
entry_losspercopt1 = Entry(option1_frame).grid(row = 4,column = 2)

entry_premopt1 =Entry(option1_frame).grid(row = 7,column = 1)
entry_prem2opt1 =Entry(option1_frame).grid(row = 9,column = 1)

clicked_roundopt1 = StringVar(option1_frame)
clicked_roundopt1.set('Up')
menu_roundopt1 = OptionMenu(option1_frame, clicked_roundopt1,'Up','Down')
menu_roundopt1.grid(row = 5,column = 1)

clicked_typerating = StringVar(option1_frame)
clicked_typerating.set('R10 000')
menu_type = OptionMenu(option1_frame, clicked_typerating,'R1000','R10 000','R100 000')
menu_type.grid(row = 6,column = 1)

clicked_overopt1 = StringVar(option1_frame)
clicked_overopt1.set('No')
menu_overopt1 = OptionMenu(option1_frame, clicked_overopt1,'No','Yes')
menu_overopt1.grid(row = 8,column = 1)

#------------------------Option 2---------------------------
label_opt2 = Label(option2_frame,text = 'Option 2- Burning Cost',font = 'times 15 bold underline')
label_showqoteopt2 = Label(option2_frame,text = 'Show on Quote:' ,font = 'times 12 bold')
label_loadingopt2 = Label(option2_frame,text = 'Loading: ')
label_totalpremopt2 = Label(option2_frame,text = 'Total Premium: ')

label_premloadingopt2 = Label(option2_frame,text = 'Premiunm loading',font = 'times 12 bold')

label_premsplitopt2 = Label(option2_frame,text = 'Premium Split: ',font = 'times 12 bold')
label_prempropopt2 = Label(option2_frame,text = 'Proportional Split: ')
label_premopt2 = Label(option2_frame,text = 'Premium: ')

label_depositpremopt2 = Label(option2_frame,text = ':Deposit premium ')
label_burner1opt2 = Label(option2_frame,text = 'Burner 1')
label_burner2opt2 = Label(option2_frame,text = 'Burner 2')


clicked_showquoteopt2 = StringVar(option2_frame)
clicked_showquoteopt2.set('No')
menu_type = OptionMenu(option2_frame, clicked_showquoteopt2,'No','Yes')
menu_type.grid(row = 1,column = 1)

label_opt2.grid(row =0,column = 0)
label_showqoteopt2.grid(row = 1, column = 0,sticky = W)
label_loadingopt2.grid(row = 2,column = 1)
label_totalpremopt2.grid(row = 2,column = 2)
label_premloadingopt2.grid(row =3,column = 0,sticky = W)
label_premsplitopt2.grid(row =4,column = 0,sticky = W)
label_prempropopt2 .grid(row =4,column = 1)
label_premopt2.grid(row =4,column = 2)

label_depositpremopt2.grid(row =5,column = 0,sticky = W)
label_burner1opt2.grid(row =6,column = 0,sticky = W)
label_burner2opt2.grid(row =7,column = 0,sticky = W)

entry_premloadingopt2 = Entry(option2_frame).grid(row = 3,column = 1)
entry_totalpremopt2 = Entry(option2_frame).grid(row = 3,column = 2)
entry_depositsplitopt2 = Entry(option2_frame).grid(row = 5,column = 1)
entry_depositpremopt2 = Entry(option2_frame).grid(row = 5,column = 2)
entry_burner1splitopt2 = Entry(option2_frame).grid(row = 6,column = 1)
entry_burner1premopt2 =Entry(option2_frame).grid(row = 6,column = 2)
ntry_burner2splitopt2 =Entry(option2_frame).grid(row = 7,column = 1)
entry_burner2premopt2 =Entry(option2_frame).grid(row = 7,column = 2)


#--------------------------Option3-------------------------------------------
label_opt3 = Label(option3_frame,text = 'Option 3- Aggregate Excess ',font = 'times 15 bold underline ')
label_showquoteopt3 = Label(option3_frame,text = 'Show On Quote: ',font = 'times 12 bold ')
label_annualopt3 = Label(option3_frame,text = 'Annual Aggregate: ',font = 'times 12 bold ')
label_applicableopt3 = Label(option3_frame,text = 'Applicable to: ',font = 'times 12 bold ')
label_stoplossopt3 = Label(option3_frame,text = 'Stop Loss Limit: ',font = 'times 12 bold ')
label_claimsopt3 = Label(option3_frame,text = 'Claims paid by insurer: ',font = 'times 12 bold')
label_numofmonthsopt3 = Label(option3_frame,text = 'No. of months before renewal: ',font = 'times 12 bold')
label_annclaimsopt3 = Label(option3_frame,text = 'Annualised Claims: ',font = 'times 12 bold')
label_rateopt3 = Label(option3_frame,text = 'Rate/Ratio applied')
label_premopt3 = Label(option3_frame,text = ' Premium')
label_premlossopt3 = Label(option3_frame,text = 'Premiium based on loss ratio: ',font = 'times 12 bold')
label_premclaimsopt3 = Label(option3_frame,text = 'Premium based on claims above stop loss limit: ',font = 'times 12 bold')
label_roundupopt3 = Label(option3_frame,text = 'Round up/down: ',font = 'times 12 bold')
label_roundnearopt3 = Label(option3_frame,text = 'Round to nearest: ',font = 'times 12 bold')
label_premquoteopt3 = Label(option3_frame,text = 'Premium on Quote: ',font = 'times 12 bold ')
label_overrideopt3 = Label(option3_frame,text = 'Override?: ',font = 'times 12 bold')
label_premquote2opt3 = Label(option3_frame,text = 'Premium on Quote: ',font = 'times 12 bold')
label_showtextopt3 = Label(option3_frame,text = 'Show the below text on quote?: ',font = 'times 12 bold')

label_opt3.grid(row = 0,column = 0,sticky = W)
label_showquoteopt3.grid(row = 1,column = 0,sticky = W)
label_annualopt3.grid(row = 2,column = 0,sticky = W)
label_applicableopt3.grid(row = 3,column = 0,sticky = W)
label_stoplossopt3.grid(row = 4,column = 0,sticky = W)
label_claimsopt3 .grid(row = 5,column = 0,sticky = W)
label_numofmonthsopt3 .grid(row = 6,column = 0,sticky = W)
label_annclaimsopt3.grid(row = 7,column = 0,sticky = W)
label_rateopt3.grid(row = 8,column = 1,sticky = W)
label_premopt3.grid(row = 8,column = 2,sticky = W)
label_premlossopt3.grid(row = 9,column = 0,sticky = W)
label_premclaimsopt3 .grid(row = 10,column = 0,sticky = W)
label_roundupopt3.grid(row = 11,column = 0,sticky = W)
label_roundnearopt3.grid(row = 12,column = 0,sticky = W)
label_premquoteopt3.grid(row = 13,column = 0,sticky = W)
label_overrideopt3.grid(row = 14,column = 0,sticky = W)
label_premquote2opt3.grid(row = 15,column = 0,sticky = W)
label_showtextopt3.grid(row = 16,column = 0,sticky = W)

clicked_showquoteopt3 = StringVar(option3_frame)
clicked_showquoteopt3.set('No')
menu_showopt3 = OptionMenu(option3_frame, clicked_showquoteopt3,'No','Yes')
menu_showopt3.grid(row = 1,column = 1)

entry_annual = Entry(option3_frame).grid(row = 2,column = 1)

clicked_sectionopt3 = StringVar(option3_frame)
clicked_sectionopt3.set('Section A & B')
menu_sectionopt3 = OptionMenu(option3_frame, clicked_sectionopt3,'Section A & B','Section A')
menu_sectionopt3.grid(row = 3,column = 1)

entry_stoplossopt3 = Entry(option3_frame).grid(row = 4,column = 1)
entry_claimsopt3= Entry(option3_frame).grid(row = 5,column = 1)
entry_numofmonthsopt3 = Entry(option3_frame).grid(row = 6,column = 1)
entry_annclaimsopt3 = Entry(option3_frame).grid(row = 7,column = 1)
entry_premrateopt3 = Entry(option3_frame).grid(row = 9,column = 1)
entry_ratiopremopt3 = Entry(option3_frame).grid(row = 9,column = 2)
entry_claimrateopt3 = Entry(option4_frame).grid(row = 10,column = 1)
entry_claimpremopt3 = Entry(option4_frame).grid(row = 10,column = 2)

clicked_roundopt3 = StringVar(option3_frame)
clicked_roundopt3.set('Up')
menu_roundopt3 = OptionMenu(option3_frame, clicked_roundopt3,'Up','Down')
menu_roundopt3.grid(row = 11,column = 1)

clicked_sectionopt3 = StringVar(option3_frame)
clicked_sectionopt3.set('Section A & B')
menu_shectionopt3 = OptionMenu(option3_frame, clicked_sectionopt3,'R1 000','R10 000','R100 000')
menu_sectionopt3.grid(row = 12,column = 1)

entry_premonquoteopt3 = Entry(option3_frame).grid(row = 13,column = 1)

clicked_overrideopt3 = StringVar(option3_frame)
clicked_overrideopt3.set('No')
menu_roundopt3 = OptionMenu(option3_frame, clicked_overrideopt3,'No','Yes')
menu_roundopt3.grid(row = 14,column = 1)

entry_premonquote2opt3 = Entry(option3_frame).grid(row = 15,column = 1)

clicked_textopt3 = StringVar(option3_frame)
clicked_textopt3.set('No')
menu_roundopt3 = OptionMenu(option3_frame, clicked_overrideopt3,'No','Yes')
menu_roundopt3.grid(row = 16,column = 1)
textlabelopt3 = 'All legal, assessor fees and other fees/expenses will contribute the aggregrate deductible'
label_textopt3 = Label(option3_frame,text = textlabelopt3,font = 'times 11 italic')
label_textopt3.grid(row = 17,column = 0) 

#-------------------Option 4----------------------------------------------------------
label_opt4 = Label(option4_frame,text = 'Option 4- Aggregate Excess with Burner ',font = 'times 15 bold underline ')
label_showquoteopt4 = Label(option4_frame,text = 'Show On Quote: ',font = 'times 12 bold ')
label_annualopt4 = Label(option4_frame,text = 'Annual Aggregate: ',font = 'times 12 bold ')
label_applicableopt4 = Label(option4_frame,text = 'Applicable to: ',font = 'times 12 bold ')
label_stoplossopt4 = Label(option4_frame,text = 'Stop Loss Limit: ',font = 'times 12 bold ')
label_claimsopt4 = Label(option4_frame,text = 'Claims paid by insurer: ',font = 'times 12 bold')
label_numofmonthsopt4 = Label(option4_frame,text = 'No. of months before renewal: ',font = 'times 12 bold')
label_annclaimsopt4 = Label(option4_frame,text = 'Annualised Claims: ',font = 'times 12 bold')
label_rateopt4= Label(option4_frame,text = 'Rate/Ratio applied')
label_premopt4 = Label(option4_frame,text = ' Premium')
label_premlossopt4 = Label(option4_frame,text = 'Premiium based on loss ratio: ',font = 'times 12 bold')
label_premclaimsopt4 = Label(option4_frame,text = 'Premium based on claims above stop loss limit: ',font = 'times 12 bold')
label_roundupopt4 = Label(option4_frame,text = 'Round up/down: ',font = 'times 12 bold')
label_roundnearopt4 = Label(option4_frame,text = 'Round to nearest: ',font = 'times 12 bold')
label_premquoteopt4 = Label(option4_frame,text = 'Premium on Quote: ',font = 'times 12 bold ')
label_overrideopt4 = Label(option4_frame,text = 'Override?: ',font = 'times 12 bold')
label_premquote2opt4 = Label(option4_frame,text = 'Premium on Quote: ',font = 'times 12 bold')
label_showtextopt4 = Label(option4_frame,text = 'Show the below text on quote?: ',font = 'times 12 bold')

label_opt4.grid(row = 0,column = 0,sticky = W)
label_showquoteopt4.grid(row = 1,column = 0,sticky = W)
label_annualopt4.grid(row = 2,column = 0,sticky = W)
label_applicableopt4.grid(row = 3,column = 0,sticky = W)
label_stoplossopt4.grid(row = 4,column = 0,sticky = W)
label_claimsopt4.grid(row = 5,column = 0,sticky = W)
label_numofmonthsopt4.grid(row = 6,column = 0,sticky = W)
label_annclaimsopt4.grid(row = 7,column = 0,sticky = W)
label_rateopt4.grid(row = 8,column = 1,sticky = W)
label_premopt4.grid(row = 8,column = 2,sticky = W)
label_premlossopt4.grid(row = 9,column = 0,sticky = W)
label_premclaimsopt4.grid(row = 10,column = 0,sticky = W)
label_roundupopt4.grid(row = 11,column = 0,sticky = W)
label_roundnearopt4.grid(row = 12,column = 0,sticky = W)
label_premquoteopt4.grid(row = 13,column = 0,sticky = W)
label_overrideopt4.grid(row = 14,column = 0,sticky = W)
label_premquote2opt4.grid(row = 15,column = 0,sticky = W)
label_showtextopt4.grid(row = 16,column = 0,sticky = W)

clicked_showquoteopt4 = StringVar(option3_frame)
clicked_showquoteopt4.set('No')
menu_showopt4= OptionMenu(option4_frame, clicked_showquoteopt4,'No','Yes')
menu_showopt4.grid(row = 1,column = 1)

entry_annual = Entry(option3_frame).grid(row = 2,column = 1)

clicked_sectionopt4 = StringVar(option4_frame)
clicked_sectionopt4.set('Section A & B')
menu_sectionopt4 = OptionMenu(option4_frame, clicked_sectionopt4,'Section A & B','Section A')
menu_sectionopt4.grid(row = 3,column = 1)

entry_stoplossopt4 = Entry(option4_frame).grid(row = 4,column = 1)
entry_claimsopt4= Entry(option4_frame).grid(row = 5,column = 1)
entry_numofmonthsopt4 = Entry(option4_frame).grid(row = 6,column = 1)
entry_annclaimsopt4 = Entry(option4_frame).grid(row = 7,column = 1)
entry_premrateopt4 = Entry(option4_frame).grid(row = 9,column = 1)
entry_ratiopremopt4 = Entry(option4_frame).grid(row = 9,column = 2)
entry_claimrateopt4 = Entry(option4_frame).grid(row = 10,column = 1)
entry_claimpremopt4 = Entry(option4_frame).grid(row = 10,column = 2)

clicked_roundopt4 = StringVar(option4_frame)
clicked_roundopt4.set('Up')
menu_roundopt4 = OptionMenu(option4_frame, clicked_roundopt4,'Up','Down')
menu_roundopt4.grid(row = 11,column = 1)

clicked_sectionopt4 = StringVar(option3_frame)
clicked_sectionopt4.set('Section A & B')
menu_shectionopt4= OptionMenu(option4_frame, clicked_sectionopt4,'R1 000','R10 000','R100 000')
menu_sectionopt4.grid(row = 12,column = 1)

entry_premonquoteopt4 = Entry(option4_frame).grid(row = 13,column = 1)

clicked_overrideopt4 = StringVar(option4_frame)
clicked_overrideopt4.set('No')
menu_roundopt4 = OptionMenu(option4_frame, clicked_overrideopt4,'No','Yes')
menu_roundopt4.grid(row = 14,column = 1)

entry_premonquote2opt4 = Entry(option4_frame).grid(row = 15,column = 1)

clicked_textopt4 = StringVar(option4_frame)
clicked_textopt4.set('No')
menu_roundopt4 = OptionMenu(option4_frame, clicked_overrideopt4,'No','Yes')
menu_roundopt4.grid(row = 16,column = 1)
textlabelopt4 = 'All legal, assessor fees and other fees/expenses will contribute the aggregrate deductible'
label_textopt4 = Label(option4_frame,text = textlabelopt4,font = 'times 11 italic')
label_textopt4.grid(row = 17,column = 0) 

button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()