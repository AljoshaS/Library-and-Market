import json
import string
from turtle import clear
from unicodedata import digit

def novichlenovi():
    novichlenovi={}
    prodolzhi="da"
    with open('chlenovi.json') as f:
        novichlenovi = json.load(f) 

    while prodolzhi.lower()=="da":
            chlenovi=input("Vnesete ime i prezime na noviot chlen: ")
            if chlenovi.isdigit():
                print("Vnesuvajte bukvi vo ova pole")
                break
            novichlenovi[chlenovi]={}

            email=input("Vnesete email kontakt na chlenot: ")
            novichlenovi[chlenovi]["email kontakt"]=email

            telbroj=input("Vnesete tel. broj kontakt na chlenot: ")
            if telbroj.isalpha():
                print("Vnesete brojki vo ova pole")
                break
            novichlenovi[chlenovi]["tel. broj"]=telbroj

            chlenskabroj=input("Vnesete broj od chlenska knishka: ")
            if chlenskabroj.isalpha():
                print("Vnesete brojki vo ova pole")
                break
            novichlenovi[chlenovi]["broj od chlenska knishka: "]=chlenskabroj

            brojPozajmeniKnigi=int(input("Broj na pozajmeni knigi? Vnesete 0 bidejki e nov chlen "))
            if brojPozajmeniKnigi.isalpha():
                print("Vnesete brojki vo ova pole")
                break
            novichlenovi[chlenovi]["kolichina na pozajmeni knigi"]=brojPozajmeniKnigi

            prodolzhi=input("Dali sakate da prodolzhite da vnesuvate novi chlenovi? ")
            if prodolzhi!="da":

                with open('chlenovi.json', 'w') as f:
                    json.dump(novichlenovi, f, indent=2)

            print("Listata chlenovi na bibliotekata e: {}".format(novichlenovi))
    return novichlenovi


def vnesknigi():
    noviknigi={}
    prodolzhi="da"
    with open("knigi.json") as f:
        noviknigi = json.load(f)

    while prodolzhi.lower()=="da":
        knigi=input("Vnesete naslov na kniga: ")
        if knigi.isdigit():
                print("Vnesuvajte bukvi vo ova pole")
                break
        noviknigi[knigi]={}

        avtor=input("Vnesete avtor na knigata: ")
        if avtor.isdigit():
                print("Vnesuvajte bukvi vo ova pole")
                break
        noviknigi[knigi]["Avtor"]=avtor

        zhanr=input("Vnesete go zhanrot na knigata: ")
        if zhanr.isdigit():
                print("Vnesuvajte bukvi vo ova pole")
                break
        noviknigi[knigi]["Zhanr"]=zhanr
        try:
            kolichina=int(input("Vnesete kolichina na knigi: "))
        except ValueError:
            print("Vo ova pole treba da vnesete brojki")
            break
        noviknigi[knigi]["kolichina na knigi"]=kolichina
        prodolzhi=input("Dali sakate da prodolzhite? ")

        if prodolzhi.lower()!="da":

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashiot spisok na knigi e: {}".format(noviknigi))
    return vnesknigi


def zemanjekniga():
    zemanjekniga={}
    prodolzhi="da"

    with open('chlenovi.json') as f:
        novichlenovi = json.load(f)

    with open('knigi.json') as f:
        noviknigi =json.load(f)

    while prodolzhi.lower()=="da":
        try:
            chlen=input("Koj chlen pozajmuva kniga? ")
            zemanjekniga[chlen]={}

            if novichlenovi[chlen]['kolichina na pozajmeni knigi']>0:
                print("Chlenot {} ne mozhe da pozajmuva novi knigi bidejki ne ja vratil prethodno pozajmenata kniga.".format(chlen))

            if novichlenovi[chlen]['kolichina na pozajmeni knigi']==0:
                kniga=input("Koja kniga ja pozajmuva? ")
                zemanjekniga[chlen]["kniga pozajmena"]=kniga
                novichlenovi[chlen]['kniga koja ja ima pozajmeno']=kniga
        except KeyError:
            print("Vnesovte pogreshen podatok")
            break
            
        kolichinaZemeno=int(input("Kolku knigi pozajmuva? "))
        if noviknigi[kniga]["kolichina na knigi"]==0:
            print("Nema kniga na zaliha za ponatamoshno pozajmuvanje")
        elif kolichinaZemeno >1:
            print("Ne mozhe da se pozajmi povekje od edna kniga")
        elif kolichinaZemeno ==1:
            zemanjekniga[chlen]['kolichina na pozajmeni knigi']=kolichinaZemeno
            novichlenovi[chlen]["kolichina na pozajmeni knigi"]=novichlenovi[chlen]["kolichina na pozajmeni knigi"]+kolichinaZemeno
            print(noviknigi[kniga])
            noviknigi[kniga]["kolichina na knigi"]=noviknigi[kniga]["kolichina na knigi"]-kolichinaZemeno

        prodolzhi=input("Dali sakate da prodolzhite? ")
        if prodolzhi.lower()!="da":

            with open('chlenovi.json', 'w') as f:
                json.dump(novichlenovi, f, indent=2)

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashiot spisok so pozajmeni knigi e: {}".format(zemanjekniga))
    return zemanjekniga


def vrakjanjekniga():
    vrakjanjekniga={}
    prodolzhi="da"

    with open('chlenovi.json') as f:
        novichlenovi = json.load(f)

    with open('knigi.json') as f:
        noviknigi =json.load(f)

    while prodolzhi.lower()=="da":
        try:
            kniga=input("Koja kniga se vrakja? ")
            vrakjanjekniga[kniga]={}

            chlen=input("Koj chlen ja vrakja? ")
            vrakjanjekniga[kniga]["Chlen"]=chlen

            kolichinaVrateni=int(input("Kolku knigi vrakja chlenot? "))
            if kolichinaVrateni>1:
                print("Klient mozhe da ima samo edna pozajmena kniga i mozhe da vrati samo edna!")
            else:
                if novichlenovi[chlen]["kolichina na pozajmeni knigi"]==0:
                    print("Klientot ja nema pozajmeno taa kniga")
                if novichlenovi[chlen]["kolichina na pozajmeni knigi"]==1:
                    novichlenovi[chlen]["kolichina na pozajmeni knigi"]=novichlenovi[chlen]["kolichina na pozajmeni knigi"]-kolichinaVrateni
                    noviknigi[kniga]["kolichina na knigi"]=noviknigi[kniga]["kolichina na knigi"]+kolichinaVrateni
        except KeyError:
            print("Vnesovte pogreshen podatok")
            break
        prodolzhi=input("Dali sakate da prodolzhite? ")
        if prodolzhi.lower()!="da":

            with open('chlenovi.json', 'w') as f:
                json.dump(novichlenovi, f, indent=2)

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashata vratena kniga i chlenot koj ja vratil: {}".format(vrakjanjekniga))
    return vrakjanjekniga



        
