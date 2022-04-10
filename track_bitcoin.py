import requests
import tkinter as tk
from datetime import datetime

canvas = tk.Tk()
canvas.geometry('400x500')
canvas.title('BITCOIN TRACKER')

f1 = ('poppins', 24, 'bold')
f2 = ('poppins', 22, 'bold')
f3 = ('poppins', 18, 'bold')

label = tk.Label(canvas, text = 'Bitcoin Price', font= f1)
label.pack(pady=20)

labelprice = tk.Label(canvas, font= f2)
labelprice.pack(pady=20)

labeltime = tk.Label(canvas, font= f3)
labeltime.pack(pady=20)

def trackbitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    price = response['bpi']['USD']['rate']
    print('Price is :', price , 'US Dollars')
    time = datetime.now().strftime("%H:%M:%S")
   
    labelprice.config(text= str(price) + " $")
    labeltime.config(text= 'Updated at :' + time)
   
    # here trackbitcoin function will be run automatically every 1 second for getting current bitcoin price
    canvas.after(1000, trackbitcoin)

trackbitcoin()
canvas.mainloop()
