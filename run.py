import time

from app import create_app
from app.config import Config

if Config.SIMULATION_MODE == "slow-startup":
    print("Simulating slow startup (40 seconds)...")
    time.sleep(40)

app = create_app()

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=True)
