import json


def prodazhba():
    prodazhba={}
    prodolzhi="da"
    kusur=0
    vkupnaCena=0
    with open('magacin.json') as f:
        vnesmagacin = json.load(f)
    while prodolzhi.lower()=="da":
        produkt=input("Vnesete go produktot shto se prodava: ")
        if produkt in vnesmagacin:
            prodazhba[produkt]={}

            kolichinaProdava=int(input("Vnesete ja kolichinata na produktot shto se prodava: "))
            if kolichinaProdava>vnesmagacin[produkt]['kolichina vo magacin']:
                print("Nema tolku produkti na zaliha")
            elif kolichinaProdava<=vnesmagacin[produkt]['kolichina vo magacin']:
                prodazhba[produkt]['kolichina shto se prodava']=kolichinaProdava

                vnesmagacin[produkt]["kolichina vo magacin"]=vnesmagacin[produkt]["kolichina vo magacin"]-prodazhba[produkt]['kolichina shto se prodava']
                poedinechnaCena=vnesmagacin[produkt]["poedinechna cena"]
                prodazhba[produkt]['poedinechna cena']=poedinechnaCena

                vnesmagacin[produkt]["vkupna cena"]=vnesmagacin[produkt]["poedinechna cena"]*vnesmagacin[produkt]["kolichina vo magacin"]

                vkupnaCena=vkupnaCena + (poedinechnaCena*kolichinaProdava)
                prodazhba[produkt]['vkupna cena']=poedinechnaCena*kolichinaProdava
        else:
            print("Go nema toj produkt vo magacin")

        prodolzhi=input("Dali sakate da prodolzhite? ")
        
        if prodolzhi.lower()=="ne":
            print("Vashite prodadeni produkti se: {}".format(prodazhba))

            plakjanje=int(input("So kolku pari kje plati klientot? "))
            if plakjanje<vkupnaCena:
                print("Klientot nema dovolno pari!")
            if plakjanje>=vkupnaCena:
                kusur=plakjanje-vkupnaCena
                print("Kusurot koj treba da go vratite na klientot e: {}".format(kusur))

            with open('magacin.json', 'w') as f:
                json.dump(vnesmagacin, f, indent=2)
        
        if prodolzhi.lower()=='kraj':
            print("Kraj na programata")
    return prodazhba    


def vnesmagacin():
    with open('magacin.json') as f:
        vnesmagacin = json.load(f) 
    prodolzhi="da"
    while prodolzhi.lower()=="da":
        produkti=input("Vnesete go produktot: ")
        if produkti.isdigit():
            print("Vo ova pole treba da vnesete bukvi")
            break
        vnesmagacin[produkti]={}

        try:
            kolichinaMagacin=int(input("Vnesete ja kolichinata na produktot: "))
            vnesmagacin[produkti]['kolichina vo magacin']=kolichinaMagacin
        except ValueError:
            print("Vo ova pole treba da vnesete brojki")
            
        poedinechnaCena=int(input("Vnesete ja cenata: "))
        vnesmagacin[produkti]['poedinechna cena']=poedinechnaCena

        vkupnaCena=poedinechnaCena*kolichinaMagacin
        vnesmagacin[produkti]['vkupna cena']=vkupnaCena
        
        prodolzhi=input("Dali sakate da prodolzhite? ")
        if prodolzhi.lower()!="da":
            with open('magacin.json', 'w') as f:
                json.dump(vnesmagacin, f, indent=2)
            print("Vashite vneseni podatoci se {}".format(vnesmagacin))
    return vnesmagacin



