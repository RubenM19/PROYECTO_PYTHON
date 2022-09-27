from typing import List, Dict
from model.Route import Route
#enconding: utf-8

def create_list_route() -> List[Route]:
    data_routes: List[Dict[str, str | int | float]] =[
        {
            "code": "LIM-AYA",
            "name": "Lima - Ayacucho",
            "price_base": 55.19,
            "eco_seat": 8.00,
            "premium_seat": 16.00,
            "plane": "A001",
            "time": "06:30",
            "min_eco_seats": 120,
            "max_eco_seats": 130,
            "min_premium_seats": 10,
            "max_premium_seats": 20
        },
        {
            "code": "LIM-CUS",
            "name": "Lima - Cusco",
            "price_base": 138.51,
            "eco_seat": 8.00,
            "premium_seat": 16.00,
            "plane": "A002",
            "time": "07:25",
            "min_eco_seats": 130,
            "max_eco_seats": 144,
            "min_premium_seats": 15,
            "max_premium_seats": 24
        },
        {
            "code": "LIM-ARE",
            "name": "Lima - Arequipa",
            "price_base": 90.59,
            "eco_seat": 8.00,
            "premium_seat": 16.00,
            "plane": "A003",
            "time": "08:10",
            "min_eco_seats": 115,
            "max_eco_seats": 138,
            "min_premium_seats": 16,
            "max_premium_seats": 22
        },
        {
            "code": "LIM-TAR",
            "name": "Lima - Tarapoto",
            "price_base": 71.89,
            "eco_seat": 8.00,
            "premium_seat": 16.00,
            "plane": "A004",
            "time": "08:50",
            "min_eco_seats": 100,
            "max_eco_seats": 120,
            "min_premium_seats": 12,
            "max_premium_seats": 18
        },
        {
            "code": "AYA-LIM",
            "name": "Ayacucho - Lima",
            "price_base": 40.42,
            "eco_seat": 7.00,
            "premium_seat": 16.00,
            "plane": "A001",
            "time": "15:45",
            "min_eco_seats": 100,
            "max_eco_seats": 115,
            "min_premium_seats": 10,
            "max_premium_seats": 15
        },
        {
            "code": "CUS-LIM",
            "name": "Cusco - Lima",
            "price_base": 124.32,
            "eco_seat": 7.00,
            "premium_seat": 16.00,
            "plane": "A002",
            "time": "16:25",
            "min_eco_seats": 105,
            "max_eco_seats": 120,
            "min_premium_seats": 14,
            "max_premium_seats": 20
        },
        {
            "code": "ARE-LIM",
            "name": "Arequipa - Lima",
            "price_base": 86.59,
            "eco_seat": 7.00,
            "premium_seat": 16.00,
            "plane": "A003",
            "time": "17:15",
            "min_eco_seats": 100,
            "max_eco_seats": 110,
            "min_premium_seats": 13,
            "max_premium_seats": 18
        },
        {
            "code": "TAR-LIM",
            "name": "Tarapoto - Lima",
            "price_base": 86.59,
            "eco_seat": 7.00,
            "premium_seat": 16.00,
            "plane": "A004",
            "time": "17:50",
            "min_eco_seats": 90,
            "max_eco_seats": 105,
            "min_premium_seats": 10,
            "max_premium_seats": 15
        }
    ]
    #Lista de objetos aerolinea
    routes: List[Route] = []

    for key, route in enumerate(data_routes):
        obj_route = Route(str(route['code']), str(route['name']), 
        float(route['price_base']), int(route['eco_seat']), 
        int(route['premium_seat']), str(route['plane']), 
        str(route['time']), int(route['min_eco_seats']),
        int(route['max_eco_seats']), int(route['min_premium_seats']),
        int(route['max_premium_seats'])
        )
        routes.append(obj_route)
    
    return routes


def main():
    """
    Función principal del módulo main_plication.py
    """
    routes: List[Route] = create_list_route()

    print("\n")
    print("*"*40)
    print("REPORTE DE AEROLINEA")
    print("*"*40)
    print("\n")

    for key, route in enumerate(routes):
        print(f"Tienda: {route.name}")
        print(f"Tienda: {route.code}")
    
    print("\n")
    print("-"*30)
    print("\n")

if __name__ == "__main__":
    main()