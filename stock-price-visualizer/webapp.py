import os
from flask import Flask, jsonify, request, send_from_directory, abort

import db
from config import DEFAULT_DB_PATH

app = Flask(__name__, static_folder="static", static_url_path="/static")


def get_conn():
    conn = db.get_connection(os.environ.get("STOCK_DB_PATH", DEFAULT_DB_PATH))
    db.init_db(conn)
    return conn


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/symbols")
def api_symbols():
    conn = get_conn()
    symbols = db.list_symbols(conn)
    return jsonify(symbols)


@app.route("/api/prices")
def api_prices():
    symbols_param = request.args.get("symbols")
    start = request.args.get("start")
    end = request.args.get("end")
    if not symbols_param or not start or not end:
        abort(400, "symbols,start,end are required")
    symbols = [s.strip().upper() for s in symbols_param.split(",") if s.strip()]
    conn = get_conn()
    data = {}
    for sym in symbols:
        rows = db.query_prices(conn, sym, start, end)
        data[sym] = rows
    return jsonify({"start": start, "end": end, "data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=19000, debug=True)
