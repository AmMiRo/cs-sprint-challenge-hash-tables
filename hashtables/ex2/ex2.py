#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # initialize cache
    cache = {}
    # initialize route
    route = []
    # initialize current to be NONE
    current = "NONE"
    # iterate through tickets to populate cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # while route shorter than length append cache[current] and set current to next
    while len(route) < length:
        route.append(cache[current])
        current = cache[current]

    return route
