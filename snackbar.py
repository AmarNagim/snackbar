# Amar Nagim
# Snackbar

def bestelling():
    while True:
        try:
            amountPatat = int(input('Hoeveel patat wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')
            continue

    while True:
        try:
            amountFrikandellen = int(input('Hoeveel frikandellen wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')

    while True:
        try:
            amountKroketten = int(input('Hoeveel kroketten wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')


        
            
    return amountPatat, amountFrikandellen, amountKroketten

def calculation():
    amountPatat, amountFrikandellen, amountkroketten = bestelling()
    patat = 2.50
    frikandel = 1.50
    kroket = 1.50
    
    pricePatat = amountPatat * patat
    priceFrikandel = amountFrikandellen * frikandel
    priceKroket = amountkroketten * kroket
    
    pricePatatFormatted = ("{:0.2f}".format(pricePatat))
    priceFrikandelFormatted = ("{:0.2f}".format(priceFrikandel)) 
    priceKroketFormatted = ("{:0.2f}".format(priceKroket))
    
    return pricePatatFormatted, priceFrikandelFormatted, priceKroketFormatted, amountPatat, amountFrikandellen, amountkroketten
pricePatatFormatted, priceFrikandelFormatted, priceKroketFormatted, amountPatat, amountFrikandellen, amountkroketten = calculation()

print(f"Patat price = {pricePatatFormatted}, amount {amountPatat}")
print(f"Frikandel price = {priceFrikandelFormatted}, amount {amountFrikandellen}")
print(f"Kroket price = {priceKroketFormatted}, amount {amountkroketten}")

