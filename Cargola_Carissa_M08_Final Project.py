import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



window = Tk()
window.title("Potty Pal")
# window.iconbitmap('C:\pythonProject19\pawprint.ico')
# puppiesingrass = image("puppiesingrass.gif")
# welcome = image('welcome.gif')



# after receiving the pets name, the function is commanded to open the second landing page
def start():
    petname = entry.get()
    windowtwo = Toplevel()
    petname = entry.get()
    # function to create the info pop up to clarify for the user why we are asking for this information
    def popup():
        messagebox.showinfo("Why are you asking this? ", """
        Just like when you wake up in the morning, or from 
        a nap, you usually need to use the bathroom. So does your puppy.\n        
        If it’s been about 20 minutes since your puppy has drank a decent
        amount of water, they likely need to use the bathroom.
        Remember their bodies are small so it does not take long for the 
        body to digest, and they don’t know yet how to recognize and 
        control their potty habits.\n        
        Similar to water, if it’s been about 30 minutes since your puppy 
        has eaten, they likely need to go potty. Food takes a bit more 
        time to work its way through then water, which is why we ask 30 
        minutes. And yes, sometimes that means you may have to take your 
        puppy outside 10 minutes after their last potty.""")
    # code that determines how to advise the user if the puppy needs to go potty
    def decision():
        if var.get() or var2.get() or var3.get():
            yes = Label(windowtwo, text="Yes! Your puppy likely needs to go potty!")
            yes.pack()
        else:
            no = Label(windowtwo, text="No, your puppy doesn't need to go potty.")
            no.pack()

    # code that establishes the checkbox frame, displays the questions, allows user to make selections and submit
    checkboxframe = LabelFrame(windowtwo, text="Does my puppy need to go potty?", padx=5, pady=5)
    checkboxframe.pack(padx=10, pady=10)

    instructions = Label(checkboxframe, text="Check the box if the statement is true, then click the submit button")
    instructions.pack()

    var = IntVar()
    sleep = Checkbutton(checkboxframe, text="Did " + petname + " just wake up?", variable=var)
    sleep.pack()
    var2 = IntVar()
    water = Checkbutton(checkboxframe, text="Has " + petname + " drank water in the last 20 minutes?", variable=var2)
    water.pack()
    var3 = IntVar()
    food = Checkbutton(checkboxframe, text="Has " + petname + " eaten in the last 30 min?", variable=var3)
    food.pack()
    decisionbutton = Button(checkboxframe, text="Submit", command=decision)
    decisionbutton.pack()
    # button allowing the user to obtain clarification
    Button(windowtwo, text="Why are you asking me these questions? ", command=popup).pack()
    quitbutton = Button(windowtwo, text="Exit App", command=window.quit) # allows use to exit application
    quitbutton.pack()

# creating the home page
greeting = Label(window, text="""HI! Welcome to Potty Pal.\n We’re here to take out the guess work and to help make 
potty training your best friend a little easier. Within this app, you will be able to input some basic information, 
the app will then tell you if your puppy might need to go potty.""")
greeting.pack()

# creates frame for separate section on the greeting page
pottyframe = LabelFrame(window, text="Potty Training 101", padx=5, pady=5)
pottyframe.pack(padx=20, pady=10)
potty = Label(pottyframe, text=(
    """Potty Training must be taught\nIt will not happen overnight\nAccidents will happen
    Puppies are like babies\nThey thrive on a schedule\nIt is a bonding experience"""))
potty.pack()

# creates frame for separate section on the greeting page
trainingframe = LabelFrame(window, text="Training Tricks and Tips", padx=5, pady=5)
trainingframe.pack(padx=20, pady=10)
training = Label(trainingframe, text=("""Crate train your puppy
Make outside playtime and potty time separate
Observe your puppy’s behavior right before they potty 
When they potty outside, throw them a party! Celebrate! 
Potty pads can be confusing, they train your puppy that it’s ok to potty inside."""))
training.pack()

# label and entry field to obtain pups name
tellUs = Label(window, text="First, tell us your pups name: ")
tellUs.pack()
entry = Entry(window)
entry.pack()
# button which allows the user to submit their pets name and launch the second page
startButton = Button(window, text="Let's Get Started", command=start)
startButton.pack()

window.mainloop()
