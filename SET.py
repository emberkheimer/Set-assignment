from tkinter import *
import Deck


#GUI
root = Tk()
selectionList=[]
class Deck:
    
    def __init__(self):
        self.cardList = []
        self.colorList = ['red','blue','green']
        self.fillList = ['solid', 'shaded', 'clear']
        self.shapeList = ['circle', 'triangle','square']
        self.numList = ['1','2','3']

        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        #c=Card(color,shape, fill, number)
                        ##self.cardList.append(Card(color, fill, shape, number))
                        #self.cardList.append(c)
                        #enumerate object list?
                        self.cardList.append((color, fill, shape, number))
        #print(self.cardList)
                        
    def getNumberOfCards(self):
        return len(self.cardList)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        return self.cardList

#start button shuffles and picks first 9 indece of shuffledDeck


def startGame():
    
    selectionList=[]
    setCount=0
    #setsFound= Label(root, text=("setsFound:" + str(setCount))
    #setsFound.pack()
    buttonList=[]
    d= Deck()
    shuffledDeck=d.shuffle()
    for i in range (0,12):
        buttonList.append(shuffledDeck[i])
        shuffledDeck.pop(i)
    button1=Button(root, text=str(buttonList[0]), command=selectCard1)
    button2=Button(root, text=str(buttonList[1]), command=selectCard2)
    button3=Button(root, text=str(buttonList[2]), command=selectCard3)
    button4=Button(root, text=str(buttonList[3]), command=selectCard4)
    button5=Button(root, text=str(buttonList[4]), command=selectCard5)
    button6=Button(root, text=str(buttonList[5]), command=selectCard6)
    button7=Button(root, text=str(buttonList[6]), command=selectCard7)
    button8=Button(root, text=str(buttonList[7]), command=selectCard8)
    button9=Button(root, text=str(buttonList[8]), command=selectCard9)
    button10=Button(root, text=str(buttonList[9]), command=selectCard10)
    button11=Button(root, text=str(buttonList[10]), command=selectCard11)
    button12=Button(root, text=str(buttonList[11]), command=selectCard12)

    button1.grid(row=1, column=1)
    button2.grid(row=1, column=2)
    button3.grid(row=1, column=3)
    button4.grid(row=1, column=4)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button7.grid(row=2, column=3)
    button8.grid(row=2, column=4)
    button9.grid(row=2, column=5)
    button10.grid(row=1, column=5)
    button11.grid(row=2, column=6)
    button12.grid(row=1, column=6)


#card click command
def selectCard1():
    selectionList.append(buttonList[0])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass

def selectCard2():
    selectionList.append(buttonList[1])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass

def selectCard3():
    selectionList.append(buttonList[2])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass       
def selectCard4():
    selectionList.append(buttonList[3])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass 
def checkSet():
    if (selectionList[0][0]==selectionList[1][0] and selectionList[0][0]==selectionList[2][0]) or (selectionList[0][0]!=selectionList[1][0] and selectionList[0][0]!=selectionList[2][0] and selectionList[1][0]!=selectionList[2][0]):
        if (selectionList[0][1]==selectionList[1][1] and selectionList[0][1]==selectionList[2][1]) or (selectionList[0][1]!=selectionList[1][1] and selectionList[0][1]!=selectionList[2][1] and selectionList[1][1]!=selectionList[2][1]):
            if (selectionList[0][2]==selectionList[1][2] and selectionList[0][2]==selectionList[2][2]) or (selectionList[0][2]!=selectionList[1][2] and selectionList[0][2]!=selectionList[2][2] and selectionList[1][2]!=selectionList[2][2]):
                if (selectionList[0][3]==selectionList[1][3] and selectionList[0][3]==selectionList[2][3]) or (selectionList[0][3]!=selectionList[1][3] and selectionList[0][3]!=selectionList[2][3] and selectionList[1][3]!=selectionList[2][3]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def selectCard5():
    selectionList.append(buttonList[4])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass

def selectCard6():
    selectionList.append(buttonList[5])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard7():
    selectionList.append(buttonList[6])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard8():
    selectionList.append(buttonList[7])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard9():
    selectionList.append(buttonList[8])
    
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard10():
    selectionList.append(buttonList[10])
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard11():
    selectionList.append(buttonList[11])
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass
def selectCard12():
    selectionList.append(buttonList[12])
    if len(selectionList)==3:
        if checkSet==True:
            setCount=setCount+1
            #remove button and replace using replace funtion
            selectionList=[]
            
        else:
            incorrect= Label(root, text='not a set')
            incorrect.grid(row=4, column=2)
    else:
        pass

myLabel = Label(root, text= "SET")
myLabel.grid(row=0, column=2)

#play/restart button
playButton = Button(root, text='Start', command=startGame)
playButton.grid(row=0, column=4)

setCount=0
setsFound= Label(root, text=("Sets found:"+ str(setCount)))
setsFound.grid(row=6, column=3)   
        
root.mainLoop()  
