from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/LesediM/Desktop/New/LI.ico")
 
main_frame = Frame(root)
main_frame.pack(fill = BOTH,expand = 1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT,fill = BOTH, expand = 1)

my_yscrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL,command = my_canvas.yview)
my_xscrollbar = ttk.Scrollbar(main_frame, orient = HORIZONTAL,command = my_canvas.xview)

my_yscrollbar.pack(side = RIGHT, fill = Y)
my_xscrollbar.pack(side = BOTTOM, fill = X)


my_canvas.configure(yscrollcommand=my_yscrollbar.set)
my_canvas.configure(xscrollcommand=my_xscrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window = second_frame,anchor = "nw")

# # my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

# # Creating labels for policyholders
label_pholder = Label(second_frame,width = 50,text = 'Policy Holder Information', font = 'times 15 bold underline')
label_type = Label(second_frame,width = 50,text = 'Type of quote: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_date = Label(second_frame,width = 50,text = 'Date of quote: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_insured = Label(second_frame,width = 50,text = 'Insured: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_pol_no = Label(second_frame,width = 50,text = 'Policy no: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_inception = Label(second_frame,width = 50,text = 'Policy inception: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_period = Label(second_frame,width = 50,text = 'Period of insurance: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_to = Label(second_frame,width = 50,text = '         	to ',font = 'times 12  bold',anchor = "w")
label_pol_type = Label(second_frame,width = 50,text = 'Policy type: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_description = Label(second_frame,width = 50,text = 'Business description: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_operation = Label(second_frame,width = 50,text = 'Key area of operation: ',font = 'times 12 bold',anchor = "w",justify= 'left')

# #Placing labels on grib for policy holder
label_pholder.pack(side = LEFT)
# label_type.grid(row = 2,column = 0)
# label_date.grid(row = 3,column = 0)
# label_insured.grid(row = 4,column = 0)
# label_pol_no.grid(row = 5,column = 0)
# label_inception.grid(row = 6,column = 0)
# label_period.grid(row = 7,column = 0)
# label_to.grid(row = 7, column = 2)
# label_pol_type.grid(row = 9,column = 0)
# label_description.grid(row = 10,column = 0)
# label_operation.grid(row = 11,column = 0)

# #Text boxes for policyholder information
# entry_dateofquote = Entry(second_frame).grid(row = 3,column = 1)
# entry_insured = Entry(second_frame).grid(row =4,column = 1)
# entry_policyno = Entry(second_frame).grid(row =5,column = 1)
# entry_policyinception = Entry(second_frame).grid(row =6,column = 1)
# enrty_periodfrom = Entry(second_frame).grid(row = 7,column =1)
# entry_periodto = Entry(second_frame).grid(row = 7,column = 3)
# entry_description = Entry(second_frame).grid(row = 10,column = 1)
# entry_operation = Entry(second_frame).grid(row =11,column = 1)

# #Dropdown menus for policy information
# clicked_type = StringVar(second_frame)
# clicked_type.set('Renewal')
# menu_type = OptionMenu(second_frame, clicked_type,'Renewal','New Business')
# menu_type.grid(row=2,column = 1)

# clicked_poltype = StringVar(second_frame)
# clicked_poltype.set('Annual')
# menu_poltype = OptionMenu(second_frame, clicked_poltype,'Annual','Monthly')
# menu_poltype.grid(row=9,column = 1)

# #Fleet Information
# label_fleet = Label(second_frame, width = 50,text = 'Fleet Information',font = 'times 15 bold underline' )
# label_space = Label(second_frame, text = "  ")
# label_space.grid(row = 12,column = 0)
# label_fleet.grid(row = 13)

# #Labels for fleet information
# label_vcategory = Label(second_frame,width = 50,text ='Vehicle Category',font = 'times 12 bold underline',justify = 'left',anchor = "w")
# label_cars = Label(second_frame,width = 50,text ='Cars- Single Vehicles',font = 'times 12',justify = 'left',anchor = "w")
# label_motorcycles = Label(second_frame,width = 50,text ='Motorcycles',font = 'times 12',anchor = "w")
# label_ldvs = Label(second_frame,width = 50,text ='LDVs',font = 'times 12',anchor = "w")
# label_commercial = Label(second_frame,width = 50,text ='Commercial Vehicles(Mass ≥ 3500kg)',font = 'times 12',anchor = "w")
# label_busses = Label(second_frame,width = 50,text ='Busses',font = 'times 12',anchor = "w")
# label_mobile = Label(second_frame,width = 50,text ='Mobile Plants ',font = 'times 12',anchor = "w")
# label_specialless = Label(second_frame,width = 50,text ='Special Types < 3500kg(incl Trailers and Forklifts) ',font = 'times 12',anchor = "w")
# label_specialmore = Label(second_frame,width = 50,text ='Special Types > 3500kg(incl Trailers and Forklifts) ',font = 'times 12',anchor = "w")
# label_total = Label(second_frame,width = 50,text ='Total',font = 'times 12 bold underline',justify = 'left',anchor = "w")




# #Place labels on grid for fleet information
# label_vcategory.grid(row = 14,column = 0)
# label_vcategory.grid(row = 15,column = 0)
# label_cars.grid(row = 16,column = 0)
# label_motorcycles.grid(row = 17,column = 0)
# label_ldvs.grid(row = 18,column = 0)
# label_commercial.grid(row = 19,column = 0)
# label_busses.grid(row = 20,column = 0)
# label_mobile.grid(row = 21,column = 0)
# label_specialless.grid(row = 22,column = 0)
# label_specialmore.grid(row = 23,column = 0)
# label_total.grid(row = 24,column = 0)

# label_units = Label(second_frame,width = 10,text = 'No. of units',font = 'times 12 bold underline')
# label_value = Label(second_frame,width = 11,text = 'Value',font = 'times 12 bold underline')
# label_damage = Label(second_frame,width = 31,text = 'Own Damage Limit',font = 'times 12 bold underline')
# label_sasria_des = Label(second_frame,width = 30,text = 'SASRIA Description',font = 'times 12 bold underline')
# label_sasria_prem = Label(second_frame,width = 15,text = 'SASRIA Premium',font = 'times 12 bold underline')

# label_units.grid(row = 14,column = 1)
# label_damage.grid(row = 14,column = 2)
# label_damage.grid(row = 14,column = 3)
# label_sasria_des.grid(row = 14,column = 4)
# label_sasria_prem.grid(row = 14,column = 5)

# entry_fleet11 = Entry(second_frame).grid(row = 16,column=1)
# entry_fleet12 = Entry(second_frame).grid(row = 16,column=3)
# entry_fleet13 = Entry(second_frame).grid(row = 16,column=4)
# entry_fleet14 = Entry(second_frame).grid(row = 16,column=5)
# entry_fleet21 = Entry(second_frame).grid(row = 17,column=1)
# entry_fleet22 = Entry(second_frame).grid(row = 17,column=3)
# entry_fleet23 = Entry(second_frame).grid(row = 17,column=4)
# entry_fleet24 = Entry(second_frame).grid(row = 17,column=5)
# entry_fleet31 = Entry(second_frame).grid(row = 18,column=1)
# entry_fleet32 = Entry(second_frame).grid(row = 18,column=3)
# entry_fleet33 = Entry(second_frame).grid(row = 18,column=4)
# entry_fleet34 = Entry(second_frame).grid(row = 18,column=5)
# entry_fleet41 = Entry(second_frame).grid(row = 19,column=1)
# entry_fleet42 = Entry(second_frame).grid(row = 19,column=3)
# entry_fleet43 = Entry(second_frame).grid(row = 19,column=4)
# entry_fleet44 = Entry(second_frame).grid(row = 19,column=5)
# entry_fleet51 = Entry(second_frame).grid(row = 20,column=1)
# entry_fleet52 = Entry(second_frame).grid(row = 20,column=3)
# entry_fleet53 = Entry(second_frame).grid(row = 20,column=4)
# entry_fleet54 = Entry(second_frame).grid(row = 20,column=5)
# entry_fleet61 = Entry(second_frame).grid(row = 21,column=1)
# entry_fleet62 = Entry(second_frame).grid(row = 21,column=3)
# entry_fleet63 = Entry(second_frame).grid(row = 21,column=4)
# entry_fleet64 = Entry(second_frame).grid(row = 21,column=5)
# entry_fleet71 = Entry(second_frame).grid(row = 22,column=1)
# entry_fleet72 = Entry(second_frame).grid(row = 22,column=3)
# entry_fleet73 = Entry(second_frame).grid(row = 22,column=4)
# entry_fleet74 = Entry(second_frame).grid(row = 22,column=5)
# entry_fleet81 = Entry(second_frame).grid(row = 23,column=1)
# entry_fleet82 = Entry(second_frame).grid(row = 23,column=3)
# entry_fleet83 = Entry(second_frame).grid(row = 23,column=4)
# entry_fleet84 = Entry(second_frame).grid(row = 23,column=5)
# entry_fleet91 = Entry(second_frame).grid(row = 24,column=1)
# entry_fleet92 = Entry(second_frame).grid(row = 24,column=3)


# label_coverinfo = Label(second_frame, text ='Cover Information',font = 'times 15 bold underline')
# label_coverinfo.grid(row = 25, column = 0)

# label_covertype = Label(second_frame, justify = 'left',anchor = "w",text = 'Cover Type: ',width = 50,font = 'times 12 bold')
# label_liability = Label(second_frame,anchor = 'w',width = 50,text = 'Third Party Liability: ',font ='times 12 bold')

# label_liability.grid(row = 27,column = 0)
# label_covertype.grid(row = 26, column = 0)

# clicked_covertype = StringVar(second_frame)
# clicked_covertype.set('Comprehensive')
# menu_cover = OptionMenu(second_frame,clicked_covertype,'Comprehensive'
# 											  ,'Third Party, Fire and Theft'
# 											  ,'Third Party Only'
# 											  ,'Own Damage Only')
# menu_cover.grid(row = 26,column = 1)
# entry_liabilty = Entry(second_frame).grid(row=27,column = 1)

# label_excess = Label(second_frame,text = 'Excess',font = 'times 12 bold',anchor = "w",width = 50)
# label_excess.grid(row = 28,column = 0)

# label_basicexcess = Label(second_frame, text = '-Basic Excess',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_theft = Label(second_frame, text = '-Theft/Hijack',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_windscreen = Label(second_frame, text = '-Windscreen',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_thirdparty = Label(second_frame, text = '-Third Party Liability',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_section2 = Label(second_frame, text = '-Section 2 only Excess',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_lossofkeys = Label(second_frame, text = '-Loss of Keys',font = 'times 11',justify = 'left',anchor = 'w',width = 50)
# label_audiosystem = Label(second_frame, text = '-Audio System',font = 'times 11',justify = 'left',anchor = 'w',width = 50)

# label_basicexcess.grid(row = 29,column = 0)
# label_theft.grid(row = 30,column = 0)
# label_windscreen.grid(row = 31,column = 0)
# label_thirdparty.grid(row = 32,column = 0)
# label_section2.grid(row = 33,column = 0)
# label_lossofkeys.grid(row = 34,column = 0)

# entry_excess = Entry(second_frame).grid(row = 29, column =1)
# entry_theft = Entry(second_frame).grid(row = 30, column =1)
# entry_windscreen = Entry(second_frame).grid(row = 31, column =1)
# entry_thirdparty = Entry(second_frame).grid(row = 32, column =1)
# entry_section2 = Entry(second_frame).grid(row = 33, column =1)
# entry_lossofkeys = Entry(second_frame).grid(row = 34, column =1)

# label_specified = Label(second_frame, width = 50,text = 'Specified Vehicles',font = 'times 15 bold underline' )
# label_specified.grid(row = 35,column = 0)

# label_showquote = Label(second_frame,width = 50,justify = 'left',anchor = "w",text = 'Show Quote',font = 'times 11 bold ')
# label_showquote.grid(row =36, column =0)
# clicked_showquote = StringVar(second_frame)
# clicked_showquote.set('Yes')
# menu_poltype = OptionMenu(second_frame, clicked_showquote,'Yes','No')
# menu_poltype.grid(row=36,column = 1)

# label_vdescription = Label(second_frame,width = 50,justify = 'left',anchor = "w",text = 'Vehicle Description',font = 'times 11 bold ')
# label_sasriacat = Label(second_frame,width = 20,justify = 'left',anchor = "w",text = 'SASRIA Category',font = 'times 11 bold ')
# label_suminsured = Label(second_frame,width = 20,justify = 'left',anchor = "w",text = 'Sum Insured',font = 'times 11 bold ')
# label_rate = Label(second_frame,width = 20,justify = 'left',anchor = "w",text = 'Rate',font = 'times 11 bold ')
# label_annpremium = Label(second_frame,width = 20,justify = 'left',anchor = "w",text = 'Annual Premium',font = 'times 11 bold ')
# label_sasria_prem2 = Label(second_frame,width = 20,justify = 'left',anchor = "w",text = 'SASRIA Premium',font = 'times 11 bold ')

# label_vdescription.grid(row = 37, column =0)
# label_sasriacat.grid(row = 37, column =1)
# label_suminsured.grid(row = 37, column =2)
# label_rate.grid(row = 37, column =3)
# label_annpremium.grid(row = 37, column =4)
# label_sasria_prem2.grid(row = 37, column =5)

# entry_spec11 = Entry(second_frame).grid(row = 39, column = 0)
# entry_spec12 = Entry(second_frame).grid(row = 40, column = 1)
# entry_spec13 = Entry(second_frame).grid(row = 41, column = 2)
# entry_spec14 = Entry(second_frame).grid(row = 42, column = 3)
# entry_spec15 = Entry(second_frame).grid(row = 43, column = 4)
# entry_spec16 = Entry(second_frame).grid(row = 44, column = 5)
# entry_spec21 = Entry(second_frame).grid(row = 45, column = 0)
# entry_spec22 = Entry(second_frame).grid(row = 46, column = 1)
# entry_spec23 = Entry(second_frame).grid(row = 47, column = 2)
# entry_spec24 = Entry(second_frame).grid(row = 48, column = 3)
# entry_spec25 = Entry(second_frame).grid(row = 49, column = 4)
# entry_spec26 = Entry(second_frame).grid(row = 50, column = 5)
# entry_spec31 = Entry(second_frame).grid(row = 51, column = 0)
# entry_spec32 = Entry(second_frame).grid(row = 52, column = 1)
# entry_spec33 = Entry(second_frame).grid(row = 53, column = 2)
# entry_spec34 = Entry(second_frame).grid(row = 54, column = 3)
# entry_spec35 = Entry(second_frame).grid(row = 55, column = 4)
# entry_spec36 = Entry(second_frame).grid(row = 56, column = 5)
# entry_spec41 = Entry(second_frame).grid(row = 57, column = 0)
# entry_spec42 = Entry(second_frame).grid(row = 58, column = 1)
# entry_spec43 = Entry(second_frame).grid(row = 59, column = 2)
# entry_spec44 = Entry(second_frame).grid(row = 60, column = 3)
# entry_spec45 = Entry(second_frame).grid(row = 61, column = 4)
# entry_spec46 = Entry(second_frame).grid(row = 62, column = 5)
# entry_spec51 = Entry(second_frame).grid(row = 63, column = 0)
# entry_spec52 = Entry(second_frame).grid(row = 64, column = 1)
# entry_spec53 = Entry(second_frame).grid(row = 65, column = 2)
# entry_spec54 = Entry(second_frame).grid(row = 66, column = 3)
# entry_spec55 = Entry(second_frame).grid(row = 67, column = 4)
# entry_spec56 = Entry(second_frame).grid(row = 68, column = 5)


# button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()
