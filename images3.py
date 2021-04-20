from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

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

pol_frame = ttk.Frame(main_frame)
fleet_frame = ttk.Frame(main_frame)
cover_frame = ttk.Frame(main_frame)
specified_frame = ttk.Frame(main_frame)

pol_frame.grid(row = 0, column =0,sticky = W)
fleet_frame.grid(row = 1, column =0,sticky = W)
cover_frame.grid(row = 2, column =0,sticky = W)
specified_frame.grid(row = 3, column =0,sticky = W)



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Desktop/New/MA.png"))
# my_label = Label(root,image=my_img,anchor = 'w',justify = 'right')

#------------------Policy Holder Infromation-------------------------------------------
label_pholder = Label(pol_frame,text = 'Policy Holder Information' ,font = 'times 20 bold underline', anchor = 'w')
label_type = Label(pol_frame,text = 'Type of quote: ' ,font = 'times 12 bold',anchor = 'w')
label_date = Label(pol_frame,text = 'Date of quote: ' ,font = 'times 12 bold',anchor = "w")
label_insured = Label(pol_frame,text = 'Insured: ',font = 'times 12 bold',anchor = "w")
label_pol_no = Label(pol_frame,text = 'Policy no: ' ,font = 'times 12 bold',anchor = "w")
label_inception = Label(pol_frame,text = 'Policy inception: ',font = 'times 12 bold',anchor = "w")
label_period = Label(pol_frame,text = 'Period of insurance(From--To): ',font = 'times 12 bold',anchor = "w")
label_to = Label(pol_frame,text = 'to ',font = 'times 12  bold' ,anchor = "w")
label_pol_type = Label(pol_frame,text = 'Policy type: ',font = 'times 12 bold',anchor = "w")
label_description = Label(pol_frame,text = 'Business description: ' ,font = 'times 12 bold',anchor = "w")
label_operation = Label(pol_frame,text = 'Key area of operation: ' ,font = 'times 12 bold',anchor = "w")

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

label_fleet = Label(fleet_frame,text = 'Fleet Information',font = 'times 20 bold underline',anchor = 'w')
label_fleet.grid(row = 0,column = 0,sticky = W)

#Labels for fleet information
label_vcategory = Label(fleet_frame,text ='Vehicle Category',font = 'times 12 bold underline',justify = 'left',anchor = "w")
label_cars = Label(fleet_frame,text ='Cars- Single Vehicles',font = 'times 12',justify = 'left',anchor = "w")
label_motorcycles = Label(fleet_frame,text ='Motorcycles',font = 'times 12',anchor = "w")
label_ldvs = Label(fleet_frame,text ='LDVs',font = 'times 12',anchor = "w")
label_commercial = Label(fleet_frame,text ='Commercial Vehicles(Mass ≥ 3500kg)',font = 'times 12',anchor = "w")
label_busses = Label(fleet_frame,text ='Busses',font = 'times 12',anchor = "w")
label_mobile = Label(fleet_frame,text ='Mobile Plants ',font = 'times 12',anchor = "w")
label_specialless = Label(fleet_frame,text ='Special Types < 3500kg(incl Trailers and Forklifts)',font = 'times 12',anchor = "w")
label_specialmore = Label(fleet_frame,text ='Special Types > 3500kg(incl Trailers and Forklifts)',font = 'times 12',anchor = "w")
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

label_units = Label(fleet_frame,text = 'No. of units',font = 'times 12 bold ',anchor = "w")
label_value = Label(fleet_frame,text = 'Value',font = 'times 12 bold ',anchor = "w")
label_damage = Label(fleet_frame,text = 'Own Damage Limit',font = 'times 12 bold ',anchor = "w")
label_sasria_des = Label(fleet_frame,text = 'SASRIA Description',font = 'times 12 bold ',anchor = "w")
label_sasria_prem = Label(fleet_frame,text = 'SASRIA Premium',font = 'times 12 bold ',anchor = "w")

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
entry_liabilty = Entry(cover_frame).grid(row=2,column = 1,sticky = W)

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

entry_excess = Entry(cover_frame).grid(row = 4, column =1)
entry_theft = Entry(cover_frame).grid(row = 5, column =1)
entry_windscreen = Entry(cover_frame).grid(row = 6, column =1)
entry_thirdparty = Entry(cover_frame).grid(row = 7, column =1)
entry_section2 = Entry(cover_frame).grid(row = 8, column =1)
entry_lossofkeys = Entry(cover_frame).grid(row = 9, column =1)

#-----------------Specified Vehicles-----------------------------
label_specified = Label(specified_frame,text = 'Specified Vehicles',font = 'times 20 bold underline' )
label_specified.grid(row = 0,column = 0,sticky = W)

label_showquote = Label(specified_frame,text = 'Show On Quote',font = 'times 11 bold ')
label_showquote.grid(row =1, column =0,sticky = W)
clicked_showquote = StringVar()
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

entry_spec11 = Entry(specified_frame).grid(row = 3, column = 1,sticky = W)
entry_spec12 = Entry(specified_frame).grid(row = 3, column = 2,sticky = W)
entry_spec13 = Entry(specified_frame).grid(row = 3, column = 3,sticky = W)
entry_spec14 = Entry(specified_frame).grid(row = 3, column = 4,sticky = W)
entry_spec15 = Entry(specified_frame).grid(row = 3, column = 5,sticky = W)
entry_spec16 = Entry(specified_frame).grid(row = 3, column = 6,sticky = W)
entry_spec21 = Entry(specified_frame).grid(row = 4, column = 1,sticky = W)
entry_spec22 = Entry(specified_frame).grid(row = 4, column = 2,sticky = W)
entry_spec23 = Entry(specified_frame).grid(row = 4, column = 3,sticky = W)
entry_spec24 = Entry(specified_frame).grid(row = 4, column = 4,sticky = W)
entry_spec25 = Entry(specified_frame).grid(row = 4, column = 5,sticky = W)
entry_spec26 = Entry(specified_frame).grid(row = 4, column = 6,sticky = W)
entry_spec31 = Entry(specified_frame).grid(row = 5, column = 1,sticky = W)
entry_spec32 = Entry(specified_frame).grid(row = 5, column = 2,sticky = W)
entry_spec33 = Entry(specified_frame).grid(row = 5, column = 3,sticky = W)
entry_spec34 = Entry(specified_frame).grid(row = 5, column = 4,sticky = W)
entry_spec35 = Entry(specified_frame).grid(row = 5, column = 5,sticky = W)
entry_spec36 = Entry(specified_frame).grid(row = 5, column = 6,sticky = W)
entry_spec41 = Entry(specified_frame).grid(row = 6, column = 1,sticky = W)
entry_spec42 = Entry(specified_frame).grid(row = 6, column = 2,sticky = W)
entry_spec43 = Entry(specified_frame).grid(row = 6, column = 3,sticky = W)
entry_spec44 = Entry(specified_frame).grid(row = 6, column = 4,sticky = W)
entry_spec45 = Entry(specified_frame).grid(row = 6, column = 5,sticky = W)
entry_spec46 = Entry(specified_frame).grid(row = 6, column = 6,sticky = W)
entry_spec51 = Entry(specified_frame).grid(row = 7, column = 1,sticky = W)
entry_spec52 = Entry(specified_frame).grid(row = 7, column = 2,sticky = W)
entry_spec53 = Entry(specified_frame).grid(row = 7, column = 3,sticky = W)
entry_spec54 = Entry(specified_frame).grid(row = 7, column = 4,sticky = W)
entry_spec55 = Entry(specified_frame).grid(row = 7, column = 5,sticky = W)
entry_spec56 = Entry(specified_frame).grid(row = 7, column = 6,sticky = W)

label_spectot = Label(specified_frame,text = 'Total ',font ='times 12 bold')
label_spectot.grid(row = 8,column = 4,sticky = W)

entry_spec64 = Entry(specified_frame).grid(row = 8,column = 5)
entry_spec65 = Entry(specified_frame).grid(row = 8,column = 6)

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

entry_excess2 = Entry(specified_frame).grid(row = 10, column =1)
entry_theft2 = Entry(specified_frame).grid(row = 11, column =1)
entry_windscreen2 = Entry(specified_frame).grid(row = 12, column =1)
entry_thirdparty2 = Entry(specified_frame).grid(row = 13, column =1)
entry_section22 = Entry(specified_frame).grid(row = 14, column =1)
entry_lossofkeys2 = Entry(specified_frame).grid(row = 15, column =1)


#---------------------------Rating Info------------------------------
rating_frame = Frame(main_frame)
option1_frame = LabelFrame(main_frame,text = 'Option 1')
option2_frame = LabelFrame(main_frame,text = 'Option 2')
option3_frame = LabelFrame(main_frame,text = 'Option 3')
option4_frame = LabelFrame(main_frame,text = 'Option 4')

rating_frame.grid(row = 4, column =0,sticky = W)
option1_frame.grid(row = 5, column =0,sticky = W)
option2_frame.grid(row = 6, column =0,sticky = W)
option3_frame.grid(row = 7, column =0,sticky = W)
option4_frame.grid(row = 8, column =0,sticky = W)


label_ratinginfo = Label(rating_frame,text = 'Rating Information',font = 'times 18 bold underline')
label_fleetvalue = Label(rating_frame,text = 'Fleet value: ',font = 'times 12 bold')
label_priorclaims = Label(rating_frame,text = 'Prior year claims: ',font = 'times 12 bold')
label_totalclaims = Label(rating_frame,text = 'Total claims YTD: ',font = 'times 12 bold')
label_numofmonths = Label(rating_frame,text = 'No. of months remaining before renewal: ',font = 'times 12 bold')
label_annclaims = Label(rating_frame,text = 'Annualised Claims: ',font = 'times 12 bold')

label_ratinginfo.grid(row =0,column = 0,columnspan = 2,sticky = W)
label_fleetvalue.grid(row = 1,column = 0,sticky = W)
label_priorclaims.grid(row = 2,column = 0,sticky = W)
label_totalclaims.grid(row = 3,column = 0,sticky = W)
label_numofmonths.grid(row = 4,column = 0,sticky = W)
label_annclaims.grid(row = 5,column = 0,sticky = W)

entry_fleetvalue= Entry(rating_frame).grid(row = 1,column = 1,sticky = W)
entry_proirclaims = Entry(rating_frame).grid(row = 2,column = 1,sticky = W)
entry_totalclaims= Entry(rating_frame).grid(row = 3,column = 1,sticky = W)
entry_numofmonths = Entry(rating_frame).grid(row = 4,column = 1,sticky = W)
entry_annclaims = Entry(rating_frame).grid(row = 5,column = 1,sticky = W)

label_premcalcs = Label(rating_frame,text = 'Premium Calcuations',font = 'times 18 bold underline')
label_premcalcs.grid(row = 6,column = 0)

label_opt1 = Label(option1_frame,text = 'Option 1- Conventional',font = 'times 15 bold underline')
label_showqoteopt1 = Label(option1_frame,text = 'Show on Quote:' ,font = 'times 12 bold')
label_premfleetopt1 = Label(option1_frame,text = 'Premiunm based on fleet value:',font = 'times 12 bold')
label_ratioapplied = Label(option1_frame,text = 'Rate/Ratio applied: ')
label_premiumopt1 = Label(option1_frame,text = 'Premium: ')
label_premlossopt1 = Label(option1_frame,text = 'Premiunm based on loss value:',font = 'times 12 bold')
label_roundupeopt1 = Label(option1_frame,text = 'Round-up/-down',font = 'times 12 bold')
label_roundnearopt1 = Label(option1_frame,text = 'Round to nearest:',font = 'times 12 bold')
label_premquoteopt1 = Label(option1_frame,text = 'Premium on Quote:',font = 'times 12 bold')
label_overrideopt1 = Label(option1_frame,text = 'Override?:',font = 'times 12 bold')
label_premquote2opt1 = Label(option1_frame,text = 'Premium on Quote:',font = 'times 12 bold')

clicked_typerating = StringVar(option1_frame)
clicked_typerating.set('No')
menu_type = OptionMenu(option1_frame, clicked_typerating,'No','Yes')
menu_type.grid(row = 1,column = 1)

label_opt1.grid(row =0,column = 1)
label_showqoteopt1.grid(row = 1, column = 0,sticky = W)
label_ratioapplied.grid(row = 2,column = 1)
label_premiumopt1.grid(row = 2,column = 2)
label_premfleetopt1.grid(row =3,column = 0,sticky = W)
label_premlossopt1.grid(row =4,column = 0,sticky = W)
label_roundupeopt1.grid(row =5,column = 0,sticky = W)
label_roundnearopt1.grid(row =6,column = 0,sticky = W)
label_premquote2opt1.grid(row =7,column = 0,sticky = W)
label_overrideopt1.grid(row =8,column = 0,sticky = W)
label_premquote2opt1.grid(row =9,column = 1,sticky = W)

entry_fleetpercopt1 = Entry(option1_frame).grid(row = 3,column = 2)
entry_fleetpremopt1 = Entry(option1_frame).grid(row = 3,column = 1)
entry_losspercopt1 = Entry(option1_frame).grid(row = 4,column = 2)
entry_losspremopt1 = Entry(option1_frame).grid(row = 4,column = 1)

clicked_typerating = StringVar(option1_frame)
clicked_typerating.set('No')
menu_type = OptionMenu(option1_frame, clicked_typerating,'Up','Down')
menu_type.grid(row = 1,column = 1)

clicked_typerating = StringVar(option1_frame)
clicked_typerating.set('No')
menu_type = OptionMenu(option1_frame, clicked_typerating,'No','Yes')
menu_type.grid(row = 1,column = 1)





button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()
