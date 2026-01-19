'''
You are given a list of unordered travel tickets. Each ticket is a list or tuple containing a source and a destination 
(e.g., [("Athens", "Madrid"), ("Berlin", "Rome"), ("Madrid", "Berlin")]). Your task is to write a function that reconstructs 
the complete path of the trip in the correct chronological order
'''
def order_itinerary(tickets: list[tuple[str, str]]) -> list[tuple[str, str]]:
    departures = []
    destinations = []
    for ticket in tickets:
        departures.append(ticket[0])
        destinations.append(ticket[1])
    
    departures = set(departures)
    destinations = set(destinations)

    unique_cities = (departures | destinations) - (departures & destinations)
    for city in unique_cities:
        if city in departures:
            start = city
        else: 
            end = city

    ordered_itinerary = []
    while len(ordered_itinerary) < len(tickets):
        for ticket in tickets:
            if start == ticket[0]:
                ordered_itinerary.append(ticket)
                start = ticket[1]
        
    return ordered_itinerary

tickets = [("Athens", "Madrid"), ("Berlin", "Rome"), ("Madrid", "Berlin")]
print(order_itinerary(tickets))


def opt_order_itinerary(tickets: list[tuple[str, str]]) -> list[tuple[str, str]]:
    itinerary_map = {}
    for ticket in tickets:
        itinerary_map[ticket[0]] = ticket[1]
    '''
    It's more professional to use a dict comprehession:
    itinerary_map = {departure: destination for departure, destination in tickets}
    '''

    start = (set(itinerary_map.keys()) - set(itinerary_map.values())).pop()

    ordered_itinerary = []
    while len(ordered_itinerary) < len(tickets):
        if start in itinerary_map: # It's the same that itinerary_map.keys() but cleaner
            ordered_itinerary.append((start, itinerary_map[start]))
            start = itinerary_map[start]
    
    return ordered_itinerary

tickets = [("Athens", "Madrid"), ("Berlin", "Rome"), ("Madrid", "Berlin")]
print(opt_order_itinerary(tickets))