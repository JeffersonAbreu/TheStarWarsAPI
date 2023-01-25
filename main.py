import requests
import sys

def getStarShipsAll():
    url = "https://swapi.dev/api/starships"
    req = requests.get(url, timeout = 10).json()
    isNext = True
    starships = []
    print("Calculating, wait!")
    while isNext:
        for starship in req['results']:
            starships.append(starship)
        
        if req['next'] == None:
            isNext = False
        else:
            url = req['next']
            req = requests.get(url, timeout = 10).json()
    
    return starships


def extractHours(unity):
    unity = str(unity)
    hours = 1
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


def error():
    print("       ERRO\nUse the command with the following example:")
    print("python main.py --distance=1000000")
    sys.exit()


def main(args):
    try:
        text, num = str(args[0]).split('=')
        distance = int(num)
        if(text != '--distance'):
            error()
        elif(distance <= 0):
            print('\nThe number must be greater than zero\n')
            error()

        print("\nRunning the app with {} MGLTs!".format(distance))
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
                    print(f"{name}: {calculateStopsNecessary(consumable, speedMGLT, distance)}")

        except Exception as e:
                print(f"Error -> {e}")
                error()

    except Exception as e:
        error()


if __name__ == "__main__":
    main(sys.argv[1:])