import random
def selectRandom(nazioni):
    return random.choice(nazioni)
nazioni = ["Albania","Italia","Belgio","Bulgaria","Canada","Croazia","Danimarca","Estonia","Francia","Germania","Grecia","Islanda","Lettonia","Lituania","Lussemburgo","Macedonia del nord","Montenegro","Norvegia","Paesi Bassi","Polonia","Portogallo","Regno Unito","Repubblica Ceca","Romania","Slovacchia","Slovenia","Spagna","Stati Uniti","Turchia","Ungheria","Brasile","Russia","India","Cina","Sud Africa","Svezia","Finlandia","Bosnia ed Erzegovina","Australia","Svizzera","Bielorussia"]
punteggio = 0
count = 0
while (count < 10):
    n = random.choice(nazioni)
    nazioni = [i for i in nazioni if i not in n]
    capitale = input("Dimmi la capitale della " + n + " :")
    if(n == "Albania"):
        if(capitale == "Tirana"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Tirana")
    if(n == "Italia"):
        if(capitale == "Roma"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato  era Roma") 
    if(n == "Belgio"):
        if(capitale == "Bruxelles"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Bruxelles")
    if(n == "Bulgaria"):
        if(capitale == "Sofia"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Sofia")
    if(n == "Canada"):
        if(capitale == "Ottawa"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Ottawa")
    if(n == "Croazia"):
        if(capitale == "Zagabria"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Zagabria")
    if(n == "Danimarca"):
        if(capitale == "Copenaghen"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era  Copenaghen")
    if(n == "Estonia"):
        if(capitale == "Tallinn"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Tallinn")
    if(n == "Francia"):
        if(capitale == "Parigi"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Parigi")
    if(n == "Germania"):
        if(capitale == "Berlino"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Berlino")
    if(n == "Grecia"):
        if(capitale == "Atene"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Atene")
    if(n == "Islanda"):
        if(capitale == "Reykjavík"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Reykjavík")
    if(n == "Lettonia"):
        if(capitale == "Riga"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Riga")
    if(n == "Lituania"):
        if(capitale == "Vilnius"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Vilnius")
    if(n == "Lussemburgo"):
        if(capitale == "Lussemburgo"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Lussemburgo")
    if(n == "Macedonia del nord"):
        if(capitale == "Skopje"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Skopje ")
    if(n == "Montenegro"):
        if(capitale == "Podgorica"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Podgorica")
    if(n == "Norvegia"):
        if(capitale == "Oslo"):
            print("Giusto")
            punteggio = punteggio + 1 
        else:
            print("Sbagliato era Oslo")
    if(n == "Paesi Bassi"):
        if(capitale == "Amsterdam"):
            print("Giusto")
            punteggio = punteggio + 1 
        else:
            print("Sbagliato era Amsterdam")
    if(n == "Polonia"):
        if(capitale == "Varsavia"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Varsavia")
    if(n == "Portogallo"):
        if(capitale == "Lisbona"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Lisbona")
    if(n == "Regno Unito"):
        if(capitale == "Londra"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Londra")
            punteggio = punteggio + 1
    if(n == "Repubblica Ceca"):
        if(capitale == "Praga"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Praga")
    if(n == "Romania"):
        if(capitale == "Bucarest"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Bucarest")
    if(n == "Slovacchia"):
        if(capitale == "Bratislava"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Bratislava")
    if(n == "Slovenia"):
        if(capitale == "Lubiana"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Lubiana")
    if(n == "Spagna"):
        if(capitale == "Madrid"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Madrid")
    if(n == "Stati Uniti"):
        if(capitale == "Washington"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Washington")
    if(n == "Turchia"):
        if(capitale == "Ankara"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Ankara")
    if(n == "Ungheria"):
        if(capitale == "Budapest"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Budapest")
    if(n == "Brasile"):
        if(capitale == "Brasilia"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Brasilia")
    if(n == "Russia"):
        if(capitale == "Mosca"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Mosca")
    if(n == "India"):
        if(capitale == "Nuova Delhi"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Nuova Delhi")
    if(n == "Cina"):
        if(capitale == "Pechino"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Pechino")
    if(n == "Sud Africa"):
        if(capitale == "Città del Capo"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Città del Capo")
    if(n == "Svezia"):
        if(capitale == "Stoccolma"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Stoccolma")
    if(n == "Finlandia"):
        if(capitale == "Helsinki"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Helsinki")
    if(n == "Bosnia ed Erzegovina"):
        if(capitale == "Sarajevo"):
            print("Giusto")
            punteggio = punteggio + 1 
        else:
            print("Sbagliato era Sarajevo")
    if(n == "Austria"):
        if(capitale == "Vienna"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Vienna")
    if(n == "Australia"):
        if(capitale == "Canberra"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Canberra")
    if(n == "Svizzera"):
        if(capitale == "Berna"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Berna")
    if(n == "Bielorussia"):
        if(capitale == "Minsk"):
            print("Giusto")
            punteggio = punteggio + 1
        else:
            print("Sbagliato era Minsk")
    count = count + 1
print("Il tuo punteggio è di " + str(punteggio) + " punti")

