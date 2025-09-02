
# itinerary.py

# Exception Classes
class NoDestinations(Exception):
    """Exception raised when no destinations are available."""
    pass

class DestinationNotFound(Exception):
    """Exception raised when a destination is not found."""
    pass

# Destination Class
class Destination:
    def __init__(self, name, country, city, visit_date, days, budget):
        self.name = name
        self.country = country
        self.city = city
        self.visit_date = visit_date
        self.days = days
        self.budget = budget

    def __str__(self):
        return f"{self.name} in {self.city}, {self.country} for {self.days} days (Budget: ${self.budget})"
