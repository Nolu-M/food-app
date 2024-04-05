from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import speech_recognition as sr
import pyttsx3

class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900")
        self.bg = PhotoImage(file="images/c-beans.png")
        
        self.my_canvas = Canvas(self.root, width=740, height=538)
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30, command=self.open_tea_options)
        self.button2 = Button(text="Coffee", bg="#8B3E2F", fg="white", pady=10, padx=30, command=self.open_coffee_options)
        self.button3 = Button(text="Voice Command", bg="#8B3E2F", fg="white", pady=10, padx=30)

        self.button1_window = self.my_canvas.create_window(200, 400, anchor="nw", window=self.button1)
        self.button2_window = self.my_canvas.create_window(300, 400, anchor="nw", window=self.button2)
        self.button3_window = self.my_canvas.create_window(420, 400, anchor="nw", window=self.button3)

        self.root.bind('<Configure>', self.resizer)

    def resizer(self, e):
        # Open the image
        bg1 = Image.open("images/c-beans.png")
        # resize the image
        resized_bg = bg1.resize((1600, 900), Image.LANCZOS)
        # Define image again
        new_bg = ImageTk.PhotoImage(resized_bg)
        # Add it back to the canvas
        self.my_canvas.create_image(0, 0, image=new_bg, anchor="nw")
        # Read the text
        self.my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        self.my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))

    def open_coffee_options(self):
        # Hide the main menu buttons
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()

        # Create a new frame for coffee options
        coffee_frame = Frame(self.root)
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

        my_canvas2.create_image(0, 0, image=coffee_bg, anchor="nw")

        # Add background image to the frame
        def resized(e):
            nonlocal coffee_bg
            # Open the image
            coffee_bg = Image.open("images/c-beans.png", )
            # Resize the image
            resized_coffee_bg = coffee_bg.resize((1600, 900), Image.LANCZOS)
            # Define image again
            new_coffee_bg = ImageTk.PhotoImage(resized_coffee_bg)
            # Add it back to the canvas
            my_canvas2.create_image(0, 0, image=new_coffee_bg, anchor="nw")
            # Read the text
            my_canvas2.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
            my_canvas2.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
            # Add coffee options
            my_canvas2.create_image(50, 300, image=cuppaccino, anchor="nw", tags="cuppaccino")
            my_canvas2.create_image(300, 300, image=espresso, anchor="nw", tags="espresso")
            my_canvas2.create_image(600, 265, image=latte, anchor="nw", tags="latte")
            my_canvas2.create_image(-25, 550, image=macch, anchor="nw", tags="macch")
            my_canvas2.create_image(330, 550, image=mocha, anchor="nw", tags="mocha")
            my_canvas2.create_image(550, 550, image=ameri, anchor="nw", tags="ameri")
            # Add text under each image
            my_canvas2.create_text(70, 480, text="Cuppaccino", font=("Arial", 14), anchor="nw")
            my_canvas2.create_text(350, 480, text="Espresso", font=("Arial", 14), anchor="nw")
            my_canvas2.create_text(650, 480, text="Latte", font=("Arial", 14), anchor="nw")
            my_canvas2.create_text(90, 700, text="Macchiato", font=("Arial", 14), anchor="nw")
            my_canvas2.create_text(360, 700, text="Mocha", font=("Arial", 14), anchor="nw")
            my_canvas2.create_text(635, 700, text="Americano", font=("Arial", 14), anchor="nw")

        self.root.bind('<Configure>', resized)

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

    def open_tea_options(self):
        # Hide the main menu buttons
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()

        # Create a new frame for coffee options
        tea_frame = Frame(self.root)
        tea_frame.place(relx=0.5, rely=0.5, anchor="center")
        # define images
        tea_bg = PhotoImage(file="images/tea.png")  # background image
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

        my_canvas3.create_image(0, 0, image=tea_bg, anchor="nw")

        # Add background image to the frame
        def resized(e):
            nonlocal tea_bg
            # Open the image
            tea_bg = Image.open("images/tea.png")
            # Resize the image
            resized_tea_bg = tea_bg.resize((1600, 900), Image.LANCZOS)
            # Define image again
            new_tea_bg = ImageTk.PhotoImage(resized_tea_bg)
            # Add it back to the canvas
            my_canvas3.create_image(0, 0, image=new_tea_bg, anchor="nw")
            # Read the text
            my_canvas3.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
            my_canvas3.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
            # Add images
            my_canvas3.create_image(50, 300, image=rooibos, anchor="nw", tags="rooibos")
            my_canvas3.create_image(350, 300, image=peppermint, anchor="nw", tags="peppermint")
            my_canvas3.create_image(600, 300, image=greentea, anchor="nw", tags="greentea")
            my_canvas3.create_image(60, 550, image=cinnamon, anchor="nw", tags="cinnamon")
            my_canvas3.create_image(240, 550, image=chamomile, anchor="nw", tags="chamomile")
            my_canvas3.create_image(570, 500, image=ceylon, anchor="nw", tags="ceylon")
            # Add text under each image
            my_canvas3.create_text(100, 480, text="Rooibos", font=("Arial", 14), anchor="nw")
            my_canvas3.create_text(370, 480, text="Peppermint", font=("Arial", 14), anchor="nw")
            my_canvas3.create_text(635, 480, text="Green Tea", font=("Arial", 14), anchor="nw")
            my_canvas3.create_text(95, 710, text="Cinnamon", font=("Arial", 14), anchor="nw")
            my_canvas3.create_text(380, 710, text="Chamomile", font=("Arial", 14), anchor="nw")
            my_canvas3.create_text(670, 710, text="Ceylon", font=("Arial", 14), anchor="nw")

        self.root.bind('<Configure>', resized)

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

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = CoffeeShopApp(root)
    app.run()











if "hello" in command:
    speak("Hello! How can I help you?")
elif "black coffee" in command:
    speak("Enjoy your coffee")
elif "cappuccino" in command:
            speak("Enjoy your cappuccino")
elif "can i please get a cappuccino" in command:
            speak("Enjoy your cappuccino")
        elif "can i get a cappuccino" in command:
            speak("Enjoy your cappuccino")
        elif "expresso" in command:
            speak("Enjoy your expresso")
        elif "can i please get expresso" in command:
            speak("Enjoy your expresso")
        elif "expresso please" in command:
            speak("Enjoy your expresso")
        elif "mocha" in command:
            speak("enjoy your mocha")
        elif "machiato" in command:
            speak("enjoy your macchiato")
        elif "can i get a machiato" in command:
            speak("enjoy your macchiato")
        elif "can i please get a machiato" in command:
            speak("enjoy your macchiato")
        elif "americano" in command:
            speak("enjoy your americano")
        elif "caffe latte" in command:
            speak("Enjoy your Latte")
        elif "black tea" in command:
            speak("Enjoy your tea")
        elif "milk tea please" in command:
            speak("Enjoy your tea")
            
        elif "can i have some coffee" in command:
            speak("How do you want your coffee?")
            
            user_response = recognize_speech()
            
            if "black" in user_response:
                speak("Enjoy your coffee")
            elif "caffe latte" in user_response:
                speak("enjoy your latte")
            elif "make it latte" in user_response:
                speak("enjoy your latte")
            elif "expresso" in user_response:
                speak("enjoy your expresso")
            elif "mocha" in user_response:
                speak("enjoy your mocha")
            elif "machiato" in user_response:
                speak("enjoy your macchiato")
            elif "americano" in user_response:
                speak("enjoy your americano")
            elif "Cappucciono" in user_response:
                speak("enjoy your cappucciono")
            else:
                speak("Sorry no such request available")
            return True
                
        elif "coffee please" in command:
            speak("How do you want your coffee?")
            
            user_input = recognize_speech()
            
            if "black" in user_input:
                speak("Enjoy your coffee")
            elif "caffe latte" in user_input:
                speak("enjoy your latte")
            elif "latte" in user_input:
                speak("enjoy your latte")
            elif "expresso" in user_input:
                speak("enjoy your expresso")
            elif "mocha" in user_input:
                speak("enjoy your mocha")
            elif "machiato" in user_input:
                speak("enjoy your macchiato")
            elif "americano" in user_input:
                speak("enjoy your americano")
            elif "Cappucciono" in user_input:
                speak("enjoy your cappucciono")
            else:
                speak("Sorry no such request available")
            return True
                
        elif "can i have some tea" in command:
            speak("How do you want your tea?")
            
            user_speak = recognize_speech()
            
            if "rooibos" in user_speak:
                speak("enjoy your tea")
            elif "green tea" in user_speak:
                speak("enjoy your green tea")
            elif "perppermint" in user_speak:
                speak("enjoy your tea")
            elif "chamomile" in user_speak:
                speak("enjoy your tea")
            elif "five roses" in user_speak:
                speak("enjoy your tea")
            elif "cinnamon" in user_speak:
                speak("enjoy your tea")
            else:
                speak("Sorry no such request available")
            return True
                
        elif "tea please" in command:
            speak("How do you want your tea?")
            
            user_talk = recognize_speech()
            
            if "rooibos" in user_talk:
                speak("enjoy your tea")
            elif "green tea" in user_talk:
                speak("enjoy your green tea")
            elif "perppermint" in user_talk:
                speak("enjoy your tea")
            elif "chamomile" in user_talk:
                speak("enjoy your tea")
            elif "five roses" in user_talk:
                speak("enjoy your tea")
            elif "cinnamon" in user_talk:
                speak("enjoy your tea")
            else:
                speak("Sorry no such request available")
            return True
                
        elif "Thank you" in command:
            speak("Enjoy")
        elif "exit the programme" in command:
            speak("Enjoy")
        elif "no nothing" in command:
            speak("Enjoy")
        elif "terminate" in command:
            speak("Enjoy")
        elif "no i'm good" in command:
            speak("Enjoy")
        elif "i'm good" in command:
            speak("Enjoy") 
        else:
            speak("Sorry, I didn't understand that command.")
        return True  
