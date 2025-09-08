import requests

BASE = "http://127.0.0.1:8000"

# -----------------------------
# 1️⃣ Register users
# -----------------------------
users = [
    {"username": "user1", "email": "user1@example.com", "password": "test123"},
    {"username": "organizer1", "email": "org1@example.com", "password": "test123"},
    {"username": "admin1", "email": "admin1@example.com", "password": "test123"}
]

tokens = {}

for u in users:
    r = requests.post(f"{BASE}/users/", json=u)
    if r.status_code == 200:
        print(f"Registered {u['username']}")
    else:
        print(f"{u['username']} -> {r.json()}")

# -----------------------------
# 2️⃣ Login and get JWT tokens
# -----------------------------
for u in users:
    r = requests.post(f"{BASE}/users/login", data={"username": u["username"], "password": u["password"]})
    if r.status_code == 200:
        tokens[u["username"]] = r.json()["access_token"]
        print(f"{u['username']} logged in, token saved")
    else:
        print(f"Login failed for {u['username']} -> {r.json()}")

# -----------------------------
# 3️⃣ Admin assigns roles
# -----------------------------
headers = {"Authorization": f"Bearer {tokens['admin1']}"}
role_updates = [
    {"user_id": 2, "role": "organizer"},  # organizer1
    {"user_id": 3, "role": "admin"}       # admin1 (already)
]

for ru in role_updates:
    r = requests.put(f"{BASE}/users/{ru['user_id']}/role?role={ru['role']}", headers=headers)
    print(r.json())

# -----------------------------
# 4️⃣ Organizer creates an event
# -----------------------------
headers_org = {"Authorization": f"Bearer {tokens['organizer1']}"}
event_data = {"name": "Fishing Championship", "description": "Annual competition", "organizer_id": 2}
r = requests.post(f"{BASE}/events/", json=event_data, headers=headers_org)
print("Event creation:", r.json())

# -----------------------------
# 5️⃣ Admin creates a payment for user1
# -----------------------------
payment_data = {"user_id": 1, "event_id": 1, "amount": 50.0}
r = requests.post(f"{BASE}/payments/", json=payment_data, headers=headers)
print("Payment creation:", r.json())

# -----------------------------
# 6️⃣ User1 marks payment as paid
# -----------------------------
headers_user = {"Authorization": f"Bearer {tokens['user1']}"}
r = requests.put(f"{BASE}/payments/1/pay", headers=headers_user)
print("Payment paid:", r.json())
