from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title ("SafeSpace") 

root.geometry("700x350") 
root.configure(bg="PaleGreen")

#BACK BUTTON
def backBtn():
  back = Button(root, text = "BACK", command = main, font = ("Times",9), bg="DarkGreen", fg="White")
  back.place(x=15,y=15)

#DELETE ALL WIDGETS
def delete():
  for widgets in root.winfo_children():
    widgets.destroy()

#CLEAR WINDOW
def exitApp():
    root.destroy()

#MENU SECTIONS

#ABOUT SECTION
def about(): #second tab, destroys elements of first tab and displays elements of second page) 
  delete()

  title1 = Label(root, text="\n About", font = ("Times",20),fg="DarkGreen", bg="PaleGreen")
  title1.pack()

  abt_text = Label(root, text=" \n Bullying (both online and in real life) is a more prevalent issue than many believe. \n Here at Safe Space, we are firmly opposed and intolerant to any forms of bullying and \n hope to promote kindness and mental wellness! ", font = ("Times",10), bg="PaleGreen", fg="Black", width="200")
  abt_text.pack()

  abt_text2 = Label(root, text="\nOur resources page provides external sources\n with more information and tips related to experiencing bullying.", font = ("Times",10), bg="PaleGreen", fg="Black",width="2000")
  abt_text2.pack()

  abt_text3 = Label(root, text="\nOur reporting system allows you to report any \n instances of bullying that you have witnessed, experienced or been involved with.", font = ("Times",10), bg="PaleGreen", fg="Black", width="2000")
  abt_text3.pack()

  abt_text4 = Label(root, text="\nOur chat feature gives you to opportunity to answer questions \n and reflect on your mental health. \n", font = ("Times",10), bg="PaleGreen", fg="Black", width="2000")
  abt_text4.pack()

  #cyberbullying image
  global img2
  img2 = ImageTk.PhotoImage(Image.open("Cyberbullying.png"))
  label_img2 = Label(image = img2)
  label_img2.pack()

  backBtn()

#RESOURCES SECTION
def resources(): #third tab, destroys elements of first tab and displays elements of third tab
  delete()

  title2 = Label(root, text="\n Resources", font = ("Times",20),fg="DarkGreen", bg="PaleGreen")
  title2.pack()

  #Displaying websites name and description

  startText = Label(text = "\n Here are some websites that helps victims of cyberbullying \n and those who are struggling:", font = ("Times",10),fg="black", bg = "PaleGreen")
  startText.pack()

  resource = Label(text = "\n NeedHelpNow", font = ("Times",12),fg="black", bg = "PaleGreen")
  resource.pack()

  description = Label(text = "This organization helps people who are struggling with inappropriate \n images being shared on social media. They stop the spread \n of inappropriate images while giving support to the victim.",font = ("Times",10),fg="black", bg = "PaleGreen")
  description.pack()

  resource2 = Label(text = "\n BullyingCanada", font = ("Times",12),fg="black", bg = "PaleGreen")
  resource2.pack()

  description2 = Label(text = "BullyingCanada is a national anti-bullying charity to help bullied youth \n to have a brighter future. They bring together bullied kids and \n provide them with information on bullying and how to stop it.",font = ("Times",10),fg="black", bg = "PaleGreen")
  description2.pack()

  resource3 = Label(text = "\n KidsHelpPhone", font = ("Times",12),fg="black", bg = "PaleGreen")
  resource3.pack()

  description3 = Label(text = "KidsHelpPhone helps people who are experiencing difficulties or \n require assistance by providing a safe and trusted place for the victims.",font = ("Times",10),fg="black", bg = "PaleGreen")
  description3.pack()

  resource4 = Label(text = "\n TalkSuicideCanada", font = ("Times",12),fg="black", bg = "PaleGreen")
  resource4.pack()

  description4 = Label(text = "TalkSuicideCanada provides a nationwide 24-hour bilingual support service to \n anyone who is facing suicide.",font = ("Times",10),fg="black", bg = "PaleGreen")
  description4.pack()

  backBtn()

#SIGNS & INFO SECTION
def signs(): 
  delete()

  title3 = Label(root, text="\n Signs and Information", font = ("Times",20),fg="DarkGreen", bg="PaleGreen")
  title3.pack()

  #Displaying defintion, statistics & bullying signs
  subtitle = Label(text = "\n What is Cyberbullying?", font = ("Times",12),fg="black", bg = "PaleGreen")
  subtitle.pack()

  info = Label(text = "Cyberbullying can occur anywhere at anytime as it occurs online. It is when \n someone uses the internet or technology to harass, threaten, embarass, or target \n another person. The effects of cyberbullying are big because information can be \n shared and saved online.",font = ("Times",10),fg="black", bg = "PaleGreen")
  info.pack()

  subtitle2 = Label(text = "\n Statistics:", font = ("Times",12),fg="black", bg = "PaleGreen")
  subtitle2.pack()

  info2 = Label(text="- 47% of Canadian parents report having a child victim of bullying\n - 1/10 teen victims will seek help from a parent or a trusted adult \n - Threats and harmful emails or messages are the most common forms \n - Instagram is the most common social media site where most young \n people experience cyberbullying",font = ("Times",10),fg="black", bg = "PaleGreen")
  info2.pack()

  subtitle3 = Label(text = "\n Signs of Bullying:", font = ("Times",12),fg="black", bg = "PaleGreen")
  subtitle3.pack()

  info3 = Label(text="- Low self esteem, depression, or anxiety \n - Changes in mood, behaviour, sleep schedules and appetite \n - Distancing themselves from group activities with family and friends \n - Not wanting to go to school or classes \n - Drop in grades", font = ("Times",10),fg="black", bg = "PaleGreen")
  info3.pack()

  #social media image
  global img3
  img3 = ImageTk.PhotoImage(Image.open("SocialMedia.png"))
  label_img3 = Label(image = img3)
  label_img3.place(relx=0.9, rely=0.1, anchor=CENTER)
  canvas=Canvas(root, width=250, height=133)

  backBtn()

#REPORT SECTION
def report(): 
  delete()

  title4 = Label(root, text="\n Report an Incident", font = ("Times",20),fg="DarkGreen", bg="PaleGreen")
  title4.pack()

  report_text = Label(root, text="\n Here you can report any instances of bullying that you have experienced, witnessed, or \n been involved in. Type 'skip' for any questions you do not wish to answer.", font = ("Times",9), bg="PaleGreen", fg="Black", width="70")
  report_text.pack()

  def destroy_except(a,b,c):
    for child in root.winfo_children():
      if child != a and child != b and child != c:
        child.destroy()

  def next_btn(x):
    next = Button(root, text="Next", font=("Times", 8), command = x, width=6, bg="DodgerBlue", fg="White")
    next.place(relx=0.896, rely=0.43, anchor=CENTER)

  def rep_back(y):
    back = Button(root, text="<<",command = y, width=6, bg="DodgerBlue", fg="White" )
    back.place(relx=0.5, rely=0.43, anchor=CENTER)

  list = Text(root, width=50, height=12, bg="PaleGreen", fg="Black", font=("Times",8) )
  list.place(relx=0.69, rely=0.72, anchor=CENTER)

  valid = ""

  def question_6():
    destroy_except(list, report_text, title4)
    backBtn()
    question6 = Label(root, text="Briefly describe the incident:", font=("Times",8),bg="PaleGreen", fg="Black")
    question6.place(relx=0.21, rely=0.52, anchor=CENTER)

    entry=Entry(root, width=22)
    entry.place(relx=0.23, rely=0.63, anchor=CENTER)
    entry.config(state="normal")

    def edit():
      list.config(state="normal")
      info = Label(root, text="Click on the the within the text box that you would like to edit", font=("Times",8))
      info.place(relx=0.5, rely=0.4, anchor=CENTER)

    def answer(t):
      string=entry.get()
      list.config(state="normal")
      list.insert(END, "Description: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q6 done":
        destroy_except(list, report_text, title4)
        backBtn()
        list.place(relx=0.3, rely=0.72, anchor=CENTER)
        edit_btn = Button(root, text="Edit", width=6, bg="DodgerBlue", fg="White", command=edit)
        edit_btn.place(relx=0.6, rely=0.5, anchor=CENTER)

    okay6 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q6 done":answer(t))
    okay6.place(relx=0.23, rely=0.8, anchor=CENTER)

  def question_5():
    destroy_except(list, report_text, title4)
    backBtn()
    question5 = Text(root, font=("Times",8),bg="PaleGreen", fg="Black", width=27, height=6.5)
    question5.insert(END, "What kind of bullying occured? \n\n 1)Verbal \n 2)Physical \n 3)Cyber bullying \n 4)Other:(specify)")
    question5.place(relx=0.23, rely=0.63, anchor=CENTER)
    question5.config(state="disable")

    entry=Entry(root, width="22")
    entry.place(relx=0.225, rely=0.82, anchor=CENTER)
    entry.config(state="normal")

    def answer(t):
      string=entry.get()
      list.config(state="normal")
      list.insert(END, "Nature: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q5 done":
        okay5.config(state="disable")
        next_btn(question_6)

    okay5 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q5 done":answer(t))
    okay5.place(relx=0.225, rely=0.9, anchor=CENTER)

  def question_4():
    destroy_except(list, report_text, title4)
    backBtn()
    question4 = Text(root, font=("Times",8),bg="PaleGreen", fg="Black", width=27, height=6.5)
    question4.insert(END, "Where did this incident occur? \n\n 1)School \n 2)Work \n 3)Other:(specify)")
    question4.place(relx=0.23, rely=0.63, anchor=CENTER)
    question4.config(state="disable")

    entry=Entry(root, width="22")
    entry.place(relx=0.225, rely=0.82, anchor=CENTER)
    entry.config(state="normal")

    def answer(t):
      string=entry.get()
      list.config(state="normal")
      list.insert(END, "Location: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q4 done":
        okay4.config(state="disable")
        next_btn(question_5)

    okay4 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q4 done":answer(t))
    okay4.place(relx=0.225, rely=0.9, anchor=CENTER)

  def question_3():
    #question 3
    destroy_except(list, report_text, title4)
    backBtn()
    question3 = Text(root, font=("Times",8),bg="PaleGreen", fg="Black", width=27, height=6.5)
    question3.insert(END, "Relationship to incident \n\n 1)I experienced bullying \n 2) I witnessed bullying \n 3) I was involved in bullying \n 4)Rather not say \n 5)Other:(specify)")
    question3.place(relx=0.23, rely=0.63, anchor=CENTER)
    question3.config(state="disable")

    entry=Entry(root, width="22")
    entry.place(relx=0.225, rely=0.82, anchor=CENTER)
    entry.config(state="normal")

    #question 3
    def answer(t):
      string=entry.get()
      list.config(state="normal")
      list.insert(END, "Relationship: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q3 done":
        okay3.config(state="disable")
        next_btn(question_4)

    okay3 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q3 done":answer(t))
    okay3.place(relx=0.225, rely=0.9, anchor=CENTER)

  def question_2():
    #question 2
    destroy_except(list, report_text, title4)
    backBtn()
    question2 = Label(root, text="What is your age?", font=("Times",8),bg="PaleGreen", fg="Black")
    question2.place(relx=0.17, rely=0.52, anchor=CENTER)

    entry=Entry(root, width="22")
    entry.place(relx=0.23, rely=0.63, anchor=CENTER)
    entry.config(state="normal")

    def answer(t):
      string=entry.get()
      list.config(state="normal")
      list.insert(END, "Age: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q2 done":
        okay2.config(state="disable")
        next_btn(question_3)

    okay2 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q2 done":answer(t))
    okay2.place(relx=0.23, rely=0.8, anchor=CENTER)

  #question 1
  def question_1():
    question1 = Label(root, text="What is your name?", font=("Times",8),bg="PaleGreen", fg="Black")
    question1.place(relx=0.18, rely=0.52, anchor=CENTER)

    entry=Entry(root, width="22")
    entry.place(relx=0.23, rely=0.63, anchor=CENTER)
    entry.config(state="normal")

    def answer(t):
      string=entry.get()
      list.insert(END, "Name: " + string + "\n")
      list.place(relx=0.69, rely=0.72, anchor=CENTER)
      list.config(state="disable")
      entry.config(state="disable")
      print(t)
      valid = t
      if valid == "q1 done":
        okay1.config(state="disable")
        next_btn(question_2)

    okay1 = Button(root, text="Okay", font=("Times",8), width=22, command=lambda t="q1 done":answer(t))
    okay1.place(relx=0.23, rely=0.8, anchor=CENTER)

  question_1()

  backBtn()

#CHAT SECTION
def chat(): 
  delete()

  title5 = Label(root, text="\n Chat", font = ("Times",20),fg="DarkGreen", bg="PaleGreen")
  title5.pack()

  question()

  backBtn()

#COMMENT SECTION
def comments(): 
  delete()

  title6 = Label (root, text = "\n Comments", font = ("Times",20), bg="PaleGreen",fg="DarkGreen")
  title6.pack()

  #saving user input
  def save():
    previous = userComment.get()

    file = open('userInput.txt','w')
    file.write(previous)
    file.close()

    #output user input
    enterLable = Label(root,text=userComment.get(),bg="PaleGreen")
    enterLable.pack()

  #outputing previous comment
  file = open('userInput.txt','r') #reading and writing text in file
  previousComment =list(file)
  file.close()

  previousInput =Label(root,text="Previous:",bg="PaleGreen",font=("Times",10)) 
  previousInput.place(y=170)

  previousText = Label(root,text=previousComment,bg="PaleGreen",font= ("Times",10))
  previousText.place(x=70,y=170)

  text1 = Label(text = "\n Do you have any feedbacks?",bg="PaleGreen",font = ("Times",10))
  text1.pack()

  holdString = StringVar()
  userComment = Entry(textvariable = holdString,width=50)
  userComment.pack()

  enterBtn = Button(root,text="ENTER",command=save,bg="LightSeaGreen",font=("Times",9))
  enterBtn.pack()

  backBtn()

#CHAT SECTION QUESTIONS/OUTPUT
def endpage(): #Window w/ reflection
  delete()
  reflection = Label(text="\n How can you improve?", bg="PaleGreen",font = ("Times",12))
  reflection.pack()

  spacing = Label(bg = "PaleGreen")
  spacing.pack()

  #return
  returnBtn = Button(root,text="RETURN TO MAIN MENU",command=main, bg ="LightSeaGreen",font = ("Times",9))
  returnBtn.pack(anchor='n')

  #scroll bar for user input
  Yscroll=Scrollbar(root)
  Yscroll.pack(side=RIGHT,fill=Y)

  textarea=Text(root,yscrollcommand=Yscroll.set)
  Yscroll.config(command=textarea.yview)
  textarea.pack(expand=1,fill=BOTH)

#Questions (1-5)

def yesButton(page):
  yesBtn = Button(root,text="YES", command=page, bg="MediumAquamarine",font = ("Times",9)) #If user clicks yes
  yesBtn.pack(padx=20,pady=20)

def noButton(page):
  noBtn = Button(root,text="NO",command=page,bg = "IndianRed",font = ("Times",9)) #If user clicks no
  noBtn.pack(padx=40,pady=15)

def Q5():
  delete()
  Q5 = Label(text= "\n Do you feel unsafe over the internet?", bg="PaleGreen",font = ("Times",12))
  Q5.pack()

  yesButton(endpage)
  noButton(endpage)
  backBtn()

def Q4():
  delete()
  Q4 = Label(text= "\n Do you have a bad sleeping schedule?", bg="PaleGreen",font = ("Times",12))
  Q4.pack()

  yesButton(Q5)
  noButton(Q5)
  backBtn()

def Q3():
  delete()
  Q3 = Label(text= "\n Are you eating proper meals?", bg="PaleGreen",font = ("Times",12))
  Q3.pack()

  yesButton(Q4)
  noButton(Q4)
  backBtn()

def Q2():
  delete()
  Q2 = Label(text= "\n Are you overwhelmed or stressed?", bg="PaleGreen",font = ("Times",12))
  Q2.pack()

  yesButton(Q3)
  noButton(Q3)
  backBtn()

def Q1():
  delete()
  Q1 = Label(text="\n Are you having a bad day?",bg="PaleGreen",font = ("Times",12))
  Q1.pack()

  yesButton(Q2)
  noButton(Q2)
  backBtn()

def question():
  intro = Label(text="\n We will be asking you 5 questions on your mental health.", bg="PaleGreen",font = ("Times",12))
  intro.pack()

  spacing = Label(bg = "PaleGreen")
  spacing.pack()

  continueBtn = Button(root,text="CONTINUE", command=Q1, bg = "LightSeaGreen",font = ("Times",9))
  continueBtn.pack()

#MAIN MENU
def main():
  delete()

  #Exit Button
  exitBtn = Button(root,text="EXIT APP",bg="IndianRed", command=exitApp,font = ("Times",9))
  exitBtn.pack(anchor="nw")

  #Main Tab Text
  main_text = Label(root,text = "\n Welcome to SafeSpace!", font = ("Times", 20), fg="DarkGreen", bg="PaleGreen") 
  main_text.place(relx=0.5, rely=0.1, anchor=CENTER)

  #Button for first tab
  about_button = Button(root, text = "ABOUT", command = about, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9)) 
  about_button.place(relx=0.2, rely=0.5, anchor=CENTER)

  #Button for second tab
  resources_button = Button(root, text = "RESOURCES", command = resources, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9)) 
  resources_button.place(relx=0.5,rely=0.5,anchor=CENTER)

  #Button for third tab
  signs_button = Button(root, text = "SIGNS & INFO", command = signs, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9))
  signs_button.place(relx=0.8, rely=0.5, anchor=CENTER)

  #Button for the fourth tab
  report_button = Button(root, text = "REPORT", command = report, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9))
  report_button.place(relx=0.2, rely=0.7, anchor=CENTER)

  #Button for the fifth tab
  chat_button = Button(root, text = "CHAT", command = chat, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9))
  chat_button.place(relx=0.5, rely=0.7, anchor=CENTER)

  #Button for the sixth tab
  comments_button = Button(root, text = "COMMENTS", command = comments, bg="DarkGreen", fg="White", width="10", height="2",font = ("Times",9))
  comments_button.place(relx=0.8, rely=0.7, anchor=CENTER)

  #LOGO
  global img
  canvas=Canvas(root, width=150, height=100)
  canvas.pack()

  img = ImageTk.PhotoImage(Image.open("SafeSpaceLogo.png"))

  canvas.create_image(0.1,0.1,anchor=NW, image=img)
  canvas.place(relx=0.9, rely=0.1, anchor=CENTER)

main()


root.mainloop()

