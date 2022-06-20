#student name: Peter Na
#student number: 36734671

#covid simple dashboard app

#imports
from doctest import master
import tkinter
from covid import Covid

from tkinter import *

import matplotlib
from matplotlib.pyplot import text
from numpy import rec
from pyparsing import col
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class getData:

    def getMasterCovidData(self) -> list:
        """ this function is called once to get the master data for 
            this application; 
            all data used in this application is derived from data 
            returned by this function
        """
        covid = Covid(source ="worldometers")
        data = covid.get_data()
        return data

    def getConfirmed(self, data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
        list of (country, confirmed) data
        """
        confirmed = []
        for i in data1:
            confirmed.append((i["country"], i["confirmed"]))
        return confirmed

    def getActive(self, data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
        list of (country, active) data
        """
        active = []
        for i in data1:
            active.append((i["country"], i["active"]))
        return active

    def getDeaths(self, data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
        list of (country, deaths) data
        """
        deaths = []
        for i in data1:
            deaths.append((i["country"], i["deaths"]))  
        return deaths 

    def getRecovered(self, data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
        list of (country, recovered) data
        """
        recovered = []
        for i in data1:
            recovered.append((i["country"], i["recovered"]))
        return recovered

class plotData: 
    def topTenCountries(self, metric: list) -> list:
        """ a helper function that takes a covid metric data list 
            (confirmed, active, deaths, recovered) and 
            returns a list with the top 10 countries for
            that metric
        """
        #construct another copy of the list
        metric_copy = []
        for i in range(len(metric)):
            metric_copy.append(metric[i])

        top10 = []
        while len(top10) < 10:
            largest = metric_copy[8][1]
            largest_index = 8
            for i in range(8, len(metric_copy)):
                if metric_copy[i][1] >= largest:
                    largest = metric_copy[i][1]
                    largest_index = i
            top10.append(metric_copy[largest_index])
            metric_copy.pop(largest_index) #remove the element from the copied list after each iteration
        return top10
        
    def plotConfirmed(self, confirmed: list):
        """ a callback function for the button;
            plots a histogram of the countries with top 10 confirmed cases 
        """
        global plotted, canvas
        if plotted:
            return
        fig = Figure(figsize = (8, 5))
        plot1= fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master = frame4) 

        top10 = [confirmed[i] for i in range(8, 18)]
        x = [top10[i][0] for i in range(10)]
        y = [top10[i][1] for i in range(10)]
        plot1.bar(x, y)

        for tick in plot1.get_xticklabels(): #rotate the text slightly
            tick.set_rotation(15) 
        canvas.draw()
        canvas.get_tk_widget().pack(fill=NONE, expand=False)
        plotted = True

    def plotActive(self, active: list):
        """ a callback function for the button;
            plots a histogram of the countries with top 10 active cases 
        """
        global plotted, canvas
        if plotted:
            return
        fig = Figure(figsize = (8, 5))
        plot1= fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master = frame4) 

        top10 = self.topTenCountries(active)
        x = [top10[i][0] for i in range(10)]
        y = [top10[i][1] for i in range(10)]
        plot1.bar(x, y)

        for tick in plot1.get_xticklabels(): #rotate the text slightly
            tick.set_rotation(15) 
        canvas.draw()
        canvas.get_tk_widget().pack(fill=NONE, expand=False)
        plotted = True


    def plotDeaths(self, deaths: list):
        """ a callback function for the button;
            plots a histogram of the countries with top 10 deaths
        """
        global plotted, canvas
        if plotted:
            return
        fig = Figure(figsize = (8, 5))
        plot1= fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master = frame4) 

        top10 = self.topTenCountries(deaths)
        x = [top10[i][0] for i in range(10)]
        y = [top10[i][1] for i in range(10)]
        plot1.bar(x, y)

        for tick in plot1.get_xticklabels(): #rotate the text slightly
            tick.set_rotation(15) 
        canvas.draw()
        canvas.get_tk_widget().pack(fill=NONE, expand=False)
        plotted = True

    def plotRecovered(self, recovered: list):
        """ a callback function for the button;
            plots a histogram of the countries with top 10 recovered cases 
        """
        global plotted, canvas
        if plotted:
            return
        fig = Figure(figsize = (8, 5))
        plot1= fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master = frame4) 

        top10 = self.topTenCountries(recovered)
        #print("DEBUG: top10", top10)
        x = [top10[i][0] for i in range(10)]
        y = [top10[i][1] for i in range(10)]
        plot1.bar(x, y)

        for tick in plot1.get_xticklabels(): #rotate the text slightly
            tick.set_rotation(15) 
        canvas.draw()
        canvas.get_tk_widget().pack(fill=NONE, expand=False)
        plotted = True


    def plotCountryData(self, data1: list, country):
        """ a callback function for the button;
            plots a histogram of the top 10 confirmed cases 
        """
        global plotted, canvas
        if plotted:
            return
        fig = Figure(figsize = (9, 6))
        plot1= fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master = frame4) 

        countryData = []
        for i in data1:
            if i["country"] == country:
                countryData.append((i["confirmed"], i["active"], i["deaths"], i["recovered"]))
        
        x = ['confirmed', 'active', 'deaths', 'recovered']
        y = [countryData[0][i] for i in range(4)]
        plot1.bar(x, y)

        for tick in plot1.get_xticklabels(): #rotate the text slightly
            tick.set_rotation(15) 
        canvas.draw()
        canvas.get_tk_widget().pack(fill=NONE, expand=False)
        plotted = True

    def clear(self):
        """ a callback for the Clear button """ 
        global plotted, canvas
        if plotted:
            canvas.get_tk_widget().destroy()
            plotted = False


#instantiate getData and plotData object
data = getData()
plot = plotData()

#get masterData
masterData = data.getMasterCovidData()

#get metric data
confirmed = data.getConfirmed(masterData)
active = data.getActive(masterData)
deaths = data.getDeaths(masterData)
recovered = data.getRecovered(masterData)

# program starts here
#instantiate the main window
window = Tk()
window.geometry("1800x800")
window.title("Covid Data Visualization")
window.resizable(False, False)
plotted = False

#instantiate separate frames for user selection and plot generation
frame1 = Frame(window, bg="#00316E", height=800, width=300)
frame1.grid(row=0, column=0)
frame1.grid_propagate(0)

frame2 = Frame(window, bg="#001C57", height=800, width=300)
frame2.grid(row=0, column=1)
frame2.grid_propagate(0)

frame3 = Frame(window, bg="#001540", height=800, width=300)
frame3.grid(row=0, column=2)
frame3.grid_propagate(0)

frame4 = Frame(window, bg="#00224B", height=800, width=900)
frame4.grid(row=0, column=3)
frame4.grid_propagate(0)

#label the options avaliable for choosing
option1 = Label(frame1, 
        text = ' Option 1', 
        font = ('georgia', 40), 
        bg="#00316E", 
        fg="darkorange2", 
        padx=40, 
        pady=30,)

option2 = Label(frame2, 
        text = 'Option 2', 
        font = ('georgia', 40), 
        bg="#001C57",
        fg="darkorange2", 
        padx=40, 
        pady=30)

option3 = Label(frame3, 
        text = 'Option 3', 
        font = ('georgia', 40), 
        bg="#001540", 
        fg="darkorange2", 
        padx=40, 
        pady=30)

option1.grid(row=0, column=0, columnspan=2)
option2.grid(row=0, column=0, columnspan=2)
option3.grid(row=0, column=0, columnspan=2)

#label the each option with descriptions
text1 = Label(frame1, 
        text="This option plots a histogram\nof the top 10 number of\nconfirmed cases by country.\n\n", 
        font=('georgia', 15), 
        bg="#00316E", 
        fg="darkorange2")
text1.grid(row=1, column=0, columnspan=2)
space1 = Label(frame1, text="\n", bg="#00316E")
space1.grid(row=2, column=0, columnspan=2)

text2 = Label(frame2, 
        text="allows user to select among\nconfirmed, active, deaths and\nrecovered, then the app displays\nthe plot of the top 10 country\ncases for that metric.", 
        font=('georgia', 15), 
        bg="#001C57",
        fg="darkorange2")
text2.grid(row=1, column=0, columnspan=2)
space2 = Label(frame2, text="\n", bg="#001C57")
space2.grid(row=2, column=0, columnspan=2)

text3 = Label(frame3, 
        text="allows user to select a\nspecific country from a list,\nthen the app displays the\nnumbers of confirmed, active,\ndeaths and recovered cases.", 
        font=('georgia', 15), 
        bg="#001540",
        fg="darkorange2")
text3.grid(row=1, column=0, columnspan=2)
space3 = Label(frame3, text="\n", bg="#001540",)
space3.grid(row=2, column=0, columnspan=2)

#instantiate buttons for user input (by click)
#Option 1
option1_button = Button(master = frame1,
                command = lambda: plot.plotConfirmed(confirmed),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#00316E", 
                fg="darkorange2",        
                text = "Plot: top 10 confirmed").grid(row=3, column=0, sticky="W")

#Option2
option2_button1 = Button(master = frame2,
                command = lambda: plot.plotConfirmed(confirmed),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001C57",
                fg="darkorange2",  
                text = "Confirmed").grid(row=3, column=0)

option2_button2 = Button(master = frame2,
                command = lambda: plot.plotActive(active),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001C57",
                fg="darkorange2", 
                text = "Active").grid(row=3, column = 1)

option2_button3 = Button(master = frame2,
                command = lambda: plot.plotDeaths(deaths),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001C57",
                fg="darkorange2",                
                text = "Deaths").grid(row=4, column = 0)

option2_button4 = Button(master = frame2,
                command = lambda: plot.plotRecovered(recovered),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001C57",
                fg="darkorange2", 
                text = "Recovered").grid(row=4, column = 1)

#Option3
option3_button1 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'USA'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "USA").grid(row=3, column=0)

option3_button2 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'Canada'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Canada").grid(row=3, column=1)

option3_button3 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'China'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "China").grid(row=4, column=0)

option3_button4 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'Japan'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Japan").grid(row=4, column=1)

option3_button5 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'India'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "India").grid(row=5, column=0)

option3_button6 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'Poland'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Poland").grid(row=5, column=1)

option3_button7 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'UK'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "UK").grid(row=6, column=0)

option3_button8 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'Russia'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Russia").grid(row=6, column=1)

option3_button9 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'France'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "France").grid(row=7, column=0)

option3_button10 = Button(master = frame3,
                command = lambda: plot.plotCountryData(masterData, 'Italy'),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Italy").grid(row=7, column=1)

clear_button = Button(master = frame4,
                command = lambda: plot.clear(),
                height = 4,
                width = 20,
                font=('georgia', 8), 
                bg="#001540",
                fg="darkorange2",
                text = "Clear").pack(fill=NONE, expand=False, side=BOTTOM)

window.mainloop()


