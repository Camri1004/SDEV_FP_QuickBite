"""

Author:  Camri Williams
Date written: 02/24/25
Assignment:   SDEV 140 Final Project - QuickBite Sandwich Ordering System
Short Desc: This program walks the user through a step-by-step sandwich customization process
across multiple windows, collecting choices for bread, protein, toppings, condiments,
and quantity before displaying the final order summary with pricing.

"""
import tkinter as tk
from tkinter import messagebox

class SandwichOrderingApp:
    def __init__(self, root):
        """Initializes the main application, hides the root window, and sets up order variables."""
        self.root = root
        self.root.withdraw()  # Hide the initial root window
        
        # Prices for each item
        self.prices = {
            "bread": {"White Bread": 1.00, "Wheat Bread": 1.50, "Sourdough": 2.00},
            "protein": {"Chicken": 3.00, "Turkey": 3.50, "Ham": 3.00, "Veggie": 2.50, "Beef": 4.00, "Tofu": 2.50, "Fish": 4.50},
            "toppings": {"Lettuce": 0.50, "Tomato": 0.50, "Cheese": 1.00, "Onion": 0.50, "Cucumbers": 0.50, "Avocado": 1.50, "Banana Peppers": 0.75},
            "condiments": {"Mayo": 0.25, "Mustard": 0.25, "Ketchup": 0.25, "Relish": 0.50, "Pickled Onion": 0.75}
        }
        
        # Variables to store user selections
        self.bread_var = tk.StringVar(value="White Bread")
        self.protein_var = tk.StringVar(value="Chicken")
        self.toppings_vars = {t: tk.BooleanVar() for t in self.prices["toppings"].keys()}
        self.condiments_vars = {c: tk.BooleanVar() for c in self.prices["condiments"].keys()}
        self.quantity_var = tk.IntVar(value=1)
        
        self.bread_window()  # Start the ordering process

    def bread_window(self):
        """Creates a window for selecting bread options."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Select Bread Type")
        
        tk.Label(self.window, text="Choose your bread:").pack()
        for bread, price in self.prices["bread"].items():
            tk.Radiobutton(self.window, text=f"{bread} - ${price:.2f}", variable=self.bread_var, value=bread).pack()
        
        tk.Button(self.window, text="Next", command=self.protein_window).pack()
    
    def protein_window(self):
        """Creates a window for selecting protein options."""
        self.window.destroy()
        self.window = tk.Toplevel(self.root)
        self.window.title("Select Protein")
        
        tk.Label(self.window, text="Choose your protein:").pack()
        for protein, price in self.prices["protein"].items():
            tk.Radiobutton(self.window, text=f"{protein} - ${price:.2f}", variable=self.protein_var, value=protein).pack()
        
        tk.Button(self.window, text="Next", command=self.toppings_window).pack()
    
    def toppings_window(self):
        """Creates a window for selecting toppings."""
        self.window.destroy()
        self.window = tk.Toplevel(self.root)
        self.window.title("Select Toppings")
        
        tk.Label(self.window, text="Choose your toppings:").pack()
        for topping, price in self.prices["toppings"].items():
            tk.Checkbutton(self.window, text=f"{topping} - ${price:.2f}", variable=self.toppings_vars[topping]).pack()
        
        tk.Button(self.window, text="Next", command=self.condiments_window).pack()
    
    def condiments_window(self):
        """Creates a window for selecting condiments."""
        self.window.destroy()
        self.window = tk.Toplevel(self.root)
        self.window.title("Select Condiments")
        
        tk.Label(self.window, text="Choose your condiments:").pack()
        for condiment, price in self.prices["condiments"].items():
            tk.Checkbutton(self.window, text=f"{condiment} - ${price:.2f}", variable=self.condiments_vars[condiment]).pack()
        
        tk.Button(self.window, text="Next", command=self.quantity_window).pack()
    
    def quantity_window(self):
        """Creates a window for selecting quantity."""
        self.window.destroy()
        self.window = tk.Toplevel(self.root)
        self.window.title("Select Quantity")
        
        tk.Label(self.window, text="Enter quantity:").pack()
        tk.Spinbox(self.window, from_=1, to=10, textvariable=self.quantity_var).pack()
        
        tk.Button(self.window, text="Submit Order", command=self.place_order).pack()
    
    def place_order(self):
        """Generates and displays the final order summary with price calculation."""
        self.window.destroy()
        
        # Calculate total price
        total_price = self.prices["bread"][self.bread_var.get()] + self.prices["protein"][self.protein_var.get()]
        total_price += sum(self.prices["toppings"][t] for t, v in self.toppings_vars.items() if v.get())
        total_price += sum(self.prices["condiments"][c] for c, v in self.condiments_vars.items() if v.get())
        total_price *= self.quantity_var.get()
        
        # Construct the order summary string
        order_summary = f"Bread: {self.bread_var.get()}\n"
        order_summary += f"Protein: {self.protein_var.get()}\n"
        order_summary += "Toppings: " + ", ".join([t for t, v in self.toppings_vars.items() if v.get()]) + "\n"
        order_summary += "Condiments: " + ", ".join([c for c, v in self.condiments_vars.items() if v.get()]) + "\n"
        order_summary += f"Quantity: {self.quantity_var.get()}\n"
        order_summary += f"Total Price: ${total_price:.2f}"
        
        # Display order summary in a message box
        messagebox.showinfo("Order Summary", order_summary)
        
        # Add Restart Order Button
        if messagebox.askyesno("Order Again?", "Would you like to place another order?"):
            self.bread_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = SandwichOrderingApp(root)
    root.mainloop()
