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
user_inputinsured = StringVar(pol_frame)
user_inputpolno = StringVar(pol_frame)
user_inputdesc = StringVar(pol_frame)
user_inputoper = StringVar(pol_frame)

def validation():

	if (user_inputinsured.get() == "" or
	    user_inputpolno.get()=="" or
	    user_inputdesc.get()  == "" or
	    user_inputoper.get() == ""):
		messagebox.showwarning('Missng Entries','Please enter missing entries')


	elif (user_inputpolno.get().isdigit()):
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font('Arial','B',11)
		# pdf.cell(20,20,my_img,0,1,'C')
		pdf.cell(10,10,f"Type of quote:\t\t\t{clicked_type.get()}",0,1,'L')
		pdf.cell(10,10,f"Date of quote:\t\t\t{entry_dateofquote.selection_get()}",0,1,'L')
		pdf.cell(10,10,f"Insured:\t\t\t{user_inputinsured.get()}",0,1,'L')
		pdf.cell(10,10,f"Policy No:\t\t\t{user_inputpolno.get()}",0,1,'L')
		pdf.cell(10,10,f"Policy Inception:\t\t\t{entry_policyinception.selection_get()}",
			     0,1,'L')
		pdf.cell(10,
			     10,
			     f"Period Of Insurance:\t\t\t{enrty_periodfrom.selection_get()} to {entry_periodto.selection_get()}",
			     0,1,'L')
		pdf.cell(10,10,f"Policy Type:\t\t\t{clicked_poltype.get()}",0,1,'L')
		pdf.cell(10,10,f"Business Description:\t\t\t{user_inputdesc.get()}",0,1,'L')
		pdf.cell(10,10,f"Key Area Of Operation:\t\t\t{user_inputoper.get()}",0,1,'L')


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
e_dateofquote = Calendar(pol_frame,selectmode = "day",year = 2020,month =5,day = 1)
e_dateofquote.grid(row = 3,column = 1) 

e_insured = Entry(pol_frame,textvariable = user_inputinsured,bg = 'light blue')
e_insured.grid(row =4,column = 1)

e_policyno = Entry(pol_frame,
	               textvariable = user_inputpolno,
	               bg = 'light blue')
e_policyno.grid(row =5,column = 1)

e_policyinception = Calendar(pol_frame,selectmode = "day",year = 2020,month =5,day = 1)
e_policyinception.grid(row =6,column = 1)


e_periodfrom = Calendar(pol_frame,selectmode = "day",year = 2020,month =5,day = 1)
e_periodfrom.grid(row = 7,column =1)

e_periodto = Calendar(pol_frame,selectmode = "day",year = 2020,month =5,day = 1)
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
clicked_type.set('Renewal')
menu_type = OptionMenu(pol_frame, clicked_type,'Renewal','New Business')
menu_type.grid(row=2,column = 1)

clicked_poltype = StringVar(pol_frame)
clicked_poltype.set('Annual')
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
label_ldvs = Label(fleet_frame,text ='LDVs',font = 'times 12',anchor = "w")
label_commercial = Label(fleet_frame,
	                     text ='Commercial Vehicles(Mass ≥ 3500kg)',
	                     font = 'times 12')
label_busses = Label(fleet_frame,text ='Busses',
	                 font = 'times 12')
label_mobile = Label(fleet_frame,text ='Mobile Plants ',font = 'times 12')
label_specialless = Label(fleet_frame,
	                      text ='Special Types < 3500kg(incl Trailers and Forklifts)',
	                      font = 'times 12',anchor = "w")
label_specialmore = Label(fleet_frame,
	                      text ='Special Types > 3500kg(incl Trailers and Forklifts)',
	                      font = 'times 12',anchor = "w")
label_total = Label(fleet_frame,text ='Total',font = 'times 12 bold underline',anchor = "w")


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


e_fleet11 = Entry(fleet_frame,
	                  textvariable = IntVar(pol_frame),
	                  width = 10,
	                  bg = 'light blue').grid(row = 2,column=1)
e_fleet12 = Entry(fleet_frame,
	                  textvariable = DoubleVar(pol_frame),
	                  bg = 'light blue').grid(row = 2,column=2)
e_fleet13 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 2,column=3)
e_fleet14 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 2,column=4)
e_fleet15 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 2,column=5)

e_fleet21 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              width = 10,
	              bg = 'light blue').grid(row = 3,column=1)
e_fleet22 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 3,column=2)
e_fleet23 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 3,column=3)
e_fleet24 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 3,column=4)
e_fleet25 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 3,column=5)

e_fleet31 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              width = 10,
	              bg = 'light blue').grid(row = 4,column=1)
e_fleet32 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 4,column=2)
e_fleet33 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 4,column=3)
e_fleet34 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 4,column=4)
e_fleet35 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 4,column=5)

e_fleet41 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              width = 10,
	              bg = 'light blue').grid(row = 5,column=1)
e_fleet42 = Entry(fleet_frame,
	               textvariable = DoubleVar(pol_frame),
	               bg = 'light blue').grid(row = 5,column=2)
e_fleet43 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 5,column=3)
e_fleet44 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 5,column=4)
e_fleet45 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 5,column=5)

e_fleet51 = Entry(fleet_frame,
	               textvariable = IntVar(pol_frame),
	               	bg = 'light blue',width = 10).grid(row = 6,column=1)
e_fleet52 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 6,column=2)
e_fleet53 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 6,column=3)
e_fleet54 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 6,column=4)
e_fleet55 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 6,column=5)

e_fleet61 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              width = 10,
	              bg = 'light blue').grid(row = 7,column=1)
e_fleet62 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 7,column=2)
e_fleet63 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 7,column=3)
e_fleet64 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 7,column=4)
e_fleet65 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 7,column=5)

e_fleet71 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              bg = 'light blue',width = 10).grid(row = 8,column=1)
e_fleet72 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 8,column=2)
e_fleet73 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 8,column=3)
e_fleet74 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 8,column=4)
e_fleet75 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 8,column=5)

e_fleet81 = Entry(fleet_frame,
	              textvariable = IntVar(pol_frame),
	              width = 10,
	              bg = 'light blue').grid(row = 9,column=1)
e_fleet82 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 9,column=2)
e_fleet83 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 9,column=3)
e_fleet84 = Entry(fleet_frame,
	              bg = 'light blue').grid(row = 9,column=4)
e_fleet85 = Entry(fleet_frame,
	              textvariable = DoubleVar(pol_frame),
	              bg = 'light blue').grid(row = 9,column=5)

e_fleet91 = Entry(fleet_frame,width = 10).grid(row = 10,column=1)
e_fleet92 = Entry(fleet_frame).grid(row = 10,column=2)


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
e_spec12 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 2,sticky = W)
e_spec13 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 3,sticky = W)
e_spec14 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 4,sticky = W)
e_spec15 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 5,sticky = W)
e_spec16 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 3, column = 6,sticky = W)
e_spec21 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 1,sticky = W)
e_spec22 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 2,sticky = W)
e_spec23 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 3,sticky = W)
e_spec24 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 4,sticky = W)
e_spec25 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 5,sticky = W)
e_spec26 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 4, column = 6,sticky = W)
e_spec31 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 1,sticky = W)
e_spec32 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 2,sticky = W)
e_spec33 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 3,sticky = W)
e_spec34 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 4,sticky = W)
e_spec35 = Entry(specified_frame,
	              bg = 'light blue').grid(row = 5, column = 5,sticky = W)
e_spec36 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 5, column = 6,sticky = W)
e_spec41 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 1,sticky = W)
e_spec42 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 2,sticky = W)
e_spec43 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 3,sticky = W)
e_spec44 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 4,sticky = W)
e_spec45 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 5,sticky = W)
e_spec46 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 6, column = 6,sticky = W)
e_spec51 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 1,sticky = W)
e_spec52 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 2,sticky = W)
e_spec53 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 3,sticky = W)
e_spec54 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 4,sticky = W)
e_spec55 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 5,sticky = W)
e_spec56 = Entry(specified_frame,
	             bg = 'light blue').grid(row = 7, column = 6,sticky = W)

label_spectot = Label(specified_frame,text = 'Total ',font ='times 12 bold')
label_spectot.grid(row = 8,column = 4,sticky = W)

e_spec64 = Entry(specified_frame).grid(row = 8,column = 5)
e_spec65 = Entry(specified_frame).grid(row = 8,column = 6)

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
label_premcalcs.grid(row = 6,column = 0)
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

entry_fleetpremopt1 = Entry(option1_frame).grid(row = 3,column = 1)
entry_fleetpercopt1 = Entry(option1_frame).grid(row = 3,column = 2)

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