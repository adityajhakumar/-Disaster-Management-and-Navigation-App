import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import osmnx as ox

# Initialize geolocator with a custom user agent
geolocator = Nominatim(user_agent="myGeocoder")

def get_coordinates(location_name):
    try:
        location = geolocator.geocode(location_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            st.error("Could not find location.")
            return None
    except Exception as e:
        st.error(f"Error in geocoding: {str(e)}")
        return None

def get_route(start_coords, end_coords):
    G = ox.graph_from_point(start_coords, dist=1000, network_type='drive')
    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])
    route = ox.shortest_path(G, start_node, end_node)
    return route, G


def display_disaster_management_options(city):
    disaster_options = {
    "Tsunami": [
        ("Life jackets", "https://www.amazon.com/s?k=life+jackets"),
        ("Emergency food supply", "https://www.amazon.com/s?k=emergency+food"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Portable water filter", "https://www.amazon.com/s?k=portable+water+filter"),
        ("Emergency radio", "https://www.amazon.com/s?k=emergency+radio"),
        ("Flashlight", "https://www.amazon.com/s?k=flashlight"),
        ("Whistle", "https://www.amazon.com/s?k=whistle"),
        ("Signal mirror", "https://www.amazon.com/s?k=signal+mirror"),
        ("Portable charger", "https://www.amazon.com/s?k=portable+charger"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Water purification tablets", "https://www.amazon.com/s?k=water+purification+tablets"),
        ("Multi-tool", "https://www.amazon.com/s?k=multi+tool"),
        ("Survival guide", "https://www.amazon.com/s?k=survival+guide"),
        ("Emergency shelter", "https://www.amazon.com/s?k=emergency+shelter"),
        ("Fishing gear", "https://www.amazon.com/s?k=fishing+gear")
    ],
    "Zombie Apocalypse": [
        ("Canned food", "https://www.amazon.com/s?k=canned+food"),
        ("Self-defense tools", "https://www.amazon.com/s?k=self-defense+tools"),
        ("Hiking boots", "https://www.amazon.com/s?k=hiking+boots"),
        ("Survival knife", "https://www.amazon.com/s?k=survival+knife"),
        ("Portable camping stove", "https://www.amazon.com/s?k=camping+stove"),
        ("Water purification system", "https://www.amazon.com/s?k=water+purification+system"),
        ("Tactical flashlight", "https://www.amazon.com/s?k=tactical+flashlight"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Multi-tool", "https://www.amazon.com/s?k=multi+tool"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Firestarter kit", "https://www.amazon.com/s?k=firestarter+kit"),
        ("Rope and cordage", "https://www.amazon.com/s?k=rope+and+cordage"),
        ("Signal mirror", "https://www.amazon.com/s?k=signal+mirror"),
        ("Camping gear", "https://www.amazon.com/s?k=camping+gear"),
        ("Portable solar charger", "https://www.amazon.com/s?k=solar+charger")
    ],
    "Alien Invasion": [
        ("Emergency food supply", "https://www.amazon.com/s?k=emergency+food"),
        ("Portable shelter", "https://www.amazon.com/s?k=portable+shelter"),
        ("Flashlight", "https://www.amazon.com/s?k=flashlight"),
        ("Signal mirror", "https://www.amazon.com/s?k=signal+mirror"),
        ("Radio", "https://www.amazon.com/s?k=radio"),
        ("Survival guide", "https://www.amazon.com/s?k=survival+guide"),
        ("Water purification tablets", "https://www.amazon.com/s?k=water+purification+tablets"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Canned food", "https://www.amazon.com/s?k=canned+food"),
        ("Multi-tool", "https://www.amazon.com/s?k=multi+tool"),
        ("Tactical gear", "https://www.amazon.com/s?k=tactical+gear"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Whistle", "https://www.amazon.com/s?k=whistle"),
        ("Portable charger", "https://www.amazon.com/s?k=portable+charger"),
        ("Hiking backpack", "https://www.amazon.com/s?k=hiking+backpack")
    ],
    "Flooding": [
        ("Sandbags", "https://www.amazon.com/s?k=sandbags"),
        ("Emergency food supply", "https://www.amazon.com/s?k=emergency+food"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Water purification tablets", "https://www.amazon.com/s?k=water+purification+tablets"),
        ("Flashlight", "https://www.amazon.com/s?k=flashlight"),
        ("Emergency radio", "https://www.amazon.com/s?k=emergency+radio"),
        ("Whistle", "https://www.amazon.com/s?k=whistle"),
        ("Portable charger", "https://www.amazon.com/s?k=portable+charger"),
        ("Waterproof storage bins", "https://www.amazon.com/s?k=waterproof+storage+bins"),
        ("Life jackets", "https://www.amazon.com/s?k=life+jackets"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Tactical gear", "https://www.amazon.com/s?k=tactical+gear"),
        ("Fishing gear", "https://www.amazon.com/s?k=fishing+gear"),
        ("Emergency shelter", "https://www.amazon.com/s?k=emergency+shelter"),
        ("Boat or kayak", "https://www.amazon.com/s?k=boat")
    ],
    "Asteroid Impact": [
        ("Emergency food supply", "https://www.amazon.com/s?k=emergency+food"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Survival gear", "https://www.amazon.com/s?k=survival+gear"),
        ("Water purification tablets", "https://www.amazon.com/s?k=water+purification+tablets"),
        ("Flashlight", "https://www.amazon.com/s?k=flashlight"),
        ("Emergency radio", "https://www.amazon.com/s?k=emergency+radio"),
        ("Portable shelter", "https://www.amazon.com/s?k=portable+shelter"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Signal mirror", "https://www.amazon.com/s?k=signal+mirror"),
        ("Tactical gear", "https://www.amazon.com/s?k=tactical+gear"),
        ("Multi-tool", "https://www.amazon.com/s?k=multi+tool"),
        ("Portable charger", "https://www.amazon.com/s?k=portable+charger"),
        ("Canned food", "https://www.amazon.com/s?k=canned+food"),
        ("Hiking gear", "https://www.amazon.com/s?k=hiking+gear"),
        ("Waterproof storage bins", "https://www.amazon.com/s?k=waterproof+storage+bins")
    ],
    "Nuclear War": [
        ("Emergency food supply", "https://www.amazon.com/s?k=emergency+food"),
        ("First aid kit", "https://www.amazon.com/s?k=first+aid+kit"),
        ("Portable shelter", "https://www.amazon.com/s?k=portable+shelter"),
        ("Radiation detection kit", "https://www.amazon.com/s?k=radiation+detection+kit"),
        ("Emergency blanket", "https://www.amazon.com/s?k=emergency+blanket"),
        ("Water purification tablets", "https://www.amazon.com/s?k=water+purification+tablets"),
        ("Tactical gear", "https://www.amazon.com/s?k=tactical+gear"),
        ("Flashlight", "https://www.amazon.com/s?k=flashlight"),
        ("Signal mirror", "https://www.amazon.com/s?k=signal+mirror"),
        ("Whistle", "https://www.amazon.com/s?k=whistle"),
        ("Portable charger", "https://www.amazon.com/s?k=portable+charger"),
        ("Canned food", "https://www.amazon.com/s?k=canned+food"),
        ("Multi-tool", "https://www.amazon.com/s?k=multi+tool"),
        ("Fishing gear", "https://www.amazon.com/s?k=fishing+gear"),
        ("Survival guide", "https://www.amazon.com/s?k=survival+guide")
    ]


}
    

    for disaster, gear in disaster_options.items():
        st.subheader(f"Survival Gear for {disaster}:")
        for item, link in gear:
            st.write(f"- [{item}]({link})")

# Initialize session state for downloaded routes
if 'downloaded_routes' not in st.session_state:
    st.session_state.downloaded_routes = []

# Sidebar for viewing downloaded routes
st.sidebar.header("Downloaded Routes")
if st.session_state.downloaded_routes:
    for route in st.session_state.downloaded_routes:
        st.sidebar.write(route)
else:
    st.sidebar.write("No routes downloaded yet.")

# Sidebar for disaster management
st.sidebar.header("Disaster Management")
input_city = st.text_input("Enter your city to get safer locations:")

# Main app title
st.title("Map Application")

# Input for starting location
start_location_name = st.text_input("Enter your starting location (full address or coordinates):")

# User input for destination
destination_type = st.radio("Choose input type:", ('Full Address', 'Coordinates'), key='destination_type_radio')

if destination_type == 'Full Address':
    destination_name = st.text_input("Enter full destination address:")
else:
    destination_coords_input = st.text_input("Enter destination coordinates (lat, lon):")

# Initialize map
map_center = (20.5937, 78.9629)  # Default center to India
m = folium.Map(location=map_center, zoom_start=5)

# Process starting location
start_coords = None
if start_location_name:
    start_coords = get_coordinates(start_location_name)
    if start_coords:
        folium.Marker(start_coords, popup="Start Location", icon=folium.Icon(color='blue')).add_to(m)

# Process destination
destination_coords = None
if destination_type == 'Full Address' and destination_name:
    destination_coords = get_coordinates(destination_name)
    if destination_coords:
        folium.Marker(destination_coords, popup="Destination").add_to(m)
elif destination_type == 'Coordinates' and destination_coords_input:
    try:
        lat, lon = map(float, destination_coords_input.split(','))
        destination_coords = (lat, lon)
        folium.Marker(destination_coords, popup="Destination").add_to(m)
    except ValueError:
        st.error("Invalid coordinates format. Please enter as 'lat, lon'.")

# Calculate and display route
if start_coords and destination_coords:
    route, G = get_route(start_coords, destination_coords)
    if route:
        route_lines = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]
        folium.PolyLine(locations=route_lines, color='red', weight=5).add_to(m)


# Display the map
st.subheader("Map")
folium_static(m)

# Download route feature
if start_coords and destination_coords:
    route_data = f"Start: {start_location_name}\n"
    if destination_type == 'Full Address':
        route_data += f"Destination: {destination_name}\nCoordinates: {start_coords}, {destination_coords}\n"
    else:
        route_data += f"Destination Coordinates: {destination_coords}\n"

    # Download button
    st.download_button("Download Route", data=route_data, file_name="route.txt", mime="text/plain")

    # Store the route in downloaded routes
    st.session_state.downloaded_routes.append(route_data)

# Start navigation option
if st.button("Start Navigation Without Downloading"):
    if start_coords and destination_coords:
        st.write("You can now navigate from your starting location to your destination!")
    else:
        st.error("Please provide valid starting and destination locations.")

# Display disaster management options if city input is provided
if input_city:
    display_disaster_management_options(input_city)
