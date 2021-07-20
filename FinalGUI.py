from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import fpdf
from fpdf import FPDF
from tkinter import ttk, filedialog
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
desc_frame = Frame(policyinfo_frame)
fleet_frame = Frame(policyinfo_frame)
cover_frame = Frame(policyinfo_frame)
specified_frame =Frame(policyinfo_frame)

pol_frame.grid(row = 0,column = 0,sticky = 'W')
desc_frame.grid(row = 1, column = 0,sticky = 'W')
fleet_frame.grid(row = 2,column = 0,sticky = 'W')
cover_frame.grid(row = 3,column = 0,sticky = 'W')
specified_frame.grid(row = 4,column = 0,sticky = 'W')



my_canvas.create_window((0,0), window = main_frame,anchor = "nw")

user_inputinsured = StringVar(pol_frame)
user_inputpolno = StringVar(pol_frame)
user_inputdesc = StringVar(pol_frame)
user_inputoper = StringVar(pol_frame)
user_units = IntVar(pol_frame)
user_value = DoubleVar(pol_frame)

user_f11 = IntVar(fleet_frame)
user_f21 = IntVar(fleet_frame)
user_f31 = IntVar(fleet_frame)
user_f41 = IntVar(fleet_frame)
user_f51 = IntVar(fleet_frame)
user_f61 = IntVar(fleet_frame)
user_f71 = IntVar(fleet_frame)
user_f81 = IntVar(fleet_frame)

user_f12 = IntVar(fleet_frame)
user_f22 = IntVar(fleet_frame)
user_f32 = IntVar(fleet_frame)
user_f42 = IntVar(fleet_frame)
user_f52 = IntVar(fleet_frame)
user_f62 = IntVar(fleet_frame)
user_f72 = IntVar(fleet_frame)
user_f82 = IntVar(fleet_frame)

user_f13 = IntVar(fleet_frame)
user_f23 = IntVar(fleet_frame)
user_f33 = IntVar(fleet_frame)
user_f43 = IntVar(fleet_frame)
user_f53 = IntVar(fleet_frame)
user_f63 = IntVar(fleet_frame)
user_f73 = IntVar(fleet_frame)
user_f83 = IntVar(fleet_frame)

user_f15 = DoubleVar(fleet_frame)
user_f25 = DoubleVar(fleet_frame)
user_f35 = DoubleVar(fleet_frame)
user_f45 = DoubleVar(fleet_frame)
user_f55 = DoubleVar(fleet_frame)
user_f65 = DoubleVar(fleet_frame)
user_f75 = DoubleVar(fleet_frame)
user_f85 = DoubleVar(fleet_frame)

select = 'Select Option                       '
cars = 'Cars(Primary use: Domestic/private)'
ldv ='LDV(Commercial use)'
taxis = 'Taxis(7-24)'
motors= 'Motors Traders'
buses = 'Buses'
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

perc4 = 0.0001879
perc5 = 0.00504
perc6 = 0.000363
perc8 = 0.0001879


minann1 = 20.18
minann2 = 45.39
minann3 = 45.39
minann4 = 54.47
minann5 = 2000.00
minann6 = 200.00
minann7 = 45.39
minann8 = 54.47

minmon1 = 2.02
minmon2 = 4.54
minmon3 = 4.54
minmon4 = 5.45
minmon5 = 200.00
minmon6 = 20.00
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
user_c19 = StringVar(cover_frame)
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
	if(len(value)==12):
		final = value[0:3] + \
		        ' ' + value[3:6] + \
		        ' ' + value[6:9] + \
		        ' ' + value[9:]	
	if(len(value)==13):
		final = value[0] + \
		        ' ' + value[1:4] + \
		        ' ' + value[4:7] + \
		        ' ' + value[7:10] + \
		        ' ' + value[10:]

	if(len(value)==14):
		final = value[0:2] + \
		        ' ' + value[2:5] + \
		        ' ' + value[5:8] + \
		        ' ' + value[8:11] + \
		        ' ' + value[11:]	
	if(len(value)==15):
		final = value[0:3] + \
		        ' ' + value[3:6] + \
		        ' ' + value[6:9] + \
		        ' ' + value[9:12] + \
		        ' ' + value[12:]			        	        
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
	                 annprem_s105)
	                 

	if(clicked_poltype.get()=="Annual"):
		#----------Row 1------------
		if(clicked_cat1.get()== select):
			pass
		else:
			string_ann1 = ""
			final_ann1 = ""
			dec_ann1 = ""			
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
				if((user_s13.get()*perc4)< minann4):
					M4 = minann4
					insert_all(txt_spec16,M4)
				else:
					M4 = round(user_s13.get()*perc4,2)
					string_ann1 = str(M4)
					if(string_ann1[-3] == "."):
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-2] == "."):
						string_ann1 += "0"
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-3] != "." and string_ann1[-2] != "."):
						dec_ann1 = ".00"
						num_ann1 = str(number_format(string_ann1))					
					final_ann1 = num_ann1 + dec_ann1 
					insert_all(txt_spec16,final_ann1)
			if(clicked_cat1.get()== buses):
				if((user_s13.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec16,M5)
				else:
					M5 = round(user_s13.get()*perc5,2)
					string_ann1 = str(M5)
					if(string_ann1[-3] == "."):
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-2] == "."):
						string_ann1 += "0"
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-3] != "." and string_ann1[-2] != "."):
						dec_ann1 = ".00"
						num_ann1 = str(number_format(string_ann1))	
					final_ann1 = num_ann1 + dec_ann1 					
					insert_all(txt_spec16,final_ann1)
			if(clicked_cat1.get()== mobile):
				if((user_s13.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec16,M6)
				else:
					M6 = round(user_s13.get()*perc6,2)
					string_ann1 = str(M6)
					if(string_ann1[-3] == "."):
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-2] == "."):
						string_ann1 += "0"
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-3] != "." and string_ann1[-2] != "."):
						dec_ann1 = ".00"
						num_ann1 = str(number_format(string_ann1))	
					final_ann1 = num_ann1 + dec_ann1 										
					insert_all(txt_spec16,final_ann1)
			if(clicked_cat1.get()== brt):
				M7 = minann7
				insert_all(txt_spec16,M7)
			if(clicked_cat1.get()== heavy):
				if((user_s13.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec16,M8)
				else:
					M8 = round(user_s13.get()*perc8,2)
					string_ann1 = str(M8)
					if(string_ann1[-3] == "."):
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-2] == "."):
						string_ann1 += "0"
						dec_ann1 = str(string_ann1[-3:])
						num_ann1 = str(string_ann1[:-3]) 
						num_ann1 = str(number_format(num_ann1))
					if(string_ann1[-3] != "." and string_ann1[-2] != "."):
						dec_ann1 = ".00"
						num_ann1 = str(number_format(string_ann1))	
					final_ann1 = num_ann1 + dec_ann1 					
					insert_all(txt_spec16,final_ann1)					 

		#----------Row 2------------
		if(clicked_cat2.get()== select):
			pass
		else:
			string_ann2 = ""
			final_ann2 = ""
			dec_ann2 = ""				

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
				if((user_s23.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec26,M4)	
				else:
					M4 = round(user_s23.get()*perc5,2)
					string_ann2 = str(M4)
					if(string_ann2[-3] == "."):
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-2] == "."):
						string_ann2 += "0"
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-3] != "." and string_ann2[-2] != "."):
						dec_ann2 = ".00"
						num_ann2 = str(number_format(string_ann2))	
					final_ann2 = num_ann2 + dec_ann2 					
					insert_all(txt_spec26,final_ann2)	
			if(clicked_cat2.get()== buses):
				if((user_s23.get()*perc5)< min_ann5):
					M5 = min_ann5
					insert_all(txt_spec26,M5)	
				else:
					M5 = round(user_s23.get()*perc5,2)
					string_ann2 = str(M5)
					if(string_ann2[-3] == "."):
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-2] == "."):
						string_ann2 += "0"
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-3] != "." and string_ann2[-2] != "."):
						dec_ann2 = ".00"
						num_ann2 = str(number_format(string_ann2))	
					final_ann2 = num_ann2 + dec_ann2 					
					insert_all(txt_spec26,final_ann2)						
			if(clicked_cat2.get()== mobile):
				if((user_s23.get()*perc6) < minann6):
					M6 = minann6					
					insert_all(txt_spec26,M6)	
				else:
					M6 = round(user_s23.get()*perc6,2)
					string_ann2 = str(M6)
					if(string_ann2[-3] == "."):
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-2] == "."):
						string_ann2 += "0"
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-3] != "." and string_ann2[-2] != "."):
						dec_ann2 = ".00"
						num_ann2 = str(number_format(string_ann2))	
					final_ann2 = num_ann2 + dec_ann2 					
					insert_all(txt_spec26,final_ann2)						
			if(clicked_cat2.get()== brt):
				M7 = minann7
				insert_all(txt_spec26,M7)	
			if(clicked_cat2.get()== heavy):
				if((user_s23.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec26,M8)	
				else:
					M8 = round(user_s23.get()*perc8,2)
					string_ann2 = str(M8)
					if(string_ann2[-3] == "."):
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-2] == "."):
						string_ann2 += "0"
						dec_ann2 = str(string_ann2[-3:])
						num_ann2 = str(string_ann2[:-3]) 
						num_ann2 = str(number_format(num_ann2))
					if(string_ann2[-3] != "." and string_ann2[-2] != "."):
						dec_ann2 = ".00"
						num_ann2 = str(number_format(string_ann2))	
					final_ann2 = num_ann2 + dec_ann2 					
					insert_all(txt_spec26,final_ann2)						


		#----------Row 3------------
		if(clicked_cat3.get()== select):
			pass
		else:
			string_ann3 = ""
			final_ann3 = ""
			dec_ann3 = ""				
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
				if((user_s33.get()*perc4) < minann4):
					M4 = minann4	
				else:
					M4 = round(user_s33.get()*perc4,2)
					string_ann3 = str(M4)
					if(string_ann3[-3] == "."):
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-2] == "."):
						string_ann3 += "0"
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-3] != "." and string_ann3[-2] != "."):
						dec_ann3 = ".00"
						num_ann3 = str(number_format(string_ann3))	
					final_ann3 = num_ann3 + dec_ann3 					
					insert_all(txt_spec36,final_ann3)					
			if(clicked_cat3.get()== buses):
				if((user_s33.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec36,M5)
				else:
					M5 = round(user_s33.get()*perc5,2)
					string_ann3 = str(M5)
					if(string_ann3[-3] == "."):
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-2] == "."):
						string_ann3 += "0"
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-3] != "." and string_ann3[-2] != "."):
						dec_ann3 = ".00"
						num_ann3 = str(number_format(string_ann3))	
					final_ann3 = num_ann3 + dec_ann3 					
					insert_all(txt_spec36,final_ann3)
			if(clicked_cat3.get()== mobile):
				if((user_s33.get()*perc6) < minann6):
					M6 = minann6
					insert_all(txt_spec36,M6)
				else:
					M6 = round(user_s33.get()*perc6,2)
					string_ann3 = str(M6)
					if(string_ann3[-3] == "."):
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-2] == "."):
						string_ann3 += "0"
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-3] != "." and string_ann3[-2] != "."):
						dec_ann3 = ".00"
						num_ann3 = str(number_format(string_ann3))	
					final_ann3 = num_ann3 + dec_ann3 					
					insert_all(txt_spec36,final_ann3)					
			if(clicked_cat3.get()== brt):
				M7 = minann7
				insert_all(txt_spec36,M7)
			if(clicked_cat3.get()== heavy):
				if((user_s13.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec36,M8)
				else:
					M8 = round(user_s33.get()*perc8,2)
					string_ann3 = str(M8)
					if(string_ann3[-3] == "."):
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-2] == "."):
						string_ann3 += "0"
						dec_ann3 = str(string_ann3[-3:])
						num_ann3 = str(string_ann3[:-3]) 
						num_ann3 = str(number_format(num_ann3))
					if(string_ann3[-3] != "." and string_ann3[-2] != "."):
						dec_ann3 = ".00"
						num_ann3 = str(number_format(string_ann3))	
					final_ann3 = num_ann3 + dec_ann3 					
					insert_all(txt_spec36,final_ann3)
		#----------Row '4------------
		if(clicked_cat4.get()== select):
			pass
		else:
			string_ann4 = ""
			final_ann4 = ""
			dec_ann4 = ""				
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
				if((user_s43.get()*perc4) < minann4):
					M4 = minann4	
					insert_all(txt_spec46,M4)									
				else:
					M4 = round(user_s43.get()*perc4,2)
					string_ann4 = str(M4)
					if(string_ann4[-3] == "."):
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-2] == "."):
						string_ann4 += "0"
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-3] != "." and string_ann4[-2] != "."):
						dec_ann4 = ".00"
						num_ann4 = str(number_format(string_ann4))	
					final_ann4 = num_ann4 + dec_ann4 					
					insert_all(txt_spec46,final_ann4)					
			if(clicked_cat4.get()== buses):
				if((user_s43.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec46,M5)
				else:
					M5 = round(user_s43.get()*perc5,2)
					string_ann4 = str(M5)
					if(string_ann4[-3] == "."):
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-2] == "."):
						string_ann4 += "0"
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-3] != "." and string_ann4[-2] != "."):
						dec_ann4 = ".00"
						num_ann4 = str(number_format(string_ann4))	
					final_ann4 = num_ann4 + dec_ann4 					
					insert_all(txt_spec46,final_ann4)						
			if(clicked_cat4.get()== mobile):
				if((user_s43.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec46,M6)
				else:
					M6 = round(user_s43.get()*perc6,2)
					string_ann4 = str(M6)
					if(string_ann4[-3] == "."):
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-2] == "."):
						string_ann4 += "0"
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-3] != "." and string_ann4[-2] != "."):
						dec_ann4 = ".00"
						num_ann4 = str(number_format(string_ann4))	
					final_ann4 = num_ann4 + dec_ann4 					
					insert_all(txt_spec46,final_ann4)						
			if(clicked_cat4.get()== brt):
				M7 = minann7
				insert_all(txt_spec46,M7)
			if(clicked_cat4.get()== heavy):
				if((user_s43.get()*perc8) < minann8):
					M8 = minann8
					insert_all(txt_spec46,M4)
				else:
					M8 = round(user_s43.get()*perc8,2)
					string_ann4 = str(M8)
					if(string_ann4[-3] == "."):
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-2] == "."):
						string_ann4 += "0"
						dec_ann4 = str(string_ann4[-3:])
						num_ann4 = str(string_ann4[:-3]) 
						num_ann4 = str(number_format(num_ann4))
					if(string_ann4[-3] != "." and string_ann4[-2] != "."):
						dec_ann4 = ".00"
						num_ann4 = str(number_format(string_ann4))	
					final_ann4 = num_ann4 + dec_ann4 					
					insert_all(txt_spec46,final_ann4)	
				
		#----------Row 5------------
		if(clicked_cat5.get()== select):
			pass
		else:
			string_ann5 = ""
			final_ann5 = ""
			dec_ann5 = ""				
			if(clicked_cat5.get()== cars):
				M1  = minann1			
			if(clicked_cat5.get()== ldv):
				M2 = minann2
			if(clicked_cat5.get()== taxis):
				M3 = minann3
				insert_all(txt_spec56,M3)
			if(clicked_cat5.get()== motors):
				if((user_s53.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec56,M4)
				else:
					M4 = round(user_s53.get()*perc4,2)
					string_ann5 = str(M4)
					if(string_ann5[-3] == "."):
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-2] == "."):
						string_ann5 += "0"
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-3] != "." and string_ann5[-2] != "."):
						dec_ann5 = ".00"
						num_ann5 = str(number_format(string_ann5))	
					final_ann5 = num_ann5 + dec_ann5 					
					insert_all(txt_spec56,final_ann5)						
			if(clicked_cat5.get()== buses):
				if((user_s53.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec56,M5)
				else:
					M5 = round(user_s53.get()*perc5,2)
					string_ann5 = str(M5)
					if(string_ann5[-3] == "."):
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-2] == "."):
						string_ann5 += "0"
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-3] != "." and string_ann5[-2] != "."):
						dec_ann5 = ".00"
						num_ann5 = str(number_format(string_ann5))	
					final_ann5 = num_ann5 + dec_ann5 					
					insert_all(txt_spec56,final_ann5)
			if(clicked_cat5.get()== mobile):
				if((user_s53.get()*perc6) < minann6):
					M6 = minann6
					insert_all(txt_spec56,M6)
				else:
					M6 = round(user_s53.get()*perc6,2)
					string_ann5 = str(M6)
					if(string_ann5[-3] == "."):
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-2] == "."):
						string_ann5 += "0"
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-3] != "." and string_ann5[-2] != "."):
						dec_ann5 = ".00"
						num_ann5 = str(number_format(string_ann5))	
					final_ann5 = num_ann5 + dec_ann5 					
					insert_all(txt_spec56,final_ann5)					
			if(clicked_cat5.get()== brt):
				M7 = minann7
				insert_all(txt_spec56,M7)
			if(clicked_cat5.get()== heavy):
				if((user_s53.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec56,M8)
				else:
					M8 = round(user_s53.get()*perc8,2)
					string_ann5 = str(M8)
					if(string_ann5[-3] == "."):
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-2] == "."):
						string_ann5 += "0"
						dec_ann5 = str(string_ann5[-3:])
						num_ann5 = str(string_ann5[:-3]) 
						num_ann5 = str(number_format(num_ann5))
					if(string_ann5[-3] != "." and string_ann5[-2] != "."):
						dec_ann5 = ".00"
						num_ann5 = str(number_format(string_ann5))	
					final_ann5 = num_ann5 + dec_ann5 					
					insert_all(txt_spec56,final_ann5)
		#----------Row 6------------
		if(clicked_cat6.get()== select):
			pass
		else:
			string_ann6 = ""
			final_ann6 = ""
			dec_ann6 = ""				
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
				if((user_s63.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec66,M4)
				else:
					M4 = round(user_s63.get()*perc4,2)
					string_ann6 = str(M4)
					if(string_ann5[-3] == "."):
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-2] == "."):
						string_ann6 += "0"
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-3] != "." and string_ann6[-2] != "."):
						dec_ann6 = ".00"
						num_ann6 = str(number_format(string_ann6))	
					final_ann6 = num_ann6 + dec_ann6 					
					insert_all(txt_spec66,final_ann6)					
			if(clicked_cat6.get()== buses):
				if((user_s63.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec66,M5)
				else:
					M5 = round(user_s63.get()*perc5,2)
					string_ann6 = str(M5)
					if(string_ann6[-3] == "."):
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-2] == "."):
						string_ann6 += "0"
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-3] != "." and string_ann6[-2] != "."):
						dec_ann6 = ".00"
						num_ann6 = str(number_format(string_ann6))	
					final_ann6 = num_ann6 + dec_ann6 					
					insert_all(txt_spec66,final_ann6)					
			if(clicked_cat6.get()== mobile):
				if((user_s63.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec66,M6)
				else:
					M6 = round(user_s63.get()*perc6,2)
					string_ann6 = str(M6)
					if(string_ann6[-3] == "."):
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-2] == "."):
						string_ann6 += "0"
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-3] != "." and string_ann6[-2] != "."):
						dec_ann6 = ".00"
						num_ann6 = str(number_format(string_ann6))	
					final_ann6 = num_ann6 + dec_ann6 					
					insert_all(txt_spec66,final_ann6)					
			if(clicked_cat6.get()== brt):
				M7 = minann7
				insert_all(txt_spec66,M7)
			if(clicked_cat6.get()== heavy):
				if((user_s63.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec66,M8)
				else:
					M8 = round(user_s63.get()*perc8,2)
					string_ann6 = str(M8)
					if(string_ann6[-3] == "."):
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-2] == "."):
						string_ann6 += "0"
						dec_ann6 = str(string_ann6[-3:])
						num_ann6 = str(string_ann6[:-3]) 
						num_ann6 = str(number_format(num_ann6))
					if(string_ann6[-3] != "." and string_ann6[-2] != "."):
						dec_ann6 = ".00"
						num_ann6 = str(number_format(string_ann6))	
					final_ann6 = num_ann6 + dec_ann6 					
					insert_all(txt_spec66,final_ann5)					
		#----------Row 7------------

		if(clicked_cat7.get()== select):
			pass
		else:
			string_ann7 = ""
			final_ann7 = ""
			dec_ann7 = ""				
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
				if((user_s73.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec76,M4)
				else:
					M4 = round(user_s73.get()*perc4,2)
					string_ann7 = str(M4)
					if(string_ann7[-3] == "."):
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-2] == "."):
						string_ann7 += "0"
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-3] != "." and string_ann7[-2] != "."):
						dec_ann7 = ".00"
						num_ann7 = str(number_format(string_ann7))	
					final_ann7 = num_ann7 + dec_ann7 					
					insert_all(txt_spec76,final_ann7)					
			if(clicked_cat7.get()== buses):
				if((user_s73.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec76,M5)
				else:
					M5 = round(user_s73.get()*perc5,2)
					string_ann7 = str(M5)
					if(string_ann7[-3] == "."):
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-2] == "."):
						string_ann7 += "0"
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-3] != "." and string_ann7[-2] != "."):
						dec_ann7 = ".00"
						num_ann7 = str(number_format(string_ann7))		
					final_ann7 = num_ann7 + dec_ann7 					
					insert_all(txt_spec76,final_ann7)					
			if(clicked_cat7.get()== mobile):
				if((user_s73.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec76,M6)
				else:
					M6 = round(user_s73.get()*perc6,2)
					string_ann7 = str(M6)
					if(string_ann7[-3] == "."):
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-2] == "."):
						string_ann7 += "0"
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-3] != "." and string_ann7[-2] != "."):
						dec_ann7 = ".00"
						num_ann7 = str(number_format(string_ann7))		
					final_ann7 = num_ann7 + dec_ann7 					
					insert_all(txt_spec76,final_ann7)					
			if(clicked_cat7.get()== brt):
				M7 = minann7
			if(clicked_cat7.get()== heavy):
				if((user_s73.get()*perc8) < minann8):
					M8 = minann8
					insert_all(txt_spec76,M8)
				else:
					M8 = round(user_s73.get()*perc8,2)
					string_ann7 = str(M8)
					if(string_ann7[-3] == "."):
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-2] == "."):
						string_ann7 += "0"
						dec_ann7 = str(string_ann7[-3:])
						num_ann7 = str(string_ann7[:-3]) 
						num_ann7 = str(number_format(num_ann7))
					if(string_ann7[-3] != "." and string_ann7[-2] != "."):
						dec_ann7 = ".00"
						num_ann7 = str(number_format(string_ann7))		
					final_ann7 = num_ann7 + dec_ann7 					
					insert_all(txt_spec76,M8) 

		#----------Row 8------------
		if(clicked_cat8.get()== select):
			pass		
		else:
			string_ann8 = ""
			final_ann8 = ""
			dec_ann8 = ""				
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
				if((user_s83.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec86,M4)
				else:
					M4 = round(user_s83.get()*perc4,2)
					string_ann8 = str(M4)
					if(string_ann8[-3] == "."):
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-2] == "."):
						string_ann8 += "0"
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-3] != "." and string_ann8[-2] != "."):
						dec_ann8 = ".00"
						num_ann8 = str(number_format(string_ann8))		
					final_ann8 = num_ann8 + dec_ann8 					
					insert_all(txt_spec86,final_ann8)					
			if(clicked_cat8.get()== buses):
				if((user_s83.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec86,M5)
				else:
					M5 = round(user_s83.get()*perc5,2)
					string_ann8 = str(M5)
					if(string_ann8[-3] == "."):
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-2] == "."):
						string_ann8 += "0"
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-3] != "." and string_ann8[-2] != "."):
						dec_ann8 = ".00"
						num_ann8 = str(number_format(string_ann8))	
					final_ann8 = num_ann8 + dec_ann8 					
					insert_all(txt_spec86,final_ann8)					
			if(clicked_cat8.get()== mobile):
				if((user_s83.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec86,M6)
				else:
					M6 = round(user_s83.get()*perc6,2)
					string_ann8 = str(M6)
					if(string_ann8[-3] == "."):
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-2] == "."):
						string_ann8 += "0"
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-3] != "." and string_ann8[-2] != "."):
						dec_ann8 = ".00"
						num_ann8 = str(number_format(string_ann8))	
					final_ann8 = num_ann8 + dec_ann8 					
					insert_all(txt_spec86,final_ann8)					
			if(clicked_cat8.get()== brt):
				M7 = minann8
				insert_all(txt_spec86,M7)		

				if((user_s83.get()*perc7) < minann7):
					M8 = minann7
					insert_all(txt_spec86,M8)
				else:
					M8 = round(user_s83.get()*perc8,2) 
					string_ann8 = str(M4)
					if(string_ann8[-3] == "."):
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-2] == "."):
						string_ann8 += "0"
						dec_ann8 = str(string_ann8[-3:])
						num_ann8 = str(string_ann8[:-3]) 
						num_ann8 = str(number_format(num_ann8))
					if(string_ann8[-3] != "." and string_ann8[-2] != "."):
						dec_ann8 = ".00"
						num_ann8 = str(number_format(string_ann8))	
					final_ann8 = num_ann8 + dec_ann8 					
					insert_all(txt_spec86,M8)


		#----------Row 9------------
		if(clicked_cat9.get()== select):
			pass
		else:
			string_ann9 = ""
			final_ann9 = ""
			dec_ann9 = ""				
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
				if((user_s93.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec96,M4)
				else:
					M4 = round(user_s93.get()*perc4,2)
					string_ann9 = str(M4)
					if(string_ann9[-3] == "."):
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-2] == "."):
						string_ann9 += "0"
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-3] != "." and string_ann9[-2] != "."):
						dec_ann9 = ".00"
						num_ann9 = str(number_format(string_ann9))	
					final_ann9 = num_ann9 + dec_ann9 					
					insert_all(txt_spec96,final_ann9)					
			if(clicked_cat9.get()== buses):
				if((user_s93.get()*perc) < minann5):
					M5 = minann5
					insert_all(txt_spec96,M5)
				else:
					M5 = round(user_s93.get()*perc5,2)
					string_ann9 = str(M5)
					if(string_ann9[-3] == "."):
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-2] == "."):
						string_ann9 += "0"
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-3] != "." and string_ann9[-2] != "."):
						dec_ann9 = ".00"
						num_ann9 = str(number_format(string_ann9))		
					final_ann9 = num_ann9 + dec_ann9 					
					insert_all(txt_spec96,final_ann9)					
			if(clicked_cat9.get()== mobile):
				if((user_s93.get()*perc6)  < minann6):
					M6 = minann6
					insert_all(txt_spec96,M6)
				else:
					M6 = round(user_s93.get()*perc6,2)
					string_ann9 = str(M6)
					if(string_ann9[-3] == "."):
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-2] == "."):
						string_ann9 += "0"
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-3] != "." and string_ann9[-2] != "."):
						dec_ann9 = ".00"
						num_ann9 = str(number_format(string_ann9))		
					final_ann9 = num_ann9 + dec_ann9 					
					insert_all(txt_spec96,final_ann9)					
			if(clicked_cat3.get()== brt):
				M7 = minann7
				insert_all(txt_spec96,M7)
			if(clicked_cat9.get()== heavy):
				if((user_s93.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec96,M8)
				else:
					M8 = round(user_s93.get()*perc8,2) 
					string_ann9 = str(M8)
					if(string_ann9[-3] == "."):
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-2] == "."):
						string_ann9 += "0"
						dec_ann9 = str(string_ann9[-3:])
						num_ann9 = str(string_ann9[:-3]) 
						num_ann9 = str(number_format(num_ann9))
					if(string_ann9[-3] != "." and string_ann9[-2] != "."):
						dec_ann9 = ".00"
						num_ann9 = str(number_format(string_ann9))		
					final_ann9 = num_ann9 + dec_ann9 					
					insert_all(txt_spec96,final_ann9)					

		#----------Row 10------------
		if(clicked_cat10.get()== select):
			pass
		else:
			string_ann10 = ""
			final_ann10 = ""
			dec_ann10 = ""				
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
				if((user_s33.get()*perc4) < minann4):
					M4 = minann4
					insert_all(txt_spec106,M4)
				else:
					M4 = round(user_s103.get()*perc4,2)
					string_ann10 = str(M4)
					if(string_ann10[-3] == "."):
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-2] == "."):
						string_ann10 += "0"
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-3] != "." and string_ann10[-2] != "."):
						dec_ann10 = ".00"
						num_ann10 = str(number_format(string_ann10))		
					final_ann10 = num_ann10 + dec_ann10 					
					insert_all(txt_spec106,final_ann10)					
			if(clicked_cat10.get()== buses):
				if((user_s103.get()*perc5) < minann5):
					M5 = minann5
					insert_all(txt_spec106,M5)
				else:
					M5 = round(user_s103.get()*perc5,2)
					string_ann10 = str(M5)
					if(string_ann10[-3] == "."):
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-2] == "."):
						string_ann10 += "0"
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-3] != "." and string_ann10[-2] != "."):
						dec_ann10 = ".00"
						num_ann10 = str(number_format(string_ann10))	
					final_ann10 = num_ann10 + dec_ann10 					
					insert_all(txt_spec106,final_ann10)						
			if(clicked_cat103.get()== mobile):
				if((user_s103.get()*perc6) < minann6):
					M6 = minann6
					insert_all(txt_spec106,M6)
				else:
					M6 = round(user_s103.get()*perc6,2)
					string_ann10 = str(M6)
					if(string_ann10[-3] == "."):
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-2] == "."):
						string_ann10 += "0"
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-3] != "." and string_ann10[-2] != "."):
						dec_ann10 = ".00"
						num_ann10 = str(number_format(string_ann10))	
					final_ann10 = num_ann10 + dec_ann10 					
					insert_all(txt_spec106,final_ann10)						
			if(clicked_cat10.get()== brt):
				M7 = minann7
				insert_all(txt_spec106,M7)
			if(clicked_cat10.get()== heavy):
				if((user_s103.get()*perc8)  < minann8):
					M8 = minann8
					insert_all(txt_spec106,M8)
				else:
					M8 = round(user_s103.get()*perc8,2)
					string_ann10 = str(M8)
					if(string_ann10[-3] == "."):
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-2] == "."):
						string_ann10 += "0"
						dec_ann10 = str(string_ann10[-3:])
						num_ann10 = str(string_ann10[:-3]) 
						num_ann10 = str(number_format(num_ann10))
					if(string_ann10[-3] != "." and string_ann10[-2] != "."):
						dec_ann10 = ".00"
						num_ann10 = str(number_format(string_ann10))	
					final_ann10 = num_ann10 + dec_ann10 					
					insert_all(txt_spec106,final_ann10)	


	if (clicked_poltype.get() =="Monthly"):
		#----------Row 1------------
		if(clicked_cat1.get()== select):
			pass
		else:
			string_mon1 = ""
			final_mon1 = ""
			dec_mon1 = ""				
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
				if((user_s13.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec16,M4)
				else:
					M4 = round(user_s13.get()*perc4,2)
					string_mon1 = str(M4)
					if(string_mon1[-3] == "."):
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-2] == "."):
						string_mon1 += "0"
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-3] != "." and string_mon1[-2] != "."):
						dec_mon1 = ".00"
						num_mon1 = str(number_format(string_mon1))	
					final_mon1 = num_mon1 + dec_mon1
					insert_all(txt_spec16,final_mon1)
			if(user_s13.get()== buses):
				if((user_s13.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec16,M5)
				else:
					M5 = round(user_s13.get()*perc5,2)
					string_mon1 = str(M5)
					if(string_mon1[-3] == "."):
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-2] == "."):
						string_mon1 += "0"
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-3] != "." and string_mon1[-2] != "."):
						dec_mon1 = ".00"
						num_mon1 = str(number_format(string_mon1))		
					final_mon1 = num_mon1 + dec_mon1
					insert_all(txt_spec16,final_mon1)					
			if(user_s13.get()== mobile):
				if((user_s13.get()*perc6) < minmon6):
					M6 = minmon6
					insert_all(txt_spec16,M6)
				else:
					M6 = round(user_s13.get()*perc6,2)
					string_mon1 = str(M6)
					if(string_mon1[-3] == "."):
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-2] == "."):
						string_mon1 += "0"
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-3] != "." and string_mon1[-2] != "."):
						dec_mon1 = ".00"
						num_mon1 = str(number_format(string_mon1))		
					final_mon1 = num_mon1 + dec_mon1
					insert_all(txt_spec16,final_mon1)					
			if(clicked_cat1.get()== brt):
				M7 = minmon7
				insert_all(txt_spec15,M7)
			if(clicked_cat1.get()== heavy):
				if((user_s13.get()*perc8) < minmon8):
					M8 = minmon8
					insert_all(txt_spec16,M8)
				else:
					M8 = round(user_s13.get()*perc8,2)
					string_mon1 = str(M8)
					if(string_mon1[-3] == "."):
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-2] == "."):
						string_mon1 += "0"
						dec_mon1 = str(string_mon1[-3:])
						num_mon1 = str(string_mon1[:-3]) 
						num_mon1 = str(number_format(num_mon1))
					if(string_mon1[-3] != "." and string_mon1[-2] != "."):
						dec_mon1 = ".00"
						num_mon1 = str(number_format(string_mon1))		
					final_mon1 = num_mon1 + dec_mon1
					insert_all(txt_spec16,final_mon1)					

		#----------Row 2------------
		if(clicked_cat2.get()== select):
			pass 
		else:
			string_mon2 = ""
			final_mon2 = ""
			dec_mon2 = ""				
			if(clicked_cat2.get()== cars):
				M1  = minmon1
				insert_all(txt_spec26,M1) 		
			if(clicked_cat2.get()== ldv):
				M2 = minmon2
				insert_all(txt_spec26,M2) 
			if(clicked_cat2.get()== taxis):
				M3 = minmon3
				insert_all(txt_spec26,M3)
			if(clicked_cat2.get()== motors):
				if((user_s23.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec26,final_mon1)				
				else:
					M4 = round(user_s23.get()*perc5,2)
					string_mon2 = str(M4)
					if(string_mon2[-3] == "."):
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-2] == "."):
						string_mon2 += "0"
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-3] != "." and string_mon2[-2] != "."):
						dec_mon2 = ".00"
						num_mon2 = str(number_format(string_mon2))		
					final_mon2 = num_mon2 + dec_mon2
					insert_all(txt_spec26,final_mon1)						
			if(clicked_cat2.get()== buses):
				if((user_s23.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec26,M5)
				else:
					M5 = round(user_s23.get()*perc5,2)
					string_mon2 = str(M5)
					if(string_mon2[-3] == "."):
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-2] == "."):
						string_mon2 += "0"
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-3] != "." and string_mon2[-2] != "."):
						dec_mon2 = ".00"
						num_mon2 = str(number_format(string_mon2))		
					final_mon2 = num_mon2 + dec_mon2
					insert_all(txt_spec26,final_mon1)	
			if(clicked_cat2.get()== mobile):
				if((user_s23.get()*perc6) < minmon6):
					M6 = minmon6
					insert_all(txt_spec26,M6)
				else:
					M6 = round(user_s23.get()*perc6,2)
					string_mon2 = str(M6)
					if(string_mon2[-3] == "."):
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-2] == "."):
						string_mon2 += "0"
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-3] != "." and string_mon2[-2] != "."):
						dec_mon2 = ".00"
						num_mon2 = str(number_format(string_mon2))		
					final_mon2 = num_mon2 + dec_mon2
					insert_all(txt_spec26,final_mon1)						
			if(clicked_cat2.get()== brt):
				M7 = minmon7
				insert_all(txt_spec26,M7)
			if(clicked_cat2.get()== heavy):
				if((user_s23.get()*perc8) < minmon8):
					M8 = minmon8
					insert_all(txt_spec26,M8)
				else:
					M8 = round(user_s23.get()*perc8,2) 
					string_mon2 = str(M8)
					if(string_mon2[-3] == "."):
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-2] == "."):
						string_mon2 += "0"
						dec_mon2 = str(string_mon2[-3:])
						num_mon2 = str(string_mon2[:-3]) 
						num_mon2 = str(number_format(num_mon2))
					if(string_mon2[-3] != "." and string_mon2[-2] != "."):
						dec_mon2 = ".00"
						num_mon2 = str(number_format(string_mon2))		
					final_mon2 = num_mon2 + dec_mon2
					insert_all(txt_spec26,final_mon2)						

		#----------Row 3------------
		if(clicked_cat3.get()== select):
			pass
		else:
			string_mon3 = ""
			final_mon3 = ""
			dec_mon3 = ""				
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
				if((user_s33.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec36,M4)
				else:
					M4 = round(user_s33.get()*perc4,2)
					string_mon3 = str(M4)
					if(string_mon3[-3] == "."):
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-2] == "."):
						string_mon3 += "0"
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-3] != "." and string_mon3[-2] != "."):
						dec_mon3 = ".00"
						num_mon3 = str(number_format(string_mon3))		
					final_mon3 = num_mon3 + dec_mon3
					insert_all(txt_spec36,final_mon3)						
			if(clicked_cat3.get()== buses):
				if((user_s33.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec36,M5)
				else:
					M5 = round(user_s33.get()*perc5,2)
					string_mon3 = str(M5)
					if(string_mon3[-3] == "."):
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-2] == "."):
						string_mon3 += "0"
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-3] != "." and string_mon3[-2] != "."):
						dec_mon3 = ".00"
						num_mon3 = str(number_format(string_mon3))	
					final_mon3 = num_mon3 + dec_mon3
					insert_all(txt_spec36,final_mon3)
			if(clicked_cat3.get()== mobile):
				if((user_s33.get()*perc6)  < 200):
					M6 = minmon6
					insert_all(txt_spec36,M6)
				else:
					M6 = round(user_s33.get()*perc6,2)
					string_mon3 = str(M6)
					if(string_mon3[-3] == "."):
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-2] == "."):
						string_mon3 += "0"
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-3] != "." and string_mon3[-2] != "."):
						dec_mon3 = ".00"
						num_mon3 = str(number_format(string_mon3))	
					final_mon3 = num_mon3 + dec_mon3
					insert_all(txt_spec36,final_mon3)					
			if(clicked_cat3.get()== brt):
				M7 = minmon7
				insert_all(txt_spec36,M7)
			if(clicked_cat3.get()== heavy):
				if((user_s13.get()*perc8)  < minmon8):
					M8 = minmon8
					insert_all(txt_spec36,M8)
				else:
					M8 = round(user_s33.get()*perc8,2)
					string_mon3 = str(M6)
					if(string_mon3[-3] == "."):
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-2] == "."):
						string_mon3 += "0"
						dec_mon3 = str(string_mon3[-3:])
						num_mon3 = str(string_mon3[:-3]) 
						num_mon3 = str(number_format(num_mon3))
					if(string_mon3[-3] != "." and string_mon3[-2] != "."):
						dec_mon3 = ".00"
						num_mon3 = str(number_format(string_mon3))	
					final_mon3 = num_mon3 + dec_mon3
					insert_all(txt_spec36,final_mon3)					


		#----------Row '4------------
		if(clicked_cat4.get()== select):
			pass
		else:
			string_mon4 = ""
			final_mon4 = ""
			dec_mon4 = ""				
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
				if((user_s43.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec46,M4)
				else:
					M4 = round(user_s43.get()*perc4,2)
					string_mon4 = str(M4)
					if(string_mon4[-3] == "."):
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-2] == "."):
						string_mon4 += "0"
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-3] != "." and string_mon4[-2] != "."):
						dec_mon4 = ".00"
						num_mon4 = str(number_format(string_mon4))	
					final_mon4 = num_mon4 + dec_mon4
					insert_all(txt_spec46,final_mon4)					
			if(clicked_cat4.get()== buses):
				if((user_s43.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec46,M5)
				else:
					M5 = round(user_s43.get()*perc5,2)
					string_mon4 = str(M5)
					if(string_mon4[-3] == "."):
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-2] == "."):
						string_mon4 += "0"
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-3] != "." and string_mon4[-2] != "."):
						dec_mon4 = ".00"
						num_mon4 = str(number_format(string_mon4))	
					final_mon4 = num_mon4 + dec_mon4
					insert_all(txt_spec46,final_mon4)					
			if(clicked_cat4.get()== mobile):
				if((user_s43.get()*perc6)  < minmon6):
					M6 = minmon6
					insert_all(txt_spec46,M6)
				else:
					M6 = round(user_s43.get()*perc6,2)
					string_mon4 = str(M6)
					if(string_mon4[-3] == "."):
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-2] == "."):
						string_mon4 += "0"
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-3] != "." and string_mon4[-2] != "."):
						dec_mon4 = ".00"
						num_mon4 = str(number_format(string_mon4))	
					final_mon4 = num_mon4 + dec_mon4
					insert_all(txt_spec46,final_mon4)					
			if(clicked_cat4.get()== brt):
				M7 = minmon7
				insert_all(txt_spec46,M7)
			if(clicked_cat4.get()== heavy):
				if((user_s43.get()*perc8)  < minmon8):
					M8 = minmon8
					insert_all(txt_spec46,M8)
				else:
					M8 = round(user_s43.get()*perc8,2)
					string_mon4 = str(M8)
					if(string_mon4[-3] == "."):
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-2] == "."):
						string_mon4 += "0"
						dec_mon4 = str(string_mon4[-3:])
						num_mon4 = str(string_mon4[:-3]) 
						num_mon4 = str(number_format(num_mon4))
					if(string_mon4[-3] != "." and string_mon4[-2] != "."):
						dec_mon4 = ".00"
						num_mon4 = str(number_format(string_mon4))	
					final_mon4 = num_mon4 + dec_mon4
					insert_all(txt_spec46,final_mon4)				 
				
		#----------Row 5------------
		if(clicked_cat5.get()== select):
			pass
		else:
			string_mon5 = ""
			final_mon5= ""
			dec_mon5 = ""				
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
				if((user_s53.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec56,M4)
				else:
					M4 = round(user_s53.get()*perc4,2)
					string_mon5 = str(M4)
					if(string_mon5[-3] == "."):
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-2] == "."):
						string_mon5 += "0"
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-3] != "." and string_mon5[-2] != "."):
						dec_mon5 = ".00"
						num_mon5 = str(number_format(string_mon5))	
					final_mon5 = num_mon5 + dec_mon5
					insert_all(txt_spec56,final_mon5)					
			if(clicked_cat5.get()== buses):
				if((user_s53.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec56,M5)
				else:
					M5 = round(user_s53.get()*perc5,2)
					string_mon5 = str(M5)
					if(string_mon5[-3] == "."):
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-2] == "."):
						string_mon5 += "0"
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-3] != "." and string_mon5[-2] != "."):
						dec_mon5 = ".00"
						num_mon5 = str(number_format(string_mon5))		
					final_mon5 = num_mon5 + dec_mon5
					insert_all(txt_spec56,final_mon5)					
			if(clicked_cat5.get()== mobile):
				if((user_s53.get()*perc6) < minmon6):
					M6 = minmon6
					insert_all(txt_spec56,M6)
				else:
					M6 = round(user_s53.get()*perc6,2)
					string_mon5 = str(M6)
					if(string_mon5[-3] == "."):
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-2] == "."):
						string_mon5 += "0"
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-3] != "." and string_mon5[-2] != "."):
						dec_mon5 = ".00"
						num_mon5 = str(number_format(string_mon5))		
					final_mon5 = num_mon5 + dec_mon5
					insert_all(txt_spec56,final_mon5)					
			if(clicked_cat5.get()== brt):
				M7 = minmon7
				insert_all(txt_spec56,M7)
			if(clicked_cat5.get()== heavy):
				if((user_s53.get()*perc8) < minmon8):
					M8 = minmon8
					insert_all(txt_spec56,M8)
				else:
					M8 = round(user_s53.get()*perc8,2)
					string_mon5 = str(M8)
					if(string_mon5[-3] == "."):
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-2] == "."):
						string_mon5 += "0"
						dec_mon5 = str(string_mon5[-3:])
						num_mon5 = str(string_mon5[:-3]) 
						num_mon5 = str(number_format(num_mon5))
					if(string_mon5[-3] != "." and string_mon5[-2] != "."):
						dec_mon5 = ".00"
						num_mon5 = str(number_format(string_mon5))		
					final_mon5 = num_mon5 + dec_mon5
					insert_all(txt_spec56,final_mon5)	

		#----------Row 6------------
		if(clicked_cat6.get()== select):
			pass
		else:
			string_mon6 = ""
			final_mon6 = ""
			dec_mon6 = ""			
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
				if((user_s63.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec66,M4)
				else:
					M4 = round(user_s63.get()*perc4,2)
					string_mon6 = str(M4)
					if(string_mon6[-3] == "."):
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-2] == "."):
						string_mon6 += "0"
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-3] != "." and string_mon6[-2] != "."):
						dec_mon6 = ".00"
						num_mon6 = str(number_format(string_mon6))		
					final_mon6 = num_mon6 + dec_mon6
					insert_all(txt_spec66,final_mon6)					
			if(clicked_cat6.get()== buses):
				if((user_s63.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec66,M5)
				else:
					M5 = round(user_s63.get()*perc5,2)
					string_mon6 = str(M5)
					if(string_mon6[-3] == "."):
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-2] == "."):
						string_mon6 += "0"
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-3] != "." and string_mon6[-2] != "."):
						dec_mon6 = ".00"
						num_mon6 = str(number_format(string_mon6))	
					final_mon6 = num_mon6 + dec_mon6
					insert_all(txt_spec66,final_mon6)					
			if(clicked_cat6.get()== mobile):
				if((user_s63.get()*perc6) < minmon6):
					M6 = minmon6
					insert_all(txt_spec66,M6)
				else:
					M6 = round(user_s63.get()*perc6,2)
					string_mon6 = str(M6)
					if(string_mon6[-3] == "."):
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-2] == "."):
						string_mon6 += "0"
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-3] != "." and string_mon6[-2] != "."):
						dec_mon6 = ".00"
						num_mon6 = str(number_format(string_mon6))	
					final_mon6 = num_mon6 + dec_mon6
					insert_all(txt_spec66,final_mon6)					
			if(clicked_cat6.get()== brt):
				M7 = minmon7
				insert_all(txt_spec66,M7)
			if(clicked_cat6.get()== heavy):
				if((user_s63.get()*perc8)  < minmon8):
					M8 = minmon8
					insert_all(txt_spec66,M8)
				else:
					M8 = round(user_s63.get()*perc8,2)
					string_mon6 = str(M8)
					if(string_mon6[-3] == "."):
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-2] == "."):
						string_mon6 += "0"
						dec_mon6 = str(string_mon6[-3:])
						num_mon6 = str(string_mon6[:-3]) 
						num_mon6 = str(number_format(num_mon6))
					if(string_mon6[-3] != "." and string_mon6[-2] != "."):
						dec_mon6 = ".00"
						num_mon6 = str(number_format(string_mon6))	
					final_mon6 = num_mon6 + dec_mon6
					insert_all(txt_spec66,final_mon6)					 

		#----------Row 7------------
		if(clicked_cat7.get()== select):
			pass
		else:
			string_mon7 = ""
			final_mon7 = ""
			dec_mon7 = ""			
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
				if((user_s73.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec76,M4)
				else:
					M4 = round(user_s73.get()*perc4,2)
					string_mon7 = str(M4)
					if(string_mon7[-3] == "."):
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-2] == "."):
						string_mon7 += "0"
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-3] != "." and string_mon7[-2] != "."):
						dec_mon7 = ".00"
						num_mon7 = str(number_format(string_mon7))	
					final_mon7 = num_mon7 + dec_mon7
					insert_all(txt_spec76,final_mon7)					
			if(clicked_cat7.get()== buses):
				if((user_s73.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec76,M5)
				else:
					M5 = round(user_s73.get()*perc5,2)
					string_mon7 = str(M5)
					if(string_mon7[-3] == "."):
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-2] == "."):
						string_mon7 += "0"
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-3] != "." and string_mon7[-2] != "."):
						dec_mon7 = ".00"
						num_mon7 = str(number_format(string_mon7))		
					final_mon7 = num_mon7 + dec_mon7
					insert_all(txt_spec76,final_mon7)						
			if(clicked_cat7.get()== mobile):
				if((user_s73.get()*perc6)  < minmon6):
					M6 = minmon6
					insert_all(txt_spec76,M6)
				else:
					M6 = round(user_s73.get()*perc6,2)
					string_mon7 = str(M6)
					if(string_mon7[-3] == "."):
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-2] == "."):
						string_mon7 += "0"
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-3] != "." and string_mon7[-2] != "."):
						dec_mon7 = ".00"
						num_mon7 = str(number_format(string_mon7))		
					final_mon7 = num_mon7 + dec_mon7
					insert_all(txt_spec76,final_mon7)						
			if(clicked_cat7.get()== brt):
				M7 = minmon7
				insert_all(txt_spec76,M7)
			if(clicked_cat7.get()== heavy):
				if((user_s73.get()*perc8)  < minmon8):
					M8 = minmon8
					insert_all(txt_spec76,M8)
				else:
					M8 = round(user_s73.get()*perc8,2) 
					string_mon7 = str(M8)
					if(string_mon7[-3] == "."):
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-2] == "."):
						string_mon7 += "0"
						dec_mon7 = str(string_mon7[-3:])
						num_mon7 = str(string_mon7[:-3]) 
						num_mon7 = str(number_format(num_mon7))
					if(string_mon7[-3] != "." and string_mon7[-2] != "."):
						dec_mon7 = ".00"
						num_mon7 = str(number_format(string_mon7))		
					final_mon7 = num_mon7 + dec_mon7
					insert_all(txt_spec76,final_mon7)		

		#----------Row 8------------
		if(clicked_cat8.get()== select):
			pass
		else:
			string_mon8 = ""
			final_mon8 = ""
			dec_mon8 = ""			
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
				if((user_s83.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec86,M4)
				else:
					M4 = round(user_s83.get()*perc4,2)
					string_mon8 = str(M4)
					if(string_mon8[-3] == "."):
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-2] == "."):
						string_mon8 += "0"
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-3] != "." and string_mon8[-2] != "."):
						dec_mon8 = ".00"
						num_mon8 = str(number_format(string_mon8))		
					final_mon8 = num_mon8 + dec_mon8
					insert_all(txt_spec86,final_mon8)						
			if(clicked_cat8.get()== buses):
				if((user_s83.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec86,M5)
				else:
					M5 = round(user_s83.get()*perc5,2)
					string_mon8 = str(M5)
					if(string_mon8[-3] == "."):
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-2] == "."):
						string_mon8 += "0"
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-3] != "." and string_mon8[-2] != "."):
						dec_mon8 = ".00"
						num_mon8 = str(number_format(string_mon8))		
					final_mon8 = num_mon8 + dec_mon8
					insert_all(txt_spec86,final_mon8)					
			if(clicked_cat8.get()== mobile):
				if((user_s83.get()*perc5)  < minmon6):
					M6 = minmon6
					insert_all(txt_spec86,M6)
				else:
					M6 = round(user_s83.get()*perc6,2)
					string_mon8 = str(M6)
					if(string_mon8[-3] == "."):
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-2] == "."):
						string_mon8 += "0"
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-3] != "." and string_mon8[-2] != "."):
						dec_mon8 = ".00"
						num_mon8 = str(number_format(string_mon8))		
					final_mon8 = num_mon8 + dec_mon8
					insert_all(txt_spec86,final_mon8)					
			if(clicked_cat8.get()== brt):
				M7 = minmon7
				insert_all(txt_spec86,M7)
			if(clicked_cat8.get()== heavy):
				if((user_s83.get()*perc8) < minmon8):
					M8 = minmon8
					insert_all(txt_spec86,M8)
				else:
					M8 = round(user_s83.get()*perc8,2)
					string_mon8 = str(M8)
					if(string_mon8[-3] == "."):
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-2] == "."):
						string_mon8 += "0"
						dec_mon8 = str(string_mon8[-3:])
						num_mon8 = str(string_mon8[:-3]) 
						num_mon8 = str(number_format(num_mon8))
					if(string_mon8[-3] != "." and string_mon8[-2] != "."):
						dec_mon8 = ".00"
						num_mon8 = str(number_format(string_mon8))		
					final_mon8 = num_mon8 + dec_mon8
					insert_all(txt_spec86,final_mon8)					
					insert_all(txt_spec86,M8) 	

		#----------Row 9------------
		if(clicked_cat9.get()== select):
			pass
		else:
			string_mon9 = ""
			final_mon9 = ""
			dec_mon9 = ""			
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
				if((user_s93.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec96,M1)
				else:
					M4 = round(user_s93.get()*perc4,2)
					string_mon9 = str(M4)
					if(string_mon9[-3] == "."):
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-2] == "."):
						string_mon9 += "0"
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-3] != "." and string_mon9[-2] != "."):
						dec_mon9 = ".00"
						num_mon9 = str(number_format(string_mon9))		
					final_mon9 = num_mon9 + dec_mon9
					insert_all(txt_spec96,final_mon9)					
			if(clicked_cat9.get()== buses):
				if((user_s93.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec96,M5)
				else:
					M5 = round(user_s93.get()*perc5,2)
					string_mon9 = str(M5)
					if(string_mon9[-3] == "."):
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-2] == "."):
						string_mon9 += "0"
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-3] != "." and string_mon9[-2] != "."):
						dec_mon9 = ".00"
						num_mon9 = str(number_format(string_mon9))		
					final_mon9 = num_mon9 + dec_mon9
					insert_all(txt_spec96,final_mon9)					
			if(clicked_cat9.get()== mobile):
				if((user_s93.get()*perc6)  < minmon6):
					M6 = minmon6
					insert_all(txt_spec96,M6)
				else:
					M6 = round(user_s93.get()*perc6,2)
					string_mon9 = str(M6)
					if(string_mon9[-3] == "."):
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-2] == "."):
						string_mon9 += "0"
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon8))
					if(string_mon9[-3] != "." and string_mon9[-2] != "."):
						dec_mon9 = ".00"
						num_mon9 = str(number_format(string_mon9))		
					final_mon9 = num_mon9 + dec_mon9
					insert_all(txt_spec96,final_mon9)					
			if(clicked_cat3.get()== brt):
				M7 = minmon7
				insert_all(txt_spec96,M7)
			if(clicked_cat9.get()== heavy):
				if((user_s93.get()*perc8) < minmon8):
					M8 = minmon8
					insert_all(txt_spec96,M8)
				else:
					M8 = round(user_s93.get()*perc8,2)
					string_mon9 = str(M8)
					if(string_mon9[-3] == "."):
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-2] == "."):
						string_mon9 += "0"
						dec_mon9 = str(string_mon9[-3:])
						num_mon9 = str(string_mon9[:-3]) 
						num_mon9 = str(number_format(num_mon9))
					if(string_mon9[-3] != "." and string_mon9[-2] != "."):
						dec_mon9 = ".00"
						num_mon9 = str(number_format(string_mon9))		
					final_mon9 = num_mon9 + dec_mon9
					insert_all(txt_spec96,final_mon9)					

		#----------Row 10------------
		if(clicked_cat10.get()== select):
			pass
		else:
			string_mon10 = ""
			final_mon10 = ""
			dec_mon10 = ""			
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
				if((user_s33.get()*perc4) < minmon4):
					M4 = minmon4
					insert_all(txt_spec106,M4)
				else:
					M4 = round(user_s103.get()*perc4,2)
					string_mon10 = str(M4)
					if(string_mon10[-3] == "."):
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-2] == "."):
						string_mon10 += "0"
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-3] != "." and string_mon10[-2] != "."):
						dec_mon10 = ".00"
						num_mon10 = str(number_format(string_mon10))		
					final_mon10 = num_mon10 + dec_mon10
					insert_all(txt_spec106,final_mon10)					
			if(clicked_cat10.get()== buses):
				if((user_s103.get()*perc5) < minmon5):
					M5 = minmon5
					insert_all(txt_spec106,M5)
				else:
					M5 = round(user_s103.get()*perc5,2)
					string_mon10 = str(M5)
					if(string_mon10[-3] == "."):
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-2] == "."):
						string_mon10 += "0"
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-3] != "." and string_mon10[-2] != "."):
						dec_mon10 = ".00"
						num_mon10 = str(number_format(string_mon10))	
					final_mon10 = num_mon10 + dec_mon10
					insert_all(txt_spec106,final_mon10)					
			if(clicked_cat103.get()== mobile):
				if((user_s103.get()*perc6)  < minmon8):
					M6 = minmon6
					insert_all(txt_spec106,M6)
				else:
					M6 = round(user_s103.get()*perc6,2)
					string_mon10 = str(M6)
					if(string_mon10[-3] == "."):
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-2] == "."):
						string_mon10 += "0"
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-3] != "." and string_mon10[-2] != "."):
						dec_mon10 = ".00"
						num_mon10 = str(number_format(string_mon10))	
					final_mon10 = num_mon10 + dec_mon10
					insert_all(txt_spec106,final_mon10)					
			if(clicked_cat10.get()== brt):
				M7 = minmon7
				insert_all(txt_spec106,M7)
			if(clicked_cat10.get()== heavy):
				if((user_s103.get()*perc8)  < minmon8):
					M8 = minmon8
					insert_all(txt_spec106,M8)
				else:
					M8 = round(user_s103.get()*perc8,2) 
					string_mon10 = str(M8)
					if(string_mon10[-3] == "."):
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-2] == "."):
						string_mon10 += "0"
						dec_mon10 = str(string_mon10[-3:])
						num_mon10 = str(string_mon10[:-3]) 
						num_mon10 = str(number_format(num_mon10))
					if(string_mon10[-3] != "." and string_mon10[-2] != "."):
						dec_mon10 = ".00"
						num_mon10 = str(number_format(string_mon10))	
					final_mon10 = num_mon10 + dec_mon10
					insert_all(txt_spec106,final_mon10)					

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
		R1 = round(user_s13.get()*user_s14.get()/100)
		R1 = number_format(R1)
		insert_all(txt_spec15,R1)
	if (clicked_cat2.get() == select):
		pass
	else:
		R2 = round(user_s23.get()*user_s24.get()/100)
		R2 = number_format(R2)		
		insert_all(txt_spec25,R2)

	if (clicked_cat3.get() == select):
		pass
	else:
		R3 = round(user_s33.get()*user_s34.get()/100)
		R3 = number_format(R3)		
		insert_all(txt_spec35,R3)
	if (clicked_cat4.get() == select):
		pass
	else:
		R4 = round(user_s43.get()*user_s44.get()/100)
		R4 = number_format(R4)		
		insert_all(txt_spec45,R4)
	if (clicked_cat5.get() == select):
		pass
	else:
		R5 = round(user_s53.get()*user_s54.get()/100)
		R5 = number_format(R5)		
		insert_all(txt_spec55,R5)
	if (clicked_cat6.get() == select):
		pass
	else:
		R6 = round(user_s63.get()*user_s64.get()/100)
		R6 = number_format(R6)		
		insert_all(txt_spec65,R6)
	if (clicked_cat7.get() == select):
		pass
	else:
		R7 = user_s73.get()*user_s74.get()/100
		R7 = number_format(R7)
		insert_all(txt_spec75,R7)

	if (clicked_cat8.get() == select):
		pass
	else:
		R8 = round(user_s83.get()*user_s84.get()/100)
		R8 = number_format(R8)		
		insert_all(txt_spec85,R8)
	if (clicked_cat9.get() == select):
		pass
	else:
		R9 = round(user_s93.get()*user_s94.get()/100)
		R9 = number_format(R9)		
		insert_all(txt_spec95,R9)

	if (clicked_cat10.get() == select):
		pass
	else:
		R10 = round(user_s103.get()*user_s104.get()/100)
		R10 = number_format(R10)		
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
	M4 = np.round((user_f42.get()*perc4),2)
	M5 = np.round((user_f52.get()*perc5),2)
	M6 = np.round((user_f62.get()*perc6),2) 
	M7 = 0.0
	M8 = np.round((user_f82.get()*perc8),2)



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

		if(user_f81.get()!=0 and user_f82.get() !=0):
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
	string1 = str(R1)
	if(string1[-3] == "."):
		dec1 = str(string1[-3:])
		num1 = str(string1[:-3]) 
		num1 = str(number_format(num1))
	if(string1[-2] == "."):
		string1 += "0"		
		dec1 = str(string1[-3:])
		num1 = str(string1[:-3]) 
		num1 = str(number_format(num1))
	final1= num1 + dec1

	R2 = np.round(M2 * user_f21.get(),2)
	string2 = str(R2)
	if(string2[-3] == "."):
		dec2 = str(string2[-3:])
		num2 = str(string2[:-3]) 
		num2 = str(number_format(num2))
	if(string2[-2] == "."):
		string2 += "0"		
		dec2 = str(string2[-3:])
		num2 = str(string2[:-3]) 
		num2 = str(number_format(num2))
	final2= num2 + dec2	

	R3 = np.round(M3 *user_f31.get(),2)
	string3 = str(R3)
	if(string3[-3] == "."):
		dec3 = str(string3[-3:])
		num3 = str(string3[:-3]) 
		num3 = str(number_format(num3))
	if(string3[-2] == "."):
		string3 += "0"		
		dec3 = str(string3[-3:])
		num3 = str(string3[:-3]) 
		num3 = str(number_format(num3))
	final3= num3 + dec3	

	R4 = M4
	string4 = str(R4)
	if(string4[-3] == "."):
		dec4 = str(string4[-3:])
		num4 = str(string4[:-3]) 
		num4 = str(number_format(num4))
	if(string4[-2] == "."):
		string4 += "0"		
		dec4 = str(string4[-3:])
		num4 = str(string4[:-3]) 
		num4 = str(number_format(num4))
	final4= num4 + dec4	

	R5 = M5
	string5 = str(R5)
	if(string5[-3] == "."):
		dec5 = str(string5[-3:])
		num5 = str(string5[:-3]) 
		num5 = str(number_format(num5))
	if(string5[-2] == "."):
		string5 += "0"		
		dec5 = str(string5[-3:])
		num5 = str(string5[:-3]) 
		num5 = str(number_format(num5))
	final5= num5 + dec5

	R6 = M6
	string6 = str(R6)
	if(string6[-3] == "."):
		dec6 = str(string6[-3:])
		num6 = str(string6[:-3]) 
		num6 = str(number_format(num6))
	if(string6[-2] == "."):
		string6 += "0"		
		dec6 = str(string6[-3:])
		num6 = str(string6[:-3]) 
		num6 = str(number_format(num6))
	final6= num6 + dec6	

	R7 = M7
	string7 = str(R7)
	if(string7[-3] == "."):
		dec7 = str(string7[-3:])
		num7 = str(string7[:-3]) 
		num7 = str(number_format(num7))
	if(string7[-2] == "."):
		string7 += "0"		
		dec7 = str(string7[-3:])
		num7 = str(string7[:-3]) 
		num7 = str(number_format(num7))
	final7= num7 + dec7	

	R8 = M8	
	string8 = str(R8)
	if(string8[-3] == "."):
		dec8 = str(string8[-3:])
		num8 = str(string8[:-3]) 
		num8 = str(number_format(num8))
	if(string8[-2] == "."):
		string8 += "0"		
		dec8 = str(string8[-3:])
		num8 = str(string8[:-3]) 
		num8 = str(number_format(num8))
	final8= num8 + dec8	

			
	insert_all(txt_fleet15,final1)
	insert_all(txt_fleet25,final2)
	insert_all(txt_fleet35,final3)
	insert_all(txt_fleet45,final4)	
	insert_all(txt_fleet55,final5)
	insert_all(txt_fleet65,final6)
	insert_all(txt_fleet75,final7)
	insert_all(txt_fleet85,final8)

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
	else:
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
			         f"Commercial Vehicles(Mass >3500kg)",0,0,'L')		
			pdf.cell(50,
			         4,
			          f"R{number_format(user_f43.get())}",0,1,'L')

		if(user_f51.get() !=0 and user_f52.get() != 0):
			
			pdf.set_font('Arial','',10)
			pdf.cell(80,
			     	 4,
			         f"{label_buses.cget('text')}",0,0,'L')		
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
		pdf.cell(50,
			     5,
			     f"",0,1,'L')			

		if(user_c11.get() != 0):
			pdf.set_font('Arial','B',11)
			pdf.cell(80,
				     10,
				     "Third Party liability",0,0,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(50,
				     10,
				     f"R{number_format(user_c11.get())}",0,1,'L')	
				
		if((user_c13.get() != "") or
			(user_c14.get() != "") or
			(user_c15.get() != "") or
			(user_c16.get() != "") or
			(user_c17.get() != "") or
			(user_c18.get() != "") or
			(user_c19.get() != "")):
			pdf.set_font('Arial','B',10)
			pdf.cell(80,
			     	 4,
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
			if(user_c19.get() != ""):
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{label_audiosystem.cget('text')}",0,0,'L')
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{user_c19.get()}",0,1,'L')				     						     					
							     								     						     										     												     												     						     					
		pdf.set_font('Arial','B',11)
		pdf.cell(80,
		     	 9,
		     	"Premium Required",0,0,'L')
		pdf.set_font('Arial','',11)
		pdf.cell(80,
		     	 9,
		     	"inclusion of 12.5% commision",0,1,'L')	
		if(clicked_showquoteopt1.get() == 'Yes'):
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
		     	 6,
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
			     	 8,
			     	"Burning Cost",0,1,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 1,
			     	"Burning Cost Basis:",0,0,'L')	
			pdf.set_font('Arial','',11)
			dep = user_depositsplit.get()
			b1 = user_burner1split.get()
			b2 = user_burner2split.get()
			pdf.cell(80,
				 	 1,
					f"{dep}/{b1}/{b2}",
					0,1,'L')
			pdf.cell(80,
				 	 12,"Deposit Premium: ",0,0,'L')	
			pdf.cell(80,
				 	 12,
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
			     	 4,
			     	"If claims reach: ",0,0,'L')
			pdf.cell(80,
			 	 	 4,
			 	 	 f"R{claims_1}",0,1,'L')
			pdf.cell(80,
			     	 5,
			     	"Premium due: ",0,0,'L')
			pdf.cell(80,
			 	 	 5,f"{entry_burner1premopt2.get('1.0',END)}",0,1,'L')

			claims_2 = 0 	 	 			
			if(user_depositsplit.get() + user_burner1split.get() != 100):	
				burner1 = multiply(prem,user_burner1split.get())
				c2 = int((burner1 + depo_prem)*0.6)
				claims_2 = number_format(c2)
			pdf.cell(80,
			     	 7,
			     	"If claims reach: ",0,0,'L')
			pdf.cell(80,
			 	 	 7,
			 	 	 f"R{claims_2}",0,1,'L')
			pdf.cell(80,
			     	 1,
			     	"Premium due: ",0,0,'L')
			pdf.cell(80,
			 	 	 1,f"{entry_burner2premopt2.get('1.0',END)}",0,1,'L')				 	 			 	 						

		if(clicked_showquoteopt3.get() == 'Yes'):
			ann_agg3 = number_format(user_annualaggopt3.get())
			stop_loss3 = number_format(user_stoploss.get())
			pdf.set_font('Arial','',11)
			pdf.cell(120,
			     	 5,
			     	" ",0,1,'L')				
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
			     	 6,
			     	"Annual Aggregate",0,1,'L')
			pdf.set_font('Arial','',11)		
			pdf.cell(80,
			     	 3,
			     	"Annual Aggregate Excess",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(40,
			     	 3,
					f"R{ann_agg3}",0,0,'L')	
			pdf.cell(30,
			     	 3,
			     	"Applicable to: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(20,
			     	 3,
					f"{clicked_appopt3.get()}",0,1,'L')

			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
			     	"Stop Loss Limit: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 5,
					f"R{stop_loss3}",0,1,'L')
			pdf.cell(80,
			     	 7,
			     	"Premium: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 7,
					f"{entry_premonquoteopt3.get('1.0',END)}",0,1,'L')															

		if(clicked_showquoteopt4.get() == 'Yes'):
			ann_agg4 = number_format(user_annualaggopt4.get())
			stop_loss4 = number_format(user_stoplossopt4.get())
			pdf.set_font('Arial','',11)
			pdf.cell(120,
			     	 5,
			     	" ",0,1,'L')				
			pdf.set_font('Arial','U',11)
			pdf.cell(80,
			     	 6,
			     	"Annual Aggregate with Burning Cost",0,1,'L')
			pdf.set_font('Arial','',11)		
			pdf.cell(80,
			     	 3,
			     	"Annual Aggregate Excess",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(40,
			     	 3,
					f"R{ann_agg4}",0,0,'L')	
			pdf.cell(30,
			     	 3,
			     	"Applicable to: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(20,
			     	 3,
					f"{clicked_sectionopt4.get()}",0,1,'L')

			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 7,
			     	"Stop Loss Limit: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 7,
					f"R{stop_loss4}",0,1,'L')
			pdf.cell(120,
			     	 5,
			     	" ",0,1,'L')
			pdf.cell(80,
			     	 7,
			     	"Burning Cost Basis:",0,0,'L')	
			pdf.set_font('Arial','',11)
			dep2 = user_depositsplitopt4.get()
			b3 = user_burner1splitopt4.get()
			b4 = user_burner2splitopt4.get()
			pdf.cell(80,
				 	 7,
					f"{dep2}/{b3}/{b4}",
					0,1,'L')

			pdf.cell(80,
			     	 7,
			     	"Deposit Premium: ",0,0,'L')	
			pdf.set_font('Arial','',11)
			pdf.cell(80,
			     	 7,
					f"{entry_depositpremopt4.get('1.0',END)}",0,1,'L')	
			pdf.cell(120,
			     	 5,
			     	" ",0,1,'L')			

			tfleet = tot_fleet()
			fprem = multiply(tfleet,user_percopt1.get())
			prem  = round_off(clicked_roundopt1.get(),
							 clicked_typerating.get(),
							 fprem)					
			depo_prem = multiply(prem,user_depositsplitopt4.get())

			c1 = int(depo_prem*0.6)
			claims_1 = number_format(c1)
			pdf.cell(80,
			     	 4,
			     	"If claims reach: ",0,0,'L')
			pdf.cell(80,
			 	 	 4,
			 	 	 f"R{claims_1}",0,1,'L')
			pdf.cell(80,
			     	 5,
			     	"Premium due: ",0,0,'L')
			pdf.cell(80,
			 	 	 5,f"{entry_burner1premopt4.get('1.0',END)}",0,1,'L')

			claims_2 = 0 	 	 			
			if(user_depositsplitopt4.get() + user_burner1splitopt4.get() != 100):	
				burner1 = multiply(prem,user_burner1splitopt4.get())
				c2 = int((burner1 + depo_prem)*0.6)
				claims_2 = number_format(c2)
				pdf.cell(80,
			     	     7,
			     	     "If claims reach: ",0,0,'L')
				pdf.cell(80,
			 	 	 	 7,
			 	 	     f"R{claims_2}",0,1,'L')
				pdf.cell(80,
			     	 	 1,
			     	     "Premium due: ",0,0,'L')
				pdf.cell(80,
			 	 	     1,
			 	 	     f"{entry_burner2premopt4.get('1.0',END)}",0,1,'L')

		if(clicked_showspec.get() == 'Yes'):
			if((user_s11.get() != "") or
				(user_s21.get() != "") or
				(user_s31.get() != "") or
				(user_s41.get() != "") or
				(user_s51.get() != "") or
				(user_s61.get() != "") or
				(user_s71.get() != "") or
				(user_s81.get() != "") or
				(user_s91.get() != "") or
				(user_s101.get() != "")):

				pdf.set_font('Arial','B',11)
				pdf.cell(120,
		     			 5,
		     			" ",0,1,'L')					
				pdf.set_font('Arial','B',11)				
				pdf.cell(80,
				     	 5,
				     	 "Specified Vehicles ",0,1,'L')
				pdf.set_font('Arial','BU',11)				
				pdf.cell(80,
				     	 5,
				     	 "Vehicle Description",0,0,'L')
				pdf.cell(50,
				     	 5,
				     	 "Sum Insured",0,0,'L')	
				pdf.cell(50,
				     	 5,
				     	 "Annual Premium",0,1,'L')
				pdf.set_font('Arial','',11)				     	 					     	 			
				if(user_s11.get() != "" ):
					user1 = user_s11.get()
					s1 = user_s13.get()
					sum1 = number_format(s1)
					ann1 = txt_spec15.get('1.0',END)
					if(clicked_cat1.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user1}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum1}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann1}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
		    	              	'Select Option for appropriate specified vehicles row')									 	 				     	 			
	
				if(user_s21.get() != "" ):
					user2 = user_s21.get()
					s2 = user_s23.get()
					sum2 = number_format(s2)
					ann2 = txt_spec25.get('1.0',END)
					if(clicked_cat2.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user2}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum2}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann2}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
		   	              	'Select Option for appropriate specified vehicles row')						
				if(user_s31.get() != "" ):
					user3 = user_s31.get()
					s3 = user_s33.get()
					sum3 = number_format(s3)
					ann3 = txt_spec35.get('1.0',END)
					if(clicked_cat3.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user3}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum3}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann3}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
	    	              	'Select Option for appropriate specified vehicles row')

				if(user_s41.get() != "" ):
					user4 = user_s41.get()
					s4 = user_s43.get()
					sum4 = number_format(s4)
					ann4 = txt_spec45.get('1.0',END)
					if(clicked_cat4.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user4}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum4}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann4}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
	    	              	'Select Option for appropriate specified vehicles row')	

				if(user_s51.get() != "" ):
					user5 = user_s51.get()
					s5 = user_s53.get()
					sum5 = number_format(s5)
					ann5 = txt_spec55.get('1.0',END)
					if(clicked_cat5.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user5}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum5}",0,0,'L')	
						pdf.cell(40,
							 	 4,
							 	 f"{ann5}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
	    	              	'Select Option for appropriate specified vehicles row')	

				if(user_s61.get() != "" ):
					user6 = user_s61.get()
					s6 = user_s63.get()
					sum6 = number_format(s6)
					ann6 = txt_spec65.get('1.0',END)
					if(clicked_cat6.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user6}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum6}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann6}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
	    	              	'Select Option for appropriate specified vehicles row')	

				if(user_s71.get() != "" ):
					user7 = user_s71.get()
					s7 = user_s73.get()
					sum7 = number_format(s7)
					ann7 = txt_spec75.get('1.0',END)
					if(clicked_cat7.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user7}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum7}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann7}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
	    	              	'Select Option for appropriate specified vehicles row')

				if(user_s81.get() != "" ):
					user8 = user_s81.get()
					s8 = user_s83.get()
					sum8 = number_format(s8)
					ann8 = txt_spec85.get('1.0',END)
					if(clicked_cat8.get() != 'Select Option'):
						pdf.cell(80,
					    	 	 4,
					     		 f"{user8}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"R{sum8}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann8}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
		           	      	'Select Option for appropriate specified vehicles row')

				if(user_s91.get() != "" ):
					user9 = user_s91.get()
					s9 = user_s93.get()
					sum9 = number_format(s9)
					ann9 = txt_spec95.get('1.0',END)
					if(clicked_cat9.get() != 'Select Option'):
						pdf.cell(80,
						     	 4,
						     	 f"{user9}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"{sum9}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann9}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
		                	'Select Option for appropriate specified vehicles row')	
				if(user_s101.get() != "" ):
					user10 = user_s101.get()
					s10 = user_s103.get()
					ann10 = txt_spec105.get('1.0',END)
					if(clicked_cat10.get() != 'Select Option'):
						pdf.cell(80,
					    	 	 4,
					    	 	 f"{user10}",0,0,'L')
						pdf.cell(50,
						     	 4,
						     	 f"{sum10}",0,0,'L')	
						pdf.cell(50,
							 	 4,
							 	 f"{ann10}",0,1,'L')	
					else:
						messagebox.showwarning('SASSRIA Category',
		           	      	'Select Option for appropriate specified vehicles row')			    	              			    	              		    	              	    	              			    	              			    	              			    	              							
		pdf.set_font('Arial','B',11)
		pdf.cell(120,
		     	 5,
		     	" ",0,1,'L')
		if((user_excess2.get() != "") or
			(user_theft2.get() != "") or
			(user_windscreen2.get() != "") or
			(user_third2.get() != "") or
			(user_section2.get() != "") or
			(user_loss2.get() != "") or 
			(user_audio2.get() != "")):
			pdf.set_font('Arial','B',10)
			pdf.cell(80,
			     	 4,
			    	f"{label_excess.cget('text')}",0,1,'L')
			pdf.set_font('Arial','',10)
			if(user_excess2.get() != ""):
				pdf.cell(80,
				     	 4,
				     	f"{label_basicexcess2.cget('text')}",0,0,'L')
				pdf.cell(80,
				   	 	 4,
				    	f"{user_excess2.get()}",0,1,'L')
			if(user_theft2.get() != ""):
				pdf.cell(80,
			    	 	 4,
			     		f"{label_theft2.cget('text')}",0,0,'L')
				pdf.cell(80,
			    	 	 4,
			     		f"{user_theft2.get()}",0,1,'L')				     						     					
			if(user_windscreen2.get() != ""):
				pdf.cell(80,
				 		 4,
				  		f"{label_windscreen2.cget('text')}",0,0,'L')
				pdf.cell(80,
					 	 4,
				    	 f"{user_windscreen2.get()}",0,1,'L')	
			if(user_third2.get() != ""):
				pdf.cell(80,
				   	 	 4,
				   		f"{label_thirdparty2.cget('text')}",0,0,'L')
				pdf.cell(80,
				   		 4,
			    		f"{user_third2.get()}",0,1,'L')

			if(user_section2.get() != ""):
				pdf.cell(80,
				   	 	 4,
			    		f"{label_section22.cget('text')}",0,0,'L')
				pdf.set_font('Arial','',10)
				pdf.cell(80,
			    	 	 4,
			     		f"{user_section2.get()}",0,1,'L')	

			if(user_loss2.get() != ""):
				pdf.cell(80,
				     	 4,
				     	f"{label_lossofkeys2.cget('text')}",0,0,'L')
				pdf.set_font('Arial','',10)
				pdf.cell(80,
				     	 4,
				     	f"{user_loss2.get()}",0,1,'L')	

			if(user_audio2.get() != ""):
				pdf.cell(80,
				     	 4,
				     	f"{label_audiosystem2.cget('text')}",0,0,'L')
				pdf.cell(80,
				     	 4,
				     	f"{user_audio2.get()}",0,1,'L')					     					     					
		if(clicked_sasria.get() == 'Yes'):
			pdf.cell(120,
		     		 5,
		     		" ",0,1,'L')
			pdf.cell(120,
		     	 7,
		     	"SASRIA",0,1,'L')
				
			pdf.set_font('Arial','BU',10)
			pdf.cell(80,
			     	 5,
			     	"Fleet Vehicle Category",0,0,'L')
			pdf.cell(30,
			     	 5,
			     	"Units/ Value",0,0,'L')
			pdf.cell(40,
			     	 5,
			     	"SASRIA Rate",0,0,'L')
			pdf.cell(40,
			     	 5,
			     	"SASRIA Premium",0,1,'L')
			sas1 = 0.0
			sas2 = 0.0
			sas3 = 0.0
			sas4 = 0.0
			sas5 = 0.0
			sas6 = 0.0
			sas7 = 0.0
			sas8 = 0.0

			ann_perunit_20 = "R20.18 per unit"
			ann_perunit_45 = "R45.39 per unit"
			mon_perunit_2 = "R2.02 per unit"
			mon_perunit_4 = "R4.54 per unit"			
			value_1879 = f"0.01879% of value"
			value_0504 = f"0.504% of value"
			value_0363 = f"0.363% of value"
			pdf.set_font('Arial','',10)


			if(clicked_poltype.get() == 'Annual'):
				if(user_f11.get() != 0 and user_f12.get() != 0):
					sas1 = user_f11.get()*minann1
					pdf.cell(80,
			    			 4,
			    	 		"Cars- Single Vehicles",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f11.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		ann_perunit_20,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet15.get('1.0',END)}",0,1,'L')			     					     					     							
	
				if(user_f21.get() != 0 and user_f22.get() != 0):
					sas2 = user_f21.get()*minann2
					pdf.cell(80,
				    	 	 4,
			     			"Motorcycles",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f21.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		ann_perunit_45,0,0,'L')
					pdf.cell(40,
				    	 	 4,
				     		f"{txt_fleet25.get('1.0',END)}",0,1,'L')					
	
				if(user_f31.get() != 0 and user_f32.get() != 0):
					sas3 = user_f31.get()*minann3
					pdf.cell(80,
			  	 	 	 	 4,
			   		  		"LDVs",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f31.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		ann_perunit_45,0,0,'L')
					pdf.cell(40,
			    	 		 4,
			     			f"{txt_fleet35.get('1.0',END)}",0,1,'L')						

				if(user_f41.get() != 0 and user_f42.get() != 0):
					sas4 = user_f42.get()*perc4
					if(sas4 < minann4):
						sas4 = minann4						
					pdf.cell(80,
			    		 	 4,
			    	 		"Commercial Vehicles(Mass > 3500kg)",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f41.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_1879,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet45.get('1.0',END)}",0,1,'L')						

				if(user_f51.get() != 0 and user_f52.get() != 0):
					sas5 = user_f52.get()*perc5
					if(sas5 < minann5):
						sas5 = minann5					
					pdf.cell(80,
			    		 	 4,
			    	 		"Buses",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f51.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_0504,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet55.get('1.0',END)}",0,1,'L')					
	
				if(user_f61.get() != 0 and user_f62.get() != 0):
					sas6 = user_f62.get()*perc6
					if(sas6 < minann6):
						sas6 = minann6					
					pdf.cell(80,
			    		 	 4,
			    	 		"Mobile Plants",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f61.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_0363,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet65.get('1.0',END)}",0,1,'L')					

				if(user_f71.get() != 0 and user_f72.get() != 0):
					sas7 = user_f71.get()*minann7
					pdf.cell(80,
			    		 	 4,
						   "Special Types< 3500kg(incl Trailers and Forklifts)",
			    	 		0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f71.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		ann_perunit_45,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet75.get('1.0',END)}",0,1,'L')					

				if(user_f81.get() != 0 and user_f82.get() != 0):
					sas8 = user_f82.get()*perc8
					if(sas8 < minann8):
						sas8 = minann8					
					pdf.cell(80,
			    		 	 4,
			    	 	   "Special Types> 3500kg(incl Trailers and Forklifts)",
			    	 		0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f81.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_1879,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet85.get('1.0',END)}",0,1,'L')

			if(clicked_poltype.get() == 'Monthly'):
				if(user_f11.get() != 0 and user_f12.get() != 0):
					sas1 = user_f11.get()*minmon1
					pdf.cell(80,
			    		 	 4,
			    	 		"Cars- Single Vehicles",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f11.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		mon_perunit_2,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet15.get('1.0',END)}",0,1,'L')			     					     					     							
	
				if(user_f21.get() != 0 and user_f22.get() != 0):
					sas2 = user_f21.get()*minmon2
					pdf.cell(80,
				    	 	 4,
			     			"Motorcycles",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f21.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		mon_perunit_4,0,0,'L')
					pdf.cell(40,
				    	 	 4,
				     		f"{txt_fleet25.get('1.0',END)}",0,1,'L')					
	
				if(user_f31.get() != 0 and user_f32.get() != 0):
					sas3 = user_f31.get()*minmon3
					pdf.cell(80,
			  	 	 	 	 4,
			   		  		"LDVs",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f31.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		mon_perunit_4,0,0,'L')
					pdf.cell(40,
			    	 		 4,
			     			f"{txt_fleet35.get('1.0',END)}",0,1,'L')						

				if(user_f41.get() != 0 and user_f42.get() != 0):
					sas4 = user_f42.get()*perc4
					if (sas4 < minmon4):
						sas4 = minmon4
					pdf.cell(80,
			    		 	 4,
			    	 		"Commercial Vehicles(Mass > 3500)",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f41.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_1879,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet45.get('1.0',END)}",0,1,'L')						

				if(user_f51.get() != 0 and user_f52.get() != 0):
					sas5 = user_f52.get()*perc5
					if(sas5 < minmon5):
						sas5 = minmon5	
					pdf.cell(80,
			    		 	 4,
			    	 		"Buses",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f51.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_0504,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet55.get('1.0',END)}",0,1,'L')					
	
				if(user_f61.get() != 0 and user_f62.get() != 0):
					sas6 = user_f62.get()*perc6
					if(sas6 < minmon6):
						sas6 = minmon6						
					pdf.cell(80,
			    		 	 4,
			    	 		"Mobile Plants",0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f61.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_0363,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet65.get('1.0',END)}",0,1,'L')					

				if(user_f71.get() != 0 and user_f72.get() != 0):
					sas7 = user_f71.get()*minmon7
					pdf.cell(80,
			    		 	 4,
						   "Special Types< 3500kg(incl Trailers and Forklifts)",
			    	 		0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f71.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		mon_perunit_4,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet75.get('1.0',END)}",0,1,'L')					

				if(user_f81.get() != 0 and user_f82.get() != 0):
					sas8 = user_f82.get()*perc8
					if(sas8 < minmon8):
						sas8 = minmon8						
					pdf.cell(80,
			    		 	 4,
			    	 	   "Special Types> 3500kg(incl Trailers and Forklifts)",
			    	 		0,0,'L')
					pdf.cell(30,
			    		 	 4,
			    	 		f"{user_f81.get()}",0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		value_1879,0,0,'L')
					pdf.cell(40,
			    		 	 4,
			    	 		f"{txt_fleet85.get('1.0',END)}",0,1,'L')	

			num = sas1 + sas2 + sas3 +sas4 + sas5 + sas6 + sas7 + sas8	
			final = ""
			dec = ""
			fnum = round(num,2)
			spec1 = 0.0
			spec2 = 0.0
			spec3 = 0.0
			spec4 = 0.0
			spec5 = 0.0
			spec6 = 0.0
			spec7 = 0.0
			spec8 = 0.0
			spec9 = 0.0
			spec10 = 0.0

			if(clicked_showspec.get()=='Yes'):

				pdf.set_font('Arial','BU',10)						
				pdf.cell(150,
		    		 	 6,
		     		   "Specified Vehicles:",
		     			0,1,'L')
				pdf.set_font('Arial','',10)						

				if(clicked_poltype.get()=='Annual'):
					final_rate = ""

					if(clicked_cat1.get()!=select):	
						if(clicked_cat1.get()== cars):
							spec1 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat1.get()== ldv):
							spec1 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat1.get()== taxis):
							spec1 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat1.get()== motors):
							spec1 = round(perc4*user_s13.get(),2)
							if(spec1 < minann4):
								spec1 = minann4			
							final_rate = value_1879

						elif(clicked_cat1.get()== buses):
							spec1 = round(perc5*user_s13.get(),2)
							if(spec1 < minann5):
								spec1 = minann5
							final_rate = value_0504

						elif(clicked_cat1.get()== mobile):
							spec1 = round(perc6*user_s13.get(),2)
							if(spec1 < minann6):
								spec1 = minann6
							final_rate = value_0363

						elif(clicked_cat1.get()== brt):
							spec1 = minann7
							final_rate = ann_perunit_45
						else:
							spec1 = round(perc8* user_s13.get(),2)
							if(spec1 < minann8):
								spec1 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s11.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec16.get('1.0',END)}",0,1,'L')
					if(clicked_cat2.get()!=select):	
						if(clicked_cat2.get()== cars):
							spec2 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat2.get()== ldv):
							spec2 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat2.get()== taxis):
							spec2 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat2.get()== motors):
							spec2 = round(perc4*user_s23.get(),2)
							if(spec2 < minann4):
								spec2 = minann4
							final_rate = value_1879

						elif(clicked_cat2.get()== buses):
							spec2 = round(perc5*user_s23.get(),2)
							if(spec2 < minann5):
								spec2 = minann5
							final_rate = value_0504

						elif(clicked_cat2.get()== mobile):
							spec2 = round(perc6*user_s23.get(),2)
							if(spec2 < minann6):
								spec2 = minann6
							final_rate = value_0363

						elif(clicked_cat2.get()== brt):
							spec2 = minann7
							final_rate = ann_perunit_45

						else:
							spec2 = round(perc8*user_s23.get(),2)
							if(spec2 < minann8):
								spec2 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s21.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    			 	 f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec26.get('1.0',END)}",0,1,'L')
					if(clicked_cat3.get()!=select):	
						if(clicked_cat3.get()== cars):
							spec3 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat3.get()== ldv):
							spec3 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat3.get()== taxis):
							spec3 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat3.get()== motors):
							spec3 = round(perc4*user_s33.get(),2)
							if(spec3 < minann4):
								spec3 = minann4
							final_rate = value_1879

						elif(clicked_cat3.get()== buses):
							spec3 = round(perc5*user_s33.get(),2)
							if(spec3 < minann5):
								spec5 = minann5
							final_rate = value_0504

						elif(clicked_cat3.get()== mobile):
							spec3 = round(perc6*user_s33.get(),2)
							if(spec3 < minann6):
								spec3 = minann6
							final_rate = value_0363

						elif(clicked_cat3.get()== brt):
							spec3 = minann7
							final_rate = ann_perunit_45
						else:
							spec3 = round(perc8*user_s33.get(),2)
							if(spec3 < minann4):
								spec3 = minann4
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s31.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec36.get('1.0',END)}",0,1,'L')	
					if(clicked_cat4.get()!=select):	
						if(clicked_cat4.get()== cars):
							spec4 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat4.get()== ldv):
							spec4 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat4.get()== taxis):
							spec4 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat4.get()== motors):
							spec4 = round(perc4*user_s43.get(),2)
							if(spec4 < minann4):
								spec4 = minann4
							final_rate = value_1879

						elif(clicked_cat4.get()== buses):
							spec4 = round(perc5*user_s43.get(),2)
							if(spec4 < minann5):
								spec4 = minann5
							final_rate = value_0504

						elif(clicked_cat4.get()== mobile):
							spec4 = round(perc6*user_s43.get(),2)
							if(spec4 < minann6):
								spec4 = minann6
							final_rate = value_0363

						elif(clicked_cat4.get()== brt):
							spec4 = minann7
							final_rate = ann_perunit_45
						else:
							spec4 = round(perc8*user_s43.get(),2)
							if(spec4 < minann8):
								spec4 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s41.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec46.get('1.0',END)}",0,1,'L')

					if(clicked_cat5.get()!=select):	
						if(clicked_cat5.get()== cars):
							spec5 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat5.get()== ldv):
							spec5 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat5.get()== taxis):
							spec5 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat5.get()== motors):
							spec5 = round(perc4*user_s53.get(),2)
							if(spec5 < minann4):
								spec5 = minann4
							final_rate = value_1879

						elif(clicked_cat5.get()== buses):
							spec5 = round(perc5*user_s53.get(),2)
							if(spec5 < minann5):
								spec5 = minann5
							final_rate = value_0504

						elif(clicked_cat5.get()== mobile):
							spec5 = round(perc6*user_s53.get(),2)
							if(spec5 < minann6):
								spec5 = minann6
							final_rate = value_0363

						elif(clicked_cat5.get()== brt):
							spec5 = minann7
							final_rate = ann_perunit_45
						else:
							spec5 = round(perc8*user_s53.get(),2)
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s51.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec56.get('1.0',END)}",0,1,'L')

					if(clicked_cat6.get()!=select):	
						if(clicked_cat6.get()== cars):
							spec6 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat6.get()== ldv):
							spec6 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat6.get()== buses):
							spec6 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat6.get()== motors):
							spec6 = round(perc4*user_s63.get(),2)
							if(spec6 < minann4):
								spec6 = minann4
							final_rate = value_1879

						elif(clicked_cat6.get()== buses):
							spec6 = round(perc5*user_s63.get(),2)
							if(spec6 < minann5):
								spec6 = minann5
							final_rate = value_0504

						elif(clicked_cat6.get()== mobile):
							spec6 = round(perc6*user_s63.get(),2)
							if(spec6 < minann6):
								spec6 = minann6
							final_rate = value_0363

						elif(clicked_cat6.get()== brt):
							spec6 = minann7
							final_rate = ann_perunit_45
						else:
							spec6 = round(perc8*user_s63.get(),2)
							if(spec6 < minann8):
								spec6 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s61.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec66.get('1.0',END)}",0,1,'L')			    		 					    		 					    		 							

					if(clicked_cat7.get()!=select):	
						if(clicked_cat7.get()== cars):
							spec7 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat7.get()== ldv):
							spec7 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat7.get()== buses):
							spec7 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat7.get()== motors):
							spec7 = round(perc4*user_s73.get(),2)
							if(spec7 < minann4):
								spec7 = minann4
							final_rate = value_1879

						elif(clicked_cat7.get()== buses):
							spec7 = round(perc5*user_s73.get(),2)
							if(spec7 < minann5):
								spec7 = minann5
							final_rate = value_0504

						elif(clicked_cat7.get()== mobile):
							spec7 = round(perc6*user_s73.get(),2)
							if(spec7 < minann6):
								spec7 = minann6
							final_rate = value_0363

						elif(clicked_cat7.get()== brt):
							spec7 = minann7
							final_rate = ann_perunit_45
						else:
							spec7 = round(perc8*user_s73.get(),2)
							if(spec7 < minann8):
								spec7 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s71.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec76.get('1.0',END)}",0,1,'L')

					if(clicked_cat8.get()!=select):	
						if(clicked_cat8.get()== cars):
							spec8 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat8.get()== ldv):
							spec8 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat8.get()== taxis):
							spec8 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat8.get()== motors):
							spec8 = round(perc4*user_s83.get(),2)
							if(spec8 < minann4):
								spec8 = minann4
							final_rate = value_1879

						elif(clicked_cat8.get()== buses):
							spec8 = round(perc5*user_s83.get(),2)
							if(spec8 < minann5):
								spec8 = minann5
							final_rate = value_0504

						elif(clicked_cat8.get()== mobile):
							spec8 = round(perc6*user_s83.get(),2)
							if(spec8 < minann6):
								spec8 = minann6
							final_rate = value_0363

						elif(clicked_cat8.get()== brt):
							spec8 = minann7
							final_rate = ann_perunit_45
						else:
							spec8 = round(perc8*user_s83.get(),2)
							if(spec8 < minann8):
								spec8 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s81.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec86.get('1.0',END)}",0,1,'L')

					if(clicked_cat9.get()!=select):	
						if(clicked_cat9.get()== cars):
							spec9 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat9.get()== ldv):
							spec9 = minann2
							final_rate = ann_perunit_45

						elif(clicked_cat9.get()== taxis):
							spec9 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat9.get()== motors):
							spec9 = perc4*user_s93.get()
							if(spec9 < minann4):
								spec9 = minann4
							final_rate = value_1879

						elif(clicked_cat9.get()== buses):
							spec9 = round(perc5*user_s93.get(),2)
							if(spec9 < minann5):
								spec9 = minann5
							final_rate = value_0504

						elif(clicked_cat9.get()== mobile):
							spec9 = round(perc6*user_s93.get(),2)
							if(spec9 < minann6):
								spec9 = minann6
							final_rate = value_0363

						elif(clicked_cat9.get()== brt):
							spec9 = minann7
							final_rate = ann_perunit_45
						else:
							spec9 = round(perc8*user_s93.get(),2)
							if(spec9 < minann8):
								spec9 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s91.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec96.get('1.0',END)}",0,1,'L')

					if(clicked_cat10.get()!=select):	
						if(clicked_cat10.get()== cars):
							spec10 = minann1
							final_rate = ann_perunit_20

						elif(clicked_cat10.get()== ldv):
							spec10= minann2
							final_rate = ann_perunit_45

						elif(clicked_cat10.get()== taxis):
							spec10 = minann3
							final_rate = ann_perunit_45

						elif(clicked_cat10.get()== motors):
							spec10 = round(perc4*user_s103.get(),2)
							if(spec10< minann4):
								spec10 = minann4
							final_rate = value_1879

						elif(clicked_cat10.get()== buses):
							spec10 = round(perc5*user_s103.get(),2)
							if(spec10 < minann5):
								spec10 = minann5
							final_rate = value_0504

						elif(clicked_cat10.get()== mobile):
							spec10 = round(perc6*user_s103.get(),2)
							if(spec10 < minann6):
								spec10 = minann6
							final_rate = value_0363

						elif(clicked_cat10.get()== brt):
							spec10 = minann7
							final_rate = ann_perunit_45
						else:
							spec10 = round(perc8*user_s103.get(),2)
							if(spec10 < minann8):
								spec10 = minann8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s101.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec106.get('1.0',END)}",0,1,'L')	 	
				else:
					if(clicked_cat1.get()!=select):	
						if(clicked_cat1.get()== cars):
							spec1 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat1.get()== ldv):
							spec1 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat1.get()== taxis):
							spec1 = minmon3
							final_rate = mon_perunit_2

						elif(clicked_cat1.get()== motors):
							spec1 = round(perc4*user_s13.get(),2)
							if(spec1 < minmon4):
								spec1 = minmon4
							final_rate = value_1879

						elif(clicked_cat1.get()== buses):
							spec1 = round(perc5*user_s13.get(),2)
							if(spec1 < minmon5):
								spec1 = minamon5
							final_rate = value_0504

						elif(clicked_cat1.get()== mobile):
							spec1 = round(perc6*user_s13.get(),2)
							if(spec1 < minmon6):
								spec1 = minmon6
							final_rate = value_0363

						elif(clicked_cat1.get()== brt):
							spec1 = minmon7
							final_rate = mon_perunit_4
						else:
							spec1 = round(perc8*user_s13.get(),2)
							if(spec1 < minmon8):
								spec1 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s11.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec16.get('1.0',END)}",0,1,'L')
					if(clicked_cat2.get()!=select):	
						if(clicked_cat2.get()== cars):
							spec2 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat2.get()== ldv):
							spec2 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat2.get()== taxis):
							spec2 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat2.get()== motors):
							spec2 = round(perc4*user_s23.get(),2)
							if(spec2 < minmon4):
								spec2 = minmon4
							final_rate = value_1879

						elif(clicked_cat2.get()== buses):
							spec2 = round(perc5*user_s23.get(),2)
							if(spec2 < minmon5):
								spec2 = minmon5
							final_rate = value_0504

						elif(clicked_cat2.get()== mobile):
							spec2 = round(perc6*user_s23.get(),2)
							if(spec2 < minmon6):
								spec2 = minmon6
							final_rate = value_0363

						elif(clicked_cat2.get()== brt):
							spec2 = minmon7
							final_rate = mon_perunit_4
						else:
							spec2 = round(perc8*user_s23.get(),2)
							if(spec2 < minmon8):
								spec2 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s21.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec26.get('1.0',END)}",0,1,'L')
					if(clicked_cat3.get()!=select):	
						if(clicked_cat3.get()== cars):
							spec3 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat3.get()== ldv):
							spec3 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat3.get()== taxis):
							spec3 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat3.get()== mootors):
							spec3 = round(perc4*user_s33.get(),2)
							if(spec3 < minmon4):
								spec3 = minmon4
							final_rate = value_1879

						elif(clicked_cat3.get()== buses):
							spec3 = round(perc5*user_s33.get(),2)
							if(spec3 < minann5):
								spec3 = minann5
							final_rate = value_0504

						elif(clicked_cat3.get()== mobile):
							spec3 = round(perc6*user_s33.get(),2)
							if(spec3 < minmon6):
								spec3 = minmon6
							final_rate = value_0363

						elif(clicked_cat3.get()== brt):
							spec3 = minmon7
							final_rate = mon_perunit_4
						else:
							spec3 = round(perc8*user_s33.get(),2)
							if(spec3 < minmon8):
								spec3 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s31.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec36.get('1.0',END)}",0,1,'L')	
					if(clicked_cat4.get()!=select):	
						if(clicked_cat4.get()== cars):
							spec4 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat4.get()== ldv):
							spec4 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat4.get()== taxis):
							spec4 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat4.get()== motors):
							spec4 = round(perc4*user_s43.get(),2)
							if(spec4 < minmon4):
								spec4 = minmon4
							final_rate = value_1879

						elif(clicked_cat4.get()== buses):
							spec4 = round(perc5*user_s43.get(),2)
							if(spec4 < minmon5):
								spec4 = minmon5
							final_rate = value_0504

						elif(clicked_cat4.get()== mobile):
							spec4 = round(perc6*user_s43.get(),2)
							if(spec4 < minmon6):
								spec4 = minmon6
							final_rate = value_0363

						elif(clicked_cat4.get()== brt):
							spec4 = minmon7
							final_rate = mon_perunit_4
						else:
							spec4 = round(perc8*user_s43.get(),2)
							if(spec4 < minmon8):
								spec4 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s41.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec46.get('1.0',END)}",0,1,'L')

					if(clicked_cat5.get()!=select):	
						if(clicked_cat5.get()== cars):
							spec5 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat5.get()== ldv):
							spec5 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat5.get()== taxis):
							spec5 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat5.get()== motors):
							spec5 = round(perc4*user_s53.get(),2)
							if(spec5 < minmon4):
								spec5 = minmon4
							final_rate = value_1879

						elif(clicked_cat5.get()== buses):
							spec5 = round(perc5*user_s53.get(),2)
							if(spec5 < minmon5):
								spec5 = minmon5
							final_rate = value_0504

						elif(clicked_cat5.get()== mobile):
							spec5 = round(perc6*user_s53.get(),2)
							if(spec5 < minmon6):
								spec5 = minmon6
							final_rate = value_0363

						elif(clicked_cat5.get()== brt):
							spec5 = minmon7
							final_rate = mon_perunit_4
						else:
							spec5 = round(perc8*user_s53.get(),2)
							if(spec5 < minmon8):
								spec5 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s51.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec56.get('1.0',END)}",0,1,'L')

					if(clicked_cat6.get()!=select):	
						if(clicked_cat6.get()== cars):
							spec6 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat6.get()== ldv):
							spec6 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat6.get()== taxis):
							spec6 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat6.get()== motors):
							spec6 = round(perc4*user_s63.get(),2)
							if(spec6 < minmon4):
								spec6 = minmon4
							final_rate = value_1879

						elif(clicked_cat6.get()== buses):
							spec6 = round(perc5*user_s63.get(),2)
							if(spec6 < minmon5):
								spec6 = minmon5
							final_rate = value_0504

						elif(clicked_cat6.get()== mobile):
							spec6 = round(perc6*user_s63.get(),2)
							if(spec6 < minmon6):
								spec6 = minmon6
							final_rate = value_0363

						elif(clicked_cat6.get()== brt):
							spec6 = minmon7
							final_rate = mon_perunit_4
						else:
							spec6 = round(perc8*user_s63.get(),2)
							if(spec6 < minmon8):
								spec6 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s61.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec66.get('1.0',END)}",0,1,'L')			    		 					    		 					    		 							

					if(clicked_cat7.get()!=select):	
						if(clicked_cat7.get()== cars):
							spec7 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat7.get()== ldv):
							spec7 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat7.get()== taxis):
							spec7 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat7.get()== motors):
							spec7 = round(perc4*user_s73.get(),2)
							if(spec7 < minmon4):
								spec7 = minmon4
							final_rate = value_1879

						elif(clicked_cat7.get()== buses):
							spec7 = round(perc5*user_s73.get(),2)
							if(spec7 < minmon5):
								spec7 = minmon5
							final_rate = value_0504

						elif(clicked_cat7.get()== mobile):
							spec7 = round(perc6*user_s73.get(),2)
							if(spec7 < minmon6):
								spec7 = minmon6
							final_rate = value_0363

						elif(clicked_cat7.get()== brt):
							spec7 = minmon7
							final_rate = mon_perunit_4
						else:
							spec7 = round(perc8*user_s73.get(),2)
							if(spec7 < minmon8):
								spec7 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s71.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec76.get('1.0',END)}",0,1,'L')

					if(clicked_cat8.get()!=select):	
						if(clicked_cat8.get()== cars):
							spec8 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat8.get()== ldv):
							spec8 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat8.get()== taxis):
							spec8 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat8.get()== motors):
							spec8 = round(perc4*user_s83.get(),2)
							if(spec8 < minmon4):
								spec8 = minmon4
							final_rate = value_1879

						elif(clicked_cat8.get()== buses):
							spec8 = perc5*user_s83.get()
							if(spec8 < minmon5):
								spec8 = minmon5
							final_rate = value_0504

						elif(clicked_cat8.get()== mobile):
							spec8 = round(perc6*user_s83.get(),2)
							if(spec8 < minmon6):
								spec8 = minmon6
							final_rate = value_0363

						elif(clicked_cat8.get()== brt):
							spec8 = minmon7
							final_rate = mon_perunit_4
						else:
							spec8 = round(perc8*user_s83.get(),2)
							if(spec8 < minmon8):
								spec8 = minmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s81.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec86.get('1.0',END)}",0,1,'L')

					if(clicked_cat9.get()!=select):	
						if(clicked_cat9.get()== cars):
							spec9 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat9.get()== ldv):
							spec9 = minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat9.get()== taxis):
							spec9 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat9.get()== motors):
							spec9 = round(perc4*user_s93.get(),2)
							if(spec9 < minmon4):
								spec9 = minnmon4
							final_rate = value_1879

						elif(clicked_cat9.get()== buses):
							spec9 = round(perc5*user_s93.get(),2)
							if(spec9 < minmon5):
								spec9 = minnmon5
							final_rate = value_0504

						elif(clicked_cat9.get()== mobile):
							spec9 = round(perc6*user_s93.get(),2)
							if(spec9 < minmon6):
								spec9 = minnmon6
							final_rate = value_0363

						elif(clicked_cat9.get()== brt):
							spec9 = minmon7
							final_rate = mon_perunit_4
						else:
							spec9 = round(perc8*user_s93.get(),2)
							if(spec9 < minmon8):
								spec9 = minnmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s91.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			  4,
			    		 	f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec96.get('1.0',END)}",0,1,'L')

					if(clicked_cat10.get()!=select):	
						if(clicked_cat10.get()== cars):
							spec10 = minmon1
							final_rate = mon_perunit_2

						elif(clicked_cat10.get()== ldv):
							spec10= minmon2
							final_rate = mon_perunit_4

						elif(clicked_cat10.get()== taxis):
							spec10 = minmon3
							final_rate = mon_perunit_4

						elif(clicked_cat10.get()== motors):
							spec10 = round(perc4*user_s103.get(),2)
							if(spec10 < minmon4):
								spec10 = minnmon4
							final_rate = value_1879

						elif(clicked_cat10.get()== buses):
							spec10 = round(perc5*user_s103.get(),2)
							if(spec10 < minmon5):
								spec10 = minnmon5
							final_rate = value_0504

						elif(clicked_cat10.get()== mobile):
							spec10 = round(perc6*user_s103.get(),2)
							if(spec10 < minmon6):
								spec10 = minnmon6
							final_rate = value_0363

						elif(clicked_cat10.get()== brt):
							spec10 = minmon7
							final_rate = mon_perunit_4
						else:
							spec10 = perc8*user_s103.get()
							if(spec10 < minmon8):
								spec10 = minnmon8
							final_rate = value_1879
						pdf.cell(80,
			    			 	 4,
							   f"{user_s101.get()}",
			    		 		0,0,'L')
						pdf.cell(30,
			    			 	 4,
			    		 		f"1",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{final_rate}",0,0,'L')
						pdf.cell(40,
			    			 	 4,
			    		 		f"{txt_spec106.get('1.0',END)}",0,1,'L')

			whole =fnum + spec1 + spec2 +spec3 +spec4 +spec5 +spec6 + \
	      		 			spec7 + spec8 +spec9 +spec10 
			frac = ""	 					
			string = str(whole)
			if(string[-3] == "."):
				dec = str(string[-3:])
				frac = str(string[:-3]) 
				frac = number_format(frac)
			if(string[-2] == "."):
				string += "0"
				dec = str(string[-3:])
				frac = str(string[:-3]) 
				frac = number_format(frac)
			if(string[-3] != "." and string[-2] != "."):
				dec = ".00"
				frac = number_format(frac)								
			final = frac + dec 						    		 						    			 				    		 					    		 								
			pdf.set_font('Arial','B',11)						
			pdf.cell(150,
			  	 	 7,
			   	   "Total SASRIA premium:",
			   		0,0,'L')
			pdf.set_font('Arial','BU',11)									
			pdf.cell(50,
			   	 	 7,
		    	   f"R{final}",
		    		0,1,'L')
			pdf.set_font('Arial','B',11)
			pdf.cell(180,
			   	 	 15,
		    	    "All figures reflected here are inclusive of VAT at 15%",
		    		0,1,'C')
			pdf.set_font('Arial','',11)
			pdf.cell(70,
			   	 	 7,
		    	   "If you have any queries, please do not hesitate to contact me.",
		    		0,1,'L')
			pdf.cell(70,
			   	 	 7,
		    	   "Kind regards",
		    		0,1,'L')
			pdf.set_font('Arial','',11)
			pdf.cell(70,
			   	 	 7,
		    	   "Grant",
		    		0,1,'L')
		file_name = filedialog.asksaveasfilename(initialdir = "C:/Users/LesediM/Documents/LombardProjects/Project2/Tool/QuotingTool",
												 title = 'Save File',
												 filetypes = (("PDF(*.pdf)","*.pdf"),
												 			 (("All files","*.*"))
												 			 )) 
		if(file_name):
			if(file_name.endswith(".pdf")):
				pass	
			else:
				file_name = f'{file_name}.pdf' 										    													     				     				
		pdf.output(file_name,'F')


	


#------------------Policy Holder Infromation-------------------------------------------

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "File",menu = file_menu)
file_menu.add_command(label="Save",command = validation)

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
label_description = Label(desc_frame,
	                      text = 'Business Description: ' ,
	                      font = 'times 12 bold')
label_operation = Label(desc_frame,
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
label_to.grid(row = 7, column = 2)
label_pol_type.grid(row = 8,column = 0,sticky = W)
label_description.grid(row = 0,column = 0,sticky = W)
label_operation.grid(row = 1,column = 0,sticky = W)

#Text boxes for policyholder information
e_dateofquote = DateEntry(pol_frame, width = 18)
e_dateofquote.grid(row = 3,column = 1,sticky = W) 

e_insured = Entry(pol_frame,
	              textvariable = user_inputinsured,
	              bg = 'light blue',
	              bd = 3)
e_insured.grid(row =4,column = 1,sticky = W)

e_policyno = Entry(pol_frame,
	               textvariable = user_inputpolno,
	               bg = 'light blue',
	               bd = 3)
e_policyno.grid(row =5,column = 1,sticky = W)

e_policyinception = DateEntry(pol_frame,width = 18)
e_policyinception.grid(row =6,column = 1,sticky = W)


e_periodfrom = DateEntry(pol_frame, width = 18)
e_periodfrom.grid(row = 7,column =1,sticky = W)

e_periodto = DateEntry(pol_frame,width = 18)
e_periodto.grid(row = 7,column = 3,sticky = W)

e_description = Entry(desc_frame,
	                  textvariable = user_inputdesc,
	                  bg = 'light blue',
	                  bd = 3,
	                  width = 70)
e_description.grid(row = 0,column = 1)

e_operation = Entry(desc_frame,
	                textvariable = user_inputoper,
	                bg = 'light blue',
	                bd = 3,
	                width = 70)
e_operation.grid(row =1,column = 1)

#Dropdown menus for policy information
clicked_type = StringVar(pol_frame)
clicked_type.set('Select Option')
menu_type = OptionMenu(pol_frame,
                       clicked_type,
                       'Renewal',
                       'New Business ')
menu_type.grid(row=2,column = 1,sticky = W)

clicked_poltype = StringVar(pol_frame)
clicked_poltype.set('Select Option')
menu_poltype = OptionMenu(pol_frame, clicked_poltype,'Annual','Monthly')
menu_poltype.grid(row=8,column = 1,sticky = W) 

#--------------------Fleet Information---------------------------------------------------

label_fleet = Label(fleet_frame,text = 'Fleet Information',
	                font = 'times 20 bold underline',
	                anchor = 'w')
label_fleet.grid(row = 0,column = 0,sticky = W)

label_sasria = Label(fleet_frame,
	                     text ='Show SASRIA',
	                     font = 'times 12')
clicked_sasria = StringVar(fleet_frame)
clicked_sasria.set('No')
menu_sasria = OptionMenu(fleet_frame,
						 clicked_sasria,
						 'Yes',
						 'No')
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
label_buses = Label(fleet_frame,text ='Buses',
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
label_sasria.grid(row = 1, column = 0,sticky = W)
label_vcategory.grid(row = 2,column = 0,sticky = W)
label_cars.grid(row = 3,column = 0,sticky = W)
label_motocycles.grid(row = 4,column = 0,sticky = W)
label_ldvs.grid(row = 5,column = 0,sticky = W)
label_commercial.grid(row = 6,column = 0,sticky = W)
label_buses.grid(row = 7,column = 0,sticky = W)
label_mobile.grid(row = 8,column = 0,sticky = W)
label_specialless.grid(row = 9,column = 0,sticky = W)
label_specialmore.grid(row = 10,column = 0,sticky = W)
label_total.grid(row = 11,column = 0,sticky = W)

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

label_units.grid(row = 2,column = 1)
label_value.grid(row = 2,column = 2)
label_damage.grid(row = 2,column = 3)
label_sasria_des.grid(row = 2,column = 4)
label_sasria_prem.grid(row = 2,column = 5)

menu_sasria.grid(row = 1,column = 1, sticky = W)
e_fleet11 = Entry(fleet_frame,
	                  textvariable = user_f11,
	                  width = 10,
	                  bg = 'light blue',
	                  bd = 3).grid(row = 3,column=1)
e_fleet12 = Entry(fleet_frame,
	                  textvariable = user_f12,
	                  bg = 'light blue',
	                  bd = 3).grid(row = 3,column=2)
e_fleet13 = Entry(fleet_frame,
	              textvariable = user_f13,
	              bg = 'light blue',
	              bd = 3).grid(row = 3,column=3)
txt_fleet14 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet14.insert(INSERT,"Cars(Primary use: Domestic/ private)")
txt_fleet14.configure(state = 'disabled')
txt_fleet14.grid(row = 3,column=4)

txt_fleet15 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet15.grid(row = 3,column=5)

e_fleet21 = Entry(fleet_frame,
	              textvariable = user_f21,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 4,column=1)
e_fleet22 = Entry(fleet_frame,
	              textvariable = user_f22,
	              bg = 'light blue',
	              bd = 3).grid(row = 4,column=2) 
e_fleet23 = Entry(fleet_frame,
	              textvariable = user_f23,
	              bg = 'light blue',
	              bd = 3).grid(row = 4,column=3)
txt_fleet24 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet24.insert(INSERT,"LDV(Commercial use)")
txt_fleet24.configure(state = 'disabled')
txt_fleet24.grid(row = 4,column=4)

txt_fleet25 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet25.grid(row = 4,column=5)

e_fleet31 = Entry(fleet_frame,
	              textvariable = user_f31,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 5,column=1)
e_fleet32 = Entry(fleet_frame,
	              textvariable = user_f32,
	              bg = 'light blue',
	              bd = 3).grid(row = 5,column=2)
e_fleet33 = Entry(fleet_frame,
	              textvariable = user_f33,
	              bg = 'light blue',
	              bd = 3).grid(row = 5,column=3)
txt_fleet34 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet34.insert(END,"LDV(Commercial use)")
txt_fleet34.configure(state = 'disabled')
txt_fleet34.grid(row = 5,column=4)

txt_fleet35 =Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet35.grid(row = 5,column=5)

e_fleet41 = Entry(fleet_frame,
	              textvariable = user_f41,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 6,column=1)
e_fleet42 = Entry(fleet_frame,
	               textvariable = user_f42,
	               bg = 'light blue',
	               bd = 3).grid(row = 6,column=2)
e_fleet43 = Entry(fleet_frame,
	              textvariable = user_f43,
	              bg = 'light blue',
	              bd = 3).grid(row = 6,column=3)
txt_fleet44 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet44.insert(INSERT,"Heavy Commercial Vehicles (>3,500kg)")
txt_fleet44.configure(state = 'disabled')
txt_fleet44.grid(row = 6,column=4)

txt_fleet45 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet45.grid(row = 6,column=5)

e_fleet51 = Entry(fleet_frame,
	               textvariable = user_f51,
	               bg = 'light blue',
	               width = 10,
	               bd = 3).grid(row = 7,column=1)
e_fleet52 = Entry(fleet_frame,
	              textvariable = user_f52,
	              bg = 'light blue',
	              bd = 3).grid(row = 7,column=2)
e_fleet53 = Entry(fleet_frame,
	              textvariable = user_f53,
	              bg = 'light blue',
	              bd = 3).grid(row = 7,column=3)
txt_fleet54 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet54.insert(INSERT,"Buses")
txt_fleet54.configure(state = 'disabled')
txt_fleet54.grid(row = 7,column=4)
txt_fleet55 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet55.grid(row = 7,column=5)

e_fleet61 = Entry(fleet_frame,
	              textvariable = user_f61,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 8,column=1)
e_fleet62 = Entry(fleet_frame,
	              textvariable = user_f62,
	              bg = 'light blue',
	              bd = 3).grid(row = 8,column=2)
e_fleet63 = Entry(fleet_frame,
	              textvariable = user_f63,
	              bg = 'light blue',
	              bd = 3).grid(row = 8,column=3)
txt_fleet64 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet64.insert(INSERT,"Mobile Plant")
txt_fleet64.configure(state = 'disabled')
txt_fleet64.grid(row = 8,column=4)
txt_fleet65 =Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet65.grid(row = 8,column=5)

e_fleet71 = Entry(fleet_frame,
	              textvariable = user_f71,
	              bg = 'light blue',
	              width = 10,
	              bd = 3).grid(row = 9,column=1)
e_fleet72 = Entry(fleet_frame,
	              textvariable = user_f72,
	              bg = 'light blue',
	              bd = 3).grid(row = 9,column=2)
e_fleet73 = Entry(fleet_frame,
	              textvariable = user_f73,
	              bg = 'light blue',
	              bd = 3).grid(row = 9,column=3)
txt_fleet74 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet74.insert(INSERT,"LDV(Commercial use)")
txt_fleet74.configure(state = 'disabled')
txt_fleet74.grid(row = 9,column=4)
txt_fleet75 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet75.grid(row = 9,column=5)

e_fleet81 = Entry(fleet_frame,
	              textvariable = user_f81,
	              width = 10,
	              bg = 'light blue',
	              bd = 3).grid(row = 10,column=1)
e_fleet82 = Entry(fleet_frame,
	              textvariable = user_f82,
	              bg = 'light blue',
	              bd = 3).grid(row = 10,column=2)
e_fleet83 = Entry(fleet_frame,
	              textvariable = user_f83,
	              bg = 'light blue',
	              bd = 3).grid(row = 10,column=3)
txt_fleet84 = Text(fleet_frame,
	               height = 0.1,
	               width = 36,
	               bd = 3)
txt_fleet84.insert(INSERT,"Heavy Commercial(>3,500kg)")
txt_fleet84.configure(state = 'disabled')
txt_fleet84.grid(row = 10,column=4)
txt_fleet85 = Text(fleet_frame,
	              width = 18,
	              height = 0.1,
	              bd = 3)
txt_fleet85.grid(row = 10,column=5)

txt_fleet91 = Text(fleet_frame,
	              width = 8,
	              height = 0.1,
	              bd = 6)
txt_fleet91.grid(row = 11,column=1)
txt_fleet92 = Text(fleet_frame,
	               width =15,
	               height = 0.1,
	               bd = 6)
txt_fleet92.grid(row = 11,column=2)

button_totfleet = Button(fleet_frame, text="Total", command=add_fleet)
button_totfleet.grid(row = 11, column = 3)


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
label_audiosystem.grid(row = 10, column = 0, sticky = W)

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
e_audiosystem = Entry(cover_frame,
	                     width = 30,
	                     bg = 'light blue',
	                     textvariable = user_c19,
	                     bd = 3).grid(row = 10, column =1)

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

user_s11 = StringVar(specified_frame)
e_spec11 = Entry(specified_frame,
				 textvariable = user_s11,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=3,
                                   column = 2)
user_s13 = IntVar(specified_frame)
e_spec13 = Entry(specified_frame,
	             textvariable = user_s13,
	             bg = 'light blue',
	             bd = 3)
e_spec13.grid(row = 3,column = 3,sticky = W)

user_s14 = IntVar(specified_frame)
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

user_s21 = StringVar(specified_frame)
e_spec21 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s21,
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
                       buses,
                       mobile,
                       brt,
                       heavy,
                       command = add_spec).grid(row=4,
                                   column = 2)
user_s23 = IntVar(specified_frame)
e_spec23 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s23)
e_spec23.grid(row = 4, column = 3,sticky = W)

user_s24 = IntVar(specified_frame)
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

user_s31 = StringVar(specified_frame)
e_spec31 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s31,
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
                       buses,
                       mobile,
                       brt,
                       heavy)
menu_cat3.grid(row=5,column = 2)

user_33 = IntVar(specified_frame)
e_spec33 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s33)
e_spec33.grid(row = 5,column = 3,sticky = W)

user_s34 = IntVar(specified_frame)
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

user_s41 = StringVar(specified_frame)
e_spec41 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s41,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=6,column = 2)

user_s43 = IntVar(specified_frame)
e_spec43 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s43)
e_spec43.grid(row = 6,column = 3,sticky = W)

user_s44 = IntVar(specified_frame)
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

user_s51 = StringVar(specified_frame)
e_spec51 = Entry(specified_frame,
				 bd = 3,
				 textvariable = user_s51,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=7,column = 2)

user_s53 = IntVar(specified_frame)
e_spec53 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s53,
	             bd = 3)
e_spec53.grid(row = 7, column = 3,sticky = W)

user_s54 = IntVar(specified_frame)
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

user_s61 = StringVar(specified_frame)
e_spec61 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s61,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=8,column = 2)
user_s63 = IntVar(specified_frame)
e_spec63 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s63)
e_spec63.grid(row = 8, column = 3, sticky = W)

user_s64 = IntVar(specified_frame)
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

user_s71 = StringVar(specified_frame)
e_spec71 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s71,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=9,column = 2)

user_s73 = IntVar(specified_frame)
e_spec73 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s73)
e_spec73.grid(row = 9, column = 3,sticky = W)

user_s74 = IntVar(specified_frame)
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

user_s81 = StringVar(specified_frame)
e_spec81 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s81,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=10,column = 2)

user_s83 = IntVar(specified_frame)
e_spec83 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s83)
e_spec83.grid(row = 10, column = 3, sticky = W)

user_s84 = IntVar(specified_frame)
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

user_s91 = StringVar(specified_frame)
e_spec91 = Entry(specified_frame,
				 textvariable = user_s91,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=11,
                                   column = 2)
user_s93 = IntVar(specified_frame)                       
e_spec93 = Entry(specified_frame,
	             bg = 'light blue',
	             bd = 3,
	             textvariable = user_s93)
e_spec93.grid(row = 11, column = 3, sticky = W)

user_s94 = IntVar(specified_frame)
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

user_s101 = StringVar(specified_frame)
e_spec101 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s101,
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
                       buses,
                       mobile,
                       brt,
                       heavy).grid(row=12,
                                   column = 2)
user_s103 = IntVar(specified_frame)                       
e_spec103 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_s103,
	             bd = 3)
e_spec103.grid(row = 12,column = 3,sticky = W)

user_s104 = IntVar(specified_frame)
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
txt_spec66 = Text(specified_frame,
	               height = 0.1,
	               bd = 3,
	               width = 15)
txt_spec66.grid(row = 13, column = 6, sticky = W)



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
label_audiosystem2.grid(row = 21,column = 0,sticky = W)

user_excess2 = StringVar(specified_frame)
e_excess2 = Entry(specified_frame,
	              bg = 'light blue',
	              textvariable = user_excess2,
	              bd = 3,
	              width = 30)
e_excess2.grid(row = 15, column =1)

user_theft2 = StringVar(specified_frame)
e_theft2 = Entry(specified_frame,
	             bg = 'light blue',
	             textvariable = user_theft2,
	             bd = 3,
	             width = 30)
e_theft2.grid(row = 16, column =1)

user_windscreen2 = StringVar(specified_frame)
e_windscreen2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  textvariable = user_windscreen2,
	                  bd = 3,
	                  width = 30)
e_windscreen2.grid(row = 17, column =1)

user_third2 = StringVar(specified_frame)
e_thirdparty2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  textvariable = user_third2,
	                  bd = 3,
	                  width = 30)
e_thirdparty2.grid(row = 18, column =1)

user_section2 = StringVar(specified_frame)
e_section22 = Entry(specified_frame,
	                bg = 'light blue',
	                textvariable = user_section2,
	                bd = 3,
	                width = 30)
e_section22.grid(row = 19, column =1)

user_loss2 = StringVar(specified_frame)
e_lossofkeys2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  textvariable = user_loss2,
	                  bd = 3,
	                  width = 30)
e_lossofkeys2.grid(row = 20, column =1)

user_audio2 = StringVar(specified_frame)
e_audiosystem2 = Entry(specified_frame,
	                  bg = 'light blue',
	                  textvariable = user_audio2,
	                  bd = 3,
	                  width = 30)
e_audiosystem2.grid(row = 21, column =1)




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
menu_type = OptionMenu(option1_frame, clicked_typerating,'R1 000','R10 000','R100 000')
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

user_premonquote2 = IntVar(option3_frame)
entry_premonquote2opt3 = Entry(option3_frame,
							   textvariable = user_premonquote2,
							   bg = 'light blue',
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
entry_premloadingopt4 = Entry(option4_frame,
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


root.mainloop()