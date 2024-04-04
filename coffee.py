from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def open_coffee_options():
    # Hide the main menu buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    
    # Create a new frame for coffee options
    coffee_frame = Frame(root)
    coffee_frame.place(relx=0.5, rely=0.5, anchor="center")
    # define images
    coffee_bg = PhotoImage(file="images/c-beans.png")
    # coffee options
    cuppaccino = PhotoImage(file="images/cuppaccino.png").subsample(3)
    espresso = PhotoImage(file="images/espresso.png").subsample(3)
    latte = PhotoImage(file="images/latte.png").subsample(3)
    macch = PhotoImage(file="images/macch.png").subsample(2)
    mocha = PhotoImage(file="images/mocha.png").subsample(3)
    ameri = PhotoImage(file="images/ameri.png").subsample(3)


    # create a canvas
    my_canvas2 = Canvas(coffee_frame, width=1600, height=900)
    my_canvas2.pack(fill="both", expand=True)

    my_canvas2.create_image(0,0, image=coffee_bg, anchor="nw")


    
    # Add background image to the frame
    def resized(e):
        global coffee_bg, resized_coffee_bg, new_coffee_bg
        # Open the image
        coffee_bg = Image.open("images/c-beans.png", )
        # Resize the image
        resized_coffee_bg = coffee_bg.resize((1600, 900), Image.LANCZOS)
        # Define image again
        new_coffee_bg = ImageTk.PhotoImage(resized_coffee_bg)
        # Add it back to the canvas
        my_canvas2.create_image(0,0, image=new_coffee_bg, anchor="nw")
        # Read the text
        my_canvas2.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        my_canvas2.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
        # Add coffee options
        my_canvas2.create_image(50,300, image=cuppaccino, anchor="nw", tags="cuppaccino")
        my_canvas2.create_image(300,300, image=espresso, anchor="nw", tags="espresso")
        my_canvas2.create_image(600,265, image=latte, anchor="nw", tags="latte")
        my_canvas2.create_image(-25,550, image=macch, anchor="nw", tags="macch")
        my_canvas2.create_image(330,550, image=mocha, anchor="nw", tags="mocha")
        my_canvas2.create_image(550,550, image=ameri, anchor="nw", tags="ameri")
        # Add text under each image
        my_canvas2.create_text(70, 480, text="Cuppaccino", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(350, 480, text="Espresso", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(650, 480, text="Latte", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(90, 700, text="Macchiato", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(360, 700, text="Mocha", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(635, 700, text="Americano", font=("Arial", 14), anchor="nw")

    root.bind('<Configure>', resized)

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "cuppaccino" in my_canvas2.gettags(item):
            messagebox.showinfo("Cuppaccino Clicked", "You clicked on Cuppaccino!")
        elif "espresso" in my_canvas2.gettags(item):
            print("espresson clicked")
        elif "latte" in my_canvas2.gettags(item):
            print("Latte clicked")
        elif "macch" in my_canvas2.gettags(item):
            print("Macchiato clicked")
        elif "mocha" in my_canvas2.gettags(item):
            print("Mocha clicked")
        elif 'ameri' in my_canvas2.gettags(item):
            print("Americano clicked")

    my_canvas2.bind("<Button-1>", on_click)


def open_tea_options():
    # Hide the main menu buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    
    # Create a new frame for coffee options
    tea_frame = Frame(root)
    tea_frame.place(relx=0.5, rely=0.5, anchor="center")
    # define images
    tea_bg = PhotoImage(file="images/tea.png") # background image
    # tea options
    rooibos = PhotoImage(file="images/rooibos.png").subsample(3)
    peppermint = PhotoImage(file="images/peppermint.png").subsample(3)
    greentea = PhotoImage(file="images/greentea.png").subsample(3)
    cinnamon = PhotoImage(file="images/cinnamon.png").subsample(3)
    chamomile = PhotoImage(file="images/chamomile.png").subsample(2)
    ceylon = PhotoImage(file="images/ceylon.png")
    # create a canvas
    my_canvas3 = Canvas(tea_frame, width=1600, height=900)
    my_canvas3.pack(fill="both", expand=True)

    my_canvas3.create_image(0,0, image=tea_bg, anchor="nw")
    
    # Add background image to the frame
    def resized(e):
        global tea_bg, resized_tea_bg, new_tea_bg
        # Open the image
        tea_bg = Image.open("images/tea.png")
        # Resize the image
        resized_tea_bg = tea_bg.resize((1600, 900), Image.LANCZOS)
        # Define image again
        new_tea_bg = ImageTk.PhotoImage(resized_tea_bg)
        # Add it back to the canvas
        my_canvas3.create_image(0,0, image=new_tea_bg, anchor="nw")
        # Read the text
        my_canvas3.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        my_canvas3.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
        # Add images
        my_canvas3.create_image(50,300, image=rooibos, anchor="nw", tags="rooibos")
        my_canvas3.create_image(350,300, image=peppermint, anchor="nw", tags="peppermint")
        my_canvas3.create_image(600,300, image=greentea, anchor="nw", tags="greentea")
        my_canvas3.create_image(60,550, image=cinnamon, anchor="nw", tags="cinnamon")
        my_canvas3.create_image(240,550, image=chamomile, anchor="nw", tags="chamomile")
        my_canvas3.create_image(570,500, image=ceylon, anchor="nw", tags="ceylon")
        # Add text under each image
        my_canvas3.create_text(100, 480, text="Rooibos", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(370, 480, text="Peppermint", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(635, 480, text="Green Tea", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(95, 710, text="Cinnamon", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(380, 710, text="Chamomile", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(670, 710, text="Ceylon", font=("Arial", 14), anchor="nw")

    root.bind('<Configure>', resized)

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "rooibos" in my_canvas3.gettags(item):
            messagebox.showinfo("Rooibos Clicked", "You clicked on rooibos!")
        elif "peppermint" in my_canvas3.gettags(item):
            print("Peppermint clicked")
        elif "greentea" in my_canvas3.gettags(item):
            print("Greentea clicked")
        elif "cinnamon" in my_canvas3.gettags(item):
            print("Cinnamon clicked")
        elif "chamomile" in my_canvas3.gettags(item):
            print("Chamomile clicked")
        elif 'ceylon' in my_canvas3.gettags(item):
            print("Ceylon clicked")

    my_canvas3.bind("<Button-1>", on_click)




root = Tk()
root.geometry("1600x900")

# Define image
bg = PhotoImage(file="images/c-beans.png")

# Create a canvas
my_canvas = Canvas(root, width=740, height=538)
my_canvas.pack(fill="both", expand=True)


my_canvas.create_image(0,0, image=bg, anchor="nw")

button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30, command=open_tea_options)
button2 = Button(text="Coffee", bg="#8B3E2F", fg="white", pady=10, padx=30, command=open_coffee_options)
button3 = Button(text="Voice Command", bg="#8B3E2F", fg="white", pady=10, padx=30)


button1_window = my_canvas.create_window(200, 400, anchor="nw", window=button1)
button2_window = my_canvas.create_window(300, 400, anchor="nw", window=button2)
button3_window = my_canvas.create_window(420, 400, anchor="nw", window=button3)

def resizer(e):
    global bg1, resized_bg, new_bg
    # Open the image
    bg1 = Image.open("images/c-beans.png")
    # resize the image
    resized_bg = bg1.resize((1600, 900), Image.LANCZOS)
    # Define image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    # Read the text
    my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
    my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20) )
root.bind('<Configure>', resizer)  



root.mainloop()

