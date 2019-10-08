from tkinter import*
running = 0
counter = 1
val=[0,0,':',0,0,':',0,0]
def stopwatch(val):

        global counter
        counter+=1
        val[len(val)-1] = counter%10
        val[len(val)-2] = int(counter/10)
        if counter == 99:
                counter = 1
                val[len(val)-4]+=1

        if val[len(val)-4] == 10:
                val[len(val)-5]+=1
                val[len(val)-4]=0

        if val[len(val)-5] == 6:
                val[1]+=1
                val[len(val)-5]=0
        if val[1] == 10:
                val[0]+=1
                val[1]=0

        if val[0] ==6 :
                sys.exit(1)

def counter_watch(label):
        def count():
                global running
                if running:
                        global val
                        label.config(text = val,font="timesnewroman 12 italic bold")
                        stopwatch(val)
                        label.after(10, count)
                else:
                        label.config(text = val)
        count()

def start(label):
        global running
        running = 1
        counter_watch(label)

def reset(label):

        global running
        global val
        val=[0,0,':',0,0,':',0,0]
        counter_watch(label)

def stop(label):
        global running
        running = 0

if __name__ == "__main__":
        win=Tk()
        win.title("StopWatch")
        win.geometry("200x65")
        win.configure(background = "light green")
        l1 = Label(win, fg = "white", width = "50",height = "2", bg="black")
        l1.pack()
        b1 = Button(win, text = "start".title(), font = "bold", padx = 15, command = lambda :start(l1)).pack(side = "left")
        b2 = Button(win, text = "reset".title(), font = "bold", command = lambda :reset(l1)).pack(side = "left")
        b3 = Button(win, text = "stop". title(), font = "bold", padx = 15, command = lambda :stop(l1)).pack(side = "left")
        win.mainloop()
