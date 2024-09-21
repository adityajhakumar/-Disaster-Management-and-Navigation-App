

# 🗺️ Disaster Management and Navigation App

![image](https://github.com/user-attachments/assets/0c59bdae-8590-443d-899f-fba54b660892)


## Overview
Welcome to the **Disaster Management and Navigation App**! This application helps users plan routes between locations while also offering essential survival gear recommendations for various disaster scenarios, like tsunamis, floods, and even zombie apocalypses 🧟. Users can download routes, view them in a 'Downloaded Routes' section, and receive survival kit suggestions based on the location.

### 🌟 Features:
- **Map-based Navigation**: Users can input a starting location and destination to calculate the shortest route. The app allows coordinates or addresses for inputs.
- **Route Downloading**: After the route is calculated, users can download it as a text file.
- **Disaster Management**: Input a city name, and the app provides safer locations and recommended survival gear based on different disaster scenarios.
- **Emergency Gear Recommendations**: Each disaster comes with a list of survival gear and links to purchase items online (e.g., Amazon).
- **Session Storage**: Downloaded routes are stored and can be viewed in the sidebar.

---

## 🎯 How It Works
1. **Start Location Input**: Enter your starting location (full address or coordinates).
2. **Destination**: Choose between entering a full address or coordinates for your destination.
3. **Route Calculation**: The app will calculate and display the shortest route on the map.
4. **Download Route**: Once the route is displayed, click the 'Download Route' button to save it as a text file.
5. **Disaster Management**: Enter a city name, and the app provides safer locations and emergency gear suggestions for various disaster scenarios.
6. **Navigation**: You can start navigation without downloading, allowing you to view the route without saving it.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or above
- `streamlit`, `folium`, `geopy`, `osmnx`, and `streamlit-folium` libraries. Install them using:

```bash
pip install streamlit folium geopy osmnx streamlit-folium
```

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg) <!-- Updated Python logo -->

### Clone the Repository

```bash
git clone https://github.com/adityajhakuma/disaster-management-app.git
cd disaster-management-app
```

### Run the App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```bash
disaster-management-app/
│
├── app.py                  # Main Streamlit app script
├── README.md               # This README file
├── requirements.txt        # List of Python dependencies
└── assets/                 # Folder for images and logos
```

---

## 🎨 App Layout
- **Map Interface**: Users can visualize routes between locations.
- **Sidebar**:
  - Displays downloaded routes.
  - Allows users to input a city for disaster management recommendations.
  
### Screenshots

![image](https://github.com/user-attachments/assets/81fc1275-b875-4826-807e-1df46f4b147b)
![image](https://github.com/user-attachments/assets/7062b5f4-d842-41e8-8594-8843d148c0c7)
![image](https://github.com/user-attachments/assets/e2b93ad3-44c7-4792-990b-2857c11608ad)


---

## 🔧 Customization
### Change the Disaster Gear Lists
- To modify the emergency gear for different scenarios, edit the `disaster_options` dictionary in the `display_disaster_management_options` function in the `app.py` file.

```python
disaster_options = {
    "Tsunami": [
        ("Life jackets", "https://www.amazon.com/s?k=life+jackets"),
        ...
    ],
    "Zombie Apocalypse": [
        ("Canned food", "https://www.amazon.com/s?k=canned+food"),
        ...
    ],
}
```

### Adding More Disasters
- Add new disaster scenarios and corresponding gear options by simply adding to the `disaster_options` dictionary.

---

## 🛠️ Future Enhancements
- **Integration with live GPS** for dynamic location updates.
- **Enhanced Safer Location Suggestions**: Use real-time disaster data to improve recommendations.
- **Multilingual Support**: Provide support for different languages based on user preference.

---

## 📄 License


This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Contributions
We welcome contributions from the community! Feel free to fork this repository, submit issues, and create pull requests. Here's how to contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## 🛡️ Security
If you discover any security issues or vulnerabilities, please send an email to [aditya](mailto:adityaneet2@gmail.com).

---

## ✨ Acknowledgements
Special thanks to the open-source libraries and tools that made this project possible:
- [Streamlit](https://streamlit.io/) ![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg)
- [Folium](https://python-visualization.github.io/folium/) ![Folium Logo](https://raw.githubusercontent.com/python-visualization/folium/main/docs/_static/logo-wide.png)
- [Geopy](https://geopy.readthedocs.io/en/stable/) ![Geopy Logo](https://geopy.readthedocs.io/en/stable/_images/geopy-logo.png)
- [OSMNx](https://osmnx.readthedocs.io/en/stable/) ![OSMNx Logo](https://osmnx.readthedocs.io/en/stable/_static/logo.png)

---

🚀 Happy Navigating and Stay Safe! 🌍

