import tkinter as tk
from tkinter import ttk
from tkinter import messagebox #for the pop-up message testing
import random
from datetime import datetime, timedelta

root = tk.Tk()  
root.geometry("900x650")
root.title("Water Bill Calculator")

WIN = random.randint(1000000, 9999999)
total_consumed = 0
total_cost = 0

#INITIALIZES ENTRIES
def Title_Section(title):
    Title_Frame = tk.Frame(mc)
    Title_Frame.pack(anchor="e", fill = "x")
    Form_title_Frame = tk.LabelFrame(Title_Frame, text = title, labelanchor="n")
    Form_title_Frame.grid(row=0, column=0, padx=0, pady=0)
    Form_title_Frame.config(font = ("Calibri", 16, "bold"))
    
    def Title_Label(title):
        label = tk.Label(Form_title_Frame, text = title)
        label.grid(row=0, column=0, padx=0, pady=0)
        label.config(font = ("Calirbri", 7, "bold"))   
        
    Title_Label("Corrales Ave. 27 Cagayan De Oro City NON-VAT REG. TIN 000-550-995-000")

    # *fields define the variables that will be used for the code. Anything under its positional parameter is consider a field and continues so on so forth.

def section(parent, title, *fields):
    #Section'd Frame
    section_frame = tk.LabelFrame(parent, text=title, font=("Calibri", 14, "bold"), labelanchor="n")
    section_frame.pack(anchor="w", fill="x", padx=10, pady=5)
    
    # Database for Entries from the *fields
    entries = {}
    
    # Loop function for labels and the entries
    for idx, field in enumerate(fields):
        # Create label
        label = tk.Label(section_frame, text=field, font=("Calibri", 11))
        label.grid(row =idx, column =0, sticky ="w", padx =5, pady =5)
        
        # Create entry
        entry = tk.Entry(section_frame, font=("Calibri", 10))
        entry.grid(row = idx, column = 1, sticky= "w", padx =5, pady =1)
        
        # Store Entries
        entries[field] = entry
    
    # Returns to entries(entries = {}) after finishing a field name
    return entries

#On going progress on validating inputs
def get_field_data(entries, field_name):    
    return entries[field_name].get()

def check_values():
    # Retrieve and compare Present and Previous values
    previous_value = float(get_field_data(Utility_Section, "Previous"))
    present_value = float(get_field_data(Utility_Section, "Present"))

    # Check if Present is less than Previous
    if present_value < previous_value:
        messagebox.showerror("INPUT ERROR", "PRESENT value cannot be lower than PREVIOUS value")
        return False
    return True

def check_int():
    try:
    
        previous_value = int(get_field_data(Utility_Section, "Previous"))
        present_value = int(get_field_data(Utility_Section, "Present"))
    except (ValueError, TypeError):
        messagebox.showerror("INPUT ERROR", "BOTH PREVIOUS and PRESENT values must be a positive integer!")
    check = True
        
    if not isinstance(previous_value, int) or previous_value <= 0:
        messagebox.showerror("INPUT ERROR", "PREVIOUS value must be a positive integer!")
        check = False
    
    if not isinstance(present_value, int) or present_value <= 0:
        messagebox.showerror("INPUT ERROR", "PRESENT value must be a positive integer!")
        check = False
    
    return check

def consumed():
    global total_cost
    global total_consumed
    
    previous_value = int(get_field_data(Utility_Section, "Previous"))
    present_value = int(get_field_data(Utility_Section, "Present"))
    
    total_consumed = present_value - previous_value

def rate_calc():
    global total_cost
    global total_consumed
    
    rate_type = int(get_field_data(Utility_Section, "Rate Type\n1: Commericial\n2: Residential\n3: Industrial\n4: Commercial"))
    
    if rate_type not in [1, 2, 3, 4]:
        messagebox.showerror("ERROR TRY AGAIN", f"You can only choose 1, 2, 3, 4 in Rate Type. Your input was {rate_type}")
        return
    
    if rate_type == 1:
        type = str("Governmental")
        total_cost = total_consumed * 25.30
    elif rate_type == 2:
        type = str("Residential")
        total_cost = total_consumed * 25.30
    elif rate_type == 3:
        type = str("Industrial")
        total_cost = total_consumed * 50.60
    elif rate_type == 4:
        type = str("Commercial")
        total_cost = total_consumed * 50.60
        #https://licabwaterdistrict.gov.ph/water-rates/
    
    print(total_cost)

def Form_Submit():
    '''
    Info_Section
    Address_Section
    Utility_Section
    '''
    
    # Validate inputs for each section
    # Validate all fields in the given Section
    input_data = {}

    for validation, entry in User_Section.items():
        input_data[validation] = entry.get()

    # Check for empty inputs
    no_input1 = next((field for field, value in input_data.items() if not value), None)
    if no_input1:
        messagebox.showerror("ERROR TRY AGAIN", f"There is no input in {no_input1}")
        return no_input1
    
    for validation, entry in Address_Section.items():
        input_data[validation] = entry.get()
    no_input2 = next((field for field, value in input_data.items() if not value), None)
    if no_input2:
        messagebox.showerror("ERROR TRY AGAIN", f"There is no input in {no_input2}")
        return no_input2   
    
    for validation, entry in Utility_Section.items():
        input_data[validation] = entry.get()
    no_input3 = next((field for field, value in input_data.items() if not value), None)
    if no_input3:
        messagebox.showerror("ERROR TRY AGAIN", f"There is no input in {no_input3}")
        return no_input3      
    
    # Check if Present value is greater than or equal to Previous value
    if not check_values():
        return
    consumed() #Calculates Cost and total consumed water
    
    # Checks if they are an int value(Present/Previous)
    if not check_int():
        return
    
    rate_calc() #Calculates cost
    display_inputs() # Displays the ENTRIES

mc = tk.Tk()
mc.title("Water Bill Receipt Maker")
mc.resizable(0,0) # Personal Choice: Makes UI unresizable. 0 makes it unresizable, a positive/negative number makes either or both x, y resizable

# Contains TITLE, and 3 sections as the User Info, Address, Utility
Title_Section("WATER BILL ONLINE FORM")
User_Section = section(mc, "Personal Info", "First Name", "Last Name", "Suffix(Optional)",  "Contact Number")
Address_Section = section(mc, "Address", "Street", "Barangay", "City", "Province", "Zip Code")
Utility_Section = section(mc, "Utility Report", "Previous", "Present", "Arrears", "Rate Type\n1: Commericial\n2: Residential\n3: Industrial\n4: Commercial")

'''
SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR SEPERATOR 
'''

#OUTPUT UI
#Function for showing Inputs
def display_inputs():
    global total_cost

    First_Name = get_field_data(User_Section, "First Name")
    Last_Name = get_field_data(User_Section, "Last Name")
    Suffix = get_field_data(User_Section, "Suffix(Optional)")
    Contact_Number = get_field_data(User_Section, "Contact Number")

    # Address Section
    Street = get_field_data(Address_Section, "Street")
    Barangay = get_field_data(Address_Section, "Barangay")
    City = get_field_data(Address_Section, "City")
    Province = get_field_data(Address_Section, "Province")
    Zip_Code = get_field_data(Address_Section, "Zip Code")

        # Utility Report
    Previous = get_field_data(Utility_Section, "Previous")
    Present = get_field_data(Utility_Section, "Present")
    Arrears = get_field_data(Utility_Section, "Arrears")
    
    total_cost = float(total_cost)
    Arrears = float(Arrears)
    
    due_fees = 143 #Cost of being late for payment\
    VAT = float(total_cost) * 0.12
    total_cost += Arrears
    total_cost += VAT
    late_fee = total_cost + due_fees
    
    
    
    nameLabel.config(text=f"Name: {First_Name} {Last_Name} {Suffix}")
    NoLabel.config(text=f"Address: {Contact_Number}")
    addressLabel.config(text=f"Address: {Street}, {Barangay}, {City}, {Province}, {Zip_Code}")
    WINLabel.config(text=f"WIN #:{WIN}")
    prevReadingLabel.config(text=f"Previous Reading (m³): {Previous}")
    currReadingLabel.config(text=f"Current Reading (m³): {Present}")
    cubicMeterLabel.config(text=f"Cubic Meters Consumed: {total_consumed}")
    VatLabel.config(text=f"VAT 12%: {VAT:.2f}")
    ArrearsLabel.config(text=f"Arrears: {Arrears:.2f}")
    amountLabel.config(text=f"Total Amount (Pesos): {total_cost:.2f}")
    lateAmtdue_Label.config(text=f"₱:{late_fee:.2f}")
    
    containerFrame.pack(fill="both", expand=True, padx=10, pady=10)
    mc.destroy()

# Title Label
label = tk.Label(root, text="Cagayan De Oro Water District", font=('Consolas', 12), bd=2, relief="ridge", bg="lightblue", fg="black")
label.pack(padx=20, pady=5)

# Separator Line
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=10, pady=5)

# Container Frame (holds all other frames below the title line)
containerFrame = tk.Frame(root)

# Left Side Frame (Customer Info, Readings, etc.)
leftFrame = tk.Frame(containerFrame)
leftFrame.pack(side=tk.LEFT, fill="both", expand=True)

# Customer Info Frame (Name and Address)
customerInfoFrame = tk.Frame(leftFrame, bd=2, relief="ridge", padx=10, pady=10)
customerInfoFrame.columnconfigure(0, weight=1)
customerInfoFrame.columnconfigure(1, weight=1)

# Name Label
nameLabel = tk.Label(customerInfoFrame, text=f"Name: ", font=('Consolas', 12))
nameLabel.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Address Label 
addressLabel = tk.Label(customerInfoFrame, text=f"Address: ", font=('Consolas', 12))
addressLabel.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# Contact no. Label
NoLabel = tk.Label(customerInfoFrame, text="Contact No.: ", font=('Consolas', 12))
NoLabel.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

# WIN Label
WINLabel = tk.Label(customerInfoFrame, text=f"WIN #:{WIN}", font=('Consolas', 12))
WINLabel.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

# Place the Customer Info Frame at the top of the container
customerInfoFrame.pack(fill = "x", anchor="w", pady=5)

# Readings Frame
readingsFrame = tk.Frame(leftFrame, bd=2, relief="ridge", padx=10, pady=10)
readingsFrame.columnconfigure(0, weight=1)
readingsFrame.columnconfigure(1, weight=1)

# Previous Reading
prevReadingLabel = tk.Label(readingsFrame, text=f"Previous Reading (m³): ", font=('Consolas', 12))
prevReadingLabel.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Current Reading
currReadingLabel = tk.Label(readingsFrame, text=f"Current Reading (m³): ", font=('Consolas', 12))
currReadingLabel.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# Place the Readings Frame below the Customer Info Frame
readingsFrame.pack(fill = "x", anchor="w", pady=5)

# Cubic Meter Frame
cubicMeterFrame = tk.Frame(leftFrame, bd=2, relief="ridge", padx=10, pady=10)
cubicMeterFrame.columnconfigure(0, weight=1)
cubicMeterFrame.columnconfigure(1, weight=1)

# Cubic Meter Label 
cubicMeterLabel = tk.Label(cubicMeterFrame, text=f"Cubic Meters Consumed: ", font=('Consolas', 12))
cubicMeterLabel.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Place the Cubic Meter Frame below the Readings Frame
cubicMeterFrame.pack(fill = "x", anchor="w", pady=5)

# Amount (pesos) Frame
amountFrame = tk.Frame(leftFrame, bd=2, relief="ridge", padx=10, pady=10)
amountFrame.columnconfigure(0, weight=1)
amountFrame.columnconfigure(1, weight=1)

# VAT
VatLabel = tk.Label(amountFrame, text=f"VAT(12%): ", font=('Consolas', 12))
VatLabel.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Arrears Label
ArrearsLabel = tk.Label(amountFrame, text=f"Arrears: ", font=('Consolas', 12))
ArrearsLabel.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# Amount Label 
amountLabel = tk.Label(amountFrame, text=f"Total Amount (Pesos): ", font=('Consolas', 12))
amountLabel.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

# Place the Amount Frame below the Cubic Meter Frame
amountFrame.pack(fill = "x", anchor="w", pady=5)

# Frame with border for details
detailFrame = tk.Frame(leftFrame, bd=2, relief="ridge", padx=10, pady=10)
detailFrame.columnconfigure(0, weight=1)
detailFrame.columnconfigure(1, weight=1)
detailFrame.columnconfigure(2, weight=1)
detailFrame.columnconfigure(3, weight=1)

# ROW 0 (labels)
readingDate = tk.Label(detailFrame, text="READING DATE", font=('Consolas', 12), bd=1, relief="solid")
readingDate.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
dateDue = tk.Label(detailFrame, text="DATE DUE", font=('Consolas', 12), bd=1, relief="solid")
dateDue.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
amountDueLate = tk.Label(detailFrame, text="AMOUNT DUE AFTER DUE DATE", font=('Consolas', 12), bd=1, relief="solid")
amountDueLate.grid(row=0, column=2, sticky=tk.W + tk.E, padx=5, pady=5)
month = tk.Label(detailFrame, text="FOR THE MONTH OF", font=('Consolas', 12), bd=1, relief="solid")
month.grid(row=0, column=3, sticky=tk.W + tk.E, padx=5, pady=5)

# ROW 1 (results)
# Reading date
dateNow = datetime.now()
dateRN = dateNow.strftime("%m-%d")
dateNow2 = tk.Label(detailFrame, text=f"{dateRN}", font=('Consolas', 12), bd=1, relief="solid")
dateNow2.grid(row=1, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
# Date due
oneweeklater = dateNow + timedelta(days=7)
dateDue2 = oneweeklater.strftime("%m-%d")
dateDue3 = tk.Label(detailFrame, text=f"{dateDue2}", font=('Consolas', 12), bd=1, relief="solid")
dateDue3.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
# Rough draft of late fee charge

lateAmtdue_Label = tk.Label(detailFrame, text=f"₱", font=('Consolas', 12), bd=1, relief="solid")
lateAmtdue_Label.grid(row=1, column=2, sticky=tk.W + tk.E, padx=5, pady=5)
# For the month of
monthOf = datetime.now().strftime("%b %Y")
monthOf2 = tk.Label(detailFrame, text=f"{monthOf}", font=('Consolas', 12), bd=1, relief="solid")
monthOf2.grid(row=1, column=3, sticky=tk.W + tk.E, padx=5, pady=5)

# Pack the detail frame at the bottom of the left frame
detailFrame.pack(fill="x", pady=10)

# Right Side Frame (Payment Options)
rightFrame = tk.Frame(containerFrame, bd=2, relief="ridge", padx=10, pady=10)
rightFrame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

paymentLabel = tk.Label(rightFrame, text="You May Pay Thru Our:", font=('Consolas', 12, 'bold'))
paymentLabel.pack(anchor="w", pady=5)

paymentOptions = [
    "1. Bank of Eder",
    "2. GCash",
    "3. PayMaya",
    "4. Local Payment Centers",
    "5. Online Banking",
]

for option in paymentOptions:
    tk.Label(rightFrame, text=option, font=('Consolas', 12), anchor="w").pack(fill="x", pady=2)


# Button for Submission of inputs
show_button = tk.Button(mc, text="SUBMIT RECEIPT FORM", command= Form_Submit, bg = "red", fg= "white")
show_button.pack(pady=10, padx =15, fill="x")


mc.mainloop()
