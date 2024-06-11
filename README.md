## Star Cinema Project Description

### Project Overview

The **Star Cinema** project is a simplified cinema hall management system designed to manage and book seats for shows in a cinema hall. It demonstrates basic functionalities such as entering new cinema halls, managing show listings, booking seats, and viewing available seats for different shows. The project is implemented using Python classes and showcases object-oriented programming principles.

### Key Components

#### 1. **Star_Cinema Class**

- **Purpose:** Manages the list of halls in the cinema.
- **Attributes:**
  - `hall_list`: A class-level attribute that stores the list of all hall identifiers.

- **Methods:**
  - `entry_hall(hall)`: Adds a new hall to the `hall_list`.

#### 2. **Hall Class**

- **Purpose:** Represents an individual hall within the cinema, inherits from `Star_Cinema`.
- **Attributes:**
  - `seats`: A dictionary to track seat availability for each show (`{show_id: seats_matrix}`).
  - `show_list`: A list to store details of shows in the hall.
  - `__rows` and `__cols`: Private attributes representing the number of rows and columns of seats.
  - `_hall_no`: A protected attribute representing the hall number.

- **Methods:**
  - `__init__(self, rows, cols, hall_no)`: Initializes a new hall with a specified number of rows, columns, and a hall number. It also registers the hall with `Star_Cinema`.
  - `entry_show(self, id, movie_name, time)`: Adds a new show to the hall’s `show_list` and initializes the seating arrangement for that show.
  - `book_seats(self, customer_name, phone_number, show_id, row, col)`: Books a specified seat for a show if it is available, or indicates if the seat is already booked.
  - `view_show_list(self)`: Prints the list of currently running shows in the hall.
  - `view_available_seats(self, id)`: Prints the seating arrangement for a specific show and indicates available and booked seats.

### Usage

The project allows users to interact with the cinema management system via a command-line interface. Users can perform the following actions:

1. **View All Shows Today:**
   - Displays the list of all shows running in the cinema hall, along with their IDs, names, and timings.

2. **View Available Seats:**
   - Displays the seating arrangement for a specific show. Available seats are represented by their seat numbers, while booked seats are marked with an 'x'.

3. **Book Seats:**
   - Allows users to book seats for a specific show by entering their name, phone number, the show ID, and the desired seat row and column. If the seat is available, it is booked; otherwise, a message indicates that the seat is already booked.

### Example Usage

1. **Initializing the Hall:**

   ```python
   bijoy_hall = Hall(3, 3, 3)
   ```

2. **Entering Shows:**

   ```python
   bijoy_hall.entry_show("abc121", "Black Adam", "12 December 2022 8:30 PM")
   bijoy_hall.entry_show("xyz123", "Avatar", "12 December 2022 5:30 PM")
   ```

3. **Viewing Shows and Seats:**

   ```python
   bijoy_hall.view_show_list()
   bijoy_hall.view_available_seats("abc121")
   ```

4. **Booking a Seat:**

   ```python
   bijoy_hall.book_seats("John Doe", "1234567890", "abc121", 1, 2)
   ```

### Project Structure

- **Star_Cinema:** Base class for cinema management.
- **Hall:** Derived class managing individual halls, shows, and seating.

### Conclusion

The **Star Cinema** project provides a foundational approach to managing a cinema hall's operations. It covers essential functionalities like show management and seat booking, making it a good starting point for more complex cinema management systems.
