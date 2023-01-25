class Util:

    @staticmethod
    def extract_hours(unity: str) -> int:
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