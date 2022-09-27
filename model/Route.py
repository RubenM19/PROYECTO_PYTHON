import random

class Route(object):
    """
    Clase Ticket de Venta
    """
    
    def __init__(self, code: str, name: str, price_base: float, eco_seat: int, premium_seat: int, plane: str, time: str, min_eco_seats: int, max_eco_seats: int, min_premium_seats: int, max_premium_seats: int):
        """
        Constructor de la clase Store
        """
        self.code: str = code
        self.name: str = name
        self.price_base: float = price_base
        self.eco_seat: int = eco_seat
        self.premium_seat: int = premium_seat
        self.plane: str =plane
        self.time: str = time
        self.min_eco_seats: int = min_eco_seats
        self.max_eco_seats: int = max_eco_seats
        self.min_premium_seats: int = min_premium_seats
        self.max_premium_seats: int = max_premium_seats

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.code, self.name, self.plane, self.time
    
    def get_rand_eco_seats(self) -> int:
        """
        Devuelve un número de venta de asientos economicos aleatorio.
        """
        return random.randint(self.min_eco_seats, self.max_eco_seats)
    
    def get_rand_premium_seats(self) -> int:
        """
        Devuelve un número de ventas de asientos premium aleatorio.
        """
        return random.randint(self.min_premium_seats, self.max_premium_seats)