import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

# Sample data for destinations, seats, and payment methods
available_seats = {
    "Economy": 100,
    "Business": 50,
    "First Class": 20
}

destinations = {
    "New York": "NYC",
    "Los Angeles": "LAX",
    "Chicago": "ORD",
    "Miami": "MIA"
}

payment_methods = ["CC", "DC", "PP"]

class FlightBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Booking System")
        self.root.geometry("600x600")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButtonBlack.TButton", foreground="black", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TText", background="#e0e0e0", font=("Arial", 12))
        self.style.configure("TEntry.TEntry", fieldbackground="black", foreground="white", bordercolor="black", font=("Arial", 12))
  
        self.frame = ttk.Frame(root, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.available_seats_label = ttk.Label(self.frame, text="Available Seats:", style="TLabel")
        self.available_seats_label.pack(anchor="w")

        self.available_seats_text = tk.Text(self.frame, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.available_seats_text.pack(anchor="w", pady=5)

        self.destinations_label = ttk.Label(self.frame, text="Available Destinations:", style="TLabel")
        self.destinations_label.pack(anchor="w")

        self.destinations_text = tk.Text(self.frame, height=3, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.destinations_text.pack(anchor="w", pady=5)

        self.payment_methods_label = ttk.Label(self.frame, text="Available Payment Methods:", style="TLabel")
        self.payment_methods_label.pack(anchor="w")

        self.payment_methods_text = tk.Text(self.frame, height=2, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.payment_methods_text.pack(anchor="w", pady=5)

        self.choice_label = ttk.Label(self.frame, text="Enter your choice (4 for Booking, 5 for Cancellation):", style="TLabel")
        self.choice_label.pack(anchor="w", pady=10)

        self.choice_entry = ttk.Entry(self.frame, style="TEntry")
        self.choice_entry.pack(anchor="w", pady=5)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.handle_choice, style="TButtonBlack.TButton")
        self.submit_button.pack(anchor="w", pady=5)

        self.output_text = tk.Text(self.frame, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#ffc2b3", font=("Arial", 12))
        self.output_text.pack(anchor="w", pady=10)

        # Initializing the GUI with available information
        self.update_available_seats()
        self.update_destinations()
        self.update_payment_methods()

    def update_available_seats(self):
        seats_text = "Available Seats:\n"
        for class_name, seats in available_seats.items():
            seats_text += f"{class_name}: {seats} seats\n"
        self.available_seats_text.config(state=tk.NORMAL)
        self.available_seats_text.delete(1.0, tk.END)
        self.available_seats_text.insert(tk.END, seats_text)
        self.available_seats_text.config(state=tk.DISABLED)

    def update_destinations(self):
        destinations_text = ""
        for city, code in destinations.items():
            destinations_text += f"{city} ({code})\n"
        self.destinations_text.config(state=tk.NORMAL)
        self.destinations_text.delete(1.0, tk.END)
        self.destinations_text.insert(tk.END, destinations_text)
        self.destinations_text.config(state=tk.DISABLED)

    def update_payment_methods(self):
        methods_text = "\n".join(payment_methods)
        self.payment_methods_text.config(state=tk.NORMAL)
        self.payment_methods_text.delete(1.0, tk.END)
        self.payment_methods_text.insert(tk.END, methods_text)
        self.payment_methods_text.config(state=tk.DISABLED)

    def handle_choice(self):
        try:
            choice = int(self.choice_entry.get())
            if choice == 4:
                self.book_ticket()
            elif choice == 5:
                self.cancel_ticket()
            else:
                self.display_output("Invalid choice. Please try again.\n", "red")
        except ValueError:
            self.display_output("Invalid input. Please enter a valid number.\n", "red")

    def book_ticket(self):
        class_name = self.show_entry_dialog("Enter class (Economy/Business/First Class): ")
        if class_name not in available_seats:
            self.display_output("Invalid class name. Please try again.\n", "red")
            return

        try:
            num_tickets = int(self.show_entry_dialog("Enter the number of tickets to book: "))
                  if num_tickets <= 0:
                self.display_output("Number of tickets must be greater than zero.\n", "red")
                return
        except ValueError:
            self.display_output("Invalid number of tickets. Please enter a valid number.\n", "red")
            return

        destination = self.show_entry_dialog("Enter destination (NYC/LAX/ORD/MIA): ").upper()
        if destination not in destinations.values():
            self.display_output("Invalid destination. Please try again.\n", "red")
            return

        payment_method = self.show_entry_dialog("Enter payment method (CC/DC/PP): ").upper()
        if payment_method not in payment_methods:
            self.display_output("Invalid payment method. Please choose CC, DC, or PP.\n", "red")
            return

        self.process_payment(class_name, num_tickets, destination, payment_method)

    def cancel_ticket(self):
        class_name = self.show_entry_dialog("Enter class (Economy/Business/First Class): ")
        if class_name not in available_seats:
            self.display_output("Invalid class name. Please try again.\n", "red")
            return

        try:
            num_tickets = int(self.show_entry_dialog("Enter the number of tickets to cancel: "))
            if num_tickets <= 0:
                self.display_output("Number of tickets must be greater than zero.\n", "red")
                return
        except ValueError:
            self.display_output("Invalid number of tickets. Please enter a valid number.\n", "red")
            return

        destination = self.show_entry_dialog("Enter destination (NYC/LAX/ORD/MIA): ").upper()
        if destination not in destinations.values():
            self.display_output("Invalid destination. Please try again.\n", "red")
            return

        payment_method = self.show_entry_dialog("Enter payment method for refund (CC/DC/PP): ").upper()
        if payment_method not in payment_methods:
              self.display_output("Invalid payment method. Please choose CC, DC, or PP.\n", "red")
            return

        self.process_refund(class_name, num_tickets, destination, payment_method)

    def process_payment(self, class_name, num_tickets, destination, payment_method):
        if payment_method in ["CC", "DC"]:
            self.show_card_details_window(class_name, num_tickets, destination)
        else:
            self.display_output(f"Booking successful!\nClass: {class_name}\nTickets: {num_tickets}\nDestination: {destination}\nPayment Method: {payment_method}\n", "green")

    def process_refund(self, class_name, num_tickets, destination, payment_method):
        if payment_method in ["CC", "DC"]:
            self.show_card_details_window(class_name, num_tickets, destination, refund=True)
        else:
            self.display_output(f"Cancellation successful!\nClass: {class_name}\nTickets: {num_tickets}\nDestination: {destination}\nRefund Payment Method: {payment_method}\n", "green")

    def show_entry_dialog(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.root)

    def show_card_details_window(self, class_name, num_tickets, destination, refund=False):
        top = tk.Toplevel(self.root)
        top.title("Enter Card Details")
        top.geometry("300x200")

        ttk.Label(top, text="Card Number:").pack(pady=5)
        card_number_entry = ttk.Entry(top)
        card_number_entry.pack(pady=5)

        ttk.Label(top, text="Expiry Date (MM/YY):").pack(pady=5)
        expiry_date_entry = ttk.Entry(top)
        expiry_date_entry.pack(pady=5)

        ttk.Label(top, text="CVV:").pack(pady=5)
        cvv_entry = ttk.Entry(top, show="*")
        cvv_entry.pack(pady=5)

        def submit_card_details():
            card_number = card_number_entry.get()
            expiry_date = expiry_date_entry.get()
            cvv = cvv_entry.get()
          
            if not card_number or not expiry_date or not cvv:
                self.display_output("All card details must be filled in.\n", "red")
                return

            if refund:
                self.display_output(f"Refund processed successfully!\nClass: {class_name}\nTickets: {num_tickets}\nDestination: {destination}\nPayment Method: {payment_method}\n", "green")
            else:
                self.display_output(f"Booking processed successfully!\nClass: {class_name}\nTickets: {num_tickets}\nDestination: {destination}\nPayment Method: {payment_method}\n", "green")

            top.destroy()

        submit_button = ttk.Button(top, text="Submit", command=submit_card_details)
        submit_button.pack(pady=10)

    def display_output(self, message, color):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.tag_add(color, "1.0", "end")
        self.output_text.tag_config(color, foreground=color)
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingGUI(root)
    root.mainloop()
