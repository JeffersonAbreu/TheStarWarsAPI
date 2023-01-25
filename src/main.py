import sys
from services.api import Api
from model.starship import StarShip

def error():
    print("       ERRO\nUse the command with the following example:")
    print("python main.py --distance=1000000")
    sys.exit()


def main(args):
    try:
        text, num = str(args[0]).split('=')
        distance: int = int(num)
        if(text != '--distance'):
            error()
        elif(distance <= 0):
            print('\nThe number must be greater than zero\n')
            error()
        print(f"\nRunning the app with {distance} MGLTs!")
        try:
            starships: list[StarShip] = Api.getStarShipsAll()
            print('\n## Stop required for each starship ##\n')
            for starship in starships:
                stops: str = starship.calc_stops(distance)
                print(f"{starship.name}: {stops}")
        except Exception as e:
            print(f"Error -> {e}")
    except Exception as e:
        error()


if __name__ == "__main__":
    main(sys.argv[1:])
    # main(["--distance=1000000"])