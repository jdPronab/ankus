import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

base = tk.Tk()  
base.geometry('800x600')
base.resizable(width=False, height=False)  
base.title("ARIKA")
base.columnconfigure(0, weight=1)

# man_loggedin = tk.BooleanVar()
# emp_loggedin = tk.BooleanVar()

IMG = Image.open("arika.jpeg")

def show_home():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	heading = ttk.Label(view_board, text="HOME", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	IMG = Image.open("arika.jpeg")
	resized_hero_img = IMG.resize((250, 100))
	hero_img = ImageTk.PhotoImage(resized_hero_img)
	hero_img_label = ttk.Label(view_board, image = hero_img)
	hero_img_label.grid(row=1, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	tk.Button(view_board, text='Manager Login',width=20,bg='brown',fg='white', command=manager_login_view).grid(row=2, column=0)
	tk.Button(view_board, text='Employee Login',width=20,bg='brown',fg='white', command=employee_login_view).grid(row=3, column=0)
	view_board.grid(row=1, column=0, sticky=(tk.N + tk.S), pady=20)


nav_panel = tk.Frame(base)
nav_panel.columnconfigure(0, weight=1) 
tk.Button(nav_panel, text='Home', width=10,bg='brown',fg='white', command=show_home).pack(side=tk.LEFT)
tk.Button(nav_panel, text='Back', width=10,bg='brown',fg='white').pack(side=tk.LEFT)
img = IMG.resize((100, 40))
img = ImageTk.PhotoImage(img)
img_label = ttk.Label(nav_panel, image = img)
img_label.pack(side=tk.RIGHT, ipady=5, ipadx=5)
nav_panel.grid(row=0, column=0, sticky=(tk.E + tk.W))   



def show_gen_report():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="GENERATE REPORT", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Employee ID:")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5) 

	# password
	password_label = ttk.Label(view_board, text="Includes:")
	password_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

	password_entry = ttk.Entry(view_board,  show="*")
	password_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	# login button
	login_button = ttk.Button(view_board, text="Apply")
	login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
	login_button = ttk.Button(view_board, text="Reset")
	login_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)


def add_employee_form():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="ADD EMPLOYEE", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	form_row = tk.Frame(view_board)

	left_col = tk.Frame(form_row)
	left_col.columnconfigure(0, weight=1)
	heading = ttk.Label(left_col, text="Customer information", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	id_label = ttk.Label(left_col, text="Employee ID")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	id_entry = ttk.Entry(left_col)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	firstname_label = ttk.Label(left_col, text="First Name")
	firstname_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	firstname_entry = ttk.Entry(left_col)
	firstname_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	lastname_label = ttk.Label(left_col, text="Last Name")
	lastname_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	lastname_entry = ttk.Entry(left_col)
	lastname_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	phone_label = ttk.Label(left_col, text="Phone")
	phone_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	phone_entry = ttk.Entry(left_col)
	phone_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	email_label = ttk.Label(left_col, text="Phone")
	email_label.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
	email_entry = ttk.Entry(left_col)
	email_entry.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
	left_col.grid(row=0, column=0, sticky=tk.E, pady=20)

	right_col = tk.Frame(form_row)
	right_col.columnconfigure(0, weight=1)
	heading = ttk.Label(right_col, text="Post details", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	depart_label = ttk.Label(right_col, text="Department")
	depart_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	depart_entry = ttk.Entry(right_col)
	depart_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	post_label = ttk.Label(right_col, text="Post")
	post_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	post_entry = ttk.Entry(right_col)
	post_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
	right_col.grid(row=0, column=1, sticky=(tk.N+tk.S), pady=20)

	save_emp_button = ttk.Button(form_row, text="Save Employee")
	save_emp_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
	form_row.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)


def show_event_details():
	for child in base.winfo_children()[1:]:
		child.destroy()

	event_list = ['Customer', 'Employee', 'Hotel', 'Vendor', 'Dates', 'Budget', 'Advance Paid', 'Remaining Balance']
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="EVENT DETAILS", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	button_row = 0 
	for i in range(len(event_list)):
		row = i + 1
		label = ttk.Label(view_board, text=event_list[i])
		label.grid(column=0, row=row, sticky=tk.E, padx=5, pady=5)
		extra_label = ttk.Label(view_board, text="")
		extra_label.grid(column=1, row=row, sticky=tk.E, padx=5, pady=5)
		button_row = row
	done_button = ttk.Button(view_board, text="Done", command=show_home)
	done_button.grid(column=1, row=button_row + 1, sticky=tk.E, padx=5, pady=5) 
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def event_status_form():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="EVENT STATUS", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Event ID")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
	give_details_button = ttk.Button(view_board, text="Give Details", command=show_event_details)
	give_details_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5) 
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)


def add_customer_form():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="ADD CUSTOMER", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	form_row = tk.Frame(view_board)

	left_col = tk.Frame(form_row)
	left_col.columnconfigure(0, weight=1)
	heading = ttk.Label(left_col, text="Customer information", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	id_label = ttk.Label(left_col, text="Customer ID")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	id_entry = ttk.Entry(left_col)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	firstname_label = ttk.Label(left_col, text="First Name")
	firstname_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	firstname_entry = ttk.Entry(left_col)
	firstname_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	lastname_label = ttk.Label(left_col, text="Last Name")
	lastname_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	lastname_entry = ttk.Entry(left_col)
	lastname_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	phone_label = ttk.Label(left_col, text="Phone")
	phone_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	phone_entry = ttk.Entry(left_col)
	phone_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	email_label = ttk.Label(left_col, text="Phone")
	email_label.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
	email_entry = ttk.Entry(left_col)
	email_entry.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
	left_col.grid(row=0, column=0, sticky=tk.E, pady=20)

	right_col = tk.Frame(form_row)
	right_col.columnconfigure(0, weight=1)
	heading = ttk.Label(right_col, text="Customer Address", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	flatno_label = ttk.Label(right_col, text="Flat No")
	flatno_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	flatno_entry = ttk.Entry(right_col)
	flatno_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	apartment_label = ttk.Label(right_col, text="Apartment")
	apartment_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	apartment_entry = ttk.Entry(right_col)
	apartment_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	area_label = ttk.Label(right_col, text="Area")
	area_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	area_entry = ttk.Entry(right_col)
	area_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	city_label = ttk.Label(right_col, text="City")
	city_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	city_entry = ttk.Entry(right_col)
	city_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
	right_col.grid(row=0, column=1, sticky=(tk.N+tk.S), pady=20)

	save_cus_button = ttk.Button(form_row, text="Save Customer")
	save_cus_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
	form_row.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def show_suggested_prop():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	view_board.columnconfigure(0, weight=1)
	tv = ttk.Treeview(view_board, columns=['city', 'budget', 'capacity'], selectmode='none')
	tv.heading('#0', text='Hotel', anchor='center')
	tv.heading('city', text='City', anchor='center')
	tv.heading('budget', text='Budget', anchor='center')
	tv.heading('capacity', text='Capacity', anchor='center')
	tv.column('#0', width=130)
	tv.column('city', width=130)
	tv.column('budget', width=130)
	tv.column('capacity', width=130)
	tv.grid(row=0, column=0, sticky=(tk.E + tk.W + tk.N + tk.S))
	btn = tk.Frame(view_board)
	copy_save_button = ttk.Button(btn, text="Copy and Save Details")
	copy_save_button.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	btn.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)

def add_event_form():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="NEW EVENT", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	form_row = tk.Frame(view_board)

	left_col = tk.Frame(form_row)
	left_col.columnconfigure(0, weight=1)
	heading = ttk.Label(left_col, text="Event information", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	id_label = ttk.Label(left_col, text="Event ID")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	id_entry = ttk.Entry(left_col)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	cust_id_label = ttk.Label(left_col, text="Customer ID")
	cust_id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	cust_id_entry = ttk.Entry(left_col)
	cust_id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	emp_id_label = ttk.Label(left_col, text="Employee ID")
	emp_id_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	emp_id_entry = ttk.Entry(left_col)
	emp_id_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	event_type_label = ttk.Label(left_col, text="Event type")
	event_type_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	event_type_entry = ttk.Entry(left_col)
	event_type_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	capa_label = ttk.Label(left_col, text="Capacity")
	capa_label.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
	capa_entry = ttk.Entry(left_col)
	capa_entry.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
	left_col.grid(row=0, column=0, sticky=tk.E, pady=20)

	right_col = tk.Frame(form_row)
	right_col.columnconfigure(0, weight=1)
	heading = ttk.Label(right_col, text="", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	date_label = ttk.Label(right_col, text="Dates")
	date_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	date_entry = ttk.Entry(right_col)
	date_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	food_pref_label = ttk.Label(right_col, text="Fod preference")
	food_pref_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	food_pref_entry = ttk.Entry(right_col)
	food_pref_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	dest_label = ttk.Label(right_col, text="Destination")
	dest_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	dest_entry = ttk.Entry(right_col)
	dest_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	budget_label = ttk.Label(right_col, text="budget")
	budget_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	budget_entry = ttk.Entry(right_col)
	budget_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
	right_col.grid(row=0, column=1, sticky=(tk.N+tk.S), pady=20)

	save_cus_button = ttk.Button(form_row, text="Suggest Property", command=show_suggested_prop)
	save_cus_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
	form_row.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def update_customer_form():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="UPDATES", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	another_heading = ttk.Label(view_board, text="Customer details", width=20,font=("bold", 10))  
	heading.grid(row=1, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Customer ID:")
	id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5) 

	# password
	change_label = ttk.Label(view_board, text="Change:")
	change_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	change_entry = ttk.Entry(view_board,  show="*")
	change_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	# login button
	aply_button = ttk.Button(view_board, text="Apply")
	aply_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
	reset_button = ttk.Button(view_board, text="Reset")
	reset_button.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def update_event_form():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="UPDATES", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	another_heading = ttk.Label(view_board, text="Event details", width=20,font=("bold", 10))  
	heading.grid(row=1, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Event ID:")
	id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5) 

	# password
	change_label = ttk.Label(view_board, text="Change:")
	change_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	change_entry = ttk.Entry(view_board,  show="*")
	change_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	# login button
	aply_button = ttk.Button(view_board, text="Apply")
	aply_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
	reset_button = ttk.Button(view_board, text="Reset")
	reset_button.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def update_hotel_form():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="UPDATES", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	another_heading = ttk.Label(view_board, text="Hotel details", width=20,font=("bold", 10))  
	heading.grid(row=1, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Hotel ID:")
	id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5) 

	# password
	change_label = ttk.Label(view_board, text="Change:")
	change_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	change_entry = ttk.Entry(view_board,  show="*")
	change_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	# login button
	aply_button = ttk.Button(view_board, text="Apply")
	aply_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
	reset_button = ttk.Button(view_board, text="Reset")
	reset_button.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def update_vendor_form():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="UPDATES", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	another_heading = ttk.Label(view_board, text="Vendor details", width=20,font=("bold", 10))  
	heading.grid(row=1, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Vendor ID:")
	id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5) 

	# password
	change_label = ttk.Label(view_board, text="Change:")
	change_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	change_entry = ttk.Entry(view_board,  show="*")
	change_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	# login button
	aply_button = ttk.Button(view_board, text="Apply")
	aply_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
	reset_button = ttk.Button(view_board, text="Reset")
	reset_button.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)

def show_update_btns():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	view_board.columnconfigure(0, weight=1)
	tk.Button(view_board, text='Update Customer Details',width=20,bg='brown',fg='white', command=update_customer_form).grid(row=0, column=0, padx=5, pady=5)
	tk.Button(view_board, text='Update Event Details',width=20,bg='brown',fg='white', command=update_event_form).grid(row=0, column=1, padx=5, pady=5)
	tk.Button(view_board, text='Update Hotel',width=20,bg='brown',fg='white', command=update_hotel_form).grid(row=1, column=0, padx=5, pady=5)
	tk.Button(view_board, text='Update Vendors',width=20,bg='brown',fg='white', command=update_vendor_form).grid(row=1, column=1, padx=5, pady=5)
	view_board.grid(row=1, column=0, sticky=(tk.N + tk.S), pady=20)


def show_billing_form():
	for child in base.winfo_children()[1:]:
		child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="BILLING", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	form_row = tk.Frame(view_board)

	left_col = tk.Frame(form_row)
	left_col.columnconfigure(0, weight=1)
	heading = ttk.Label(left_col, text="Billing information", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	id_label = ttk.Label(left_col, text="Billing ID")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	id_entry = ttk.Entry(left_col)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	cust_id_label = ttk.Label(left_col, text="Customer ID")
	cust_id_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	cust_id_entry = ttk.Entry(left_col)
	cust_id_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	emp_id_label = ttk.Label(left_col, text="Employee ID")
	emp_id_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	emp_id_entry = ttk.Entry(left_col)
	emp_id_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	event_id_label = ttk.Label(left_col, text="Event ID")
	event_id_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	event_id_entry = ttk.Entry(left_col)
	event_id_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

	bill_amount_label = ttk.Label(left_col, text="Bill Amount")
	bill_amount_label.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
	bill_amount_entry = ttk.Entry(left_col)
	bill_amount_entry.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
	left_col.grid(row=0, column=0, sticky=tk.E, pady=20)

	right_col = tk.Frame(form_row)
	right_col.columnconfigure(0, weight=1)
	heading = ttk.Label(right_col, text="Accounts", width=20,font=("bold", 10))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S))
	adv_label = ttk.Label(right_col, text="Advance")
	adv_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
	adv_entry = ttk.Entry(right_col)
	adv_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

	bal_label = ttk.Label(right_col, text="Balance")
	bal_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
	bal_entry = ttk.Entry(right_col)
	bal_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	gst_label = ttk.Label(right_col, text="GST")
	gst_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
	gst_entry = ttk.Entry(right_col)
	gst_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

	final_bill_label = ttk.Label(right_col, text="Final Bill")
	final_bill_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
	final_bill_entry = ttk.Entry(right_col)
	final_bill_entry.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
	right_col.grid(row=0, column=1, sticky=(tk.N+tk.S), pady=20)

	print_button = ttk.Button(form_row, text="Print Bill")
	print_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
	form_row.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), pady=20)
	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=50, pady=20)


def manager_loggedin():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	view_board.columnconfigure(0, weight=1)
	tk.Button(view_board, text='Add Employee',width=20,bg='brown',fg='white', command=add_employee_form).grid(row=0, column=0)
	tk.Button(view_board, text='Event Status',width=20,bg='brown',fg='white', command=event_status_form).grid(row=1, column=0)
	tk.Button(view_board, text='Generate Report',width=20,bg='brown',fg='white', command=show_gen_report).grid(row=2, column=0)
	view_board.grid(row=1, column=0, sticky=(tk.N + tk.S), pady=20)
		
def employee_loggedin():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	view_board.columnconfigure(0, weight=1)
	tk.Button(view_board, text='New Customer',width=20,bg='brown',fg='white', command=add_customer_form).grid(row=0, column=0, padx=5, pady=5)
	tk.Button(view_board, text='New Event',width=20,bg='brown',fg='white', command=add_event_form).grid(row=0, column=1, padx=5, pady=5)
	tk.Button(view_board, text='Updates',width=20,bg='brown',fg='white', command=show_update_btns).grid(row=1, column=0, padx=5, pady=5)
	tk.Button(view_board, text='Billings',width=20,bg='brown',fg='white', command=show_billing_form).grid(row=1, column=1, padx=5, pady=5)
	view_board.grid(row=1, column=0, sticky=(tk.N + tk.S), pady=20)


def manager_login_view():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	# view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="MANAGER LOG-IN", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky='ne') 

	id_label = ttk.Label(view_board, text="Manager ID")
	id_label.grid(column=0, row=1, sticky='e', padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=1, sticky='e', padx=5, pady=5) 

	# password
	password_label = ttk.Label(view_board, text="Password")
	password_label.grid(column=0, row=2, sticky='e', padx=5, pady=5)

	password_entry = ttk.Entry(view_board,  show="*")
	password_entry.grid(column=1, row=2, sticky='e', padx=5, pady=5)

	# login button
	login_button = ttk.Button(view_board, text="Login", command=manager_loggedin)
	login_button.grid(column=1, row=3, sticky='e', padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky='nswe', padx=200, pady=20)

def employee_login_view():
	for child in base.winfo_children()[1:]:
			child.destroy()
	view_board = tk.Frame(base)
	view_board.columnconfigure(0, weight=1)
	heading = ttk.Label(view_board, text="EMPLOYEE LOG-IN", width=20,font=("bold", 20))  
	heading.grid(row=0, columnspan=2, sticky=(tk.E + tk.W + tk.N + tk.S)) 

	id_label = ttk.Label(view_board, text="Employee ID:")
	id_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=20)
	id_entry = ttk.Entry(view_board)
	id_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5) 

	# password
	password_label = ttk.Label(view_board, text="Password:")
	password_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

	password_entry = ttk.Entry(view_board,  show="*")
	password_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

	# login button
	login_button = ttk.Button(view_board, text="Login", command=employee_loggedin)
	login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

	view_board.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S), padx=200, pady=20)

# manager and employee login menu 
view_board = tk.Frame(base)
view_board.columnconfigure(0, weight=1)
heading = ttk.Label(view_board, text="HOME",width=20, font=("bold", 20))  
heading.grid(row=0, column=0, padx=350)
resized_hero_img = IMG.resize((250, 100))
hero_img = ImageTk.PhotoImage(resized_hero_img)
hero_img_label = ttk.Label(view_board, image = hero_img)
hero_img_label.grid(row=1, column=0, pady=5)
tk.Button(view_board, text='Manager Login',width=20,bg='brown',fg='white', command=manager_login_view).grid(row=2, column=0)
tk.Button(view_board, text='Employee Login',width=20,bg='brown',fg='white', command=employee_login_view).grid(row=3, column=0)
view_board.grid(row=1, column=0, sticky="we", pady=20)


 
base.mainloop()  
