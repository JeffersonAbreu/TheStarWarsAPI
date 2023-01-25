from model.starship import StarShip
import requests

class Api:

    @staticmethod
    def getStarShipsAll():
        url:str = "https://swapi.dev/api/starships"
        req: list[str] = []
        req = requests.get(url, timeout = 10).json()
        isNext:bool = True
        starships_list: list[StarShip] = []
        print("Calculating, wait!")
        while isNext:
            starships: list[str] = req['results']
            for s in starships:
                starship: StarShip = StarShip(s['name'], s['consumables'], s['MGLT'])
                starships_list.append(starship)
            if req['next'] is None:
                isNext = False
            else:
                url = req['next']
                req = requests.get(url, timeout = 10).json()
        return starships_list