from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import pyaudio
import tkinter as tk
import csv
from datetime import datetime


# Initialize counters globally
coffee_order_count = 0
tea_order_count = 0
sugar_level = 0
milk_level = 0
cup_size = "Small"

def open_coffee_options(root, button1, button2, button3):
    global coffee_frame

    if 'coffee_frame' in globals():
        coffee_frame.destroy()
        root.deiconify()

    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    
    coffee_frame = Frame(root)
    coffee_frame.place(relx=0.5, rely=0.5, anchor="center")
    coffee_bg = PhotoImage(file="images/c-beans.png")
    cuppaccino = PhotoImage(file="images/cuppaccino.png").subsample(3)
    espresso = PhotoImage(file="images/espresso.png").subsample(3)
    latte = PhotoImage(file="images/latte.png").subsample(3)
    macch = PhotoImage(file="images/macch.png").subsample(2)
    mocha = PhotoImage(file="images/mocha.png").subsample(3)
    ameri = PhotoImage(file="images/ameri.png").subsample(3)

    my_canvas2 = Canvas(coffee_frame, width=1600, height=900)
    my_canvas2.pack(fill="both", expand=True)
    my_canvas2.create_image(0,0, image=coffee_bg, anchor="nw")
    
    def resized(e):
        global coffee_bg, resized_coffee_bg, new_coffee_bg
        coffee_bg = Image.open("images/c-beans.png", )
        resized_coffee_bg = coffee_bg.resize((1600, 900), Image.LANCZOS)
        new_coffee_bg = ImageTk.PhotoImage(resized_coffee_bg)
        my_canvas2.create_image(0,0, image=new_coffee_bg, anchor="nw")
        my_canvas2.create_text(400, 100, text="ArdaCiti Machine", font=("Segoe Script", 40))
        my_canvas2.create_text(400, 150, text="Where Coffee Meets Tea, Harmony in Every Cup", font=("Segoe Script", 20))
        my_canvas2.create_image(50,250, image=cuppaccino, anchor="nw", tags="cuppaccino")
        my_canvas2.create_image(300,250, image=espresso, anchor="nw", tags="espresso")
        my_canvas2.create_image(600,205, image=latte, anchor="nw", tags="latte")
        my_canvas2.create_image(-25,500, image=macch, anchor="nw", tags="macch")
        my_canvas2.create_image(330,500, image=mocha, anchor="nw", tags="mocha")
        my_canvas2.create_image(550,500, image=ameri, anchor="nw", tags="ameri")
        my_canvas2.create_text(70, 430, text="Cuppaccino", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(350, 430, text="Espresso", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(650, 430, text="Latte", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(90, 640, text="Macchiato", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(360, 640, text="Mocha", font=("Arial", 14), anchor="nw")
        my_canvas2.create_text(635, 640, text="Americano", font=("Arial", 14), anchor="nw")
    root.bind('<Configure>', resized)

    def customize_coffee(coffee_type):
        popup = tk.Toplevel(root)
        popup.title("Customize Coffee")

        global sugar_level, milk_level, cup_size, coffee_order_count
        
        #incrementing coffee order count
        coffee_order_count += 1
       
        sugar_level = 0
        milk_level = 0
        cup_size = "Small"

        def increment_sugar():
            global sugar_level
            sugar_level += 1
            sugar_label.config(text=f" Sugar Level: {sugar_level}")

        def decrement_sugar():
            global sugar_level
            if sugar_level > 0:
                sugar_level -= 1
                sugar_label.config(text=f" Sugar Level: {sugar_level}")

        def increment_milk():
            global milk_level
            milk_level += 1
            milk_label.config(text=f" Milk Level: {milk_level}")

        def decrement_milk():
            global milk_level
            if milk_level > 0:
                milk_level -= 1
                milk_label.config(text=f" Milk Level: {milk_level}")

        def update_cup_size(size):
            global cup_size
            cup_size = size
            cup_label.config(text=f"Cup Size: {cup_size}")

        def confirm_order():
            global sugar_level, milk_level, cup_size, coffee_order_count, order_name
            order_name = f"{coffee_type}"
            order_details = {
                'Name': order_name,
                'Number': 1,
                'Type': 'Coffee',
                'Size': cup_size,
                'Sugar_Level': sugar_level,
                'Milk_Level': milk_level,
                'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            with open('orders.csv', 'a', newline='') as csvfile:
                fieldnames = ['Name', 'Number', 'Type', 'Size', 'Sugar_Level', 'Milk_Level', 'Date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(order_details)

            print("Order confirmed and saved to CSV.")
            popup.destroy()

        sugar_frame = tk.Frame(popup)#, bg="white")
        sugar_frame.grid(row=0, column=0, padx=10, pady=10)

        sugar_label = tk.Label(sugar_frame, text="Sugar Level:")
        sugar_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        sugar_increment_button = tk.Button(sugar_frame, text="+", command=increment_sugar)
        sugar_increment_button.grid(row=0, column=1, padx=5, pady=5)

        sugar_decrement_button = tk.Button(sugar_frame, text="-", command=decrement_sugar)
        sugar_decrement_button.grid(row=0, column=2, padx=5, pady=5)

        # Milk section
        milk_frame = tk.Frame(popup)
        milk_frame.grid(row=1, column=0, padx=10, pady=10)

        milk_label = tk.Label(milk_frame, text="Milk Level:")
        milk_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        milk_increment_button = tk.Button(milk_frame, text="+", command=increment_milk)
        milk_increment_button.grid(row=0, column=1, padx=5, pady=5)

        milk_decrement_button = tk.Button(milk_frame, text="-", command=decrement_milk)
        milk_decrement_button.grid(row=0, column=2, padx=5, pady=5)

        # Cup size section
        cup_frame = tk.Frame(popup)
        cup_frame.grid(row=2, column=0, padx=10, pady=10)

        cup_label = tk.Label(cup_frame, text="Cup Size:")
        cup_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#Lindelani
        def update_cup_label(size):
            cup_label.config(text=f"Cup Size: {size}")

        small_button = tk.Button(cup_frame, text="Small", command=lambda: (update_cup_size("Small"), update_cup_label("Small")))
        small_button.grid(row=0, column=1, padx=5, pady=5)

        medium_button = tk.Button(cup_frame, text="Medium", command=lambda: (update_cup_size("Medium"), update_cup_label("Medium")))
        medium_button.grid(row=0, column=2, padx=5, pady=5)

        large_button = tk.Button(cup_frame, text="Large", command=lambda: (update_cup_size("Large"), update_cup_label("Large")))
        large_button.grid(row=0, column=3, padx=5, pady=5)

        confirm_button = tk.Button(popup, text="Confirm", command=confirm_order)
        confirm_button.grid(row=4, column=0, padx=10, pady=10)

        # recognizer = sr.Recognizer()
        # engine = pyttsx3.init()

        # def speak(text):
        #     engine.say(text)
        #     engine.runAndWait()

        # def confirm_order(coffee_type):
        #     speak(f"Enjoy your {coffee_type}")
        #     popup.destroy()
        #     coffee_frame.destroy()

#Mtiza

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "cuppaccino" in my_canvas2.gettags(item):
            customize_coffee("Cuppaccino")
        elif "espresso" in my_canvas2.gettags(item):
            customize_coffee("Espresso")
        elif "latte" in my_canvas2.gettags(item):
            customize_coffee("Latte")
        elif "macch" in my_canvas2.gettags(item):
            customize_coffee("Macchiato")
        elif "mocha" in my_canvas2.gettags(item):
            customize_coffee("Mocha")
        elif 'ameri' in my_canvas2.gettags(item):
            customize_coffee("Americano")
    my_canvas2.bind("<Button-1>", on_click)

    # Go back to main menu
    def go_back():
        root.deiconify()
        coffee_frame.destroy()
    # Create a button to go back
    back_button = Button(coffee_frame, text="Back to Menu", bg="#8B3E2F", fg="white", pady=10, padx=30, command=go_back)
    back_button_window = my_canvas2.create_window(320, 680, anchor="nw", window=back_button)



def open_tea_options(root, button1, button2, button3):
    global tea_frame

    if 'tea_frame' in globals():
        tea_frame.destroy()
        root.deiconify()
        
    # Hide the main menu buttons
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    
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
        my_canvas3.create_text(400, 100, text="ArdaCiti Machine", font=("Segoe Script", 40))
        my_canvas3.create_text(400, 150, text="Where Coffee Meets Tea, Harmony in Every Cup", font=("Segoe Script", 20))
        # Add images
        my_canvas3.create_image(50,250, image=rooibos, anchor="nw", tags="rooibos")
        my_canvas3.create_image(350,250, image=peppermint, anchor="nw", tags="peppermint")
        my_canvas3.create_image(600,250, image=greentea, anchor="nw", tags="greentea")
        my_canvas3.create_image(60,480, image=cinnamon, anchor="nw", tags="cinnamon")
        my_canvas3.create_image(240,480, image=chamomile, anchor="nw", tags="chamomile")
        my_canvas3.create_image(570,430, image=ceylon, anchor="nw", tags="ceylon")
        # Add text under each image
        my_canvas3.create_text(100, 410, text="Rooibos", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(370, 410, text="Peppermint", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(635, 410, text="Green Tea", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(95, 640, text="Cinnamon", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(380, 640, text="Chamomile", font=("Arial", 14), anchor="nw")
        my_canvas3.create_text(670, 640, text="Ceylon", font=("Arial", 14), anchor="nw")
    root.bind('<Configure>', resized)

    # Customizing the tea pop-up
    def customize_tea(tea_type):
        # Create a pop-up window
        popup = tk.Toplevel(root)
        popup.title("Customize Coffee")

        global sugar_level, milk_level, cup_size, tea_order_count # Declare variables as global to see it incrementing and decrementing

        #incrementing tea order count
        tea_order_count += 1 
        
        sugar_level = 0
        milk_level = 0
        cup_size = "Small"  # Default cup size

        def increment_sugar():
            global sugar_level
            sugar_level += 1
            sugar_label.config(text=f" Sugar Level: {sugar_level}")

        def decrement_sugar():
            global sugar_level
            if sugar_level > 0:
                sugar_level -= 1
                sugar_label.config(text=f" Sugar Level: {sugar_level}")

        def increment_milk():
            global milk_level
            milk_level += 1
            milk_label.config(text=f" Milk Level: {milk_level}")

        def decrement_milk():
            global milk_level
            if milk_level > 0:
                milk_level -= 1
                milk_label.config(text=f" Milk Level: {milk_level}")

        def update_cup_size(size):
            global cup_size
            cup_size = size
            cup_label.config(text=f"Cup Size: {cup_size}")

        def confirm_order():
            global sugar_level, milk_level, cup_size, tea_order_count
            order_name = f"{tea_type}"
            order_details = {
                'Name': order_name,
                'Number': 1,
                'Type': 'Tea',
                'Size': cup_size,
                'Sugar_Level': sugar_level,
                'Milk_Level': milk_level,
                'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            with open('orders.csv', 'a', newline='') as csvfile:
                fieldnames = ['Name', 'Number', 'Type', 'Size', 'Sugar_Level', 'Milk_Level', 'Date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(order_details)

            print("Order confirmed and saved to CSV.")
            popup.destroy()

        # def confirm_order():
        #     # This function should handle the confirmation of the order
        #     # For now, let's just print the chosen options
        #     print("Sugar Level:", sugar_level)
        #     print("Milk Level:", milk_level)
        #     print("Cup Size:", cup_size)

        #     popup.destroy()  # Close the popup window

        sugar_frame = tk.Frame(popup)#, bg="white")
        sugar_frame.grid(row=0, column=0, padx=10, pady=10)

        sugar_label = tk.Label(sugar_frame, text="Sugar Level:")
        sugar_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        sugar_increment_button = tk.Button(sugar_frame, text="+", command=increment_sugar)
        sugar_increment_button.grid(row=0, column=1, padx=5, pady=5)

        sugar_decrement_button = tk.Button(sugar_frame, text="-", command=decrement_sugar)
        sugar_decrement_button.grid(row=0, column=2, padx=5, pady=5)

        # Milk section
        milk_frame = tk.Frame(popup)
        milk_frame.grid(row=1, column=0, padx=10, pady=10)

        milk_label = tk.Label(milk_frame, text="Milk Level:")
        milk_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        milk_increment_button = tk.Button(milk_frame, text="+", command=increment_milk)
        milk_increment_button.grid(row=0, column=1, padx=5, pady=5)

        milk_decrement_button = tk.Button(milk_frame, text="-", command=decrement_milk)
        milk_decrement_button.grid(row=0, column=2, padx=5, pady=5)

        # Cup size section
        cup_frame = tk.Frame(popup)
        cup_frame.grid(row=2, column=0, padx=10, pady=10)

        cup_label = tk.Label(cup_frame, text="Cup Size:")
        cup_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # def update_cup_label(size):
        #     cup_label.config(text=f"Cup Size: {size}")

        # small_button = tk.Button(cup_frame, text="Small", command=lambda: (update_cup_size("Small"), update_cup_label("Small")))
        # small_button.grid(row=0, column=1, padx=5, pady=5)

        # medium_button = tk.Button(cup_frame, text="Medium", command=lambda: (update_cup_size("Medium"), update_cup_label("Medium")))
        # medium_button.grid(row=0, column=2, padx=5, pady=5)

        # large_button = tk.Button(cup_frame, text="Large", command=lambda: (update_cup_size("Large"), update_cup_label("Large")))
        # large_button.grid(row=0, column=3, padx=5, pady=5)
        
# Lindelani
        def update_cup_label(size):
            cup_label.config(text=f"Cup Size: {size}")

        small_button = tk.Button(cup_frame, text="Small", command=lambda: (update_cup_size("Small"), update_cup_label("Small")))
        small_button.grid(row=0, column=1, padx=5, pady=5)

        medium_button = tk.Button(cup_frame, text="Medium", command=lambda: (update_cup_size("Medium"), update_cup_label("Medium")))
        medium_button.grid(row=0, column=2, padx=5, pady=5)

        large_button = tk.Button(cup_frame, text="Large", command=lambda: (update_cup_size("Large"), update_cup_label("Large")))
        large_button.grid(row=0, column=3, padx=5, pady=5)

        confirm_button = tk.Button(popup, text="Confirm", command=confirm_order)
        confirm_button.grid(row=4, column=0, padx=10, pady=10)

#Mtiza
        # recognizer = sr.Recognizer()
        # engine = pyttsx3.init()

        # def speak(text):
        #     engine.say(text)
        #     engine.runAndWait()

        # def confirm_order(tea_type):
        #     speak(f"Enjoy your {tea_type} tea")
        #     popup.destroy()
        #     tea_frame.destroy()


        # confirm_button = tk.Button(popup, text="Confirm", command=lambda: confirm_order(tea_type))
        # confirm_button.grid(row=4, column=0, padx=10, pady=10)

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "rooibos" in my_canvas3.gettags(item):
            customize_tea("Rooibos")
        elif "peppermint" in my_canvas3.gettags(item):
            customize_tea("Peppermint")
        elif "greentea" in my_canvas3.gettags(item):
            customize_tea("Greentea")
        elif "cinnamon" in my_canvas3.gettags(item):
            customize_tea("Cinnamon")
        elif "chamomile" in my_canvas3.gettags(item):
            customize_tea("Chamomile")
        elif 'ceylon' in my_canvas3.gettags(item):
            customize_tea("Ceylon")
    my_canvas3.bind("<Button-1>", on_click)
    
    def go_back():
        root.deiconify()
        tea_frame.destroy()
    # Create a button to go back
    back_button = Button(tea_frame, text="Back to Menu", bg="#8B3E2F", fg="white", pady=10, padx=30, command=go_back)
    back_button_window = my_canvas3.create_window(360, 690, anchor="nw", window=back_button)

# main menu
def create_main_menu():
# Voice recognition
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def recognize_speech():
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            print("Recognizing...")
            user_response = recognizer.recognize_google(audio)
            print("User said:", user_response)
            return user_response.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
        return False

    def process_command(command):
    
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
        elif "espresso" in command:
            speak("Enjoy your expresso")
        elif "can i please get expresso" in command:
            speak("Enjoy your expresso")
        elif "espresso please" in command:
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
            elif "ceylon" in user_speak:
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
            elif "ceylon" in user_talk:
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

    def on_click1():
        main()

    def main():
        speak("Hello! How can I help you?")
        while True:
            try:
                command = recognize_speech()
                if process_command(command):
                    break
            except Exception as e:
                print("Error:", e)
                speak("Sorry, there was an error processing your request.")


    root = Tk()
    root.geometry("1600x900")
    root.iconbitmap('images/coffee_icon.ico')
    root.title("ArdaCiTi Machine")

    # Define image
    bg = PhotoImage(file="images/c-beans.png")

    # Create a canvas
    my_canvas = Canvas(root, width=740, height=538)
    my_canvas.pack(fill="both", expand=True)

    
    my_canvas.create_image(0,0, image=bg, anchor="nw")

    
    # Buttons leading to the different frames and the voice recognition
    button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30, command=lambda: open_tea_options(root, button1, button2, button3))
    button2 = Button(text="Coffee", bg="#8B3E2F", fg="white", pady=10, padx=30, command=lambda:open_coffee_options(root, button1, button2, button3))
    button3 = Button(text="Voice Command", bg="#8B3E2F", fg="white", pady=10, padx=30, command=on_click1)


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
        my_canvas.create_text(400, 100, text="ArdaCiti Machine", font=("Segoe Script", 40))
        my_canvas.create_text(400, 150, text="Where Coffee Meets Tea, Harmony in Every Cup", font=("Segoe Script", 20) )
    root.bind('<Configure>', resizer)  

    root.mainloop()

create_main_menu() 