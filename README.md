# CodeAlpha_DataRedundancyRemoval

A Flask-based Data Redundancy Removal System that stores only validated and unique data entries in MongoDB.

## ✅ Features
- Validates incoming data format
- Checks for duplicates using SHA-256 hashing
- Stores only unique data in MongoDB
- REST API for data submission

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/CodeAlpha_DataRedundancyRemoval.git
cd CodeAlpha_DataRedundancyRemoval
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start MongoDB
Make sure MongoDB is running on your local machine.

### 4. Run Flask App
```bash
python app.py
```

### 5. Test API (Example using curl)
```bash
curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @sample_input.json
```

## 📁 API Response Examples

| Input                          | Response                         |
|--------------------------------|----------------------------------|
| Valid & unique data            | "Data inserted successfully"     |
| Duplicate data                 | "Duplicate data found"           |
| Invalid or missing fields      | "Invalid data format"            |

---