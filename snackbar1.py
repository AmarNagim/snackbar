# Amar Nagim
# Snackbar Coding Assignment 1


def bestelling():
    # In deze functie word de gebruiker gevraagd om zijn bestelling.
    # Mocht de input van de gebruiker geen integer zijn, word deze vraag
    # opnieuw gesteld totdat er wel een integer word geinput
    # Uiteraard worden ten slot alles veriabelen die ik nog nodig heb gereturned
    while True:
        try:
            amountPatat = int(input('Hoeveel patat wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')
            continue

    while True:
        try:
            amountFrikandel = int(input('Hoeveel frikandellen wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')

    while True:
        try:
            amountKroket = int(input('Hoeveel kroketten wilt u?: '))
            break
        except ValueError:
            print('Dat begreep ik niet..')

    return amountPatat, amountFrikandel, amountKroket


amountPatat, amountFrikandel, amountKroket = bestelling()


def calculation():
    # Hier word de prijs van de bestelling berekend.
    # Deze prijzen worden vervolgens geformateerd in
    # getallen met twee decimalen achter de komma en worden in aparte variabele gestopt.
    # De reden dat ik niet de 'raw' prijzen formatteer is omdat ik deze 'raw'
    # data wil behouden voor potentiele uitbreidingen (raw data is exacter dan de geformateerde data in dit geval)
    # Uiteraard worden ten slot alles veriabelen die ik nog nodig heb gereturned

    patat = 2.50
    frikandel = 1.50
    kroket = 1.50

    pricePatat = amountPatat * patat
    priceFrikandel = amountFrikandel * frikandel
    priceKroket = amountKroket * kroket
    subTotalPrice = pricePatat + priceFrikandel + priceKroket
    totalAmount = amountPatat + amountFrikandel + amountKroket
    priceDict = {}
    kortingVijfProcent = subTotalPrice/100*5
    kortingZevenEnEenHalfProcent = subTotalPrice/100*7.5

    pricePatatFormatted = ("{:0.2f}".format(pricePatat))
    priceFrikandelFormatted = ("{:0.2f}".format(priceFrikandel))
    priceKroketFormatted = ("{:0.2f}".format(priceKroket))
    subTotalPriceFormatted = ("{:0.2f}".format(subTotalPrice))
    extraFees = float(subTotalPriceFormatted)+4.00

    if subTotalPrice < 10:
        # 4 euro bestelkosten
        priceDict['Bestelkosten'] = "{:0.2f}".format(4.00)
        totalPriceFormatted = ("{:0.2f}".format(extraFees))
    elif subTotalPrice < 40:
        # Niks
        totalPriceFormatted = ("{:0.2f}".format(subTotalPrice))
    elif subTotalPrice < 100:
        # 5% Korting
        priceDict['5% Korting'] = "{:0.2f}".format(kortingVijfProcent)
        totalPriceFormatted = float(subTotalPriceFormatted)-float(kortingVijfProcent)
    else:
        # 7,5% korting
        priceDict['7,5% Korting'] = "{:0.2f}".format(kortingZevenEnEenHalfProcent)
        totalPriceFormatted = float(subTotalPriceFormatted)-float(kortingZevenEnEenHalfProcent)
    print(priceDict)
    return pricePatatFormatted, priceFrikandelFormatted, priceKroketFormatted, amountPatat, amountFrikandel, amountKroket, subTotalPrice, subTotalPriceFormatted, totalAmount, priceDict, totalPriceFormatted


pricePatatFormatted, priceFrikandelFormatted, priceKroketFormatted, amountPatat, amountFrikandel, amountKroket, subTotalPrice, subTotalPriceFormatted, totalAmount, priceDict, totalPriceFormatted = calculation()


def bon():
    # Hier maakt 'ie een dicionary voor alle items
    itemDict = {}

    if amountPatat > 0:
        itemDict['Patat'] = [amountPatat, pricePatatFormatted]
    if amountFrikandel > 0:
        itemDict['Frikandel'] = [amountFrikandel, priceFrikandelFormatted]
    if amountKroket > 0:
        itemDict['Kroket'] = [amountKroket, priceKroketFormatted]
          
    def formatItems(itemDict):
        # Hij looped over de keys in itemDict om de lengte van de woorden te krijgen
        wordLengths = [len(x) for x in itemDict]
        # Hier pakt 'ie het langste woord, dit gaan we gebruiken als pad waarde
        padLength = max(wordLengths)
        formattedItems = []
        # Hier looped hij over de dictionary, in word zitten de woorden, en in info zit de lijst met prijzen en hoeveelheden
        for word, info in itemDict.items():
            # Hij split de info in hoeveelheden en prijzen
            hoeveelheid, price = info
            # Hier formatteer ik de line
            item = f"x{hoeveelheid} {word:<{padLength}} €{price}"
            # Hier voeg ik het toe aan de output list
            formattedItems.append(item)

        return formattedItems, padLength

    def formatPrice(dictionary):
        # In deze function print ik de potentiele kortingen en bestelkosten
        for key, value in dictionary.items():
            print (f'{key}  €{value}')


    formattedItems, padLength = formatItems(itemDict)


    print(f"""
=======================
==========BON==========
=======================""")
    # Hier print ik de bon
    for line in formattedItems:
        # In deze for loop print ik alle bestelde items
        print(line)
    print('-----------------------')        
    print(f'Subtotaal  €{subTotalPriceFormatted}')    
    formatPrice(priceDict)
    print(f'Totaalprijs  €{totalPriceFormatted}')
bon()
