'''''''''
    barrasCode39='code39'
    numeroInvitado=input("Coloque el numero ultimo invitado")
    numeroLargo=input("Coloque el largo del codigo de barras")
    nombreInvitado=input("Coloque el nombre del invitado")




    geneCall = codigoBarras()
    geneCall.runGenerador(numeroInvitado,numeroLargo,nombreInvitado,barrasCode39)
'''''