odgovor=input("Dali kje vnesuvate produkti ili kje prodavate? Odgovori: vnesuvam ili prodavam; \n")
if odgovor.lower()=="vnesuvam":
    print("Pochnete so vnesuvanje na produkti vo magacin")
    from funkciimarket import vnesmagacin
    vnesmagacin()
if odgovor.lower()=="prodavam":
    print("Pochnete da prodavate produkti od magacin")
    from funkciimarket import prodazhba 
    prodazhba()
    

    
    
    

