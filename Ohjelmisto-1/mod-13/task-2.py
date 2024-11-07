from flask import Flask, jsonify
import mysql.connector
from os import environ

app = Flask(__name__)

def get_airport_details(icao_code):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=environ['MYSQL_ROOT_PASSWORD'],
        database='flight_game',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, municipality
        FROM airport
        WHERE ident = %s
    """, (icao_code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"ICAO": icao_code, "Name": row[0], "Municipality": row[1]}
    else:
        return None

@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def get_airport(icao_code):
    details = get_airport_details(icao_code)
    if details:
        return jsonify(details)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)