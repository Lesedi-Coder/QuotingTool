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
lk = "C:/Users/LesediM/Documents/LombardProjects/"
image = lk + "Project2/Tool/QuotingTool/MA.png"

 
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


pol_frame = Frame(policyinfo_frame)
fleet_frame = Frame(policyinfo_frame)
cover_frame = Frame(policyinfo_frame)
specified_frame =Frame(policyinfo_frame)

pol_frame.grid(row = 0,column = 0,sticky = 'W')
fleet_frame.grid(row = 1,column = 0,sticky = 'W')
cover_frame.grid(row = 2,column = 0,sticky = 'W')
specified_frame.grid(row = 3,column = 0,sticky = 'W')



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

# my_img = ImageTk.PhotoImage(Image.open("C:/Users/LesediM/Documents/LombardProjects/Project2/Tool/QuotingTool/MA.png"))
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

user_f12 = IntVar(pol_frame)
user_f22 = IntVar(pol_frame)
user_f32 = IntVar(pol_frame)
user_f42 = IntVar(pol_frame)
user_f52 = IntVar(pol_frame)
user_f62 = IntVar(pol_frame)
user_f72 = IntVar(pol_frame)
user_f82 = IntVar(pol_frame)

user_f13 = IntVar(pol_frame)
user_f23 = IntVar(pol_frame)
user_f33 = IntVar(pol_frame)
user_f43 = IntVar(pol_frame)
user_f53 = IntVar(pol_frame)
user_f63 = IntVar(pol_frame)
user_f73 = IntVar(pol_frame)
user_f83 = IntVar(pol_frame)

user_f15 = DoubleVar(pol_frame)
user_f25 = DoubleVar(pol_frame)
user_f35 = DoubleVar(pol_frame)
user_f45 = DoubleVar(pol_frame)
user_f55 = DoubleVar(pol_frame)
user_f65 = DoubleVar(pol_frame)
user_f75 = DoubleVar(pol_frame)
user_f85 = DoubleVar(pol_frame)

select = 'Select Option                       '
cars = 'Cars(Primary use: Domestic/private)'
ldv ='LDV(Commercial use)'
taxis = 'Taxis(7-24)'
motors= 'Motors Traders'
busses = 'Busses'
mobile = 'Mobile Plant'
brt = 'BRT'
heavy = 'Heavy Commercial Vehicles(>3,500kg)'
# ------------------Specified Entries-------------------
user_s13 = IntVar(specified_frame)
user_s23 = IntVar(specified_frame)
user_s33 = IntVar(specified_frame)
user_s43 = IntVar(specified_frame)
user_s53 = IntVar(specified_frame)
user_s63 = IntVar(specified_frame)
user_s73 = IntVar(specified_frame)
user_s83 = IntVar(specified_frame)
user_s93 = IntVar(specified_frame)
user_s103 = IntVar(specified_frame)


user_s14 = IntVar(specified_frame)
user_s24 = IntVar(specified_frame)
user_s34 = IntVar(specified_frame)
user_s44 = IntVar(specified_frame)
user_s54 = IntVar(specified_frame)
user_s64 = IntVar(specified_frame)
user_s74 = IntVar(specified_frame)
user_s84 = IntVar(specified_frame)
user_s94 = IntVar(specified_frame)
user_s104 = IntVar(specified_frame)

perc4 = 0.00868
perc5 = 0.504
perc6 = 0.0363
perc8 = 0.01879


minann1 = 20.18
minann2 = 45.39
minann3 = 45.39
minann4 = 100
minann5 = 2000
minann6 = 200
minann7 = 45.39
minann8 = 54.47

minmon1 = 2.02
minmon2 = 4.54
minmon3 = 4.54
minmon4 = 5.45
minmon5 = 200
minmon6 = 20
minmon7 = 4.54
minmon8 = 5.45

#------------------Cover Entries---------------------
user_c11 = IntVar(cover_frame)
user_c13 = StringVar(cover_frame)
user_c14 = StringVar(cover_frame)
user_c15 = StringVar(cover_frame)
user_c16 = StringVar(cover_frame)
user_c17 = StringVar(cover_frame)
user_c18 = StringVar(cover_frame)
def tot_fleet():
	total = user_f12.get() + user_f22.get() + \
			user_f32.get() + user_f42.get() + \
			user_f52.get() + user_f62.get() + \
			user_f72.get() + user_f82.get() 

	return total		
def ann_claims(v1,v2):
	return int((v1*12)/(12-v2))

def numofmonths(text,value):
	text.configure(state = NORMAL)
	text.delete(1.0,END)
	text.insert(END,f"{value}")
	text.configure(state = DISABLED)

def rating():
	final =tot_fleet()
	insert_all(txt_fleetvalue,number_format(final))
	diff = round((e_periodfrom.get_date() - e_dateofquote.get_date()).days/30)
	numofmonths(entry_numofmonths,diff)
	annual = ann_claims(user_totalclaims.get(),diff)
	display_ann = number_format(annual)
	insert_all(entry_annclaims,display_ann)
def option1():
	tfleet = tot_fleet()
	fleet_prem = multiply(tfleet,user_percopt1.get())
	diff = round((e_periodfrom.get_date() - e_dateofquote.get_date()).days/30)
	display_fleetprem =number_format(fleet_prem)
	insert_all(entry_fleetpremopt1,display_fleetprem)

	annual = ann_claims(user_totalclaims.get(),diff)
	ratio_prem = divide(annual,user_lossopt1.get())
	display_ratioprem = number_format(ratio_prem)
	insert_all(entry_losspremcopt1,display_ratioprem)

	prem_onquote = round_off(clicked_roundopt1.get(),
							 clicked_typerating.get(),
							 fleet_prem)
	prem_onquote = number_format(prem_onquote)
	insert_all(entry_premopt1,prem_onquote)
def option2(): 
	if(clicked_overopt1.get()=="No"):
		if((type(user_premloading.get()) is not int) or
		   (type(user_depositsplit.get()) is not  int) or 
		   (type(user_burner1split.get()) is not int)or 
		   (type(user_burner2split.get()) is not int)):
			messagebox.showwarning('Type Error',
			                       'One of option 2 percentages '        
			                       'is not of the required type. '
			                       'Please enter percentage as a number.')		
		else:
			
			if((user_depositsplit.get() +
				user_burner1split.get() + 
				user_burner2split.get() != 100)):
				messagebox.showwarning('Percentage Error',
			                       'Percentages do not add up '
			                       'to 100%')
			else:

				tfleet = tot_fleet()
				fprem = multiply(tfleet,user_percopt1.get())
				prem  = round_off(clicked_roundopt1.get(),
								 clicked_typerating.get(),
								 fprem)				
			
				prem = total_prem(prem,user_premloading.get())

				prem_onquote = number_format(prem)					 	
				insert_all(entry_totalpremopt2,prem_onquote)		


				depo_prem = multiply(prem,user_depositsplit.get())
				depo_prem = number_format(depo_prem)
				insert_all(entry_depositpremopt2,depo_prem)

				burner1 = multiply(prem,user_burner1split.get())
				burner1 = number_format(burner1)
				insert_all(entry_burner1premopt2,burner1)

				burner2 = multiply(prem,user_burner2split.get())
				burner2 = number_format(burner2)
				insert_all(entry_burner2premopt2,burner2)		 	  

	else:
		if((type(user_premloading.get()) is not int) or
		   (type(user_depositsplit.get()) is not int) or 
		   (type(user_burner1split.get()) is not int )or 
		   type(user_burner2split.get()) is not int):
			messagebox.showwarning('Type Error',
			                      'One of option 2 percentages '
			                       'is not of the required type.'
			                       'Please enter percentage as a number.')
		else:		                       			
			fleet_prem = entry_prem2opt1.get()
			prem_onquote = number_format(fleet_prem)					 	
			insert_all(entry_totalpremopt2,prem_onquote)	
			if((user_depositsplit.get() +
				user_burner1split.get() + 
				user_burner2split.get() != 100)):
				messagebox.showwarning('Percentage Error',
			                       'Percentages do not add up '
			                       'to 100%')
			else:
				
				depo_prem = multiply(fleet_prem,user_depositsplit.get())
				depo_prem = number_format(depo_prem)
				insert_all(entry_depositsplitopt2,depo_prem)

				burner1 = multiply(fleet_prem,user_burner1split.get())
				burner1 = number_format(burner1)
				insert_all(entry_burner1splitopt2,burner1)

				burner2 = multiply(fleet_prem,user_burner2split.get())
				burner2 = number_format(burner2)
				insert_all(entry_burner2splitopt2,burner2)

def option3():
	diff = round((e_periodfrom.get_date() - e_dateofquote.get_date()).days/30)
	numofmonths(entry_numofmonthsopt3,diff)	

	annual = ann_claims(user_claimspaidopt3.get(),diff)
	display_ann = number_format(annual)
	insert_all(entry_annclaimsopt3,display_ann)

	if(user_premrateopt3.get()==0):
		messagebox.showwarning('Division Error',
			                      'Premium based on loss ratio '
			                       'cannot be zero. '
			                       'Percentage value has to be greater than zero.')	

	if(user_premrateopt3.get()!=0):
		claims_paid = ann_claims(user_totalclaims.get(),diff)
		prem1 =loss_ratio(claims_paid,
						  user_annualaggopt3.get(),
						  user_premrateopt3.get())

		if(prem1 < 0):			
			f_prem1 = number_format(abs(prem1))
			insert_negative(entry_ratiopremopt3,f_prem1)
		else:
			f_prem1 = number_format(prem1)
			insert_all(entry_ratiopremopt3,f_prem1)
	if(user_limitrateopt3.get()==0):
		messagebox.showwarning('Division Error',
			                      'Premium based on claims above stop loss limit '
			                       'cannot be zero. '
			                       'Percentage value has to be greater than zero.')		 		
	if(user_limitrateopt3.get() !=0):
		prem2 = divide(annual,user_limitrateopt3.get())
		f_prem2 = number_format(prem2)
		insert_all(entry_limitpremopt3,f_prem2)
		rnd = round_off(clicked_roundopt3.get(),clicked_nearestopt3.get(),prem2)
		rnd = number_format(rnd)
		insert_all(entry_premonquoteopt3,rnd)

def option4():
	diff = round((e_periodfrom.get_date() - e_dateofquote.get_date()).days/30)
	numofmonths(entry_numofmonthsopt4,diff)	
	annual = ann_claims(user_claimspaidopt4.get(),diff)
	display_ann = number_format(annual)
	insert_all(entry_annclaimsopt4,display_ann)

	if(user_premrateopt4.get()==0):
		messagebox.showwarning('Division Error',
			                      'Premium based on loss ratio '
			                       'cannot be zero. '
			                       'Percentage value has to be greater than zero.')	
	elif(user_limitrateopt4.get()==0):
		messagebox.showwarning('Division Error',
			                      'Premium based on claims above stop loss limit '
			                       'cannot be zero. '
			                       'Percentage value has to be greater than zero.')		
	else:
		if(user_premrateopt4.get()!=0):
			claims_paid = ann_claims(user_totalclaims.get(),diff)
			prem1 =loss_ratio(claims_paid,
							  user_annualaggopt4.get(),
							  user_premrateopt4.get())

			if(prem1 < 0):			
				f_prem1 = number_format(abs(prem1))
				insert_negative(entry_ratiopremopt4,f_prem1)
			else:
				f_prem1 = number_format(prem1)
				insert_all(entry_ratiopremopt4,f_prem1)
			 		
		if(user_limitrateopt4.get() !=0):
			prem2 = divide(annual,user_limitrateopt4.get())
			f_prem2 = number_format(prem2)
			insert_all(entry_limitpremopt4,f_prem2)
			rnd = round_off(clicked_roundopt4.get(),clicked_nearestopt4.get(),prem2)
			f_rnd = number_format(rnd)
			insert_all(entry_aggpremeopt4,f_rnd)




				
			if((user_depositsplitopt4.get() +
				user_burner1splitopt4.get() + 
				user_burner2splitopt4.get() != 100)):
				messagebox.showwarning('Percentage Error',
				                       'Percentages do not add up '
				                       'to 100%')
			else:

				tfleet = tot_fleet()
				fprem = multiply(tfleet,user_percopt1.get())
				prem  = round_off(clicked_roundopt4.get(),
								 clicked_nearestopt4.get(),
								 fprem)				
		
				prem = total_prem(rnd,user_premloadingopt4.get())

				agg_prem = number_format(prem)					 	
				insert_all(entry_premtotopt4,agg_prem)		


				depo_prem = multiply(prem,user_depositsplitopt4.get())
				depo_prem = number_format(depo_prem)
				insert_all(entry_depositpremopt4,depo_prem)

				burner1 = multiply(prem,user_burner1splitopt4.get())
				burner1 = number_format(burner1)
				insert_all(entry_burner1premopt4,burner1)

				burner2 = multiply(prem,user_burner2splitopt4.get())
				burner2 = number_format(burner2)
				insert_all(entry_burner2premopt4,burner2)		 	  
	
			
			
def loss_ratio(v1,v2,v3):
	return round((v1-v2)*(100/v3))
def insert_negative(text,value):
	text.configure(state = NORMAL)
	text.delete(1.0,END)
	text.insert(END,f"-R{value}")
	text.configure(state = DISABLED)			 	  

def total_prem(fleet,perc):
	total = fleet *(1+(perc/100))			
	return int(total)

def multiply(v1,v2):
	return int(v1 *(v2/100))

def divide(v1,v2):
	return int(v1 *(100/v2))

def round_off(state,nearest,value):
	if(state == "Up"):
		if(nearest =='R1 000'):
			value =(value - (value % 1000)) + 1000
		if(nearest =='R10 000'):
			value =(value - (value % 10000)) + 10000
		if(nearest =='R100 000'):
			value =(value - (value % 100000)) + 100000
	else:
		if(nearest =='R1 000'):
			value =value - (value % 1000)
		if(nearest =='R10 000'):
			value =value- (value % 10000)
		if(nearest =='R100 000'):
			value =value - (value % 100000)																																																																
	return int(value)



def number_format(v):
	value = str(v)
	final = ""
	if(len(value) == 1 or 
	   len(value) == 2 or
	   len(value) == 3 ):
		final = value
	if(len(value)==4):
		final = value[0] + ' '+ value[1:]
	if(len(value)==5):
		final = value[0:2] + ' '+ value[2:]	
	if(len(value)==6):
		final = value[0:3] + ' '+ value[3:]		
	if(len(value)==7):
		final = value[0] + ' '+ value[1:4] + ' ' + value[4:]	
	if(len(value)==8):
		final = value[0:2] + ' '+ value[2:5] + ' ' + value[5:]	
	if(len(value)==9):
		final = value[0:3] + ' '+ value[3:6] + ' ' + value[6:]								
	if(len(value)==10):
		final = value[0] + \
		        ' ' + value[1:4] +\
		        ' ' + value[4:7] + \
		        ' ' + value[7:] 
	if(len(value)==11):
		final = value[0:2] + \
		        ' ' + value[2:5] + \
		        ' ' + value[5:8] + \
		        ' ' + value[8:]
	if(len(value)==11):
		final = value[0:3] + \
		        ' ' + value[3:6] + \
		        ' ' + value[6:9] + \
		        ' ' + value[9:]	
	if(len(value)==12):
		final = value[0:3] + \
		        ' ' + value[3:6] + \
		        ' ' + value[6:9] + \
		        ' ' + value[9:]	
	return final	        

def insert_all(text,value):
	text.configure(state = NORMAL)
	text.delete(1.0,END)
	text.insert(END,f"R{value}")
	text.configure(state = DISABLED)

def add_spec():

	M1 = 0.0
	M2 = 0.0
	M3 = 0.0
	M4 = 0.0
	M5 = 0.0
	M6 = 0.0 
	M7 = 0.0
	M8 = 0.0
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
	annprem_s65 = ((user_s63.get()
		           *user_s64.get())/100)
	annprem_s75 = ((user_s73.get()
		           *user_s74.get())/100)
	annprem_s85 = ((user_s83.get()
		           *user_s84.get())/100)
	annprem_s95 = ((user_s93.get()
		           *user_s94.get())/100)
	annprem_s105 = ((user_s103.get()
		           *user_s104.get())/100)		           		           		           		           		           		           	
	total_annprem = (annprem_s15 +
		             annprem_s25 +
		             annprem_s35 + 
	                 annprem_s45 +
	                 annprem_s55 +
	                 annprem_s65 +
	                 annprem_s75 +
	                 annprem_s85 +
	                 annprem_s95 +
	                 annprem_s105 

	                 )
	                 

	if(clicked_poltype.get()=="Annual"):
		#----------Row 1------------
		if(clicked_cat1.get()== select):
			pass
		else:
			if(clicked_cat1.get()== cars):
				M1  = minann1
				insert_all(txt_spec16,M1)			
			if(clicked_cat1.get()== ldv):
				M2 = minann2
				insert_all(txt_spec16,M2)
			if(clicked_cat1.get()== taxis):
				M3 = minann3
				insert_all(txt_spec16,M3)
			if(clicked_cat1.get()== motors):
				if((user_s13.get()*perc4)/100 < minann1):
					M4 = minann4
					insert_all(txt_spec16,M4)
				else:
					M4 = (user_s13.get()*perc4/100)
					insert_all(txt_spec16,M4)
			if(user_s13.get()== busses):
				if((user_s13.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec16,M5)
				else:
					M5 = (user_s13.get()*perc5)/100
					insert_all(txt_spec16,M5)
			if(user_s13.get()== mobile):
				if((user_s13.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec16,M6)
				else:
					M6 = (user_s13.get()*perc6)/100
					insert_all(txt_spec16,M6)
			if(clicked_cat1.get()== brt):
				M7 = minann7
				insert_all(txt_spec16,M7)
			if(clicked_cat1.get()== heavy):
				if((user_s13.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec16,M8)
				else:
					M8 = (user_s13.get()*perc8)/100 
					insert_all(txt_spec16,M8)		

		#----------Row 2------------
		if(clicked_cat2.get()== select):
			pass
		else:
			if(clicked_cat2.get()== cars):
				M1  = minann1
				insert_all(txt_spec26,M1)			
			if(clicked_cat2.get()== ldv):
				M2 = minann2
				insert_all(txt_spec26,M2)	
			if(clicked_cat2.get()== taxis):
				M3 = minann3
				insert_all(txt_spec26,M3)	
			if(clicked_cat2.get()== motors):
				if((user_s23.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec26,M4)	
				else:
					M4 = (user_s23.get()*perc5)/100
					insert_all(txt_spec26,M4)	
			if(clicked_cat2.get()== busses):
				if((user_s23.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec26,M5)	
				else:
					M5 = (user_s23.get()*perc5)/100
					insert_all(txt_spec26,M5)	
			if(clicked_cat2.get()== mobile):
				if((user_s23.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec26,M6)	
				else:
					M6 = (user_s23.get()*perc6)/100
					insert_all(txt_spec26,M6)	
			if(clicked_cat2.get()== brt):
				M7 = minann7
				insert_all(txt_spec26,M7)	
			if(clicked_cat2.get()== heavy):
				if((user_s23.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec26,M8)	
				else:
					M8 = (user_s23.get()*perc8)/100


		#----------Row 3------------
		if(clicked_cat3.get()== select):
			pass
		else:
			if(clicked_cat3.get()== cars):
				M1  = minann1
				insert_all(txt_spec36,M1)				
			if(clicked_cat3.get()== ldv):
				M2 = minann2
				insert_all(txt_spec36,M2)
			if(clicked_cat3.get()== taxis):
				M3 = minann3
				insert_all(txt_spec36,M3)
			if(clicked_cat3.get()== motors):
				if((user_s33.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec36,M4)
				else:
					M4 = (user_s33.get()*perc4)/100
					insert_all(txt_spec36,M4)
			if(clicked_cat3.get()== busses):
				if((user_s33.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec36,M5)
				else:
					M5 = (user_s33.get()*perc5)/100
					insert_all(txt_spec36,M5)
			if(clicked_cat3.get()== mobile):
				if((user_s33.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec36,M6)
				else:
					M6 = (user_s33.get()*perc6)/100
					insert_all(txt_spec36,M6)
			if(clicked_cat3.get()== brt):
				M7 = minann7
				insert_all(txt_spec36,M7)
			if(clicked_cat3.get()== heavy):
				if((user_s13.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec36,M8)
				else:
					M8 = (user_s33.get()*perc8)/100 
					insert_all(txt_spec36,M8)	

		#----------Row '4------------
		if(clicked_cat4.get()== select):
			pass
		else:
			if(clicked_cat4.get()== cars):
				M1  = minann1
				insert_all(txt_spec46,M1)		
			if(clicked_cat4.get()== ldv):
				M2 = minann2
				insert_all(txt_spec46,M2)
			if(clicked_cat4.get()== taxis):
				M3 = minann2
				insert_all(txt_spec46,M3)
			if(clicked_cat4.get()== motors):
				if((user_s43.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec46,M4)
				else:
					M4 = (user_s43.get()*perc4)/100
					insert_all(txt_spec46,M4)
			if(clicked_cat4.get()== busses):
				if((user_s43.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec46,M5)
				else:
					M5 = (user_s43.get()*perc5)/100
					insert_all(txt_spec46,M5)
			if(clicked_cat4.get()== mobile):
				if((user_s43.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec46,M6)
				else:
					M6 = (user_s43.get()*perc6)/100
					insert_all(txt_spec46,M6)
			if(clicked_cat4.get()== brt):
				M7 = minann7
				insert_all(txt_spec46,M7)
			if(clicked_cat4.get()== heavy):
				if((user_s43.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec46,M4)
				else:
					M8 = (user_s43.get()*perc8)/100
					insert_all(txt_spec46,M8) 						
				
		#----------Row 5------------
		if(clicked_cat5.get()== select):
			pass
		else:
			if(clicked_cat5.get()== cars):
				M1  = minann1			
			if(clicked_cat5.get()== ldv):
				M2 = minann2
			if(clicked_cat5.get()== taxis):
				M3 = minann3
				insert_all(txt_spec56,M3)
			if(clicked_cat5.get()== motors):
				if((user_s53.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec56,M4)
				else:
					M4 = (user_s53.get()*perc4)/100
					insert_all(txt_spec56,M4)
			if(clicked_cat5.get()== busses):
				if((user_s53.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec56,M5)
				else:
					M5 = (user_s33.get()*perc5)/100
					insert_all(txt_spec56,M5)
			if(clicked_cat5.get()== mobile):
				if((user_s53.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec56,M6)
				else:
					M6 = (user_s53.get()*perc6)/100
			if(clicked_cat5.get()== brt):
				M7 = minann7
				insert_all(txt_spec56,M7)
			if(clicked_cat5.get()== heavy):
				if((user_s53.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec56,M8)
				else:
					M8 = (user_s53.get()*perc8)/100
					insert_all(txt_spec56,M8)	

		#----------Row 6------------
		if(clicked_cat6.get()== select):
			pass
		else:
			if(clicked_cat6.get()== cars):
				M1  = minann1
				insert_all(txt_spec66,M1)			
			if(clicked_cat6.get()== ldv):
				M2 = minann2
				insert_all(txt_spec66,M2)
			if(clicked_cat6.get()== taxis):
				M3 = minann3
				insert_all(txt_spec66,M3)
			if(clicked_cat6.get()== motors):
				if((user_s63.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec66,M4)
				else:
					M4 = (user_s63.get()*perc4)/100
					insert_all(txt_spec66,M4)
			if(clicked_cat6.get()== busses):
				if((user_s63.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec66,M5)
				else:
					M5 = (user_s63.get()*perc5)/100
					insert_all(txt_spec66,M5)
			if(clicked_cat6.get()== mobile):
				if((user_s63.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec66,M6)
				else:
					M6 = (user_s63.get()*perc6)/100
					insert_all(txt_spec66,M6)
			if(clicked_cat6.get()== brt):
				M7 = minann7
				insert_all(txt_spec66,M7)
			if(clicked_cat6.get()== heavy):
				if((user_s63.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec66,M8)
				else:
					M8 = (user_s63.get()*perc8)/100
					insert_all(txt_spec66,M8)		

		#----------Row 7------------
		if(clicked_cat7.get()== select):
			pass
		else:
			if(clicked_cat7.get()== cars):
				M1  = minann1
				insert_all(txt_spec66,M1)		
			if(clicked_cat7.get()== ldv):
				M2 = minann2
				insert_all(txt_spec76,M2)
			if(clicked_cat7.get()== taxis):
				M3 = minann3
				insert_all(txt_spec76,M3)
			if(clicked_cat7.get()== motors):
				if((user_s73.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec76,M4)
				else:
					M4 = (user_s73.get()*perc4)/100
					insert_all(txt_spec76,M4)
			if(clicked_cat7.get()== busses):
				if((user_s73.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec76,M5)
				else:
					M5 = (user_s73.get()*perc5)/100
					insert_all(txt_spec76,M5)
			if(clicked_cat7.get()== mobile):
				if((user_s73.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec76,M6)
				else:
					M6 = (user_s73.get()*perc6)/100
					insert_all(txt_spec76,M6)
			if(clicked_cat7.get()== brt):
				M7 = minann7
			if(clicked_cat7.get()== heavy):
				if((user_s73.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec76,M8)
				else:
					M8 = (user_s73.get()*perc8)/100
					insert_all(txt_spec76,M8) 


			if(clicked_cat7.get()== heavy):
					M8 = (user_s73.get()*perc8)/100 
					insert_all(txt_spec76,M8)	

		#----------Row 8------------
		if(clicked_cat8.get()== select):
			pass		
		else:
			if(clicked_cat8.get()== cars):
				M1  = minann1
				insert_all(txt_spec86,M1)		
			if(clicked_cat8.get()== ldv):
				M2 = minann2
				insert_all(txt_spec86,M2)
			if(clicked_cat8.get()== taxis):
				M3 = minann3
				insert_all(txt_spec86,M3)
			if(clicked_cat7.get()== motors):
				if((user_s83.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec86,M4)
				else:
					M4 = (user_s83.get()*perc4)/100
					insert_all(txt_spec86,M4)
			if(clicked_cat8.get()== busses):
				if((user_s83.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec86,M5)
				else:
					M5 = (user_s83.get()*perc5)/100
					insert_all(txt_spec86,M6)
			if(user_s73.get()== mobile):
				if((user_s83.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec86,M6)
				else:
					M6 = (user_s83.get()*perc6)/100
					insert_all(txt_spec86,M6)
			if(clicked_cat8.get()== brt):
				M7 = minann8
				insert_all(txt_spec86,M7)		

			if((user_s83.get()*perc7)/100  < minann7):
				M8 = minann7
				insert_all(txt_spec86,M8)
			else:
				M8 = (user_s83.get()*perc8)/100 
				insert_all(txt_spec86,M8)


		#----------Row 9------------
		if(clicked_cat9.get()== select):
			pass
		else:
			if(clicked_cat9.get()== cars):
				M1  = minann1
				insert_all(txt_spec96,M1)		
			if(clicked_cat9.get()== ldv):
				M2 = minann2
				insert_all(txt_spec96,M2)
			if(clicked_cat9.get()== taxis):
				M3 = minann3
				insert_all(txt_spec96,M3)
			if(clicked_cat9.get()== motors):
				if((user_s93.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec96,M4)
				else:
					M4 = (user_s93.get()*perc4)/100
					insert_all(txt_spec96,M4)
			if(clicked_cat9.get()== busses):
				if((user_s93.get()*perc)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec96,M5)
				else:
					M5 = (user_s93.get()*perc5)/100
					insert_all(txt_spec96,M5)
			if(clicked_cat9.get()== mobile):
				if((user_s93.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec96,M6)
				else:
					M6 = (user_s93.get()*perc6)/100
					insert_all(txt_spec96,M6)
			if(clicked_cat3.get()== brt):
				M7 = minann7
				insert_all(txt_spec96,M7)
			if(clicked_cat9.get()== heavy):
				if((user_s93.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec96,M8)
				else:
					M8 = (user_s93.get()*perc8)/100 
					insert_all(txt_spec96,M8)	

		#----------Row 10------------
		if(clicked_cat10.get()== select):
			pass
		else:
			if(clicked_cat10.get()== cars):
				M1  = minann1
				insert_all(txt_spec106,M1)		
			if(clicked_cat10.get()== ldv):
				M2 = minann2
				insert_all(txt_spec106,M2)
			if(clicked_cat10.get()== taxis):
				M3 = minann3
				insert_all(txt_spec106,M3)
			if(clicked_cat10.get()== motors):
				if((user_s33.get()*perc4)/100 < minann4):
					M4 = minann4
					insert_all(txt_spec106,M4)
				else:
					M4 = (user_s103.get()*perc4)/100
					insert_all(txt_spec106,M4)
			if(clicked_cat10.get()== busses):
				if((user_s103.get()*perc5)/100 < minann5):
					M5 = minann5
					insert_all(txt_spec106,M5)
				else:
					M5 = (user_s103.get()*perc5)/100
					insert_all(txt_spec106,M5)
			if(clicked_cat103.get()== mobile):
				if((user_s103.get()*perc6)/100  < minann6):
					M6 = minann6
					insert_all(txt_spec106,M6)
				else:
					M6 = (user_s103.get()*perc6)/100
					insert_all(txt_spec106,M6)
			if(clicked_cat10.get()== brt):
				M7 = minann7
				insert_all(txt_spec106,M7)
			if(clicked_cat10.get()== heavy):
				if((user_s103.get()*perc8)/100  < minann8):
					M8 = minann8
					insert_all(txt_spec106,M8)
				else:
					M8 = (user_s103.get()*perc8)/100
					insert_all(txt_spec106,M8) 																



	if (clicked_poltype.get() =="Monthly"):
		#----------Row 1------------
		if(clicked_cat1.get()== select):
			pass
		else:
			if(clicked_cat1.get()== cars):
				M1  = minmon1
				insert_all(txt_spec16,M1)			
			if(clicked_cat1.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec16,M2)
			if(clicked_cat1.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec16,M3)
			if(clicked_cat1.get()== motors):
				if((user_s13.get()*perc4)/10 < minmon4):
					M4 = minmon4
					insert_all(txt_spec16,M4)
				else:
					M4 = (user_s13.get()*perc4)/100
			if(user_s13.get()== busses):
				if((user_s13.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec16,M5)
				else:
					M5 = (user_s13.get()*perc5)/100
					insert_all(txt_spec16,M5)
			if(user_s13.get()== mobile):
				if((user_s13.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec16,M6)
				else:
					M6 = (user_s13.get()*perc6)/100
					insert_all(txt_spec16,M6)
			if(clicked_cat1.get()== brt):
				M7 = minmon7
				insert_all(txt_spec15,M7)
			if(clicked_cat1.get()== heavy):
				if((user_s13.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec16,M8)
				else:
					M8 = (user_s13.get()*perc8)/100
					insert_all(txt_spec16,M8) 		

		#----------Row 2------------
		if(clicked_cat2.get()== select):
			pass 
		else:
			if(clicked_cat2.get()== cars):
				M1  = minmon1
				insert_all(txt_spec15,txt_spec26,M1) 		
			if(clicked_cat2.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec26,M2) 
			if(clicked_cat2.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec26,M3)
			if(clicked_cat2.get()== motors):
				if((user_s23.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec26,M4)
				else:
					M4 = (user_s23.get()*perc5)/100
					insert_all(txt_spec26,M4)
			if(clicked_cat2.get()== busses):
				if((user_s23.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec26,M5)
				else:
					M5 = (user_s23.get()*perc5)/100
					insert_all(txt_spec26,M5)
			if(clicked_cat2.get()== mobile):
				if((user_s23.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec26,M6)
				else:
					M6 = (user_s23.get()*perc6)/100
					insert_all(txt_spec26,M6)
			if(clicked_cat2.get()== brt):
				M7 = minmon7
				insert_all(txt_spec26,M7)
			if(clicked_cat2.get()== heavy):
				if((user_s23.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec26,M8)
				else:
					M8 = (user_s23.get()*perc8)/100 
					insert_all(txt_spec26,M8)	

		#----------Row 3------------
		if(clicked_cat3.get()== select):
			pass
		else:
			if(clicked_cat3.get()== cars):
				M1  = minmon1
				insert_all(txt_spec36,M1)			
			if(clicked_cat3.get()== lv):
				M2 =minmon2
				insert_all(txt_spec36,M2)
			if(clicked_cat3.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec36,M3)
			if(clicked_cat3.get()== motors):
				if((user_s33.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec36,M4)
				else:
					M4 = (user_s33.get()*perc4)/100
					insert_all(txt_spec36,M4)
			if(clicked_cat3.get()== busses):
				if((user_s33.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec36,M5)
				else:
					M5 = (user_s33.get()*pec5)/100
					insert_all(txt_spec36,M5)
			if(clicked_cat3.get()== mobile):
				if((user_s33.get()*perc6)/100  < 200):
					M6 = minmon6
					insert_all(txt_spec36,M6)
				else:
					M6 = (user_s33.get()*perc6)/100
					insert_all(txt_spec36,M6)
			if(clicked_cat3.get()== brt):
				M7 = minmon7
				insert_all(txt_spec36,M7)
			if(clicked_cat3.get()== heavy):
				if((user_s13.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec36,M8)
				else:
					M8 = (user_s33.get()*perc8)/100
					insert_all(txt_spec36,M8)


		#----------Row '4------------
		if(clicked_cat4.get()== select):
			pass
		else:
			if(clicked_cat4.get()== cars):
				M1  = minmon1
				insert_all(txt_spec46,M1)		
			if(clicked_cat4.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec46,M2)
			if(clicked_cat4.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec46,M3)
			if(clicked_cat4.get()== motors):
				if((user_s43.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec46,M4)
				else:
					M4 = (user_s43.get()*perc4)/100
					insert_all(txt_spec46,M4)
			if(clicked_cat4.get()== busses):
				if((user_s43.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec46,M5)
				else:
					M5 = (user_s43.get()*perc5)/100
					insert_all(txt_spec46,M5)
			if(clicked_cat4.get()== mobile):
				if((user_s43.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec46,M6)
				else:
					M6 = (user_s43.get()*perc6)/100
					insert_all(txt_spec46,M6)
			if(clicked_cat4.get()== brt):
				M7 = minmon7
				insert_all(txt_spec46,M7)
			if(clicked_cat4.get()== heavy):
				if((user_s43.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec46,M8)
				else:
					M8 = (user_s43.get()*perc8)/100 
					insert_all(txt_spec46,M8)						
				
		#----------Row 5------------
		if(clicked_cat5.get()== select):
			pass
		else:
			if(clicked_cat5.get()== cars):
				M1  = minmon1
				insert_all(txt_spec56,M1)		
			if(clicked_cat5.get()== ldv):
				M2 = mimon2
				insert_all(txt_spec56,M2)
			if(clicked_cat5.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec56,M3)
			if(clicked_cat5.get()== motors):
				if((user_s53.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec56,M4)
				else:
					M4 = (user_s53.get()*perc4)/100
					insert_all(txt_spec56,M4)
			if(clicked_cat5.get()== busses):
				if((user_s53.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec56,M5)
				else:
					M5 = (user_s53.get()*perc5)/100
					insert_all(txt_spec56,M5)
			if(clicked_cat5.get()== mobile):
				if((user_s53.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec56,M6)
				else:
					M6 = (user_s53.get()*perc6)/100
					insert_all(txt_spec56,M6)
			if(clicked_cat5.get()== brt):
				M7 = minmon7
				insert_all(txt_spec56,M7)
			if(clicked_cat5.get()== heavy):
				if((user_s53.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec56,M8)
				else:
					M8 = (user_s53.get()*perc8)/100 
					insert_all(txt_spec56,M8)	

		#----------Row 6------------
		if(clicked_cat6.get()== select):
			pass
		else:
			if(clicked_cat6.get()== cars):
				M1  = minmon1
				insert_all(txt_spec66,M1)		
			if(clicked_cat6.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec66,M2)
			if(clicked_cat6.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec66,M3)
			if(clicked_cat6.get()== motors):
				if((user_s63.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec66,M4)
				else:
					M4 = (user_s63.get()*perc4)/100
					insert_all(txt_spec66,M4)
			if(clicked_cat6.get()== busses):
				if((user_s63.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec66,M5)
				else:
					M5 = (user_s63.get()*perc5)/100
					insert_all(txt_spec66,M5)
			if(clicked_cat6.get()== mobile):
				if((user_s63.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec66,M6)
				else:
					M6 = (user_s63.get()*perc6)/100
					insert_all(txt_spec66,M6)
			if(clicked_cat6.get()== brt):
				M7 = minmon7
				insert_all(txt_spec66,M7)
			if(clicked_cat6.get()== heavy):
				if((user_s63.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec66,M8)
				else:
					M8 = (user_s63.get()*perc8)/100 
					insert_all(txt_spec66,M8)		

		#----------Row 7------------
		if(clicked_cat7.get()== select):
			pass
		else:
			if(clicked_cat7.get()== cars):
				M1  = minmon1
				insert_all(txt_spec76,M1)		
			if(clicked_cat7.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec76,M2)
			if(clicked_cat7.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec76,M3)
			if(clicked_cat7.get()== motors):
				if((user_s73.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec76,M4)
				else:
					M4 = (user_s73.get()*perc4)/100
					insert_all(txt_spec76,M4)
			if(clicked_cat7.get()== busses):
				if((user_s73.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec76,M5)
				else:
					M5 = (user_s73.get()*perc5)/100
					insert_all(txt_spec76,M5)
			if(clicked_cat7.get()== mobile):
				if((user_s73.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec76,M6)
				else:
					M6 = (user_s73.get()*perc6)/100
					insert_all(txt_spec76,M6)
			if(clicked_cat7.get()== brt):
				M7 = minmon7
				insert_all(txt_spec76,M7)
			if(clicked_cat7.get()== heavy):
				if((user_s73.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec76,M8)
				else:
					M8 = (user_s73.get()*perc8)/100 
					insert_all(txt_spec76,M8)	

		#----------Row 8------------
		if(clicked_cat8.get()== select):
			pass
		else:
			if(clicked_cat8.get()== cars):
				M1  = minmon1
				insert_all(txt_spec86,M1)
			if(clicked_cat7.get()== ldv):
				M2 = minmon2	
				insert_all(txt_spec86,M2)		
			if(clicked_cat7.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec86,M3)
			if(clicked_cat8.get()== motors):
				if((user_s83.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec86,M4)
				else:
					M4 = (user_s83.get()*perc4)/100
					insert_all(txt_spec86,M4)
			if(clicked_cat8.get()== busses):
				if((user_s83.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec86,M5)
				else:
					M5 = (user_s83.get()*perc5)/100
					insert_all(txt_spec86,M5)
			if(clicked_cat8.get()== mobile):
				if((user_s83.get()*perc5)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec86,M6)
				else:
					M6 = (user_s83.get()*perc6)/100
					insert_all(txt_spec86,M6)
			if(clicked_cat8.get()== brt):
				M7 = minmon7
				insert_all(txt_spec86,M7)
			if(clicked_cat8.get()== heavy):
				if((user_s83.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec86,M8)
				else:
					M8 = (user_s83.get()*perc8)/100
					insert_all(txt_spec86,M8) 	

		#----------Row 9------------
		if(clicked_cat9.get()== select):
			pass
		else:
			if(clicked_cat9.get()== cars):
				M1  = minmon1
				insert_all(txt_spec96,M1)			
			if(clicked_cat9.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec96,M2)
			if(clicked_cat9.get()== taxis):
				insert_all(txt_spec96,M2)
				M3 = minmon3
			if(clicked_cat9.get()== motors):
				if((user_s93.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec96,M1)
				else:
					M4 = (user_s93.get()*perc4)/100
					insert_all(txt_spec96,M4)
			if(clicked_cat9.get()== busses):
				if((user_s93.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec96,M5)
				else:
					M5 = (user_s93.get()*perc5)/100
					insert_all(txt_spec96,M5)
			if(clicked_cat9.get()== mobile):
				if((user_s93.get()*perc6)/100  < minmon6):
					M6 = minmon6
					insert_all(txt_spec96,M6)
				else:
					M6 = (user_s93.get()*perc6)/100
					insert_all(txt_spec96,M6)
			if(clicked_cat3.get()== brt):
				M7 = minmon7
				insert_all(txt_spec96,M7)
			if(clicked_cat9.get()== heavy):
				if((user_s93.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec96,M8)
				else:
					M8 = (user_s93.get()*perc8)/100
					insert_all(txt_spec96,M8) 	

		#----------Row 10------------
		if(clicked_cat10.get()== select):
			pass
		else:
			if(clicked_cat10.get()== cars):
				M1  = minmon1
				insert_all(txt_spec106,M1)
			if(clicked_cat10.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec106,M2)
			if(clicked_cat10.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec106,M3)
			if(clicked_cat10.get()== motors):
				if((user_s33.get()*perc4)/100 < minmon4):
					M4 = minmon4
					insert_all(txt_spec106,M4)
				else:
					M4 = (user_s103.get()*perc4)/100
					insert_all(txt_spec106,M4)
			if(clicked_cat10.get()== busses):
				if((user_s103.get()*perc5)/100 < minmon5):
					M5 = minmon5
					insert_all(txt_spec106,M5)
				else:
					M5 = (user_s103.get()*perc5)/100
					insert_all(txt_spec106,M5)
			if(clicked_cat103.get()== mobile):
				if((user_s103.get()*perc6)/100  < minmon8):
					M6 = minmon6
					insert_all(txt_spec106,M6)
				else:
					M6 = (user_s103.get()*perc6)/100
					insert_all(txt_spec106,M6)
			if(clicked_cat10.get()== brt):
				M7 = minmon7
				insert_all(txt_spec106,M7)
			if(clicked_cat10.get()== heavy):
				if((user_s103.get()*perc8)/100  < minmon8):
					M8 = minmon8
					insert_all(txt_spec106,M8)
				else:
					M8 = (user_s103.get()*perc8)/100 
					insert_all(txt_spec106,M8)																

	R1 = M1 
	R2 = M2 
	R3 = M3 
	R4 = M4
	R5 = M5
	R6 = M6
	R7 = M7
	R8 = M8		
			
	


	if (clicked_cat1.get() == select):
		pass
	else:
		R1 = user_s13.get()*user_s14.get()/100
		insert_all(txt_spec15,R1)
	if (clicked_cat2.get() == select):
		pass
	else:
		R2 = user_s23.get()*user_s24.get()/100
		insert_all(txt_spec25,R2)

	if (clicked_cat3.get() == select):
		pass
	else:
		R3 = user_s33.get()*user_s34.get()/100
		insert_all(txt_spec35,R3)
	if (clicked_cat4.get() == select):
		pass
	else:
		R4 = user_s43.get()*user_s44.get()/100
		insert_all(txt_spec45,R4)
	if (clicked_cat5.get() == select):
		pass
	else:
		R5 = user_s53.get()*user_s54.get()/100
		insert_all(txt_spec55,R5)
	if (clicked_cat6.get() == select):
		pass
	else:
		R6 = user_s63.get()*user_s64.get()/100
		insert_all(txt_spec65,R6)
	if (clicked_cat7.get() == select):
		pass
	else:
		R7 = user_s73.get()*user_s74.get()/100
		insert_all(txt_spec75,R7)

	if (clicked_cat8.get() == select):
		pass
	else:
		R8 = user_s83.get()*user_s84.get()/100
		insert_all(txt_spec85,R8)
	if (clicked_cat9.get() == select):
		pass
	else:
		R9 = user_s93.get()*user_s94.get()/100
		insert_all(txt_spec95,R9)

	if (clicked_cat10.get() == select):
		pass
	else:
		R10 = user_s103.get()*user_s104.get()/100
		insert_all(txt_spec105,R10)														
             
def get_fleet():
	total_values = (user_f12.get()+
	                user_f22.get()+
	                user_f32.get()+
	                user_f42.get()+
	                user_f52.get()+
	                user_f62.get()+
	                user_f72.get()+
	                user_f82.get())	
	return total_values
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
	insert_all(txt_fleet92,number_format(total_values))
	insert_all(txt_fleetvalue,number_format(total_values))

	M1 = 0.0
	M2 = 0.0
	M3 = 0.0
	M4 = np.round((user_f42.get()*perc4)/100,2)
	M5 = np.round((user_f52.get()*perc5)/100,2)
	M6 = np.round((user_f62.get()*perc6)/100,2) 
	M7 = 0.0
	M8 = np.round((user_f82.get()*perc8)/100,2)



	if(clicked_poltype.get()=="Annual"):
		M1 = minann1
		M2 = minann2
		M3 = minann3
		if(user_f41.get()!=0 and user_f42.get() !=0):
			if (M4 < minann4):
				M4 = minann4
			else:
				pass
		if(user_f51.get()!=0 and user_f52.get() !=0):
			if(M5 < minann5 ):
				M5 = minann5
			else:
				pass
		if(user_f61.get()!=0 and user_f62.get() !=0):
			if(M6 <minann6):
				M6 = minann6 
			else:
				pass 
		if(user_f71.get()!=0 and user_f72.get() !=0):
			if(M7 <minann7):
				M7 = minann7
			else:
				pass 

		if(user_f81.get()!=0 and user_f82.get(S) !=0):
			if(M8 < minann8):
				M8 = minann8 
			else:
				pass

	if (clicked_poltype.get() =="Monthly"):
		M1  = minmon1
		M2 = minmon2
		M3 = minmon3
		if(user_f41.get()!=0 and user_f42.get() !=0):

			if (M4 < minmon4):
				M4 = minmon4
			else:
				pass
		if(user_f51.get()!=0 and user_f52.get() !=0):
			if(M5 < minmon5):
				M5 = minmon5
			else:
				pass
		if(user_f61.get()!=0 and user_f62.get() !=0):
			if(M6 < minmon6 ):
				M6 = minmon6 
			else:
				pass
		if(user_f71.get()!=0 and user_f72.get() !=0):
			if(M7 < minmon7 ):
				M7 = minmon7 
			else:
				pass
		if(user_f81.get()!=0 and user_f82.get() !=0):
			if(M8 < minmon8 ):
				M8 = minmon8 
			else:
				pass

	R1 = np.round(M1 *user_f11.get(),2)
	R2 = np.round(M2 * user_f21.get(),2)
	R3 = np.round(M3 *user_f31.get(),2)
	R4 = M4
	R5 = M5
	R6 = M6
	R7 = M7
	R8 = M8		
			
	insert_all(txt_fleet15,R1)
	insert_all(txt_fleet25,R2)
	insert_all(txt_fleet35,R3)
	insert_all(txt_fleet55,R5)
	insert_all(txt_fleet65,R6)
	insert_all(txt_fleet75,R7)
	insert_all(txt_fleet85,R8)


	if (total_values == "R0.0"):
		if(user_f41.get() == 0 and user_f42.get() ==0):
			R4 = 0
			insert_all(txt_fleet45,R4)
		else:
			insert_all(txt_fleet45,R4)

		if (user_f51.get() == 0 and user_f52.get() ==0):
			R5 = 0
			insert_all(txt_fleet45,R5)
		else:
			insert_all(txt_fleet45,R5)

		if (user_f61.get() == 0 and user_f62.get() ==0):
			R6 = 0
			insert_all(txt_fleet45,R6)
		else:
			insert_all(txt_fleet45,R6)

		if (user_f81.get() == 0 and user_f82.get() ==0):
			R8 = 0
			insert_all(txt_fleet45,R8)
		else:
			insert_all(txt_fleet45,R8)		

	else:
		insert_all(txt_fleet45,R4)
		insert_all(txt_fleet55,R5)
		insert_all(txt_fleet65,R6)
		insert_all(txt_fleet75,R7)
		insert_all(txt_fleet85,R8)


def validation():

	if (user_inputinsured.get() == "" or
	    user_inputpolno.get()==""):
		messagebox.showwarning('Missng Entries','Please enter missing entries')
	elif(clicked_type.get() == 'Select Option'):
			messagebox.showwarning('Tpye of quote','Please select the type of quote')

	elif(clicked_poltype.get() == 'Select Option'):
		messagebox.showwarning('Policy type','Please select the type of policy')			

	elif(e_policyinception.get_date() > e_periodfrom.get_date()):
		messagebox.showwarning('Date correlation',
			                   'Policy inception date cannot \
			                    be after starting period date. Please correct it')
	elif(e_periodfrom.get_date() > e_periodto.get_date()):
		messagebox.showwarning('Date correlation',
			                   'Starting period date cannot be after \
			                   the ending period date. Please correct it')
	elif(txt_fleet92.get('1.0','end') ==""):
		messagebox.showwarning('Missing Value',
		                       'Press total to calculate \
		                       the total fleet value.')	
	elif (user_inputpolno.get().isdigit()):
		pdf = FPDF()
		pdf.add_page()
		pdf.image(image, x=0, y=10, w=210, h=40)
		pdf.set_font('Arial','B',11)
		pdf.cell(300,40,' ',0,1,'L')
		pdf.cell(80,
			     8,
			     f"{label_type.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(40,
			     8,
			     f"{clicked_type.get()}",0,1,'L')

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_date.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{e_dateofquote.get_date()}",0,1,'L')		

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_insured.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{user_inputinsured.get()}",0,1,'L')

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_pol_no.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{e_policyno.get()}",0,1,'L')		

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_inception.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{e_policyinception.get_date()}",0,1,'L')

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     "Period Of Insurance:",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{e_periodfrom.get_date()}   to   {e_periodto.get_date()}",
			     0,1,'L')		

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_pol_type.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{clicked_poltype.get()}",0,1,'L')


		if(user_inputdesc.get()!=""):
			pdf.set_font('Arial','B',11)
			pdf.cell(80,
				     8,
				     f"{label_description.cget('text')}",0,0,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(50,
				     8,
				     f"{user_inputdesc.get()}",0,1,'L')

		if( user_inputoper.get()!=""):
			pdf.set_font('Arial','B',11)
			pdf.cell(80,
				     8,
				     f"{label_operation.cget('text')}",0,0,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(50,
				     8,
				     f"{user_inputoper.get()}",0,1,'L')
			
			
		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     "Total Fleet Value:",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{txt_fleet92.get('1.0','end')}",0,1,'L')				

		pdf.set_font('Arial','B',11)
		pdf.cell(80,
			     8,
			     f"{label_covertype.cget('text')}",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(50,
			     8,
			     f"{clicked_covertype.get()}",0,1,'L')
		#------------------------------------------------------------------ 

		pdf.set_font('Arial','U',10)
		pdf.cell(80,
			     5,
			     f"{label_vcategory.cget('text')}",0,0,'L')		
		pdf.cell(50,
			     5,
			     f"{label_damage.cget('text')}",0,1,'L')

		if(user_f11.get() !=0 and user_f12.get() != 0 ):

			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_cars.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			         f"R{number_format(user_f13.get())}",0,1,'L')

		if(user_f21.get() !=0 and user_f22.get() != 0):

			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_motocycles.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f23.get())}",0,1,'L')

		if(user_f31.get() !=0 and user_f32.get() != 0):

			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_ldvs.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f33.get())}",0,1,'L')

		if(user_f41.get() !=0 and user_f42.get() != 0):

			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_commercial.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f43.get())}",0,1,'L')

		if(user_f51.get() !=0 and user_f52.get() != 0):
			
			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_busses.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f53.get())}",0,1,'L')
					

		if(user_f61.get() !=0 and user_f62.get() != 0):
			
			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_mobile.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f63.get())}",0,1,'L')
				          	
		if(user_f71.get() !=0 and user_f72.get() != 0):

			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_specialless.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f73.get())}",0,1,'L')						
		if(user_f81.get() !=0 and user_f82.get() != 0):
			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_specialmore.cget('text')}",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f83.get())}",0,1,'L')	

		if(user_c11.get() != 0):
			pdf.set_font('Arial','B',11)
			pdf.cell(80,
				     8,
				     "Third Party liability",0,0,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(50,
				     8,
				     f"R{number_format(user_c11.get())}",0,1,'L')	
		if((user_c13.get() != "") or
			(user_c14.get() != "") or
			(user_c15.get() != "") or
			(user_c16.get() != "") or
			(user_c17.get() != "") or
			(user_c18.get() != "")):
			pdf.set_font('Arial','B',10)
			pdf.cell(80,
			     	 7,
			    	f"{label_excess.cget('text')}",0,1,'L')

			if(user_c13.get() != ""):
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{label_basicexcess.cget('text')}",0,0,'L')
				pdf.cell(80,
				   	 	 4,
				    	f"{user_c13.get()}",0,1,'L')
			if(user_c14.get() != ""):
				pdf.set_font('Arial','',10)

				pdf.cell(80,
			    	 	 4,
			     		f"{label_theft.cget('text')}",0,0,'L')
				pdf.cell(80,
			    	 	 4,
			     		f"{user_c14.get()}",0,1,'L')				     						     					
			if(user_c15.get() != ""):
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				 		 4,
				  		f"{label_windscreen.cget('text')}",0,0,'L')
				pdf.cell(80,
					 	 4,
				    	 f"{user_c15.get()}",0,1,'L')	
			if(user_c16.get() != ""):
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				   	 	 4,
				   		f"{label_thirdparty.cget('text')}",0,0,'L')
				pdf.cell(80,
				   		 4,
			    		f"{user_c16.get()}",0,1,'L')

			if(user_c17.get() != ""):
				pdf.set_font('Arial','',10)			
				pdf.cell(80,
				   	 	 4,
			    		f"{label_section2.cget('text')}",0,0,'L')
				pdf.set_font('Arial','',10)
				pdf.cell(80,
			    	 	 4,
			     		f"{user_c17.get()}",0,1,'L')	

			if(user_c18.get() != ""):
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{label_lossofkeys.cget('text')}",0,0,'L')
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{user_c18.get()}",0,1,'L')					     					
							     								     						     										     												     												     						     					
		pdf.set_font('Arial','B',11)
		pdf.cell(80,
		     	 7,
		     	"Premium Required",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(80,
		     	 7,
		     	"inclusion of 12.5% commision",0,1,'L')	
		if(clicked_showquoteopt1.get() == 'Yes'):
			pdf.set_font('Arial','U',11)
		pdf.cell(80,
		     	 5,
		     	"Conventional",0,1,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(80,
		     	 3,
		     	"Conventional Premium",0,0,'L')	
		pdf.set_font('Arial','',11)
		pdf.cell(80,
		     	 3,
				f"{entry_premopt1.get('1.0',END)}",0,1,'L')		

		if(clicked_showquoteopt2.get() == 'Yes'):
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
			     	 9,
			     	"Burning Cost",0,1,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 3,
			     	"Burning Cost Basis:",0,0,'L')	
			pdf.set_font('Arial','',11)
			dep = user_depositsplit.get()
			b1 = user_burner1split.get()
			b2 = user_burner2split.get()
			pdf.cell(80,
				 	 3,
					f"{dep}/{b1}/{b2}",
					0,1,'L')
			pdf.cell(80,
				 	 7,"Deposit Premium: ",0,0,'L')	
			pdf.cell(80,
				 	 7,
				 	 f"{entry_depositpremopt2.get('1.0',END)}",0,1,'L')	

			tfleet = tot_fleet()
			fprem = multiply(tfleet,user_percopt1.get())
			prem  = round_off(clicked_roundopt1.get(),
							 clicked_typerating.get(),
							 fprem)					
			depo_prem = multiply(prem,user_depositsplit.get())

			c1 = int(depo_prem*0.6)
			claims_1 = number_format(c1)
			pdf.cell(80,
			     	 5,
			     	"If claims reach: ",0,0,'L')
			pdf.cell(80,
			 	 	 5,
			 	 	 f"R{claims_1}",0,1,'L')
			pdf.cell(80,
			     	 5,
			     	"Premium due: ",0,0,'L')
			pdf.cell(80,
			 	 	 5,f"{entry_burner1premopt2.get('1.0',END)}",0,1,'L')			
		
			burner1 = multiply(prem,user_burner1split.get())
			c2 = int((burner1 + depo_prem)*0.6)
			claims_2 = number_format(c2)
			pdf.cell(80,
			     	 7,
			     	"If claims reach: ",0,0,'L')
			pdf.cell(80,
			 	 7,f"R{claims_2}",0,1,'L')
			pdf.cell(80,
			     	 5,
			     	"Premium due: ",0,0,'L')
			pdf.cell(80,
			 	 	 5,f"{entry_burner2premopt2.get('1.0',END)}",0,1,'L')				 	 			 	 						

		if(clicked_showquoteopt3.get() == 'Yes'):
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
			     	 7,
			     	"Aggregate Cost ",0,1,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
			     	"Aggregate Cost Premium",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
					f"{txt_fleetvalue.get('1.0',END)}",0,1,'L')	

		if(clicked_showquoteopt4.get() == 'Yes'):
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
			     	 7,
			     	"Aggregate Cost With Burner ",0,1,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
			     	"Aggregate Cost With Burner Premium",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
					f"{txt_fleetvalue.get('1.0',END)}",0,1,'L')     					          			
		pdf.output('Quote.pdf','F')
	else:	
		messagebox.showwarning('Non Numeric Values',
		    	              ' "Policy no" accepts numeric values only')

	


#------------------Policy Holder Infromation-------------------------------------------

label_pholder = Label(pol_frame,
	                  text = 'Policy Holder Information' ,
	                  font = 'times 20 bold underline')
label_date = Label(pol_frame,
	               text = 'Date Of Quote: ' ,
	               font = 'times 12 bold')
label_type = Label(pol_frame,
	               text = 'Type Of Quote: ' ,
	               font = 'times 12 bold')
label_insured = Label(pol_frame,
	                  text = 'Insured: '
	                  ,font = 'times 12 bold')
label_pol_no = Label(pol_frame,
	                 text = 'Policy No: ' ,
	                 font = 'times 12 bold')
label_inception = Label(pol_frame,
	                    text = 'Policy Inception: '
	                    ,font = 'times 12 bold')
label_period = Label(pol_frame,
	                 text = 'Period Of Insurance(From--To): ',
	                 font = 'times 12 bold')
label_to = Label(pol_frame,
	             text = 'to ',
	             font = 'times 12  bold')
label_pol_type = Label(pol_frame,
	                   text = 'Policy Type: ',
	                   font = 'times 12 bold')
label_description = Label(pol_frame,
	                      text = 'Business Description: ' ,
	                      font = 'times 12 bold')
label_operation = Label(pol_frame,
	                    text = 'Key Area of Operation: ' ,
	                    font = 'times 12 bold')

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
e_dateofquote = DateEntry(pol_frame, width = 18)
e_dateofquote.grid(row = 3,column = 1) 

e_insured = Entry(pol_frame,
	              textvariable = user_inputinsured,
	              bg = 'light blue',
	              bd = 3)
e_insured.grid(row =4,column = 1)

e_policyno = Entry(pol_frame,
	               textvariable = user_inputpolno,
	               bg = 'light blue',
	               bd = 3)
e_policyno.grid(row =5,column = 1)

e_policyinception = DateEntry(pol_frame,width = 18)
e_policyinception.grid(row =6,column = 1)


e_periodfrom = DateEntry(pol_frame, width = 18)
e_periodfrom.grid(row = 7,column =1)

e_periodto = DateEntry(pol_frame,width = 18)
e_periodto.grid(row = 7,column = 3)

e_description = Entry(pol_frame,
	                  textvariable = user_inputdesc,
	                  bg = 'light blue',
	                  bd = 3)
e_description.grid(row = 9,column = 1)

e_operation = Entry(pol_frame,
	                textvariable = user_inputoper,
	                bg = 'light blue',
	                bd = 3)
e_operation.grid(row =10,column = 1)

#Dropdown menus for policy information
clicked_type = StringVar(pol_frame)
clicked_type.set('Select Option')
menu_type = OptionMenu(pol_frame,
                       clicked_type,
                       'Renewal',
                       'New Business ')
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
label_motocycles = Label(fleet_frame,text ='Motorcycles',
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
label_motocycles.grid(row = 3,column = 0,sticky = W)
label_ldvs.grid(row = 4,column = 0,sticky = W)
label_commercial.grid(row = 5,column = 0,sticky = W)
label_busses.grid(row = 6,column = 0,sticky = W)
label_mobile.grid(row = 7,column = 0,sticky = W)
label_specialless.grid(row = 8,column = 0,sticky = W)
label_specialmore.grid(row = 9,column = 0,sticky = W)
label_total.grid(row = 10,column = 0,sticky = W)

label_units = Label(fleet_frame,
	                text = 'No. Of Units',
	                font = 'times 12 bold ')
label_value = Label(fleet_frame,
	                text = 'Value',
	                font = 'times 12 bold ')
label_damage = Label(fleet_frame,
	                 text = 'Own Damage Limit',
	                 font = 'times 12 bold ')
label_sasria_des = Label(fleet_frame,
	                     text = 'SASRIA Description',
	                     font = 'times 12 bold ')
label_sasria_prem = Label(fleet_frame,
	                      text = 'SASRIA Premium',
	                      font = 'times 12 bold ')

label_units.grid(row = 1,column = 1)
label_value.grid(row = 1,column = 2)
label_damage.grid(row = 1,column = 3)
label_sasria_des.grid(row = 1,column = 4)
label_sasria_prem.grid(row = 1,column = 5)


e_fleet11 = Entry(fleet_frame,
	                  textvariable = user_f11,
	                  width = 10,
	                  bg = 'light blue',
	                  bd = 3).grid(row = 2,column=1)
e_fleet12 = Entry(fleet_frame,
	                  textvariable = user_f12,
	                  bg = 'light blue',
	                  bd = 3).grid(row = 2,column=2)
e_fleet13 = Entry(fleet_frame,
	              textvariable = user_f13,
	              bg = 'light blue',
	              bd = 3).grid(row = 2,column=3)
txt_fleet14 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet14.insert(INSERT,"Cars(Primary use: Domestic/ private)")
txt_fleet14.configure(state = 'disabled')
txt_fleet14.grid(row = 2,column=4)

txt_fleet15 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet15.grid(row = 2,column=5)

e_fleet21 = Entry(fleet_frame,
	              textvariable = user_f21,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 3,column=1)
e_fleet22 = Entry(fleet_frame,
	              textvariable = user_f22,
	              bg = 'light blue',
	              bd = 3).grid(row = 3,column=2)
e_fleet23 = Entry(fleet_frame,
	              textvariable = user_f23,
	              bg = 'light blue',
	              bd = 3).grid(row = 3,column=3)
txt_fleet24 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet24.insert(INSERT,"LDV(Commercial use")
txt_fleet24.configure(state = 'disabled')
txt_fleet24.grid(row = 3,column=4)

txt_fleet25 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet25.grid(row = 3,column=5)

e_fleet31 = Entry(fleet_frame,
	              textvariable = user_f31,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 4,column=1)
e_fleet32 = Entry(fleet_frame,
	              textvariable = user_f32,
	              bg = 'light blue',\
	              bd = 3).grid(row = 4,column=2)
e_fleet33 = Entry(fleet_frame,
	              textvariable = user_f33,
	              bg = 'light blue',
	              bd = 3).grid(row = 4,column=3)
txt_fleet34 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet34.insert(END,"LDV(Commercial use)")
txt_fleet34.configure(state = 'disabled')
txt_fleet34.grid(row = 4,column=4)

txt_fleet35 =Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet35.grid(row = 4,column=5)

e_fleet41 = Entry(fleet_frame,
	              textvariable = user_f41,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 5,column=1)
e_fleet42 = Entry(fleet_frame,
	               textvariable = user_f42,
	               bg = 'light blue',
	               bd = 3).grid(row = 5,column=2)
e_fleet43 = Entry(fleet_frame,
	              textvariable = user_f43,
	              bg = 'light blue',
	              bd = 3).grid(row = 5,column=3)
txt_fleet44 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet44.insert(INSERT,"Heavy Commercial Vehicles (>3,500kg)")
txt_fleet44.configure(state = 'disabled')
txt_fleet44.grid(row = 5,column=4)

txt_fleet45 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet45.grid(row = 5,column=5)

e_fleet51 = Entry(fleet_frame,
	               textvariable = user_f51,
	               bg = 'light blue',
	               width = 10,
	               bd = 3).grid(row = 6,column=1)
e_fleet52 = Entry(fleet_frame,
	              textvariable = user_f52,
	              bg = 'light blue',
	              bd = 3).grid(row = 6,column=2)
e_fleet53 = Entry(fleet_frame,
	              textvariable = user_f53,
	              bg = 'light blue',
	              bd = 3).grid(row = 6,column=3)
txt_fleet54 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet54.insert(INSERT,"Buses")
txt_fleet54.configure(state = 'disabled')
txt_fleet54.grid(row = 6,column=4)
txt_fleet55 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet55.grid(row = 6,column=5)

e_fleet61 = Entry(fleet_frame,
	              textvariable = user_f61,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 7,column=1)
e_fleet62 = Entry(fleet_frame,
	              textvariable = user_f62,
	              bg = 'light blue',
	              bd = 3).grid(row = 7,column=2)
e_fleet63 = Entry(fleet_frame,
	              textvariable = user_f63,
	              bg = 'light blue',
	              bd = 3).grid(row = 7,column=3)
txt_fleet64 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet64.insert(INSERT,"Mobile Plant")
txt_fleet64.configure(state = 'disabled')
txt_fleet64.grid(row = 7,column=4)
txt_fleet65 =Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet65.grid(row = 7,column=5)

e_fleet71 = Entry(fleet_frame,
	              textvariable = user_f71,
	              bg = 'light blue',
	              width = 10,
	              bd = 3).grid(row = 8,column=1)
e_fleet72 = Entry(fleet_frame,
	              textvariable = user_f72,
	              bg = 'light blue',
	              bd = 3).grid(row = 8,column=2)
e_fleet73 = Entry(fleet_frame,
	              textvariable = user_f73,
	              bg = 'light blue',
	              bd = 3).grid(row = 8,column=3)
txt_fleet74 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet74.insert(INSERT,"LDV(Commercial use)")
txt_fleet74.configure(state = 'disabled')
txt_fleet74.grid(row = 8,column=4)
txt_fleet75 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet75.grid(row = 8,column=5)

e_fleet81 = Entry(fleet_frame,
	              textvariable = user_f81,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 9,column=1)
e_fleet82 = Entry(fleet_frame,
	              textvariable = user_f82,
	              bg = 'light blue',
	              bd = 3).grid(row = 9,column=2)
e_fleet83 = Entry(fleet_frame,
	              textvariable = user_f83,
	              bg = 'light blue',
	              bd = 3).grid(row = 9,column=3)
txt_fleet84 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet84.insert(INSERT,"Heavy Commercial(>3,500kg)")
txt_fleet84.configure(state = 'disabled')
txt_fleet84.grid(row = 9,column=4)
txt_fleet85 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet85.grid(row = 9,column=5)

txt_fleet91 = Text(fleet_frame,
	              width = 8,
	              height = 0.1,
	              bd = 6)
txt_fleet91.grid(row = 10,column=1)
txt_fleet92 = Text(fleet_frame,
	               width =15,
	               height = 0.1,
	               bd = 6)
txt_fleet92.grid(row = 10,column=2)

button_totfleet = Button(fleet_frame, text="Total", command=add_fleet)
button_totfleet.grid(row = 10, column = 3)


#----------------Cover Information----------------------------

label_coverinfo = Label(cover_frame,
                        text ='Cover Information',
                        font = 'times 20 bold underline')
label_coverinfo.grid(row = 0, column = 0,sticky = W)

label_covertype = Label(cover_frame,
	                    text = 'Cover Type: ',
	                    font = 'times 12 bold')
label_liability = Label(cover_frame,
	                    text = 'Third Party Liability: ',
	                    font ='times 12 bold')

label_covertype.grid(row = 1, column = 0,sticky = W)
label_liability.grid(row = 2,column = 0,sticky = W)

clicked_covertype = StringVar(cover_frame)
clicked_covertype.set('Comprehensive')
menu_cover = OptionMenu(cover_frame,
	                    clicked_covertype,
	                    'Comprehensive,'
			            'Third Party, Fire and Theft',
					    'Third Party Only',
			            'Own Damage Only')
menu_cover.grid(row = 1,
	            column = 1,
	            sticky = W)
entry_c11 = Entry(cover_frame,
	                    width = 30,
	                    textvariable = user_c11,
	                    bg = 'light blue',
	                    bd = 3).grid(row=2,
	                                 column = 1,
	                                 sticky = W)

label_excess = Label(cover_frame,
	                 text = 'Excess',
	                 font = 'times 12 bold')
label_excess.grid(row = 3,column = 0,sticky = W)

label_basicexcess = Label(cover_frame,
                          text = '-Basic Excess',
                          font = 'times 11')
label_theft = Label(cover_frame,
	                text = '-Theft/Hijack',
	                font = 'times 11')
label_windscreen = Label(cover_frame,
                         text = '-Windscreen',
                         font = 'times 11')
label_thirdparty = Label(cover_frame,
                         text = '-Third Party Liability',
                         font = 'times 11')
label_section2 = Label(cover_frame, 
	                   text = '-Section 2 only Excess',
	                   font = 'times 11')
label_lossofkeys = Label(cover_frame,
                         text = '-Loss of Keys',
                         font = 'times 11')
label_audiosystem = Label(cover_frame,
	                      text = '-Audio System',
	                      font = 'times 11')

label_basicexcess.grid(row = 4,column =0 ,sticky = W)
label_theft.grid(row = 5,column = 0,sticky = W)
label_windscreen.grid(row = 6,column = 0,sticky = W)
label_thirdparty.grid(row = 7,column = 0,sticky = W)
label_section2.grid(row =8 ,column = 0,sticky = W)
label_lossofkeys.grid(row = 9,column = 0,sticky = W)

e_excess = Entry(cover_frame,
	                 width = 30,
	                 textvariable = user_c13,
	                 bg = 'light blue',
	                 bd = 3).grid(row = 4, column =1)
e_theft = Entry(cover_frame,
	                width = 30,
	                textvariable = user_c14,
	                bg = 'light blue',
	                bd = 3).grid(row = 5, column =1)
e_windscreen = Entry(cover_frame,
	                     width = 30,
	                     textvariable = user_c15,
	                     bg = 'light blue',
	                     bd = 3).grid(row = 6, column =1)
e_thirdparty = Entry(cover_frame,
	                     width = 30,
	                     textvariable = user_c16,
	                     bg = 'light blue',
	                     bd = 3).grid(row = 7, column =1)
e_section2 = Entry(cover_frame,
	                   width = 30,
	                   bg = 'light blue',
	                   textvariable = user_c17,
	                   bd = 3).grid(row = 8, column =1)
e_lossofkeys = Entry(cover_frame,
	                     width = 30,
	                     bg = 'light blue',
	                     textvariable = user_c18,
	                     bd = 3).grid(row = 9, column =1)

#-----------------Specified Vehicles-----------------------------
label_specified = Label(specified_frame,
	                    text = 'Specified Vehicles',
	                    font = 'times 20 bold underline' )
label_specified.grid(row = 0,column = 0,sticky = W)

label_showquote = Label(specified_frame,
	                    text = 'Show On Quote',
	                    font = 'times 11 bold ')
label_showquote.grid(row =1, column =0,sticky = W)


clicked_showspec = StringVar(specified_frame)
clicked_showspec.set('No')
menu_showspec = OptionMenu(specified_frame,
						    clicked_showspec,
	                       'Yes',
	                        'No')
menu_showspec.grid(row=1,
	               column =1 ,
	               sticky = W)

label_vdescription = Label(specified_frame,
	                       text = 'Vehicle Description',
	                       font = 'times 11 bold ')
label_sasriacat = Label(specified_frame,
	                    text = 'SASRIA Category',
	                    font = 'times 11 bold ')
label_suminsured = Label(specified_frame,
	                     text = 'Sum Insured',
	                     font = 'times 11 bold ')
label_rate = Label(specified_frame,
	               text = 'Rate',
	               font = 'times 11 bold ')
label_annpremium = Label(specified_frame,
	                     text = 'Annual Premium',
	                     font = 'times 11 bold ')
label_sasria_prem2 = Label(specified_frame,
	                       text = 'SASRIA Premium',
	                       font = 'times 11 bold ')

label_vdescription.grid(row = 2, column =1,sticky = W)
label_sasriacat.grid(row = 2, column =2,sticky = W)
label_suminsured.grid(row = 2, column =3,sticky = W)
label_rate.grid(row = 2, column =4,sticky = W)
label_annpremium.grid(row = 2, column =5,sticky = W)
label_sasria_prem2.grid(row = 2, column =6,sticky = W)


e_spec11 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec11.grid(row = 3, column = 1,sticky = W)
clicked_cat1 = StringVar(specified_frame)
clicked_cat1.set('Select Option                       ')
menu_cat1 = OptionMenu(specified_frame,
                       clicked_cat1,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=3,
                                   column = 2)

e_spec13 = Entry(specified_frame,
	             textvariable = user_s13,
	             bg = 'light blue',
	             bd = 3)
e_spec13.grid(row = 3,column = 3,sticky = W)
e_spec14 = Entry(specified_frame,
	             textvariable = user_s14,
	             bg = 'light blue',
	             bd = 3).grid(row = 3, 
	                          column = 4,
	                          sticky = W)
txt_spec15 = Text(specified_frame,
	              height = 0.1,
	              width = 15,
	              bd = 3)
txt_spec15.grid(row = 3, column = 5,sticky = W)

txt_spec16 = Text(specified_frame,
	               height = 0.1,
	               width = 15,
	               bd = 3)
txt_spec16.grid(row = 3, column = 6,sticky = W)

e_spec21 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec21.grid(row = 4, column = 1,sticky = W)

clicked_cat2 = StringVar(specified_frame)
clicked_cat2.set('Select Option                       ')
menu_cat2 = OptionMenu(specified_frame,
                       clicked_cat2,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy,
                       command = add_spec).grid(row=4,
                                   column = 2)
e_spec23 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s23)
e_spec23.grid(row = 4, column = 3,sticky = W)
txt_spec24 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s24)
txt_spec24.grid(row = 4, column = 4,sticky = W)

txt_spec25 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec25.grid(row = 4, column = 5,sticky = W)

txt_spec26 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec26.grid(row = 4, column = 6,sticky = W)

e_spec31 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec31.grid(row = 5,column = 1,sticky = W)
clicked_cat3 = StringVar(specified_frame)
clicked_cat3.set('Select Option                       ')
menu_cat3 = OptionMenu(specified_frame,
                       clicked_cat3,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy)
menu_cat3.grid(row=5,column = 2)
e_spec33 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s33)
e_spec33.grid(row = 5,column = 3,sticky = W)
e_spec34 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s34)
e_spec34.grid(row = 5, column = 4,sticky = W)
txt_spec35 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3,)
txt_spec35.grid(row = 5,column = 5,sticky = W)
txt_spec36 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec36.grid(row = 5, column = 6, sticky= W)

e_spec41 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec41.grid(row = 6, column = 1,sticky = W)
clicked_cat4 = StringVar(specified_frame)
clicked_cat4.set('Select Option                       ')
menu_cat4 = OptionMenu(specified_frame,
                       clicked_cat4,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=6,column = 2)
e_spec43 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s43)
e_spec43.grid(row = 6,column = 3,sticky = W)
e_spec44 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s44)
e_spec44.grid(row = 6, column = 4,sticky = W)
txt_spec45 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec45.grid(row = 6, column = 5, sticky = W)
txt_spec46 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec46.grid(row = 6, column = 6,sticky = W)

e_spec51 = Entry(specified_frame,
				 bd = 3,
	             bg = 'light blue',
	             width = 40)
e_spec51.grid(row = 7, column = 1,sticky = W)
clicked_cat5 = StringVar(specified_frame)
clicked_cat5.set('Select Option                       ')
menu_cat5 = OptionMenu(specified_frame,
                       clicked_cat5,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=7,column = 2)
e_spec53 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s53,
	             bd = 3)
e_spec53.grid(row = 7, column = 3,sticky = W)
e_spec54 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s54)
e_spec54.grid(row = 7, column = 4, sticky = W)
txt_spec55 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec55.grid(row = 7, column = 5,sticky = W)
txt_spec56 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec56.grid(row = 7, column = 6,sticky = W)

e_spec61 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec61.grid(row = 8, column = 1,sticky = W)
clicked_cat6 = StringVar(specified_frame)
clicked_cat6.set('Select Option                       ')
menu_cat6 = OptionMenu(specified_frame,
                       clicked_cat6,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=8,column = 2)
e_spec63 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s63)
e_spec63.grid(row = 8, column = 3, sticky = W)
e_spec64 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s64)
e_spec64.grid(row = 8, column = 4,sticky = W)
txt_spec65 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec65.grid(row = 8, column = 5,sticky = W)
txt_spec66 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec66.grid(row = 8,column = 6, sticky = W)

e_spec71 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec71.grid(row = 9,column = 1,sticky = W)
clicked_cat7 = StringVar(specified_frame)
clicked_cat7.set('Select Option                       ')
menu_cat7 = OptionMenu(specified_frame,
                       clicked_cat7,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=9,column = 2)
e_spec73 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s73)
e_spec73.grid(row = 9, column = 3,sticky = W)
e_spec74 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s74)
e_spec74.grid(row = 9, column = 4,sticky = W)
txt_spec75 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec75.grid(row = 9, column = 5,sticky = W)
txt_spec76 = Text(specified_frame,
	             height = 0.1,
	             width = 15,
	             bd = 3)
txt_spec76.grid(row = 9, column = 6,sticky = W)

e_spec81 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec81.grid(row = 10, column = 1,sticky = W)
clicked_cat8 = StringVar(specified_frame)
clicked_cat8.set('Select Option                       ')
menu_cat8 = OptionMenu(specified_frame,
                       clicked_cat8,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=10,column = 2)
e_spec83 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s83)
e_spec83.grid(row = 10, column = 3, sticky = W)
e_spec84 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s84)
e_spec84.grid(row = 10, column = 4,sticky = W)
txt_spec85 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec85.grid(row = 10, column = 5, sticky = W)
txt_spec86 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec86.grid(row = 10, column = 6, sticky = W)

e_spec91 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40)
e_spec91.grid(row = 11, column = 1, sticky = W)
clicked_cat9 = StringVar(specified_frame)
clicked_cat9.set('Select Option                       ')
menu_cat9 = OptionMenu(specified_frame,
                       clicked_cat9,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=11,
                                   column = 2)
e_spec93 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s73)
e_spec93.grid(row = 11, column = 3, sticky = W)
e_spec94 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s74)
e_spec94.grid(row = 11, column = 4, sticky = W)
txt_spec95 = Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec95.grid(row = 11, column = 5, sticky = W)
txt_spec96 = Text(specified_frame,
	            height = 0.1,
	            bd = 3,
	            width = 15)
txt_spec96.grid(row = 11, column = 6,sticky = W)

e_spec101 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             width = 40).grid(row = 12, column = 1,sticky = W)
clicked_cat10 = StringVar(specified_frame)
clicked_cat10.set('Select Option                       ')
menu_cat10 = OptionMenu(specified_frame,
                       clicked_cat10,
                       cars,
                       ldv,
                       taxis,
                       motors,
                       busses,
                       mobile,
                       brt,
                       heavy).grid(row=12,
                                   column = 2)
e_spec103 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s103,
	             bd = 3)
e_spec103.grid(row = 12,column = 3,sticky = W)
e_spec104 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s104)
e_spec104.grid(row = 12, column = 4, sticky = W)
txt_spec105 = Text(specified_frame,
	              height = 0.1,
	              bd = 3,
	              width = 15)
txt_spec105.grid(row = 12, column = 5,sticky = W)
txt_spec106 =Text(specified_frame,
	             height = 0.1,
	             bd = 3,
	             width = 15)
txt_spec106.grid(row = 12, column = 6, sticky = W)

button_totfleet = Button(specified_frame, text=
	"Total", command=add_spec)
button_totfleet.grid(row = 13,column = 4)

txt_spec65 = Text(specified_frame,
	              height = 0.1,
	              width = 15,
	              bd = 3)
txt_spec65.grid(row = 13, column = 5, sticky = W)
# txt_spec66 = Text(specified_frame,
# 	               height = 0.1,
# 	               bd = 3,
# 	               width = 15)
# txt_spec66.grid(row = 13, column = 6, sticky = W)

label_excess2 = Label(specified_frame,
	                  text = 'Excess',
	                  font = 'times 12 bold')
label_excess2.grid(row = 14,column = 0,sticky = W)

label_basicexcess2 = Label(specified_frame,
                           text = '-Basic Excess',
                           font = 'times 11')
label_theft2 = Label(specified_frame,
                     text = '-Theft/Hijack',
                     font = 'times 11')
label_windscreen2 = Label(specified_frame,
                          text = '-Windscreen',
                          font = 'times 11')
label_thirdparty2 = Label(specified_frame,
                          text = '-Third Party Liability',
                          font = 'times 11')
label_section22 = Label(specified_frame,
                        text = '-Section 2 only Excess',
                        font = 'times 11')
label_lossofkeys2 = Label(specified_frame,
                          text = '-Loss of Keys',
                          font = 'times 11')
label_audiosystem2 = Label(specified_frame,
                           text = '-Audio System',
                           font = 'times 11')

label_basicexcess2.grid(row = 15,column =0 ,sticky = W)
label_theft2.grid(row = 16,column = 0,sticky = W)
label_windscreen2.grid(row = 17,column = 0,sticky = W)
label_thirdparty2.grid(row = 18,column = 0,sticky = W)
label_section22.grid(row =19 ,column = 0,sticky = W)
label_lossofkeys2.grid(row = 20,column = 0,sticky = W)

e_excess2 = Entry(specified_frame,
	              bg = 'light blue',
	              bd = 3)
e_excess2.grid(row = 15, column =1)
e_theft2 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3)
e_theft2.grid(row = 16, column =1)
e_windscreen2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  bd = 3)
e_windscreen2.grid(row = 17, column =1)
e_thirdparty2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  bd = 3)
e_thirdparty2.grid(row = 18, column =1)
e_section22 = Entry(specified_frame,
	                bg = 'light blue',
	                bd = 3)
e_section22.grid(row = 19, column =1)
e_lossofkeys2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  bd = 3)
e_lossofkeys2.grid(row = 20, column =1)


#---------------------------Rating Info------------------------------
rating_frame = LabelFrame(main_frame,text = 'Rating Information')
rating_frame.grid(row = 1, column =0,sticky = W)

option1_frame = LabelFrame(rating_frame,text = 'Option 1')
option2_frame = LabelFrame(rating_frame,text = 'Option 2')
option3_frame = LabelFrame(rating_frame,text = 'Option 3')
option4_frame = LabelFrame(rating_frame,text = 'Option 4')




label_ratinginfo = Label(rating_frame,
	                     text = 'Rating Information',
	                     font = 'times 18 bold underline')
label_fleetvalue = Label(rating_frame,
	                     text = 'Fleet value: ',
	                     font = 'times 12 bold')
label_priorclaims = Label(rating_frame,
	                      text = 'Prior year claims: ',
	                      font = 'times 12 bold')
label_totalclaims = Label(rating_frame,
	                      text = 'Total claims YTD: ',
	                      font = 'times 12 bold')
label_numofmonths = Label(rating_frame,
	                      text = 'No. of months remaining before renewal: ',
	                      font = 'times 12 bold')
label_annclaims = Label(rating_frame,
	                    text = 'Annualised Claims: ',
	                    font = 'times 12 bold')

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

txt_fleetvalue= Text(rating_frame,
	                 height = 0.1,
	                 width = 15,
					 bd = 3)
txt_fleetvalue.grid(row = 1,column = 1,sticky = W)

user_priorclaims = IntVar(rating_frame)
entry_priorclaims = Entry(rating_frame,
						  textvariable = user_priorclaims,
						  bd = 3,
						  bg = 'light blue')
entry_priorclaims.grid(row = 2,column = 1,sticky = W)

user_totalclaims = IntVar(rating_frame)
entry_totalclaims= Entry(rating_frame,
						 textvariable = user_totalclaims,
						 bd = 3,
						 bg = 'light blue')
entry_totalclaims.grid(row = 3,column = 1,sticky = W)

entry_numofmonths = Text(rating_frame,
						 height = 0.1,
						 width = 15,
						  bd = 3)
entry_numofmonths.grid(row = 4,column = 1,sticky = W)

entry_annclaims = Text(rating_frame,
						height = 0.1,
						width = 15,
						bd = 3)
entry_annclaims.grid(row = 5,column = 1,sticky = W)
calc_rating = Button(rating_frame,text ="Calculate",command = rating)
calc_rating.grid(row = 6, column = 1)

label_premcalcs = Label(rating_frame,
	                    text = 'Premium Calcuations',
	                    font = 'times 18 bold underline')
label_premcalcs.grid(row = 6,column = 0,sticky ='W')

#------------------------Option 1 ---------------------------------
label_opt1 = Label(option1_frame,
	               text = 'Option 1- Conventional',
	               font = 'times 15 bold underline')
label_showqoteopt1 = Label(option1_frame,
	                       text = 'Show on Quote:' ,
	                       font = 'times 12 bold')
label_premfleetopt1 = Label(option1_frame,
	                        text = 'Premium based on fleet value:',
	                        font = 'times 12 bold')
label_ratioapplied = Label(option1_frame,
	                       text = 'Rate/Ratio applied: ')
label_premiumopt1 = Label(option1_frame,text = 'Premium: ')
label_premlossopt1 = Label(option1_frame,
	                       text = 'Premium based on loss value:',
	                       font = 'times 12 bold')
label_roundupeopt1 = Label(option1_frame,
	                       text = 'Round-up/-down',
	                       font = 'times 12 bold')
label_roundnearopt1 = Label(option1_frame,
	                        text = 'Round to nearest:',
	                        font = 'times 12 bold')
label_premquoteopt1 = Label(option1_frame,
	                        text = 'Premium on Quote:',
	                        font = 'times 12 bold')
label_overrideopt1 = Label(option1_frame,
	                       text = 'Override?',
	                       font = 'times 12 bold')
label_premquote2opt1 = Label(option1_frame,
	                         text = 'Premium on Quote:',
	                         font = 'times 12 bold')

clicked_showquoteopt1 = StringVar(option1_frame)
clicked_showquoteopt1.set('No')
menu_type = OptionMenu(option1_frame, clicked_showquoteopt1,'No','Yes')
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

user_percopt1 = IntVar(option1_frame)
entry_fleetpercopt1 = Entry(option1_frame,
							textvariable = user_percopt1,
							bg= 'light blue',
							bd = 3)
entry_fleetpercopt1.grid(row = 3,column = 1,sticky = 'W')

entry_fleetpremopt1 = Text(option1_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_fleetpremopt1.grid(row = 3,column = 2,sticky = 'W')

user_lossopt1 = IntVar(option1_frame)
entry_losspercopt1 = Entry(option1_frame,
						   textvariable = user_lossopt1,
						   bd = 3,
						   bg = 'light blue').grid(row = 4,column = 1)

entry_losspremcopt1 = Text(option1_frame,
						   height = 0.1,
						   width = 15,
						   bd = 3)
entry_losspremcopt1.grid(row = 4,column = 2)

entry_premopt1 =Text(option1_frame,
					  bd = 3,
					  height = 0.1,
					  width = 15)
entry_premopt1.grid(row = 7,column = 1)

user_prem2opt1 = IntVar(option1_frame)
entry_prem2opt1 =Entry(option1_frame,
					   bd = 3,
					   textvariable = user_prem2opt1,
					   bg = 'light blue')
entry_prem2opt1.grid(row = 9,column = 1)

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
calc_opt1 = Button(option1_frame,text ="Calculate",command = option1)
calc_opt1.grid(row = 10, column = 1)

#------------------------Option 2---------------------------
label_opt2 = Label(option2_frame,text = 'Option 2- Burning Cost',font = 'times 15 bold underline')
label_showqoteopt2 = Label(option2_frame,text = 'Show on Quote:' ,font = 'times 12 bold')
label_loadingopt2 = Label(option2_frame,text = 'Loading: ')
label_totalpremopt2 = Label(option2_frame,text = 'Total Premium: ')

label_premloadingopt2 = Label(option2_frame,text = 'Premium loading',font = 'times 12 bold')

label_premsplitopt2 = Label(option2_frame,text = 'Premium Split: ',font = 'times 12 bold')
label_prempropopt2 = Label(option2_frame,text = 'Proportional Split: ')
label_premopt2 = Label(option2_frame,text = 'Premium: ')

label_depositpremopt2 = Label(option2_frame,text = 'Deposit premium ')
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

user_premloading = IntVar(option2_frame)
entry_premloadingopt2 = Entry(option2_frame,
							  textvariable = user_premloading,
							  bd = 3,
							  bg = 'light blue')
entry_premloadingopt2.grid(row = 3,column = 1)

entry_totalpremopt2 = Text(option2_frame,
							height = 0.1,
							width = 15,
						    bd = 3)
entry_totalpremopt2.grid(row = 3,column = 2)

user_depositsplit = IntVar(option2_frame)
entry_depositsplitopt2 = Entry(option2_frame,
							   textvariable = user_depositsplit,
							   bd = 3,
							   bg = 'light blue')
entry_depositsplitopt2.grid(row = 5,column = 1)

entry_depositpremopt2 = Text(option2_frame,
							  height = 0.1,
							  width = 15,
							  bd = 3)
entry_depositpremopt2.grid(row = 5,column = 2)

user_burner1split = IntVar(option2_frame)
entry_burner1splitopt2 = Entry(option2_frame,
							   textvariable = user_burner1split,
							   bd = 3,
							   bg = 'light blue')
entry_burner1splitopt2.grid(row = 6,column = 1)

entry_burner1premopt2 =Text(option2_frame,
							 bd = 3,
							 height = 0.1,
							 width = 15)
entry_burner1premopt2.grid(row = 6,column = 2)

user_burner2split = IntVar(option2_frame)
ntry_burner2splitopt2 =Entry(option2_frame,
							 textvariable = user_burner2split,
							 bg = 'light blue',
							 bd = 3).grid(row = 7,column = 1)
entry_burner2premopt2 =Text(option2_frame,
							 height = 0.1,
							 width = 15,
							 bd = 3)
entry_burner2premopt2.grid(row = 7,column = 2)
calc_rating = Button(option2_frame,text ="Calculate",command = option2)
calc_rating.grid(row = 8, column = 1)


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
label_premlossopt3 = Label(option3_frame,text = 'Premium based on loss ratio: ',font = 'times 12 bold')
label_premclaimsopt3 = Label(option3_frame,text = 'Premium based on claims above stop loss limit: ',font = 'times 12 bold')
label_roundupopt3 = Label(option3_frame,text = 'Round up/down: ',font = 'times 12 bold')
label_roundnearopt3 = Label(option3_frame,text = 'Round to nearest: ',font = 'times 12 bold')
label_premquoteopt3 = Label(option3_frame,text = 'Premium on Quote: ',font = 'times 12 bold ')
label_overrideopt3 = Label(option3_frame,text = 'Override?: ',font = 'times 12 bold')
label_premquote2opt3 = Label(option3_frame,text = 'Premium on Quote: ',font = 'times 12 bold')
label_showtextopt3 = Label(option3_frame,text = 'Show the below text on quote? ',font = 'times 12 bold')

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

user_annualaggopt3 = IntVar(option3_frame)
entry_annualaggopt3 = Entry(option3_frame,
					 textvariable = user_annualaggopt3,
					 bd = 3,
					 bg = 'light blue').grid(row = 2,column = 1)

clicked_appopt3 = StringVar(option3_frame)
clicked_appopt3.set('Section A & B')
menu_appopt3 = OptionMenu(option3_frame,
							  clicked_appopt3,
							  'Section A & B',
							  'Section A')
menu_appopt3.grid(row = 3,column = 1)

user_stoploss = IntVar(option3_frame)
entry_stoplossopt3 = Entry(option3_frame,
						   textvariable = user_stoploss,
						   bd = 3,
						   bg = 'light blue').grid(row = 4,column = 1)

user_claimspaidopt3 = IntVar(option3_frame)
entry_claimspaidopt3= Entry(option3_frame,
						textvariable =user_claimspaidopt3,
					    bd = 3,
					    bg = 'light blue').grid(row = 5,column = 1)

entry_numofmonthsopt3 = Text(option3_frame,
							 height = 0.1,
							 width = 15,
                             bd = 3)
entry_numofmonthsopt3.grid(row = 6,column = 1)

entry_annclaimsopt3 = Text(option3_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_annclaimsopt3.grid(row = 7,column = 1)

user_premrateopt3 = IntVar(option3_frame)
entry_premrateopt3 = Entry(option3_frame,
							textvariable = user_premrateopt3,
						   bd = 3,
						   bg = 'light blue').grid(row = 9,column = 1)

entry_ratiopremopt3 = Text(option3_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_ratiopremopt3.grid(row = 9,column = 2)

user_limitrateopt3 = IntVar(option3_frame)
entry_limitrateopt3 = Entry(option3_frame,
							textvariable = user_limitrateopt3,
							bd = 3,
							bg = 'light blue').grid(row = 10,column = 1)
entry_limitpremopt3 = Text(option3_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_limitpremopt3.grid(row = 10,column = 2)

clicked_roundopt3 = StringVar(option3_frame)
clicked_roundopt3.set('Up')
menu_roundopt3 = OptionMenu(option3_frame, clicked_roundopt3,'Up','Down')
menu_roundopt3.grid(row = 11,column = 1)

clicked_nearestopt3 = StringVar(option3_frame)
clicked_nearestopt3.set('R10 000')
menu_sectionopt3 = OptionMenu(option3_frame, clicked_nearestopt3,'R1 000','R10 000','R100 000')
menu_sectionopt3.grid(row = 12,column = 1)

user_overrideopt3 = IntVar(option3_frame)
entry_premonquoteopt3 = Text(option3_frame,
							  height = 0.1,
							  width = 15,
							  bd = 3)
entry_premonquoteopt3.grid(row = 13,column = 1)

clicked_overrideopt3 = StringVar(option3_frame)
clicked_overrideopt3.set('No')
menu_roundopt3 = OptionMenu(option3_frame, clicked_overrideopt3,'No','Yes')
menu_roundopt3.grid(row = 14,column = 1)

entry_premonquote2opt3 = Entry(option3_frame,
							   bd = 3).grid(row = 15,column = 1)

clicked_textopt3 = StringVar(option3_frame)
clicked_textopt3.set('No')
menu_roundopt3 = OptionMenu(option3_frame, clicked_overrideopt3,'No','Yes')
menu_roundopt3.grid(row = 16,column = 1)
textlabelopt3 = 'All legal, assessor fees and other fees/expenses will contribute the aggregrate deductible'
label_textopt3 = Label(option3_frame,text = textlabelopt3,font = 'times 11 italic')
label_textopt3.grid(row = 17,column = 0)
calc_opt3 = Button(option3_frame,text ="Calculate",command = option3)
calc_opt3.grid(row = 18, column = 1)


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
label_premlossopt4 = Label(option4_frame,text = 'Premium based on loss ratio: ',font = 'times 12 bold')
label_premclaimsopt4 = Label(option4_frame,text = 'Premium based on claims above stop loss limit: ',font = 'times 12 bold')
label_roundupopt4 = Label(option4_frame,text = 'Round up/down: ',font = 'times 12 bold')
label_roundnearopt4 = Label(option4_frame,text = 'Round to nearest: ',font = 'times 12 bold')
label_aggpremopt4 = Label(option4_frame,text = 'Aggregate Excess Premium: ',font = 'times 12 bold ')
label_loadingopt4 = Label(option4_frame,text = 'Loading: ')
label_totalpremopt4 = Label(option4_frame,text = 'Total Premium: ')
label_premloadingopt4 = Label(option4_frame,text = 'Premium loading',font = 'times 12 bold')
label_premsplitopt4 = Label(option4_frame,text = 'Premium Split: ',font = 'times 12 bold')
label_prempropopt4 = Label(option4_frame,text = 'Proportional Split: ')
label_premopt4 = Label(option4_frame,text = 'Premium: ')
label_depositpremopt4 = Label(option4_frame,text = 'Deposit premium ')
label_burner1opt4 = Label(option4_frame,text = 'Burner 1')
label_burner2opt4 = Label(option4_frame,text = 'Burner 2')
label_showtextopt4 = Label(option4_frame,text = 'Show the below text on quote? ',font = 'times 12 bold')


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
label_aggpremopt4.grid(row = 13,column = 0,sticky = W)
label_loadingopt4.grid(row = 14,column = 1,sticky = W)
label_totalpremopt4.grid(row = 14,column = 2,sticky = W)
label_premloadingopt4.grid(row = 15,column = 0,sticky = W)
label_premsplitopt4.grid(row = 16,column = 0,sticky = W)
label_prempropopt4.grid(row = 16,column = 1,sticky = W)
label_premopt4.grid(row = 16,column = 2,sticky = W)
label_depositpremopt4.grid(row = 17,column = 0,sticky = W)
label_burner1opt4.grid(row = 18,column = 0,sticky = W)
label_burner2opt4.grid(row = 19,column = 0,sticky = W)
label_showtextopt4.grid(row = 20,column = 0,sticky = W)

clicked_showquoteopt4 = StringVar(option4_frame)
clicked_showquoteopt4.set('No')
menu_showopt4= OptionMenu(option4_frame, clicked_showquoteopt4,'No','Yes')
menu_showopt4.grid(row = 1,column = 1)

user_annualaggopt4 = IntVar(option4_frame)
entry_annual2 = Entry(option4_frame,
					 textvariable = user_annualaggopt4,
					 bd = 3,
					 bg = 'light blue').grid(row = 2,column = 1)

clicked_sectionopt4 = StringVar(option4_frame)
clicked_sectionopt4.set('Section A & B')
menu_sectionopt4 = OptionMenu(option4_frame, clicked_sectionopt4,'Section A & B','Section A')
menu_sectionopt4.grid(row = 3,column = 1)

user_stoplossopt4 = IntVar(option4_frame)
entry_stoplossopt4 = Entry(option4_frame,
						   textvariable = user_stoplossopt4,
						   bd = 3,
						   bg = 'light blue').grid(row = 4,column = 1)

user_claimspaidopt4 = IntVar(option4_frame)
entry_claimspaidopt4= Entry(option4_frame,
						bd = 3,
						textvariable = user_claimspaidopt4,
						bg = 'light blue').grid(row = 5,column = 1)

entry_numofmonthsopt4 = Text(option4_frame,
							  height = 0.1,
							  width = 15,
							  bd = 3)
entry_numofmonthsopt4.grid(row = 6,column = 1)

entry_annclaimsopt4 = Text(option4_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_annclaimsopt4.grid(row = 7,column = 1)

user_premrateopt4 = IntVar(option4_frame)
entry_premrateopt4 = Entry(option4_frame,
						   bd = 3,
						   textvariable = user_premrateopt4,
						   bg = 'light blue').grid(row = 9,column = 1)
entry_ratiopremopt4 = Text(option4_frame,
							height = 0.1,
							width = 15,
							bd = 3)
entry_ratiopremopt4.grid(row = 9,column = 2)

user_limitrateopt4 = IntVar(option4_frame)
entry_limitrateopt4 = Entry(option4_frame,
							bd = 3,
							textvariable = user_limitrateopt4,
							bg = 'light blue').grid(row = 10,column = 1)
entry_limitpremopt4 = Text(option4_frame,
							bd = 3,
							height = 0.1,
							width = 15)
entry_limitpremopt4.grid(row = 10,column = 2)

clicked_roundopt4 = StringVar(option4_frame)
clicked_roundopt4.set('Up')
menu_roundopt4 = OptionMenu(option4_frame, clicked_roundopt4,'Up','Down')
menu_roundopt4.grid(row = 11,column = 1)

clicked_nearestopt4 = StringVar(option4_frame)
clicked_nearestopt4.set('R10 000')
menu_nearestopt4= OptionMenu(option4_frame,
							 clicked_nearestopt4,
							 'R1 000',
							 'R10 000','R100 000')
menu_nearestopt4.grid(row = 12,column = 1)

entry_aggpremeopt4 = Text(option4_frame,
						  height = 0.1,
						  width = 15,
						  bd = 3)
entry_aggpremeopt4.grid(row = 13,column = 1)

user_premloadingopt4 = IntVar(option4_frame)
entry_premonquote2opt4 = Entry(option4_frame,
								textvariable = user_premloadingopt4,
								bd = 3,
								bg = 'light blue').grid(row = 15,column = 1)
entry_premtotopt4 = Text(option4_frame,
						 height = 0.1,
						 width = 15,
						 bd = 3)
entry_premtotopt4.grid(row = 15,column = 2)

user_depositsplitopt4 = IntVar(option4_frame)
entry_depositsplitopt4 = Entry(option4_frame,
								textvariable = user_depositsplitopt4,
								bd = 3,
								bg = 'light blue').grid(row = 17,column = 1)
entry_depositpremopt4 = Text(option4_frame,
						 height = 0.1,
						 width = 15,
						 bd = 3)
entry_depositpremopt4.grid(row = 17,column = 2)

user_burner1splitopt4 = IntVar(option4_frame)
entry_burner1plitopt4 = Entry(option4_frame,
								textvariable = user_burner1splitopt4,
								bd = 3,
								bg = 'light blue').grid(row = 18,column = 1)
entry_burner1premopt4 = Text(option4_frame,
						 height = 0.1,
						 width = 15,
						 bd = 3)
entry_burner1premopt4.grid(row = 18,column = 2)

user_burner2splitopt4 = IntVar(option4_frame)
entry_burner2plitopt4 = Entry(option4_frame,
								textvariable = user_burner2splitopt4,
								bd = 3,
								bg = 'light blue').grid(row = 19,column = 1)
entry_burner2premopt4 = Text(option4_frame,
						 height = 0.1,
						 width = 15,
						 bd = 3)
entry_burner2premopt4.grid(row = 19,column = 2)


clicked_textopt4 = StringVar(option4_frame)
clicked_textopt4.set('No')
menu_roundopt4 = OptionMenu(option4_frame, clicked_textopt4,'No','Yes')
menu_roundopt4.grid(row = 20,column = 1)
textlabelopt4 = 'All legal, assessor fees and other fees/expenses will contribute the aggregrate deductible'
label_textopt4 = Label(option4_frame,text = textlabelopt4,font = 'times 11 italic')
label_textopt4.grid(row = 21,column = 0) 
calc_opt4 = Button(option4_frame,text ="Calculate",command = option4)
calc_opt4.grid(row = 22, column = 1)

button_quit = Button(root, text="Exit Program", command=root.quit)


root.mainloop()