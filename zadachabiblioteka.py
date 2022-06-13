odgovor=input("Nov chlen: novchlen ; \n Nova kniga: novakniga ; \n Zemanje kniga: zemanjekniga ; \n Vrakjanje kniga: vrakjanjekniga ; :")
if odgovor=="novchlen":
    from funkciibiblioteka import novichlenovi
    novichlenovi()
if odgovor=="novakniga":
    from funkciibiblioteka import vnesknigi
    vnesknigi()
if odgovor=="zemanjekniga":
    from funkciibiblioteka import zemanjekniga
    zemanjekniga()
if odgovor=="vrakjanjekniga":
    from funkciibiblioteka import vrakjanjekniga
    vrakjanjekniga()
