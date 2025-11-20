# 🌎 Comunidad Connect

**Comunidad Connect** is an early demo web application designed to help the Latino community access emergency resources and translate English emergency instructions into simple, accessible Spanish.

> ⚠️ **Note:** This is a very early demo. Some words or phrases may not be translated perfectly, and not all ZIP codes or resources may be available.  
> 📍 **Current Coverage:** The ZIP codes included are the "hot spots" in the U.S. for Latino communities right now, including Northern Virginia (e.g., `20164`). 

---

## ✨ Features

- **Search for Local Resources by ZIP Code:**  
  Find food banks, legal aid, shelters, health clinics, and community centers in your area.  

- **Translate Text to Simple Spanish:**  
  Enter English text and receive an accessible Spanish translation along with key actions extracted from the text.

---

## 🛠 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.

---

### 🚀 Running the App

1. **Build the Docker image:**

```bash
docker build -t comunidadconnect:latest .

⚠️ Make sure no other containers are using port 5000. Stop extra containers with:
docker ps       # List running containers
docker stop <CONTAINER_ID>   # Stop any container using port 5000
Open your browser at:
http://localhost:5000

---

📝 How to Use

---

1️⃣ Search for Resources
Enter a ZIP code (e.g., 20164) in the search box.
Optionally select a category (Food, Legal, Shelter, Medical, Community).
Click Search to see local resources in your area.
Example Output:
{
  "count": 2,
  "resources": [
      {
          "zip": "20164",
          "name": "Ashburn Food Pantry",
          "category": "food",
          "address": "456 Community Way, Ashburn, VA 20164",
          "phone": "703-555-0202",
          "description": "Distributes free food and essentials to families in need."
      },
      {
          "zip": "20164",
          "name": "Northern Virginia Health Clinic",
          "category": "medical",
          "address": "101 Health Blvd, Ashburn, VA 20164",
          "phone": "703-555-0404",
          "description": "Free or low-cost medical care for uninsured residents."
      }
  ]
}

---

2️⃣ Translate Text
Type or paste English text into the translation box.
Click Translate.
View a simple Spanish translation and highlighted key actions.
Example:
"Evacuate and seek shelter." → "Evacuar y buscar refugio."

---

⚙ Notes
The app runs on port 5000 inside Docker.
Only one Docker container should be running at a time to avoid port conflicts.
ZIP codes are based on current "hot spots" in the U.S. Latino communities.
Early demo: Some words or phrases may not translate perfectly.






