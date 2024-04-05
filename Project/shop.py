import tkinter as tk
from tkinter import messagebox

class CoffeeShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ardaciti Coffee")
        self.master.geometry("400x300")  # Set window size

        # Create main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(side="top", expand=True)  # Pack at the top

        # Create Coffee Shop name
        self.shop_name_label = tk.Label(self.main_frame, text="Ardaciti Coffee", font=("Arial", 18))
        self.shop_name_label.pack(pady=10)

        # Create buttons frame
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack()

        # Create Coffee and Tea buttons
        self.coffee_button = tk.Button(self.buttons_frame, text="Coffee", command=self.show_coffee_page)
        self.coffee_button.grid(row=0, column=0, padx=5)

        self.tea_button = tk.Button(self.buttons_frame, text="Tea", command=self.show_tea_page)
        self.tea_button.grid(row=0, column=1, padx=5)

    def show_coffee_page(self):
        # Hide current frame
        self.main_frame.pack_forget()

        # Create Coffee Page
        self.coffee_page = tk.Frame(self.master)
        self.coffee_page.pack(expand=True)

        # Create Coffee Page elements
        coffee_label = tk.Label(self.coffee_page, text="COFFEE", font=("Arial", 18))
        coffee_label.pack(pady=10)

        # Create top and bottom buttons frame
        top_coffee_frame = tk.Frame(self.coffee_page)
        top_coffee_frame.pack()

        bottom_coffee_frame = tk.Frame(self.coffee_page)
        bottom_coffee_frame.pack()

        # Create buttons for different types of coffee
        types_of_coffee = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato"]
        for i, coffee_type in enumerate(types_of_coffee):
            coffee_button = tk.Button(top_coffee_frame if i < len(types_of_coffee)//2 else bottom_coffee_frame, text=coffee_type, command=lambda t=coffee_type: self.order_coffee(t))
            coffee_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create Back button
        back_button = tk.Button(self.coffee_page, text="Back", command=self.show_main_page)
        back_button.pack(pady=10)

    def show_tea_page(self):
        # Hide current frame
        self.main_frame.pack_forget()

        # Create Tea Page
        self.tea_page = tk.Frame(self.master)
        self.tea_page.pack(expand=True)

        # Create Tea Page elements
        tea_label = tk.Label(self.tea_page, text="TEA", font=("Arial", 18))
        tea_label.pack(pady=10)

        # Create Back button
        back_button = tk.Button(self.tea_page, text="Back", command=self.show_main_page)
        back_button.pack(pady=10)

    def show_main_page(self):
        # Show main frame
        self.main_frame.pack(side="top", expand=True)  # Pack at the top

        # Destroy pages
        if hasattr(self, "coffee_page"):
            self.coffee_page.destroy()
        if hasattr(self, "tea_page"):
            self.tea_page.destroy()

    def order_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            self.show_espresso_page()
        else:
            # Ask if customer wants sweetener
            choice = messagebox.askyesno("Sweetener", f"Do you want sweetener with your {coffee_type}?")
            if choice:
                message = f"You ordered {coffee_type} with sweetener."
            else:
                message = f"You ordered {coffee_type} without sweetener."

            # Display message and confirm button
            self.confirm_frame = tk.Frame(self.master)
            self.confirm_frame.pack(pady=10)

            message_label = tk.Label(self.confirm_frame, text=message)
            message_label.pack()

            confirm_button = tk.Button(self.confirm_frame, text="Confirm", command=self.show_main_page)
            confirm_button.pack(pady=5)

    def show_espresso_page(self):
        # Hide current frame
        self.coffee_page.pack_forget()

        # Create Espresso Page
        self.espresso_page = tk.Frame(self.master)
        self.espresso_page.pack(expand=True)

        # Create Espresso Page elements
        espresso_label = tk.Label(self.espresso_page, text="ESPRESSO", font=("Arial", 18))
        espresso_label.pack(pady=10)

        # Create frame for ingredient selection
        ingredient_frame = tk.Frame(self.espresso_page)
        ingredient_frame.pack(pady=10)

        # Ingredients labels and buttons
        sugars_label = tk.Label(ingredient_frame, text="Sugars:")
        sugars_label.grid(row=0, column=0, padx=5)
        self.sugars_var = tk.IntVar()
        self.sugars_var.set(0)
        sugars_entry = tk.Entry(ingredient_frame, textvariable=self.sugars_var, width=5, state="readonly")
        sugars_entry.grid(row=0, column=1)
        sugars_plus_button = tk.Button(ingredient_frame, text="+", command=self.increment_sugars)
        sugars_plus_button.grid(row=0, column=2, padx=5)
        sugars_minus_button = tk.Button(ingredient_frame, text="-", command=self.decrement_sugars)
        sugars_minus_button.grid(row=0, column=3)

        milk_label = tk.Label(ingredient_frame, text="Milk:")
        milk_label.grid(row=1, column=0, padx=5)
        self.milk_var = tk.IntVar()
        self.milk_var.set(0)
        milk_entry = tk.Entry(ingredient_frame, textvariable=self.milk_var, width=5, state="readonly")
        milk_entry.grid(row=1, column=1)
        milk_plus_button = tk.Button(ingredient_frame, text="+", command=self.increment_milk)
        milk_plus_button.grid(row=1, column=2, padx=5)
        milk_minus_button = tk.Button(ingredient_frame, text="-", command=self.decrement_milk)
        milk_minus_button.grid(row=1, column=3)

        # Create Confirm button
        confirm_button = tk.Button(self.espresso_page, text="Confirm Order", command=self.confirm_espresso_order)
        confirm_button.pack(pady=10)

        # Create Back button
        back_button = tk.Button(self.espresso_page, text="Back", command=self.show_main_page)
        back_button.pack(pady=10)

    def increment_sugars(self):
        self.sugars_var.set(self.sugars_var.get() + 1)

    def decrement_sugars(self):
        sugars = self.sugars_var.get()
        if sugars > 0:
            self.sugars_var.set(sugars - 1)

    def increment_milk(self):
        self.milk_var.set(self.milk_var.get() + 1)

    def decrement_milk(self):
        milk = self.milk_var.get()
        if milk > 0:
            self.milk_var.set(milk - 1)

    def confirm_espresso_order(self):
        sugars = self.sugars_var.get()
        milk = self.milk_var.get()
        message = f"You ordered Espresso with {sugars} sugars and {milk} milk."
        messagebox.showinfo("Order Confirmation", message)
        self.show_main_page()
        self.espresso_page.destroy()

def main():
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
