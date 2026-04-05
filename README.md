# Accuknox Django Assignment

## Django Signals

### Q1: Are Django signals synchronous?
Yes, Django signals are synchronous by default. They execute immediately when triggered.

### Q2: Do Django signals run in the same thread?
Yes, Django signals run in the same thread as the caller.

### Q3: Do Django signals run in the same database transaction?
Yes, Django signals run inside the same transaction. If an error occurs, all operations are rolled back.

### Test Endpoint
http://127.0.0.1:8000/test/

---

## Rectangle Class

A custom Rectangle class is implemented in rectangle.py.

Features:
- Takes length and breadth as input
- Calculates area and perimeter
- Supports iteration using __iter__

### Example Output:
Area: 50  
Perimeter: 30  
length: 10  
width: 5