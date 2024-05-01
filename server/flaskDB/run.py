from app import hub

flaskDB = hub()

if __name__ == "__main__":
    flaskDB.run(host='172.17.0.1', port=5000, debug=True)
