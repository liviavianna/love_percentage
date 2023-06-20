from tkinter import *
import requests


bg_color = '#590d22'
root = Tk()
root.geometry('600x500')
root.eval('tk::PlaceWindow . center')
root.configure(background=bg_color)



def margin(height):
    mg = Canvas(root, width=600, bg=bg_color, height=height,
                bd=0, highlightthickness=0, relief='ridge')
    mg.pack()


def btn_click():
    fname = e_1.get()
    sname = e_2.get()

    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    
    querystring = {"sname": sname, "fname": fname}

    headers = {
        "X-RapidAPI-Key": '',
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    percentage = response.json()['percentage']
    result = response.json()['result']

    if result == 'Can choose someone better.':
        result = 'Pode escolher alguém melhor.'
    elif result == 'Congratulations! Good choice':
        result = 'Parabéns! Boa escolha'
    else:
        result = 'Não é uma boa escolha'

    percentage_txt = Label(root, bg=bg_color, text=percentage + '%',
                           fg='#FFFFFF', font=('Montserrat', 24, 'bold'))
    percentage_txt.pack()

    result_txt = Label(root, bg=bg_color, text=result,
                       fg='#FFFFFF', font=('Montserrat', 24, 'bold'))
    result_txt.pack()


margin(100)
title = Label(root, bg=bg_color, text='Calculadora do amor',
              fg='#FFFFFF', font=('Montserrat', 24, 'bold'))
title.pack()
margin(20)
e_1 = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#000000',
            bg='#FFFFFF', font=('Montserrat', 18, 'bold'), justify=CENTER)
e_1.pack()
margin(20)
e_2 = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#000000',
            bg='#FFFFFF', font=('Montserrat', 18, 'bold'), justify=CENTER)
e_2.pack()
margin(20)
love_btn = Button(root, text='Calcular amor', relief=FLAT, bg='#FFFFFF',
                  borderwidth=3, font=('Montserrat', 12, 'bold'), command=btn_click)
love_btn.pack()

# run app
root.mainloop()
