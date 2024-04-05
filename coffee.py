from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3



def open_coffee_options(root, button1, button2, button3):
    global coffee_frame

    if 'coffee_frame' in globals():
        coffee_frame.destroy()
        root.deiconify()

    # Hide the main menu buttons
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    
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

    def add_sweetner(item):
        amount = simpledialog.askinteger("Add Sweetner", "Enter the amount of sweetner (teaspoons):", parent=root)
        if amount is not None:
            messagebox.showinfo("Sweetner Added", f"You added {amount} teaspoons of sweetner to your {item}.")
            root.deiconify()
            #coffee_frame.destroy() commented the line out so that if someone wants another cup, they don't have to restart the whole process again.

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "cuppaccino" in my_canvas2.gettags(item):
            add_sweetner("Cuppaccino")
        elif "espresso" in my_canvas2.gettags(item):
            add_sweetner("Espresso")
        elif "latte" in my_canvas2.gettags(item):
            add_sweetner("Latte")
        elif "macch" in my_canvas2.gettags(item):
            add_sweetner("Macchiato")
        elif "mocha" in my_canvas2.gettags(item):
            add_sweetner("Mocha")
        elif 'ameri' in my_canvas2.gettags(item):
            add_sweetner("Americano")
    my_canvas2.bind("<Button-1>", on_click)

    # Go back to main menu
    def go_back():
        root.deiconify()
        coffee_frame.destroy()
    # Create a button to go back
    back_button = Button(coffee_frame, text="Back to Menu", bg="#8B3E2F", fg="white", pady=10, padx=30, command=go_back)
    back_button_window = my_canvas2.create_window(300, 750, anchor="nw", window=back_button)



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

    def add_sweetner(item):
        amount = simpledialog.askinteger("Add Sweetner", "Enter the amount of sweetner (teaspoons):", parent=root)
        if amount is not None:
            messagebox.showinfo("Sweetner Added", f"You added {amount} teaspoons of sweetner to your {item}.")
            root.deiconify()
            #tea_frame.destroy() commented the line out so that if someone wants another cup, they don't have to restart the whole process again.

    def on_click(event):
        # get clicked item
        item = event.widget.find_closest(event.x, event.y)[0]
        
        if "rooibos" in my_canvas3.gettags(item):
            add_sweetner("Rooibos")
        elif "peppermint" in my_canvas3.gettags(item):
            add_sweetner("Peppermint")
        elif "greentea" in my_canvas3.gettags(item):
            add_sweetner("Greentea")
        elif "cinnamon" in my_canvas3.gettags(item):
            add_sweetner("Cinnamon")
        elif "chamomile" in my_canvas3.gettags(item):
            add_sweetner("Chamomile")
        elif 'ceylon' in my_canvas3.gettags(item):
            add_sweetner("Ceylon")

    my_canvas3.bind("<Button-1>", on_click)
    
    def go_back():
        root.deiconify()
        tea_frame.destroy()
    # Create a button to go back
    back_button = Button(tea_frame, text="Back to Menu", bg="#8B3E2F", fg="white", pady=10, padx=30, command=go_back)
    back_button_window = my_canvas3.create_window(350, 760, anchor="nw", window=back_button)

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

    

    # Define image
    bg = PhotoImage(file="images/c-beans.png")

    # Create a canvas
    my_canvas = Canvas(root, width=740, height=538)
    my_canvas.pack(fill="both", expand=True)

    
    my_canvas.create_image(0,0, image=bg, anchor="nw")

    

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
        my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20) )
    root.bind('<Configure>', resizer)  

    root.mainloop()

create_main_menu() 

