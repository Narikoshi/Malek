# Feature 1

---

## Local inscription and connection via CMD

### 1️⃣ First step: Create a simple login system
To use my application, I needed a system of connection (login/registration).  
I used a **CSV file** as a local database.  
⚠️ It only works locally and is not secure, but for personal use it’s enough.

---

### 2️⃣ Before the graphical interface
Before implementing it graphically (with KivyMD), I tested the logic with a **Command Line (CMD) system**.

Steps:
- 📂 Create a Python file and import the necessary library (`csv`).
- ⌨️ Add an input to know if the user wants to **register (1)** or **log in (2)**.
- 🔄 Add conditions:  
  - If user writes **1 → Register**  
  - If user writes **2 → Log in**
- 📝 Add input fields to collect information (`name`, `password`) and store them as variables.
- 📤 Use `print()` to display outputs for the user.
- 📂 Create a csv file named `connexion.csv`.
- ⚙️ Create a function named `register()`.
  - Prompt the user to enter their `username` and `password`.
  - Store these values in variables named `information` for use in the registration or login process:
- 🔍 Check if the username already exists.
  - Before adding a new user, verify that the username is not already in the CSV.
    - If it exists → print a message like: "The username 'X' already exists."
    - Otherwise → add the new user and print a success message.
- 💾 Use the CSV library to write data.







---

### 3️⃣ Example screenshots

📌 **Import CSV library and setup:**

<img width="1247" height="65" alt="image" src="https://github.com/user-attachments/assets/088b1903-8daf-4ea8-8325-72578d2aca37" />

📌 **Register vs Login system (with conditions):**

<img width="1248" height="477" alt="image" src="https://github.com/user-attachments/assets/00c9716d-b9b7-4a5b-bc82-12f09ce832dd" />

📌 **csv file:**

<img width="1253" height="97" alt="image" src="https://github.com/user-attachments/assets/b53d16be-b5d0-48c7-9c2f-0ad9c437df1f" />

📌 **the Register function:**

<img width="1243" height="493" alt="image" src="https://github.com/user-attachments/assets/51e77313-b280-4916-ae17-c1d682e801d1" />


---

✅ Next step: I will transform this CMD system into a **graphical interface** using **KivyMD**

📘 What I learned: How to manage user input, conditions, and a CSV-based database.
