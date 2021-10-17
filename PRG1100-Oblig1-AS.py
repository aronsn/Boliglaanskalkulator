# Importerer tkinter GUI pakken for at IDE'en kan bruke modulene som følger med
from tkinter import *

# Funksjon for å beregne inndata'ene
def beregn_lan():
    if int(husstand.get()) == 1:
        barnefradrag = 785000*int(antallbarn.get())
        
    elif int(husstand.get()) == 2:
        barnefradrag = 370000*int(antallbarn.get())

    makslaan2 = int(bruttoinntekt.get())*5-barnefradrag
    
    teoretiskKjopesum = int(egenkapital.get()) / 17.5 * 100
    maksbud_DA  = (makslaan2 + int(egenkapital.get()))/1.025
    laan_krav = teoretiskKjopesum - (teoretiskKjopesum / 100) * 15

    
    if makslaan2 >= laan_krav:
        makslaan.set(makslaan2)
        maksbud.set(teoretiskKjopesum)
    else:
        makslaan.set(makslaan2)
        maksbud.set(maksbud_DA)
        
# Variabel for hovedvindu   
window = Tk()

# Navn
window.title('Lånekalkulator')

# Bruttoinntekt - ledetekst
lbl_bruttoinntekt = Label(window, text = 'Bruttoinntekt:')
lbl_bruttoinntekt.grid(row = 0, column = 0, padx = 5, pady = 5, sticky=E)
# Bruttoinntekt - tekstboks
bruttoinntekt = StringVar()
ent_bruttoinntekt = Entry(window, width = 8, textvariable = bruttoinntekt)
ent_bruttoinntekt.grid(row = 0, column = 1, padx = 5, pady = 5, sticky=W)

# Egenkapital - ledetekst
lbl_egenkapital = Label(window, text = 'Egenkapital:')
lbl_egenkapital.grid(row = 1, column = 0, padx = 5, pady = 5, sticky=E)
# Egenkapital - tekstboks
egenkapital = StringVar()
ent_egenkapital = Entry(window, width = 7, textvariable = egenkapital)
ent_egenkapital.grid(row = 1, column = 1, padx = 5, pady = 5, sticky=W)

# Husstand - ledetekst
lbl_husstand = Label(window, text = 'Antall inntektskilder:')
lbl_husstand.grid(row = 2, column = 0, padx = 5, pady = 5, sticky=E)
# Husstand - radiobutton
husstand = IntVar()
rbtn_husstand = Radiobutton(window, text='1', value=1, variable = husstand)
rbtn_husstand.grid(row = 2, column = 1, pady = 5, sticky=W)
rbtn_husstand2 = Radiobutton(window, text='2', value=2, variable = husstand)
rbtn_husstand2.grid(row = 2, column = 1, pady = 5)

# Antall barn - ledetekst
lbl_antallbarn = Label(window, text = 'Antall barn:')
lbl_antallbarn.grid(row = 3, column = 0, padx = 5, pady = 5, sticky=E)
# Antall barn - Spinbox
antallbarn = StringVar()
spn_antallbarn = Spinbox(window, width = 2, from_=0, to=3, state='readonly', text = antallbarn)
spn_antallbarn.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

# Maksimal lån - ledetekst
lbl_makslaan = Label(window, text = 'Maksimal lånebeløp:')
lbl_makslaan.grid(row = 5, column = 0, padx = 5, pady = 15, sticky = SW)
# Maksimal lån - tekstboks - readonly
makslaan = StringVar()
ent_makslaan = Entry(window, width = 20, state = 'readonly', textvariable = makslaan)
ent_makslaan.grid(row = 5, column = 1, padx = 5, pady = 15, sticky=SW)

# Maksimal bud/kjøpesum - ledetekst
lbl_maksbud = Label(window, text = 'Maksimal kjøpesum:')
lbl_maksbud.grid(row = 6, column = 0, padx = 5, pady = 0, sticky = NW)
# Maksimal bud/kjøpesum - tekstboks - readonly
maksbud = StringVar()
ent_maksbud = Entry(window, width = 20, state = 'readonly', textvariable = maksbud)
ent_maksbud.grid(row = 6, column = 1, padx = 5, pady = 0, sticky = NW)

#lånetilsagn - Beregn
btn_beregn = Button(window, text = 'Beregn lånetilsagn', command = beregn_lan)
btn_beregn.grid(row = 4, column = 0 , columnspan = 2, pady = 5)

# Avslutte
btn_avslutt = Button(window, text = 'Avslutt', command = window.destroy)
btn_avslutt.grid(row = 7, column = 1, padx = 5, pady = 5, sticky=E)

# løkke for at programmet skal håndtere ulike handlinger
window.mainloop()
