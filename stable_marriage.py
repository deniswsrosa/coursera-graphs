def stableMatching(n, menPreferences, womenPreferences):
    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    manSpouse = [None] * n
    womenSpouse = [None] * n
    marriedWoman = []
    marriedMan = []

    while len(marriedMan) < n :
        for men in unmarriedMen:
            if men not in marriedMan:
                hisPref = menPreferences[men].pop(0)
                if hisPref != None:
                    if hisPref not in marriedWoman:
                        womenSpouse[hisPref] = men
                        marriedMan.append(men)
                        manSpouse[men] = hisPref
                        marriedWoman.append(hisPref)
                        noChanges = True
                    else:
                        if isHerPref(men, hisPref, womenSpouse, womenPreferences[hisPref]):
                            manSpouse[womenSpouse[hisPref]] = None
                            marriedMan.remove(womenSpouse[hisPref])
                            manSpouse[men] = hisPref
                            womenSpouse[hisPref] = men
                            marriedMan.append(men)
                            noChanges = True
    return manSpouse

def isHerPref(men, woman, womenSpouse, herPreferences  ):
    if(herPreferences.index(men) < herPreferences.index(womenSpouse[woman]) ):
        return True
    else:
        return False
    