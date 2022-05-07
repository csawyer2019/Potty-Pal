
import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Potty Pal")
window.iconbitmap('')


# after receiving the pets name, the function is commanded to open the second landing page
def start():
    petname = entry.get()
    windowtwo = Toplevel()
    petname = entry.get()
    # function to create the info pop up to clarify for the user why we are asking for this information
    def popup():
        messagebox.showinfo("Why are you asking me these questions? ", """Did they just wake up?
        Just like when you wake up in the morning, or from a nap, you usually need to use the bathroom. So does your puppy.\n
        Have they drank water in the last 20 minutes?
        If it’s been about 20 minutes since your puppy has drank a decent amount of water, they likely need to use the
        bathroom? Remember their bodies are small so it does not take long for the body to digest, and they don’t know yet 
        how to recognize and control their potty habits.\n
        Have they eaten in the last 30 min?
        Similar to water, if it’s been about 30 minutes since your puppy has eaten, they likely need to go potty. Food takes
        a bit more time to work its way through then water, which is why we ask 30 minutes. And yes, sometimes that means 
        you may have to take your puppy outside 10 minutes after their last potty.""")
    # code that determines how to advise the user if the puppy needs to go potty
    def decision():
        if sleep == 0 or water == 0 or food == 0:
            yes = Label(windowtwo, text="Yes! Your puppy likely needs to go potty!")
            yes.pack()
        else:
            no = Label(windowtwo, text="No, your puppy probably doesn't need to go potty.However, keep a close eye on "
                                       "them to watch for their tells.")
            no.pack()

    checkboxframe = LabelFrame(windowtwo, text="Does my puppy need to go potty?", padx=5, pady=5)
    checkboxframe.pack(padx=10, pady=10)

    instructions = Label(checkboxframe, text="Check the box if the statement is true, then click the submit button")
    instructions.pack()

    var = IntVar()
    sleep = Checkbutton(checkboxframe, text="Did " + petname + " just wake up?", variable=var)
    sleep.pack()
    var = IntVar()
    water = Checkbutton(checkboxframe, text="Has " + petname + " drank water in the last 20 minutes?", variable=var)
    water.pack()
    var = IntVar()
    food = Checkbutton(checkboxframe, text="Has " + petname + " eaten in the last 30 min?", variable=var)
    food.pack()
    decisionbutton = Button(checkboxframe, text="Submit", command=decision)
    decisionbutton.pack()
    # button allowing the user to obtain clarification
    Button(windowtwo, text="Why are you asking me these questions? ", command=popup).pack()
    quitbutton = Button(windowtwo, text="Exit", command=window.quit)
    quitbutton.pack()


# creating the home page
greeting = Label(window, text="""HI! Welcome to Potty Pal.\n We’re here to take out the guess work and to help make 
potty training your best friend a little easier. Within this app, you will be able to input some basic information, 
the app will then tell you if your puppy might need to go potty. \nPotty Training 101: \nHolding their bladders to 
only potty outside is not a skill that your puppy is born with. They must be taught. The younger and the smaller your 
puppy, the less they understand and the less they can control. Potty training will not happen overnight. It is an 
opportunity for you and your puppy to bond and get to know each other’s behavior. Accidents will happen, but the more 
consistent you are the faster your pup will learn. Puppies are like babies, they thrive when they have a schedule. 
Sleeping allows them the time they need to process the things they learn and recharge so their body has the energy it 
needs to grow. Just like a baby, your puppy may not always seem enthusiastic about a sleep, potty, play schedule. But 
unless you are able to give them you’re undivided attention 24/7, the schedule may work best for everyone.""")
greeting.pack()
trainingframe = LabelFrame(window, text="Training Tricks and Tips", padx=5, pady=5)
trainingframe.pack(padx=20, pady=10)
trainingTips = Label(trainingframe, text="""\nObserve your puppy’s behavior right before they go potty. This will 
help you identify their telltale signs. Do they sniff the floor, do they start to go in circles, do they abruptly 
stop what they’re doing, do they bark at you or paw at you? Each puppy is unique, but they will find a way to 
communicate with you if you’re willing to listen. \n If at all possible, crate train your puppy. There are so many 
benefits to crate training. Among these benefits, it will keep both your home and your puppy safe. The appropriate 
size crate will also prevent the puppy from having an accident, because for the most part they do not want to dirty 
their safe space. \n When your puppy successfully pottys outside, throw them a party! Celebrate! Pet them, 
give those treats, reward them with their favorite toy or chew. They’ll catch on that pottying outside is better than 
inside. \n Make outside playtime and potty time separate. If your puppy needs to go potty, take them outside tell 
them to go potty and do not play with them. If you want to play outside, when they are done going potty do your 
celebration, go back inside and close the door. Then announce its playtime, then go back outside to have fun! \n 
Potty pads can be confusing, if possible avoid using them. They train your puppy that it’s ok to potty inside 
sometimes.""")
trainingTips.pack()
tellUs = Label(window, text="Alright, let's get started, tell us your pups name: ")
tellUs.pack()
entry = Entry(window)
entry.pack()

startButton = Button(window, text="Let's Get Started", command=start)
startButton.pack()

window.mainloop()
