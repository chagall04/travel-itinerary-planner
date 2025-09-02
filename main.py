
# gui_app.py

from tkinter import *
from tkinter import messagebox
from itinerary import Destination, NoDestinations, DestinationNotFound
from datetime import datetime

# Main Application Class
class ItineraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Itinerary Planner")
        self.root.geometry("400x500")
        self.destinations = []

        # Title Label
        Label(root, text="Travel Itinerary Planner", font=("Arial", 16, "bold"), bg="lightblue").pack(fill=X, pady=10)

        # Input Fields
        self.create_input_fields(root)

        # Buttons
        self.create_buttons(root)

        # Output Area
        self.create_output_area(root)

    def create_input_fields(self, root):
        """Creates input fields for the application."""
        frame = Frame(root)
        frame.pack(pady=10)

        Label(frame, text="Destination Name:").grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(frame, width=30)
        self.name_entry.grid(row=0, column=1)

        Label(frame, text="Country:").grid(row=1, column=0, sticky=W)
        self.country_entry = Entry(frame, width=30)
        self.country_entry.grid(row=1, column=1)

        Label(frame, text="City:").grid(row=2, column=0, sticky=W)
        self.city_entry = Entry(frame, width=30)
        self.city_entry.grid(row=2, column=1)

        Label(frame, text="Visit Date (YYYY-MM-DD):").grid(row=3, column=0, sticky=W)
        self.date_entry = Entry(frame, width=30)
        self.date_entry.grid(row=3, column=1)

        Label(frame, text="Number of Days:").grid(row=4, column=0, sticky=W)
        self.days_entry = Entry(frame, width=30)
        self.days_entry.grid(row=4, column=1)

        Label(frame, text="Estimated Budget:").grid(row=5, column=0, sticky=W)
        self.budget_entry = Entry(frame, width=30)
        self.budget_entry.grid(row=5, column=1)

    def create_buttons(self, root):
        """Creates buttons for interacting with the application."""
        frame = Frame(root)
        frame.pack(pady=10)

        Button(frame, text="Add Destination", command=self.add_destination).grid(row=0, column=0, padx=5)
        Button(frame, text="View Itinerary", command=self.view_itinerary).grid(row=0, column=1, padx=5)
        Button(frame, text="Search Destination", command=self.search_destination).grid(row=0, column=2, padx=5)
        Button(frame, text="Calculate Total Budget", command=self.calculate_budget).grid(row=1, column=0, columnspan=3, pady=5)

    def create_output_area(self, root):
        """Creates the output display area."""
        Label(root, text="Output:", font=("Arial", 12)).pack(pady=5)
        self.output_text = Text(root, height=10, width=50, state=DISABLED)
        self.output_text.pack()

    def add_destination(self):
        """Adds a new destination to the itinerary."""
        try:
            name = self.name_entry.get()
            country = self.country_entry.get()
            city = self.city_entry.get()
            visit_date = self.date_entry.get()
            days = int(self.days_entry.get())
            budget = float(self.budget_entry.get())

            # Input validation
            if not name or not country or not city or not visit_date:
                raise ValueError("All fields must be filled out.")
            datetime.strptime(visit_date, "%Y-%m-%d")  # Validate date format

            destination = Destination(name, country, city, visit_date, days, budget)
            self.destinations.append(destination)
            self.clear_inputs()
            self.display_message(f"Destination '{name}' added successfully!")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def view_itinerary(self):
        """Displays all destinations in the itinerary."""
        if not self.destinations:
            self.display_message("No destinations in the itinerary.")
            return

        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
        for dest in self.destinations:
            self.output_text.insert(END, f"{dest}\n")
        self.output_text.config(state=DISABLED)

    def search_destination(self):
        """Searches for a specific destination by name."""
        name = self.name_entry.get()
        try:
            if not name:
                raise ValueError("Please enter the destination name to search.")
            found = next((dest for dest in self.destinations if dest.name.lower() == name.lower()), None)
            if not found:
                raise DestinationNotFound(f"Destination '{name}' not found in the itinerary.")
            self.display_message(f"Found: {found}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except DestinationNotFound as e:
            messagebox.showwarning("Search Error", str(e))

    def calculate_budget(self):
        """Calculates the total budget for all destinations."""
        try:
            if not self.destinations:
                raise NoDestinations("No destinations available to calculate the budget.")
            total_budget = sum(dest.budget for dest in self.destinations)
            self.display_message(f"Total Estimated Budget: ${total_budget:.2f}")
        except NoDestinations as e:
            messagebox.showerror("Calculation Error", str(e))

    def clear_inputs(self):
        """Clears all input fields."""
        self.name_entry.delete(0, END)
        self.country_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.days_entry.delete(0, END)
        self.budget_entry.delete(0, END)

    def display_message(self, message):
        """Displays a message in the output text area."""
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
        self.output_text.insert(END, message)
        self.output_text.config(state=DISABLED)

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = ItineraryApp(root)
    root.mainloop()
