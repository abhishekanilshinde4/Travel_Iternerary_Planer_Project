import tkinter as tk
from tkinter import ttk, messagebox
from geopy.distance import geodesic

DESTINATIONS = {
    "Mumbai": {"lat":19.0760,"lon":72.8777,"type":"metro"},
    "Pune": {"lat":18.5204,"lon":73.8567,"type":"metro"},
    "Delhi": {"lat":28.6139,"lon":77.2090,"type":"metro"},
    "Bangalore": {"lat":12.9716,"lon":77.5946,"type":"metro"},
    "Hyderabad": {"lat":17.3850,"lon":78.4867,"type":"metro"},
    "Chennai": {"lat":13.0827,"lon":80.2707,"type":"metro"},
    "Kolkata": {"lat":22.5726,"lon":88.3639,"type":"metro"},
    "Ahmedabad": {"lat":23.0225,"lon":72.5714,"type":"metro"},
    "Surat": {"lat":21.1702,"lon":72.8311,"type":"metro"},
    "Nagpur": {"lat":21.1458,"lon":79.0882,"type":"metro"},
    "Indore": {"lat":22.7196,"lon":75.8577,"type":"metro"},
    "Bhopal": {"lat":23.2599,"lon":77.4126,"type":"metro"},
    "Lucknow": {"lat":26.8467,"lon":80.9462,"type":"metro"},
    "Patna": {"lat":25.5941,"lon":85.1376,"type":"metro"},
    "Chandigarh": {"lat":30.7333,"lon":76.7794,"type":"metro"},
    "Agra": {"lat":27.1767,"lon":78.0081,"type":"historical"},
    "Hampi": {"lat":15.3350,"lon":76.4600,"type":"historical"},
    "Udaipur": {"lat":24.5854,"lon":73.7125,"type":"historical"},
    "Khajuraho": {"lat":24.8318,"lon":79.9199,"type":"historical"},
    "Ajanta": {"lat":20.5519,"lon":75.7033,"type":"historical"},
    "Ellora": {"lat":20.0268,"lon":75.1790,"type":"historical"},
    "Gwalior": {"lat":26.2183,"lon":78.1828,"type":"historical"},
    "Chittorgarh": {"lat":24.8887,"lon":74.6269,"type":"historical"},
    "Orchha": {"lat":25.3513,"lon":78.6403,"type":"historical"},
    "Bijapur": {"lat":16.8302,"lon":75.7100,"type":"historical"},
    "Goa": {"lat":15.2993,"lon":74.1240,"type":"beach"},
    "Gokarna": {"lat":14.5479,"lon":74.3188,"type":"beach"},
    "Kochi": {"lat":9.9312,"lon":76.2673,"type":"beach"},
    "Varkala": {"lat":8.7379,"lon":76.7163,"type":"beach"},
    "Puri": {"lat":19.8135,"lon":85.8312,"type":"beach"},
    "Digha": {"lat":21.6237,"lon":87.5037,"type":"beach"},
    "Alibaug": {"lat":18.6414,"lon":72.8722,"type":"beach"},
    "Kovalam": {"lat":8.4000,"lon":76.9784,"type":"beach"},
    "Rameswaram": {"lat":9.2881,"lon":79.3174,"type":"beach"},
    "Pondicherry": {"lat":11.9416,"lon":79.8083,"type":"beach"},
    "Manali": {"lat":32.2432,"lon":77.1892,"type":"hill"},
    "Shimla": {"lat":31.1048,"lon":77.1734,"type":"hill"},
    "Darjeeling": {"lat":27.0410,"lon":88.2663,"type":"hill"},
    "Ooty": {"lat":11.4102,"lon":76.6950,"type":"hill"},
    "Munnar": {"lat":10.0889,"lon":77.0595,"type":"hill"},
    "Nainital": {"lat":29.3919,"lon":79.4542,"type":"hill"},
    "Kodaikanal": {"lat":10.2381,"lon":77.4892,"type":"hill"},
    "Mussoorie": {"lat":30.4598,"lon":78.0644,"type":"hill"},
    "Lonavala": {"lat":18.7546,"lon":73.4062,"type":"hill"},
    "Mahabaleshwar": {"lat":17.9307,"lon":73.6477,"type":"hill"},
    "Tawang": {"lat":27.5866,"lon":91.8697,"type":"hill"},
    "Gangtok": {"lat":27.3389,"lon":88.6065,"type":"hill"},
    "Varanasi": {"lat":25.3176,"lon":83.0061,"type":"religious"},
    "Amritsar": {"lat":31.6340,"lon":74.8723,"type":"religious"},
    "Tirupati": {"lat":13.6288,"lon":79.4192,"type":"religious"},
    "Haridwar": {"lat":29.9457,"lon":78.1642,"type":"religious"},
    "Shirdi": {"lat":19.7645,"lon":74.4762,"type":"religious"},
    "Bodh Gaya": {"lat":24.6951,"lon":84.9913,"type":"religious"},
    "Ayodhya": {"lat":26.7993,"lon":82.2044,"type":"religious"},
    "Dwarka": {"lat":22.2442,"lon":68.9685,"type":"religious"},
    "Somnath": {"lat":20.8880,"lon":70.4012,"type":"religious"},
    "Kedarnath": {"lat":30.7352,"lon":79.0669,"type":"religious"},
    "Badrinath": {"lat":30.7433,"lon":79.4938,"type":"religious"},
    "Rishikesh": {"lat":30.0869,"lon":78.2676,"type":"adventure"},
    "Leh": {"lat":34.1526,"lon":77.5771,"type":"adventure"},
    "Spiti": {"lat":32.2460,"lon":78.0340,"type":"adventure"},
    "Auli": {"lat":30.5285,"lon":79.5658,"type":"adventure"},
    "Bir": {"lat":32.0500,"lon":76.7167,"type":"adventure"},
    "Zanskar": {"lat":33.5000,"lon":76.8333,"type":"adventure"},
    "Mechuka": {"lat":28.5971,"lon":94.1267,"type":"adventure"},
    "Dzukou Valley": {"lat":25.5733,"lon":94.0596,"type":"adventure"},
    "Jim Corbett": {"lat":29.5300,"lon":78.7747,"type":"wildlife"},
    "Kaziranga": {"lat":26.5775,"lon":93.1711,"type":"wildlife"},
    "Ranthambore": {"lat":26.0173,"lon":76.5026,"type":"wildlife"},
    "Gir": {"lat":21.1240,"lon":70.8245,"type":"wildlife"},
    "Sundarbans": {"lat":21.9497,"lon":89.1833,"type":"wildlife"},
    "Bandipur": {"lat":11.7400,"lon":76.6300,"type":"wildlife"},
    "Periyar": {"lat":9.4625,"lon":77.2363,"type":"wildlife"},
    "Tadoba": {"lat":20.2132,"lon":79.3713,"type":"wildlife"},
    "Kanha": {"lat":22.3345,"lon":80.6115,"type":"wildlife"},
    "Jaisalmer": {"lat":26.9157,"lon":70.9083,"type":"desert"},
    "Bikaner": {"lat":28.0229,"lon":73.3119,"type":"desert"},
    "Barmer": {"lat":25.7500,"lon":71.3833,"type":"desert"},
    "Jodhpur": {"lat":26.2389,"lon":73.0243,"type":"desert"},
    "Coorg": {"lat":12.3375,"lon":75.8069,"type":"nature"},
    "Wayanad": {"lat":11.6854,"lon":76.1320,"type":"nature"},
    "Cherrapunji": {"lat":25.2700,"lon":91.7320,"type":"nature"},
    "Shillong": {"lat":25.5788,"lon":91.8933,"type":"nature"},
    "Valley of Flowers": {"lat":30.7280,"lon":79.6044,"type":"nature"},
    "Ziro": {"lat":27.5941,"lon":93.8383,"type":"nature"},
    "Majuli": {"lat":26.9500,"lon":94.2000,"type":"nature"},
    "Andaman": {"lat":11.7401,"lon":92.6586,"type":"island"},
    "Nicobar": {"lat":7.0000,"lon":93.0000,"type":"island"},
    "Lakshadweep": {"lat":10.5667,"lon":72.6417,"type":"island"},
    "Dudhsagar": {"lat":15.3144,"lon":74.3140,"type":"waterfall"},
    "Athirappilly": {"lat":10.2850,"lon":76.5690,"type":"waterfall"},
    "Jog Falls": {"lat":14.2294,"lon":74.8123,"type":"waterfall"},
    "Nohkalikai": {"lat":25.2756,"lon":91.6938,"type":"waterfall"},
    "Triund": {"lat":32.2520,"lon":76.3234,"type":"trek"},
    "Roopkund": {"lat":30.2570,"lon":79.7325,"type":"trek"},
    "Kedarkantha": {"lat":31.0200,"lon":78.1700,"type":"trek"},
    "Hampta Pass": {"lat":32.2990,"lon":77.3660,"type":"trek"}
}

types = []
for city in DESTINATIONS:
    t = DESTINATIONS[city]["type"]
    if t not in types:
        types.append(t)

availablex = list(DESTINATIONS.keys())

HOTEL_OPTIONS_REF = {
    "7 Star": {"First Class": 15000, "Middle Class": 10000, "Lower Class": 7000},
    "5 Star": {"First Class": 8000, "Middle Class": 5000, "Lower Class": 3000},
    "Normal": {"First Class": 2500, "Middle Class": 1500, "Lower Class": 800}
}


# --- 2. GUI EVENT FUNCTIONS ---
def update_destinations(event=None):
    try:
        type_choice = int(type_var.get().split(".")[0])
        selected_type = types[type_choice-1]
        available_list = [city for city in DESTINATIONS if DESTINATIONS[city]["type"] == selected_type]
        dest_combo['values'] = [f"{i+1}. {c}" for i, c in enumerate(available_list)]
        dest_combo.set('')
    except ValueError:
        pass

def update_hotel_options(event=None):
    try:
        plan = int(plan_var.get().split(".")[0])
        if plan == 1:
            hotel_frame.pack(pady=10, fill="x")
        else:
            hotel_frame.pack_forget()
    except ValueError:
        pass

def update_rooms(event=None):
    try:
        cat_choice = int(cat_var.get().split(".")[0])
        selected_cat = list(HOTEL_OPTIONS_REF.keys())[cat_choice - 1]
        room_classes = list(HOTEL_OPTIONS_REF[selected_cat].keys())
        room_combo['values'] = [f"{i+1}. {r}" for i, r in enumerate(room_classes)]
        room_combo.set('')
    except ValueError:
        pass

def gui_print(*args):
    text = " ".join(map(str, args))
    output_text.insert(tk.END, text + "\n")
    output_text.see(tk.END)


# --- 3. MAIN CORE LOGIC ---
def run_logic():
    output_text.delete('1.0', tk.END)
    try:
        gui_print("\nTypes of Travel Places:")
        for i,t in enumerate(types):
            gui_print(i+1,".",t)

        type_choice = int(type_var.get().split(".")[0])
        selected_type = types[type_choice-1]

        available = []
        gui_print("\nCities available in",selected_type,"category:\n")
        for city in DESTINATIONS:
            if DESTINATIONS[city]["type"] == selected_type:
                available.append(city)
                gui_print(len(available),".",city)

        dest_choice = int(dest_var.get().split(".")[0])
        city = available[dest_choice-1]

        gui_print("\nAll available cities:\n")
        for i, cityx in enumerate(availablex):
            gui_print(i+1, ".", cityx)

        startx = int(start_var.get().split(".")[0])
        start = availablex[startx - 1]

        if start in DESTINATIONS and city in DESTINATIONS:
            start_coord = (DESTINATIONS[start]["lat"], DESTINATIONS[start]["lon"])
            dest_coord = (DESTINATIONS[city]["lat"], DESTINATIONS[city]["lon"])
            distance = geodesic(start_coord, dest_coord).km

            gui_print("\nDestination:",city)
            gui_print("\nDistance from",start,"to",city,"=",round(distance,2),"km")
            gui_print("\nEnter Mode Of Travel")
            gui_print("\n1. Rented Car\n2. Train\n3. Flight\n4. Own Car")

            mode = int(mode_var.get().split(".")[0])

            if mode == 1:
                speed = 60
                mode_name = "Rented Car"
                ppk=4
                gui_print(f"\nCost Required by the mode by the rate of {ppk} Rs per kilometer {mode_name} is {round(distance*ppk, 2)} Rupees")
            elif mode == 2:
                speed = 80
                mode_name = "Train"
                ppk=10
                gui_print(f"\nCost Required by the mode by the rate of {ppk} Rs per kilometer {mode_name} is {round(distance*ppk, 2)} Rupees")
            elif mode == 3:
                speed = 600
                mode_name = "Flight"
                ppk=20
                gui_print(f"\nCost Required by the mode by the rate of {ppk} Rs per kilometer {mode_name} is {round(distance*ppk, 2)} Rupees")
            elif mode == 4:
                speed = 60
                mode_name = "Own Car"
                ppk=2
                gui_print(f"\nCost Required by the mode by the rate of {ppk} Rs per kilometer {mode_name} is {round(distance*ppk, 2)} Rupees") 
            else:
                gui_print("Invalid mode")
                return

            time = distance / speed
            gui_print("\nYour Travel Time :", round(time,2),"hours")

            total_hotel_cost = 0
            plan = int(plan_var.get().split(".")[0])
            
            if plan == 1:
                hotel_categories = list(HOTEL_OPTIONS_REF.keys())
                gui_print("\nHotel Categories ")
                for i, cat in enumerate(hotel_categories):
                    gui_print(f"{i + 1}. {cat}")

                cat_choice = int(cat_var.get().split(".")[0])
                selected_cat = hotel_categories[cat_choice - 1]
                room_options = HOTEL_OPTIONS_REF[selected_cat]
                room_classes = list(room_options.keys())

                gui_print(f"\nRoom Classes in {selected_cat} Hotel")
                for i, room in enumerate(room_classes):
                    price = room_options[room]
                    gui_print(f"{i + 1}. {room} (Rs. {price}/night)")

                room_choice = int(room_var.get().split(".")[0])
                selected_room = room_classes[room_choice - 1]
                days = int(days_var.get())

                price_per_night = HOTEL_OPTIONS_REF[selected_cat][selected_room]
                total_hotel_cost = price_per_night * days

                gui_print("Bill is :\n")
                gui_print(f"Hotel Summary: {selected_cat} - {selected_room}")
                gui_print(f"Stay Duration: {days} days")
                gui_print(f"Total Hotel Cost according with the Rent per Day {price_per_night}: Rs. {round(total_hotel_cost, 2)}")  
            else:
                gui_print("\nNo hotel planning selected. Have a safe journey!")        
            
            gui_print(f"Total cost of traveling and staying is : {round(ppk*distance, 2)} + {round(total_hotel_cost, 2)} = {round(ppk*distance + total_hotel_cost, 2)} Rupees")
            
    except Exception as e:
        messagebox.showerror("Validation Error", "Please ensure all selections and fields are correctly filled out.")


# --- 4. SIMPLE GUI SETUP ---
root = tk.Tk()
root.title("Simple Travel Planner")
root.geometry("600x800")

# Input Variables
type_var = tk.StringVar()
dest_var = tk.StringVar()
start_var = tk.StringVar()
mode_var = tk.StringVar()
plan_var = tk.StringVar()
cat_var = tk.StringVar()
room_var = tk.StringVar()
days_var = tk.StringVar()

# Form Frame
form_frame = tk.Frame(root, padx=20, pady=10)
form_frame.pack(fill="x")

# --- Form Elements ---
tk.Label(form_frame, text="Travel Type:").grid(row=0, column=0, sticky="w", pady=5)
type_combo = ttk.Combobox(form_frame, textvariable=type_var, state="readonly", width=30)
type_combo['values'] = [f"{i+1}. {t}" for i, t in enumerate(types)]
type_combo.grid(row=0, column=1, pady=5)
type_combo.bind("<<ComboboxSelected>>", update_destinations)

tk.Label(form_frame, text="Destination City:").grid(row=1, column=0, sticky="w", pady=5)
dest_combo = ttk.Combobox(form_frame, textvariable=dest_var, state="readonly", width=30)
dest_combo.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Starting City:").grid(row=2, column=0, sticky="w", pady=5)
start_combo = ttk.Combobox(form_frame, textvariable=start_var, state="readonly", width=30)
start_combo['values'] = [f"{i+1}. {cityx}" for i, cityx in enumerate(availablex)]
start_combo.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Preferred Transport:").grid(row=3, column=0, sticky="w", pady=5)
mode_combo = ttk.Combobox(form_frame, textvariable=mode_var, state="readonly", width=30)
mode_combo['values'] = ["1. Rented Car", "2. Train", "3. Flight", "4. Own Car"]
mode_combo.grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="Plan for Stay?:").grid(row=4, column=0, sticky="w", pady=5)
plan_combo = ttk.Combobox(form_frame, textvariable=plan_var, state="readonly", width=30)
plan_combo['values'] = ["1. Yes", "0. No"]
plan_combo.grid(row=4, column=1, pady=5)
plan_combo.bind("<<ComboboxSelected>>", update_hotel_options)

# --- Hotel Sub-frame (Hidden by Default) ---
hotel_frame = tk.Frame(root, padx=20)

tk.Label(hotel_frame, text="Hotel Category:").grid(row=0, column=0, sticky="w", pady=5)
cat_combo = ttk.Combobox(hotel_frame, textvariable=cat_var, state="readonly", width=30)
cat_combo['values'] = [f"{i+1}. {cat}" for i, cat in enumerate(list(HOTEL_OPTIONS_REF.keys()))]
cat_combo.grid(row=0, column=1, pady=5)
cat_combo.bind("<<ComboboxSelected>>", update_rooms)

tk.Label(hotel_frame, text="Room Class:").grid(row=1, column=0, sticky="w", pady=5)
room_combo = ttk.Combobox(hotel_frame, textvariable=room_var, state="readonly", width=30)
room_combo.grid(row=1, column=1, pady=5)

tk.Label(hotel_frame, text="Duration (Days):").grid(row=2, column=0, sticky="w", pady=5)
days_entry = tk.Entry(hotel_frame, textvariable=days_var, width=33)
days_entry.grid(row=2, column=1, pady=5)

# --- Action Button & Output ---
btn = tk.Button(root, text="Calculate Itinerary", bg="lightblue", font=("Arial", 12, "bold"), command=run_logic)
btn.pack(pady=15)

output_text = tk.Text(root, height=18, width=70)
output_text.pack(padx=10, pady=10)

root.mainloop()