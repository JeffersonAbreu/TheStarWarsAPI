import requests
URL = 'https://swapi.dev/api'


def getStarShipsAll():
    req = requests.get(f'{URL}/starships')
    req = req.json()
    isNext = True
    starships = []
    print("Calculating, wait!")
    while isNext:
        for starship in req['results']:
            starships.append(starship)
        
        if req['next'] == None:
            isNext = False
        else:
            req = requests.get(req['next'])
            req = req.json()
    
    return starships


def extractHours(unity: str):
    hours: int = 1
    if (unity.startswith('year')):
        hours = 8760
    elif (unity.startswith('month')):
        hours = 720
    elif (unity.startswith('week')):
        hours = 168
    elif (unity.startswith('day')):
        hours = 24
    return hours


def calculateStopsNecessary(consumable, speed, distance):
    hoursNeeded = distance / int(speed)
    digit, unity = consumable.split(' ')
    consumptionPerHour = int(digit) * extractHours(unity)
    # return stops needed
    return int(hoursNeeded / consumptionPerHour)


def main():
    try:
        # distanceInMGLTs = int(input("How many mega lights do you want to run?\nEnter an integer: "))
        print("Running the app with 1.000.000 MGLTs!")
        distanceInMGLTs = int(1000000)
        try:
            starships = getStarShipsAll()
            print(f'\n## Stop required for each starship ##\n')
            for starship in starships:
                name = starship['name']
                consumable = starship['consumables']
                speedMGLT = starship['MGLT']
                if((consumable == 'unknown') or (speedMGLT == 'unknown')):
                    print(f"{name}: unknown")
                else:
                    print(f"{name}: {calculateStopsNecessary(consumable, speedMGLT, distanceInMGLTs)}")

        except Exception as e:
                print(f"Error -> {e}")

    except Exception as e:
        print("The value entered is not an integer!")


if __name__ == "__main__":
    main()