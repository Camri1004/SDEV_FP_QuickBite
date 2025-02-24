import tkinter as tk
from tkinter import messagebox

class SandwichOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickBite Sandwich Ordering System")
        
        # Initialize variables
        self.bread_var = tk.StringVar(value="White Bread")
        self.protein_var = tk.StringVar(value="Chicken")
        self.toppings_vars = {
            "Lettuce": tk.BooleanVar(),
            "Tomato": tk.BooleanVar(),
            "Cheese": tk.BooleanVar(),
            "Onion": tk.BooleanVar(),
            "Cucumbers": tk.BooleanVar(),
            "Avocado": tk.BooleanVar(),
            "Banana Peppers": tk.BooleanVar()
        }
        self.condiments_vars = {
            "Mayo": tk.BooleanVar(),
            "Mustard": tk.BooleanVar(),
            "Ketchup": tk.BooleanVar(),
            "Relish": tk.BooleanVar(),
            "Pickled Onion": tk.BooleanVar()
        }
        self.quantity_var = tk.IntVar(value=1)

        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Select Bread:").pack()
        breads = ["White Bread", "Wheat Bread", "Sourdough"]
        for bread in breads:
            tk.Radiobutton(self.root, text=bread, variable=self.bread_var, value=bread).pack()
        
        tk.Label(self.root, text="Select Protein:").pack()
        proteins = ["Chicken", "Turkey", "Ham", "Veggie", "Beef", "Tofu", "Fish"]
        for protein in proteins:
            tk.Radiobutton(self.root, text=protein, variable=self.protein_var, value=protein).pack()
        
        tk.Label(self.root, text="Select Toppings:").pack()
        for topping, var in self.toppings_vars.items():
            tk.Checkbutton(self.root, text=topping, variable=var).pack()
        
        tk.Label(self.root, text="Select Condiments:").pack()
        for condiment, var in self.condiments_vars.items():
            tk.Checkbutton(self.root, text=condiment, variable=var).pack()
        
        tk.Label(self.root, text="Quantity:").pack()
        tk.Spinbox(self.root, from_=1, to=10, textvariable=self.quantity_var).pack()
        
        tk.Button(self.root, text="Place Order", command=self.place_order).pack()
    
    def place_order(self):
        order_summary = f"Bread: {self.bread_var.get()}\n"
        order_summary += f"Protein: {self.protein_var.get()}\n"
        order_summary += "Toppings: " + ", ".join([t for t, v in self.toppings_vars.items() if v.get()]) + "\n"
        order_summary += "Condiments: " + ", ".join([c for c, v in self.condiments_vars.items() if v.get()]) + "\n"
        order_summary += f"Quantity: {self.quantity_var.get()}"
        
        messagebox.showinfo("Order Summary", order_summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = SandwichOrderingApp(root)
    root.mainloop()
