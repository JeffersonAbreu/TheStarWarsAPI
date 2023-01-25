
from utils.util import Util

class StarShip:

    def __init__(self, name: str, consumables: str, speed: str) -> None:
        self.name: str = name
        self.consumables: str = consumables
        self.speed: str = speed

    def calc_stops(self, distance: int) -> str:
        stops: str = ""
        if((self.consumables == 'unknown') or (self.speed == 'unknown')):
            stops = "unknown"
        else:
            hoursNeeded: float = distance / int(self.speed)
            digit, unity = self.consumables.split(' ')
            consumptionPerHour: int = int(digit) * Util.extract_hours(unity)
            # return stops needed
            stops = str(int(hoursNeeded / consumptionPerHour))
        return(stops)