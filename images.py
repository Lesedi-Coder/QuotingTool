from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

HEIGHT = 700
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

pol_frame = ttk.Frame(main_frame)
fleet_frame = ttk.Frame(main_frame)
cover_frame = ttk.Frame(main_frame)
specified_frame = ttk.Frame(main_frame)

pol_frame.grid(column =0,row = 0)
fleet_frame.grid(column =0,row = 1)
cover_frame.grid(column =0,row = 2)
specified_frame.grid(column =0,row = 3)



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

#------------------Policy Holder Infromation-------------------------------------------
label_pholder = Label(pol_frame,text = 'Policy Holder Information',width = 50 ,font = 'times 13 bold underline', anchor = 'w')
label_type = Label(pol_frame,text = 'Type of quote: ',width = 50 ,font = 'times 12 bold',anchor = 'w')
label_date = Label(pol_frame,text = 'Date of quote: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_insured = Label(pol_frame,text = 'Insured: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_pol_no = Label(pol_frame,text = 'Policy no: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_inception = Label(pol_frame,text = 'Policy inception: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_period = Label(pol_frame,text = 'Period of insurance(From--To): ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_to = Label(pol_frame,text = '             to ',width = 20,font = 'times 12  bold' ,anchor = "w")
label_pol_type = Label(pol_frame,text = 'Policy type: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_description = Label(pol_frame,text = 'Business description: ',width = 50 ,font = 'times 12 bold',anchor = "w")
label_operation = Label(pol_frame,text = 'Key area of operation: ',width = 50 ,font = 'times 12 bold',anchor = "w")

#Placing labels on grib for policy holder
label_pholder.grid(row  = 0,rowspan =2)
label_type.grid(row = 2,column = 0)
label_date.grid(row = 3,column = 0)
label_insured.grid(row = 4,column = 0)
label_pol_no.grid(row = 5,column = 0)
label_inception.grid(row = 6,column = 0)
label_period.grid(row = 7,column = 0)
label_to.grid(row = 7, column = 2)
label_pol_type.grid(row = 8,column = 0)
label_description.grid(row = 9,column = 0)
label_operation.grid(row = 10,column = 0)

#Text boxes for policyholder information
entry_dateofquote = Entry(pol_frame).grid(row = 3,column = 1)
entry_insured = Entry(pol_frame).grid(row =4,column = 1)
entry_policyno = Entry(pol_frame).grid(row =5,column = 1)
entry_policyinception = Entry(pol_frame).grid(row =6,column = 1)
enrty_periodfrom = Entry(pol_frame).grid(row = 7,column =1)
entry_periodto = Entry(pol_frame).grid(row = 7,column = 3)
entry_description = Entry(pol_frame).grid(row = 9,column = 1)
entry_operation = Entry(pol_frame).grid(row =10,column = 1,rowspan = 2)

#Dropdown menus for policy information
clicked_type = StringVar(pol_frame)
clicked_type.set('Renewal')
menu_type = OptionMenu(pol_frame, clicked_type,'Renewal','New Business')
menu_type.grid(row=2,column = 1)

clicked_poltype = StringVar(pol_frame)
clicked_poltype.set('Annual')
menu_poltype = OptionMenu(pol_frame, clicked_poltype,'Annual','Monthly')
menu_poltype.grid(row=8,column = 1)

#--------------------Fleet Information---------------------------------------------------

label_fleet = Label(fleet_frame, width = 50,text = 'Fleet Information',font = 'times 13 bold underline',anchor = 'w')
label_fleet.grid(row = 0,column = 0)

#Labels for fleet information
label_vcategory = Label(fleet_frame,width = 50,text ='Vehicle Category',font = 'times 12 bold underline',justify = 'left',anchor = "w")
label_cars = Label(fleet_frame,width = 50,text ='Cars- Single Vehicles',font = 'times 12',justify = 'left',anchor = "w")
label_motorcycles = Label(fleet_frame,width = 50,text ='Motorcycles',font = 'times 12',anchor = "w")
label_ldvs = Label(fleet_frame,text ='LDVs',width = 50,font = 'times 12',anchor = "w")
label_commercial = Label(fleet_frame,width = 50,text ='Commercial Vehicles(Mass ≥ 3500kg)',font = 'times 12',anchor = "w")
label_busses = Label(fleet_frame,width = 50,text ='Busses',font = 'times 12',anchor = "w")
label_mobile = Label(fleet_frame,width = 50,text ='Mobile Plants ',font = 'times 12',anchor = "w")
label_specialless = Label(fleet_frame,width = 50,text ='Special Types < 3500kg(incl Trailers and Forklifts)',font = 'times 12',anchor = "w")
label_specialmore = Label(fleet_frame,width = 50,text ='Special Types > 3500kg(incl Trailers and Forklifts)',font = 'times 12',anchor = "w")
label_total = Label(fleet_frame,width = 50,text ='Total',font = 'times 12 bold underline',justify = 'left',anchor = "w")


#Place labels on grid for fleet information
label_vcategory.grid(row = 1,column = 0)
label_cars.grid(row = 2,column = 0)
label_motorcycles.grid(row = 3,column = 0)
label_ldvs.grid(row = 4,column = 0,)
label_commercial.grid(row = 5,column = 0)
label_busses.grid(row = 6,column = 0)
label_mobile.grid(row = 7,column = 0)
label_specialless.grid(row = 8,column = 0)
label_specialmore.grid(row = 9,column = 0)
label_total.grid(row = 10,column = 0)

label_units = Label(fleet_frame,text = 'No. of units',font = 'times 12 bold underline',anchor = "w")
label_value = Label(fleet_frame,text = 'Value',font = 'times 12 bold underline',anchor = "w")
label_damage = Label(fleet_frame,text = 'Own Damage Limit',font = 'times 12 bold underline',anchor = "w")
label_sasria_des = Label(fleet_frame,text = 'SASRIA Description',font = 'times 12 bold underline',anchor = "w")
label_sasria_prem = Label(fleet_frame,text = 'SASRIA Premium',font = 'times 12 bold underline',anchor = "w")

label_units.grid(row = 1,column = 1)
label_damage.grid(row = 1,column = 2)
label_damage.grid(row = 1,column = 3)
label_sasria_des.grid(row = 1,column = 4)
label_sasria_prem.grid(row = 1,column = 5)

entry_fleet11 = Entry(fleet_frame,width = 10).grid(row = 2,column=1)
entry_fleet12 = Entry(fleet_frame).grid(row = 2,column=3)
entry_fleet13 = Entry(fleet_frame).grid(row = 2,column=4)
entry_fleet14 = Entry(fleet_frame).grid(row = 2,column=5)
entry_fleet21 = Entry(fleet_frame,width = 10).grid(row = 3,column=1)
entry_fleet22 = Entry(fleet_frame).grid(row = 3,column=3)
entry_fleet23 = Entry(fleet_frame).grid(row = 3,column=4)
entry_fleet24 = Entry(fleet_frame).grid(row = 3,column=5)
entry_fleet31 = Entry(fleet_frame,width = 10).grid(row = 4,column=1)
entry_fleet32 = Entry(fleet_frame).grid(row = 4,column=3)
entry_fleet33 = Entry(fleet_frame).grid(row = 4,column=4)
entry_fleet34 = Entry(fleet_frame).grid(row = 4,column=5)
entry_fleet41 = Entry(fleet_frame,width = 10).grid(row = 5,column=1)
entry_fleet42 = Entry(fleet_frame).grid(row = 5,column=3)
entry_fleet43 = Entry(fleet_frame).grid(row = 5,column=4)
entry_fleet44 = Entry(fleet_frame).grid(row = 5,column=5)
entry_fleet51 = Entry(fleet_frame,width = 10).grid(row = 6,column=1)
entry_fleet52 = Entry(fleet_frame).grid(row = 6,column=3)
entry_fleet53 = Entry(fleet_frame).grid(row = 6,column=4)
entry_fleet54 = Entry(fleet_frame).grid(row = 6,column=5)
entry_fleet61 = Entry(fleet_frame,width = 10).grid(row = 7,column=1)
entry_fleet62 = Entry(fleet_frame).grid(row = 7,column=3)
entry_fleet63 = Entry(fleet_frame).grid(row = 7,column=4)
entry_fleet64 = Entry(fleet_frame).grid(row = 7,column=5)
entry_fleet71 = Entry(fleet_frame,width = 10).grid(row = 8,column=1)
entry_fleet72 = Entry(fleet_frame).grid(row = 8,column=3)
entry_fleet73 = Entry(fleet_frame).grid(row = 8,column=4)
entry_fleet74 = Entry(fleet_frame).grid(row = 8,column=5)
entry_fleet81 = Entry(fleet_frame,width = 10).grid(row = 9,column=1)
entry_fleet82 = Entry(fleet_frame).grid(row = 9,column=3)
entry_fleet83 = Entry(fleet_frame).grid(row = 9,column=4)
entry_fleet84 = Entry(fleet_frame).grid(row = 9,column=5)
entry_fleet91 = Entry(fleet_frame,width = 10).grid(row = 10,column=1)
entry_fleet92 = Entry(fleet_frame).grid(row = 10,column=3)

#----------------Cover Information----------------------------

label_coverinfo = Label(cover_frame,width = 50, text ='Cover Information',font = 'times 13 bold underline',justify = 'left',anchor = 'w')
label_coverinfo.grid(row = 0, column = 0)

label_covertype = Label(cover_frame, justify = 'left',anchor = "w",text = 'Cover Type: ',width = 50,font = 'times 12 bold')
label_liability = Label(cover_frame,anchor = 'w',width = 50,text = 'Third Party Liability: ',font ='times 12 bold')

label_covertype.grid(row = 1, column = 0)
label_liability.grid(row = 2,column = 0)

clicked_covertype = StringVar(cover_frame)
clicked_covertype.set('Comprehensive')
menu_cover = OptionMenu(cover_frame,clicked_covertype,'Comprehensive'
											  ,'Third Party, Fire and Theft'
											  ,'Third Party Only'
											  ,'Own Damage Only')
menu_cover.grid(row = 1,column = 1)
entry_liabilty = Entry(cover_frame).grid(row=2,column = 1)

label_excess = Label(cover_frame,text = 'Excess',font = 'times 12 bold',anchor = "w",width = 50)
label_excess.grid(row = 3,column = 0)

label_basicexcess = Label(cover_frame, text = '-Basic Excess',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_theft = Label(cover_frame, text = '-Theft/Hijack',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_windscreen = Label(cover_frame, text = '-Windscreen',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_thirdparty = Label(cover_frame, text = '-Third Party Liability',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_section2 = Label(cover_frame, text = '-Section 2 only Excess',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_lossofkeys = Label(cover_frame, text = '-Loss of Keys',font = 'times 12',justify = 'left',anchor = 'w',width = 50)
label_audiosystem = Label(cover_frame, text = '-Audio System',font = 'times 12',justify = 'left',anchor = 'w',width = 50)

label_basicexcess.grid(row = 4,column = 0)
label_theft.grid(row = 5,column = 0)
label_windscreen.grid(row = 6,column = 0)
label_thirdparty.grid(row = 7,column = 0)
label_section2.grid(row =8 ,column = 0)
label_lossofkeys.grid(row = 9,column = 0)

entry_excess = Entry(cover_frame).grid(row = 4, column =1)
entry_theft = Entry(cover_frame).grid(row = 5, column =1)
entry_windscreen = Entry(cover_frame).grid(row = 6, column =1)
entry_thirdparty = Entry(cover_frame).grid(row = 7, column =1)
entry_section2 = Entry(cover_frame).grid(row = 8, column =1)
entry_lossofkeys = Entry(cover_frame).grid(row = 9, column =1)

# label_specified = Label(cover_frame, width = 50,text = 'Specified Vehicles',font = 'times 13 bold underline',justify = 'left',anchor = 'w' )
# label_specified.grid(row = 35,column = 0)

# label_showquote = Label(cover_frame,width = 50,justify = 'left',anchor = "w",text = 'Show Quote',font = 'times 11 bold ')
# label_showquote.grid(row =36, column =0)
# clicked_showquote = StringVar(cover_frame)
# clicked_showquote.set('Yes')
# menu_poltype = OptionMenu(cover_frame, clicked_showquote,'Yes','No')
# menu_poltype.grid(row=36,column = 1)

# label_vdescription = Label(cover_frame,width = 50,justify = 'left',anchor = "w",text = 'Vehicle Description',font = 'times 11 bold ')
# label_sasriacat = Label(cover_frame,width = 20,justify = 'left',anchor = "w",text = 'SASRIA Category',font = 'times 11 bold ')
# label_suminsured = Label(cover_frame,width = 20,justify = 'left',anchor = "w",text = 'Sum Insured',font = 'times 11 bold ')
# label_rate = Label(cover_frame,width = 20,justify = 'left',anchor = "w",text = 'Rate',font = 'times 11 bold ')
# label_annpremium = Label(cover_frame,width = 20,justify = 'left',anchor = "w",text = 'Annual Premium',font = 'times 11 bold ')
# label_sasria_prem2 = Label(cover_frame,width = 20,justify = 'left',anchor = "w",text = 'SASRIA Premium',font = 'times 11 bold ')

# label_vdescription.grid(row = 37, column =0)
# label_sasriacat.grid(row = 37, column =1)
# label_suminsured.grid(row = 37, column =2)
# label_rate.grid(row = 37, column =3)
# label_annpremium.grid(row = 37, column =4)
# label_sasria_prem2.grid(row = 37, column =5)

# entry_spec11 = Entry(cover_frame).grid(row = 39, column = 0)
# entry_spec12 = Entry(cover_frame).grid(row = 40, column = 1)
# entry_spec13 = Entry(cover_frame).grid(row = 41, column = 2)
# entry_spec14 = Entry(cover_frame).grid(row = 42, column = 3)
# entry_spec15 = Entry(cover_frame).grid(row = 43, column = 4)
# entry_spec16 = Entry(cover_frame).grid(row = 44, column = 5)
# entry_spec21 = Entry(cover_frame).grid(row = 45, column = 0)
# entry_spec22 = Entry(cover_frame).grid(row = 46, column = 1)
# entry_spec23 = Entry(cover_frame).grid(row = 47, column = 2)
# entry_spec24 = Entry(cover_frame).grid(row = 48, column = 3)
# entry_spec25 = Entry(cover_frame).grid(row = 49, column = 4)
# entry_spec26 = Entry(cover_frame).grid(row = 50, column = 5)
# entry_spec31 = Entry(cover_frame).grid(row = 51, column = 0)
# entry_spec32 = Entry(cover_frame).grid(row = 52, column = 1)
# entry_spec33 = Entry(cover_frame).grid(row = 53, column = 2)
# entry_spec34 = Entry(cover_frame).grid(row = 54, column = 3)
# entry_spec35 = Entry(cover_frame).grid(row = 55, column = 4)
# entry_spec36 = Entry(cover_frame).grid(row = 56, column = 5)
# entry_spec41 = Entry(cover_frame).grid(row = 57, column = 0)
# entry_spec42 = Entry(cover_frame).grid(row = 58, column = 1)
# entry_spec43 = Entry(cover_frame).grid(row = 59, column = 2)
# entry_spec44 = Entry(cover_frame).grid(row = 60, column = 3)
# entry_spec45 = Entry(cover_frame).grid(row = 61, column = 4)
# entry_spec46 = Entry(cover_frame).grid(row = 62, column = 5)
# entry_spec51 = Entry(cover_frame).grid(row = 63, column = 0)
# entry_spec52 = Entry(cover_frame).grid(row = 64, column = 1)
# entry_spec53 = Entry(cover_frame).grid(row = 65, column = 2)
# entry_spec54 = Entry(cover_frame).grid(row = 66, column = 3)
# entry_spec55 = Entry(cover_frame).grid(row = 67, column = 4)
# entry_spec56 = Entry(cover_frame).grid(row = 68, column = 5)


button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()
