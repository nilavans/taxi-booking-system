<h1>TAXI BOOKING SYSTEM</h1>
<h2>Overview</h2>
This is a Python-based command-line application for managing a taxi booking system. The application allows users to: <br/>

1. Add taxis to the system
2. Book taxis
3. Print details of all taxis
4. Add new route
5. Print a taxi's booking history by taxi ID
6. Automatically free occupied taxis using threading after the journey's travel time elapses.

<h2>Features</h2>
<b>Add Taxis</b>
<pre>Allows the addition of new taxis to the system. Each taxi is initialized at station 'A' and is free to take new bookings.</pre>

<b>Book Taxis</b>
<pre>Books a taxi for a specified route and ensures that if no taxis are available at the starting station, the system allocates the nearest available taxi. If multiple taxis are available, the one with the lowest earnings is prioritized.</pre>

<b>Print All Taxis</b>
<pre>Displays the current status of all taxis, including their: </br>
ID
Status (free or occupied)
Total earnings
Station
</pre>

<b>Add a Route</b>
<pre>Dynamically adds a new route to the system. Routes are represented as stations (e.g., 'A', 'B', 'C', etc.), with a fixed distance of 15 km between consecutive stations.</pre>

<b>Print a Taxi's Booking History</b>
<pre>Prints the entire booking history of a specific taxi, identified by its unique taxi ID. This includes details like pickup point, drop point, pickup time, and fare for each booking.</pre>

<b>Free Occupied Taxis</b>

<pre>Utilizes Python threads to automatically free taxis after their travel time has elapsed. Travel times are based on the route: <br/>

A to B: 30 seconds

A to C: 60 seconds

A to D: 90 seconds

And so on...
</pre>
