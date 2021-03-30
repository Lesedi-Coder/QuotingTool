from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/LesediM/Desktop/New/LI.ico")
label_space = Label(root, text = "  ")



# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

# Creating labels for policyholders
label_pholder = Label(root,width = 50,text = 'Policy Holder Information', font = 'times 15 bold underline')
label_type = Label(root,width = 50,text = 'Type of quote: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_date = Label(root,width = 50,text = 'Date of quote: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_insured = Label(root,width = 50,text = 'Insured: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_pol_no = Label(root,width = 50,text = 'Policy no: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_inception = Label(root,width = 50,text = 'Policy inception: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_period = Label(root,width = 50,text = 'Period of insurance: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_to = Label(root,text = 'to ',font = 'times 12  bold',anchor = "w")
label_pol_type = Label(root,width = 50,text = 'Policy type: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_description = Label(root,width = 50,text = 'Business description: ',font = 'times 12 bold',anchor = "w",justify= 'left')
label_operation = Label(root,width = 50,text = 'Key area of operation: ',font = 'times 12 bold',anchor = "w",justify= 'left')

#Placing labels on grib for policy holder
label_pholder.grid(row  = 0)
label_type.grid(row = 2,column = 0)
label_date.grid(row = 3,column = 0)
label_insured.grid(row = 4,column = 0)
label_pol_no.grid(row = 5,column = 0)
label_inception.grid(row = 6,column = 0)
label_period.grid(row = 7,column = 0)
label_to.grid(row = 7, column = 2)
label_pol_type.grid(row = 9,column = 0)
label_description.grid(row = 10,column = 0)
label_operation.grid(row = 11,column = 0)

#Text boxes for policyholder information
entry_dateofquote = Entry(root).grid(row = 3,column = 1)
entry_insured = Entry(root).grid(row =4,column = 1)
entry_policyno = Entry(root).grid(row =5,column = 1)
entry_policyinception = Entry(root).grid(row =6,column = 1)
enrty_periodfrom = Entry(root).grid(row = 7,column =1)
entry_periodto = Entry(root).grid(row = 7,column = 3)
entry_description = Entry(root).grid(row = 10,column = 1)
entry_operation = Entry(root).grid(row =11,column = 1)

#Dropdown menus for policy information
clicked_type = StringVar(root)
clicked_type.set('Renewal')
menu_type = OptionMenu(root, clicked_type,'Renewal','New Business')
menu_type.grid(row=2,column = 1)

clicked_poltype = StringVar(root)
clicked_poltype.set('Annual')
menu_poltype = OptionMenu(root, clicked_poltype,'Annual','Monthly')
menu_poltype.grid(row=9,column = 1)

#Fleet Information
label_fleet = Label(root, width = 50,text = 'Fleet Information',font = 'times 15 bold underline' )
label_space.grid(row = 12,column = 0)
label_fleet.grid(row = 13)

#Labels for fleet information
label_vcategory = Label(root,width = 50,text ='Vehicle Category',font = 'times 12 bold underline',justify = 'left',anchor = "w")
label_cars = Label(root,width = 50,text ='Cars- Single Vehicles',font = 'times 12',justify = 'left',anchor = "w")
label_motorcycles = Label(root,width = 50,text ='Motorcycles',font = 'times 12',anchor = "w")
label_ldvs = Label(root,width = 50,text ='LDVs',font = 'times 12',anchor = "w")
label_commercial = Label(root,width = 50,text ='Commercial Vehicles(Mass ≥ 3500kg)',font = 'times 12',anchor = "w")
label_busses = Label(root,width = 50,text ='Busses',font = 'times 12',anchor = "w")
label_mobile = Label(root,width = 50,text ='Mobile Plants ',font = 'times 12',anchor = "w")
label_specialless = Label(root,width = 50,text ='Special Types < 3500kg(incl Trailers and Forklifts) ',font = 'times 12',anchor = "w")
label_specialmore = Label(root,width = 50,text ='Special Types > 3500kg(incl Trailers and Forklifts) ',font = 'times 12',anchor = "w")



#Place labels on grid for fleet information
label_vcategory.grid(row = 14,column = 0)
label_vcategory.grid(row = 15,column = 0)
label_cars.grid(row = 16,column = 0)
label_motorcycles.grid(row = 17,column = 0)
label_ldvs.grid(row = 18,column = 0)
label_commercial.grid(row = 19,column = 0)
label_busses.grid(row = 20,column = 0)
label_mobile.grid(row = 21,column = 0)
label_specialless.grid(row = 22,column = 0)
label_specialmore.grid(row = 23,column = 0)

label_units = Label(root,width = 10,text = 'No. of units',font = 'times 12 bold underline')
label_value = Label(root,width = 11,text = 'Value',font = 'times 12 bold underline')
label_damage = Label(root,width = 31,text = 'Own Damage Limit',font = 'times 12 bold underline')
label_sasria_des = Label(root,width = 30,text = 'SASRIA Description',font = 'times 12 bold underline')
label_sasria_prem = Label(root,width = 15,text = 'SASRIA Premium',font = 'times 12 bold underline')

label_units.grid(row = 14,column = 1)
label_damage.grid(row = 14,column = 2)
label_damage.grid(row = 14,column = 3)
label_sasria_des.grid(row = 14,column = 4)
label_sasria_prem.grid(row = 14,column = 5)

entry_11 = Entry(root).grid(row = 16,column=1)
entry_12 = Entry(root).grid(row = 16,column=3)
entry_13 = Entry(root).grid(row = 16,column=4)
entry_14 = Entry(root).grid(row = 16,column=5)
entry_21 = Entry(root).grid(row = 17,column=1)
entry_22 = Entry(root).grid(row = 17,column=3)
entry_23 = Entry(root).grid(row = 17,column=4)
entry_24 = Entry(root).grid(row = 17,column=5)
entry_31 = Entry(root).grid(row = 18,column=1)
entry_32 = Entry(root).grid(row = 18,column=3)
entry_33 = Entry(root).grid(row = 18,column=4)
entry_34 = Entry(root).grid(row = 18,column=5)
entry_41 = Entry(root).grid(row = 19,column=1)
entry_42 = Entry(root).grid(row = 19,column=3)
entry_43 = Entry(root).grid(row = 19,column=4)
entry_44 = Entry(root).grid(row = 19,column=5)
entry_51 = Entry(root).grid(row = 20,column=1)
entry_52 = Entry(root).grid(row = 20,column=3)
entry_53 = Entry(root).grid(row = 20,column=4)
entry_54 = Entry(root).grid(row = 20,column=5)
entry_61 = Entry(root).grid(row = 21,column=1)
entry_62 = Entry(root).grid(row = 21,column=3)
entry_63 = Entry(root).grid(row = 21,column=4)
entry_64 = Entry(root).grid(row = 21,column=5)
entry_71 = Entry(root).grid(row = 22,column=1)
entry_72 = Entry(root).grid(row = 22,column=3)
entry_73 = Entry(root).grid(row = 22,column=4)
entry_74 = Entry(root).grid(row = 22,column=5)
entry_81 = Entry(root).grid(row = 23,column=1)
entry_82 = Entry(root).grid(row = 23,column=3)
entry_83 = Entry(root).grid(row = 23,column=4)
entry_84 = Entry(root).grid(row = 23,column=5)

label_coverinfo = Label(root, text ='Cover Information',font = 'times 15 bold underline')
label_coverinfo.grid(row = 24, column = 0)

label_covertype = Label(root, justify = 'left',anchor = "w",text = 'Cover Type: ',width = 50,font = 'times 12 bold')
label_covertype.grid(row = 25, column = 0)

clicked_covertype = StringVar(root)
clicked_covertype.set('Comprehensive')
menu_cover = OptionMenu(root,clicked_covertype,'Comprehensive', 'Third Party, Fire and Theft','Third Party Only','Own Damage Only')
menu_cover.grid(row = 25,column = 1)

label_liability = Label(root,anchor = 'w',width = 50,text = 'Third Party Liability: ',font ='times 12 bold')
label_liability.grid(row = 26,column = 0)

entry_liabilty = Entry(root).grid(row=26,column = 1)


button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()
