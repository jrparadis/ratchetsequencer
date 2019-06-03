from tkinter import *
import time
from rtmidi.midiutil import open_midioutput
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON,ALL_SOUND_OFF, CONTROL_CHANGE, RESET_ALL_CONTROLLERS
import logging
log = logging.getLogger('midiout')
logging.basicConfig(level=logging.DEBUG)
midiout, port_name = open_midioutput(1)

root=Tk()
variable=DoubleVar()
root.title("ratchetseq")
root.geometry('275x90')

def playnote(thenote, sus, amount):
    for each in range(int(amount)):
        root.after(sus, midiout.send_message([0x90, thenote, 127]), midiout.send_message([0x80, thenote, 127]))
    
def checkratchetleng(current):
    current = int(current)
    beat = bpmrate.get()
    sustain = (60/int(beat) / current) * 1000
    print(f'{round(sustain)}ms, {current} retriggers, {bpmrate.get()} bpm')
    return round(sustain)

def updatevars(step1, step2, step3, step4, step5, step6, step7, step8):
    step1text.set(step1)
    step2text.set(step2)
    step3text.set(step3)
    step4text.set(step4)
    step5text.set(step5)
    step6text.set(step6)
    step7text.set(step7)
    step8text.set(step8)
    root.update()
    
def checkandplay(thenote, amount):
    sus = checkratchetleng(amount)
    playnote(thenote, sus, amount)
    
def update():
    curstep = 1
    while 1:
        if curstep == 9:
            curstep = 1
        variable.set(curstep)
        if curstep == 1:
            updatevars(1, 0, 0, 0, 0, 0, 0, 0)
            checkandplay(int(step1entry.get()), int(step1entryratchettext.get()))
        elif curstep == 2:
            updatevars(0, 2, 0, 0, 0, 0, 0, 0)
            checkandplay(int(step2entry.get()), int(step2entryratchettext.get()))
        elif curstep == 3:
            updatevars(0, 0, 3, 0, 0, 0, 0, 0)
            checkandplay(int(step3entry.get()), int(step3entryratchettext.get()))
        elif curstep == 4:
            updatevars(0, 0, 0, 4, 0, 0, 0, 0)
            checkandplay(int(step4entry.get()), int(step4entryratchettext.get()))
        elif curstep == 5:
            updatevars(0, 0, 0, 0, 5, 0, 0, 0)
            checkandplay(int(step5entry.get()), int(step5entryratchettext.get()))
        elif curstep == 6:
            updatevars(0, 0, 0, 0, 0, 6, 0, 0)
            checkandplay(int(step6entry.get()), int(step6entryratchettext.get()))
        elif curstep == 7:
            updatevars(0, 0, 0, 0, 0, 0, 7, 0)
            checkandplay(int(step7entry.get()), int(step7entryratchettext.get()))
        elif curstep == 8:
            updatevars(0, 0, 0, 0, 0, 0, 0, 8)
            checkandplay(int(step8entry.get()), int(step8entryratchettext.get()))
        curstep += 1
        bpmconvert = 60 / int(bpmrate.get())
        if int(bpmrate.get()) <= 20:
            bpmtext.set(20)
        elif int(bpmrate.get()) >= 700:
            bpmtext.set(700)

your_label=Label(root,textvariable=variable)
your_label.grid(column=1,row=0)
start_button=Button(root,text="start",command=update)
start_button.grid(column=0,row=0)

bpmtext = DoubleVar()
bpmtext.set(120)
bpmrate = Entry(root,width=5, textvariable=bpmtext)
bpmrate.grid(column=3,row=0)

step1text= StringVar()
step1text.set('0')
step1label = Label(root, textvariable=step1text)
step1label.grid(column=0, row=1)
step1entrytext= StringVar()
step1entrytext.set('30')
step1entry = Entry(root,width=5,textvariable=step1entrytext)
step1entry.grid(column=0,row=2)
step1entryratchettext= StringVar()
step1entryratchet = Entry(root,width=5,textvariable=step1entryratchettext)
step1entryratchet.grid(column=0,row=3)
step1entryratchettext.set('1')

step2text= StringVar()
step2text.set('0')
step2label = Label(root, textvariable=step2text)
step2label.grid(column=1, row=1)
step2entrytext= StringVar()
step2entrytext.set('20')
step2entry = Entry(root,width=5, textvariable=step2entrytext)
step2entry.grid(column=1,row=2)
step2entryratchettext= StringVar()
step2entryratchet = Entry(root,width=5,textvariable=step2entryratchettext)
step2entryratchet.grid(column=1,row=3)
step2entryratchettext.set('2')

step3text= StringVar()
step3text.set('0')
step3label = Label(root, textvariable=step3text)
step3label.grid(column=2, row=1)
step3entrytext= StringVar()
step3entrytext.set('35')
step3entry = Entry(root,width=5, textvariable=step3entrytext)
step3entry.grid(column=2,row=2)
step3entryratchettext= StringVar()
step3entryratchet = Entry(root,width=5,textvariable=step3entryratchettext)
step3entryratchet.grid(column=2,row=3)
step3entryratchettext.set('3')

step4text= StringVar()
step4text.set('0')
step4label = Label(root, textvariable=step4text)
step4label.grid(column=3, row=1)
step4entrytext= StringVar()
step4entrytext.set('45')
step4entry = Entry(root,width=5, textvariable=step4entrytext)
step4entry.grid(column=3,row=2)
step4entryratchettext= StringVar()
step4entryratchet = Entry(root,width=5,textvariable=step4entryratchettext)
step4entryratchet.grid(column=3,row=3)
step4entryratchettext.set('4')

step5text= StringVar()
step5text.set('0')
step5label = Label(root, textvariable=step5text)
step5label.grid(column=4, row=1)
step5entrytext= StringVar()
step5entrytext.set('50')
step5entry = Entry(root,width=5, textvariable=step5entrytext)
step5entry.grid(column=4,row=2)
step5entryratchettext= StringVar()
step5entryratchet = Entry(root,width=5,textvariable=step5entryratchettext)
step5entryratchet.grid(column=4,row=3)
step5entryratchettext.set('3')

step6text= StringVar()
step6text.set('0')
step6label = Label(root, textvariable=step6text)
step6label.grid(column=5, row=1)
step6entrytext= StringVar()
step6entrytext.set('60')
step6entry = Entry(root,width=5, textvariable=step6entrytext)
step6entry.grid(column=5,row=2)
step6entryratchettext= StringVar()
step6entryratchet = Entry(root,width=5,textvariable=step6entryratchettext)
step6entryratchet.grid(column=5,row=3)
step6entryratchettext.set('1')

step7text= StringVar()
step7text.set('0')
step7entrytext= StringVar()
step7entrytext.set('80')
step7label = Label(root, textvariable=step7text)
step7label.grid(column=6, row=1)
step7entry = Entry(root,width=5, textvariable=step7entrytext)
step7entry.grid(column=6,row=2)
step7entryratchettext= StringVar()
step7entryratchet = Entry(root,width=5,textvariable=step7entryratchettext)
step7entryratchet.grid(column=6,row=3)
step7entryratchettext.set('2')


step8text= StringVar()
step8text.set('0')
step8entrytext= StringVar()
step8entrytext.set('90')
step8label = Label(root, textvariable=step8text)
step8label.grid(column=7, row=1)
step8entry = Entry(root,width=5, textvariable=step8entrytext)
step8entry.grid(column=7,row=2)
step8entryratchettext= StringVar()
step8entryratchet = Entry(root,width=5,textvariable=step8entryratchettext)
step8entryratchet.grid(column=7,row=3)
step8entryratchettext.set('2')

root.mainloop()
