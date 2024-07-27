from colorama import Fore, Style
from flask import Flask, render_template, request, jsonify
import logging
from datetime import datetime
import time
app = Flask(__name__)

# logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


teams = {
    "127.0.0.1" : "TEAM-0",
}

start_time = datetime.now()

@app.route("/")
def index():
    client_ip = request.remote_addr
    return render_template("index.html", client_ip=client_ip)

@app.route("/submit", methods=["POST"])
def toggle():
    data = request.get_json()
    client_ip = data.get("ip")
    # difference = str(datetime.now()-start_time).split(":")
    # time_str = f"{int(difference[1])} minute(s) {difference[2]} seconds"
    print(f"Sumbission received from {Fore.GREEN} {teams.get(client_ip,client_ip)} {Style.RESET_ALL}, time taken {Fore.RED}{datetime.now()-start_time} {Style.RESET_ALL}")
    return jsonify(success=True, message="Submitted successfully", ip=client_ip)

@app.route("/master", methods=["GET"])
def master():
    client_ip = request.remote_addr
    return render_template("master.html", client_ip=client_ip)

@app.route("/reset", methods=["POST"])
def reset():
    global start_time
    data = request.get_json()
    client_ip = data.get("ip")
    start_time = datetime.now()
    print("\n"*10)
    print(f"{Fore.BLUE}Timer started.{Style.RESET_ALL}")
    return jsonify(success=True, message="Submitted successfully", ip=client_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

