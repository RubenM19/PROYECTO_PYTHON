from typing import List, Dict
import random

import statistics
import operator

from config import IGV_TOTAL, CURRENCY_SYMBOL


def main():

    # Se inicializa la variable 'flights'
    flights: List[Dict[str, str | float | int]] = [{
        'code': 'LIM-AYA',
        'name': 'Lima - Ayacucho',
        'base_price': 55.19,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A001',
        'ticket_sale_economy_min_range': 120,
        'ticket_sale_economy_max_range': 130,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 20
    }, {
        'code': 'LIM-CUS',
        'name': 'Lima - Cusco',
        'base_price': 136.51,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A002',
        'ticket_sale_economy_min_range': 130,
        'ticket_sale_economy_max_range': 144,
        'ticket_sale_premium_min_range': 15,
        'ticket_sale_premium_max_range': 24
    }, {
        'code': 'LIM-ARE',
        'name': 'Lima - Arequipa',
        'base_price': 90.29,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A003',
        'ticket_sale_economy_min_range': 115,
        'ticket_sale_economy_max_range': 138,
        'ticket_sale_premium_min_range': 16,
        'ticket_sale_premium_max_range': 22
    }, {
        'code': 'LIM-TAR',
        'name': 'Lima - Tarapoto',
        'base_price': 71.89,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A004',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 120,
        'ticket_sale_premium_min_range': 12,
        'ticket_sale_premium_max_range': 18
    }, {
        'code': 'AYA-LIM',
        'name': 'Ayacucho - Lima',
        'base_price': 40.42,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A001',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 115,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 15
    }, {
        'code': 'CUS-LIM',
        'name': 'Cusco - Lima',
        'base_price': 124.32,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A002',
        'ticket_sale_economy_min_range': 105,
        'ticket_sale_economy_max_range': 120,
        'ticket_sale_premium_min_range': 14,
        'ticket_sale_premium_max_range': 20
    }, {
        'code': 'ARE-LIM',
        'name': 'Arequipa - Lima',
        'base_price': 86.59,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A003',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 110,
        'ticket_sale_premium_min_range': 13,
        'ticket_sale_premium_max_range': 18
    }, {
        'code': 'TAR-LIM',
        'name': 'Tarapoto - Lima',
        'base_price': 68.42,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A004',
        'ticket_sale_economy_min_range': 90,
        'ticket_sale_economy_max_range': 105,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 15
    }]

    # Se inicializa la variable que almacenar?? el total de tickets
    total_ticket: int = 0

    # Se inicializa la variable que almacenar?? la venta total de los pasajes econ??micos
    total_economic_tickets_sales: float = 0

    # Se inicializa la variable que almacenar?? la venta total de los pasajes premium
    total_premium_tickets_sales: float = 0

    # Se inicializa la variable que almacenar?? el total de IGV
    total_IGV: float = 0

    # Se inicializa la variable all_cheap_tickets que almacenar?? los precios de pasaje econ??mico
    all_cheap_tickets: List[float] = []

    # Se inicializa la variable all_premium_tickets que almacenar?? los precios de pasaje premium
    all_premium_tickets: List[float] = []

    # Se inicializa la variable all_flights que almacenar?? los  vuelos programados
    all_scheduled_flights: List[Dict[str, str | float]] = []

    # Iteraci??n para cada vuelo
    for key, flight in enumerate(flights):

        # Se inicializa la variable que almacenar?? el total de pasajes econ??micos vendidos
        economic_ticket: int = random.randint(int(flight['ticket_sale_economy_min_range']), int(
            flight['ticket_sale_economy_max_range']))

        # Se inicializa la variable que almacenar?? el total de pasajes premium vendidos
        premium_ticket: int = random.randint(int(flight['ticket_sale_premium_min_range']), int(
            flight['ticket_sale_premium_max_range']))

        # Sumar?? los pasajes vendidos
        total_ticket += economic_ticket + premium_ticket

        # Iteraci??n por cada asiento econ??mico de cada vuelo
        for i in range(economic_ticket):

            # Se inicializa el precio del pasaje econ??mico sin IGV
            economic_ticket_cost: float = (
                float(flight['base_price']) + float(flight['economy_seat']))

            # Se agrega a la lista all_cheap_tickets el precio de un pasaje con asiento econ??mico
            all_cheap_tickets.append(economic_ticket_cost)

            # Se inicializa el precio total del pasaje econ??mico con IGV
            total_economic_ticket_cost: float = economic_ticket_cost + \
                economic_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el impuesto de cada pasaje econ??mico del vuelo
            total_IGV += economic_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el precio total del pasaje econ??mico del vuelo
            total_economic_tickets_sales += total_economic_ticket_cost

        # Iteraci??n por cada asiento premium de cada vuelo
        for i in range(premium_ticket):

            # Se inicializa el precio del pasaje premium sin IGV
            premium_ticket_cost: float = (
                float(flight['base_price']) + float(flight['premium_seat']))

            # Se agrega a la lista all_premium_tickets el precio de un pasaje con asiento premium
            all_premium_tickets.append(premium_ticket_cost)

            # Se inicializa el precio total del pasaje premium con IGV
            total_premium_ticket_cost: float = premium_ticket_cost + \
                premium_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el impuesto de cada pasaje premium del vuelo
            total_IGV += premium_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el precio total del pasaje premium del vuelo
            total_premium_tickets_sales += total_premium_ticket_cost

        # Sumando total de tickets premium y total de tickets econ??micos vendidos y
        total_ticket_sales = round(
            total_premium_tickets_sales + total_economic_tickets_sales, 2)

        total_tickets_per_fly: int = economic_ticket + premium_ticket
        # Creamos el diccionario para los vuelos programados
        scheduled_flights: Dict[str, str | int | float] = {
            "route": flight["name"],
            "airplane": flight["airplane"],
            "total_tickets_sales": total_ticket_sales,
            "total_tickets_per_fly": total_tickets_per_fly,

        }
        all_scheduled_flights.append(scheduled_flights)

    # Se imprime la cantidad de pasajes por todos los vuelos
    # Pregunta 1
    print(f"Se vendieron un total de {total_ticket} tickets")

    print("-" * 30)

    # Se imprime el total de pasajes econ??micos que se han vendido
    # Pregunta 2
    print(f"Se ingres?? un total de $ {round(total_economic_tickets_sales,2)} en pasajes econ??micos")

    # Se imprime el total de pasajes premium que se han vendido
    # Pregunta 3
    print(f"Se ingres?? un total de $ {round(total_premium_tickets_sales,2)} en pasajes premium")

    # Se imprime el total IGV que se ha cobrado
    # Pregunta 4
    print(f"Se cobr?? un total de $ {round(total_IGV,2)} en IGV")
    print("-" * 30)

    # Pregunta 5
    # Se imprime el valor promedio del pasaje econ??mico
    average_economic_ticket_cost: float = statistics.mean(all_cheap_tickets)
    average_formatted_economy_ticket: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, average_economic_ticket_cost)
    print(f"El valor promedio del pasaje econ??mico es: {average_formatted_economy_ticket}")
    print("-" * 30)

    # Pregunta 6
    # Se imprime el valor promedio del pasaje premium
    average_premium_ticket_cost: float = statistics.mean(all_premium_tickets)
    average_formatted_premium_ticket: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, average_premium_ticket_cost)
    print(f"El valor promedio del pasaje premium es: {average_formatted_premium_ticket}")
    print("-" * 30)

    # Ordenemos lista de vuelos seg??n el n??mero de pasajeros (de menor a mayor)
    sorted_passengers: List[Dict[str, str | float]] = sorted(
        all_scheduled_flights, key=lambda x: x["total_tickets_per_fly"])
    print("-" * 30)

    # Pregunta 7
    # Se obtiene el maximo de pasajeros a traves de los pasajes vendidos
    print(
        f"El vuelo con la mayor cantidad de pasajeros es: {sorted_passengers[-1]['route']} con una cantidad de {sorted_passengers[-1]['total_tickets_per_fly']}")

    # Pregunta 8
    # Se obtiene el m??nimo de pasajeros a traves de los pasajes vendidos
    print(f"El vuelo con la menor cantidad de pasajeros es: {sorted_passengers[0]['route']} con una cantidad de {sorted_passengers[0]['total_tickets_per_fly']}")
    print("-" * 30)

    # Pregunta 9
    # Ordenemos lista de vuelos seg??n los ingresos por la venta de asientos (de mayor a menor)
    order_total_tickets_sales: List[Dict[str, str | float]] = sorted(
        all_scheduled_flights, key=lambda x: x["total_tickets_sales"], reverse=True)

    # Iteramos los 3 veces la lista ordeana de vuelos
    for i in range(3):
        print(f"El {i+1}?? vuelo con mayor ingresos es: {order_total_tickets_sales[i]['route']} con un total de {CURRENCY_SYMBOL}{order_total_tickets_sales[i]['total_tickets_sales']}")

    print("-" * 50)
    # Pregunta 10
    print(f"El avi??n que transport?? mas pasajeros es: {sorted_passengers[-1]['airplane']}")
    print("-" * 30)

if __name__ == "__main__":
    main()