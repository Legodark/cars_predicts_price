def modelTransmission(transmission):
    if transmission == 'Automatica':
        return 0
    elif transmission == 'Manual':
        return 1
    elif transmission == 'Semi-automatica':
        return 2
    elif transmission == 'Other':
        return 3


def combustibleType(fuelType):
    if fuelType == 'Electric':
        return 0
    elif fuelType == 'Diesel':
        return 1
    elif fuelType == 'Hybrid':
        return 2
    elif fuelType == 'Gasolina':
        return 3
    elif fuelType == 'Other':
        return 4
