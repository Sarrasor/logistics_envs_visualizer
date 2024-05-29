from abc import ABC, abstractmethod
from io import BytesIO
import json
import logging
import pathlib
import gymnasium as gym

import logistics_envs
from logistics_envs.sim import LocationMode
from logistics_envs.envs.ride_hailing_env_config import RideHailingEnvConfig
import numpy as np

logger = logging.getLogger("logviz_backend.runner")


# TODO(dburakov): Use agents from the rl_logistics package
class Agent(ABC):
    @abstractmethod
    def act(self, observation: dict, info: dict) -> dict:
        pass


class QCommerceAgent(Agent):
    def act(self, observation: dict, info: dict) -> dict:
        n_couriers = len(observation["couriers_status"])
        action = {
            "action": [0] * n_couriers,
            "target": [0] * n_couriers,
            "location": [0.0, 0.0] * n_couriers,
        }
        assigned_orders = set()
        n_orders = observation["n_orders"]
        for courier_index in range(n_couriers):
            if observation["couriers_status"][courier_index] == 0:
                for order_index in range(n_orders):
                    if (
                        observation["orders_status"][order_index] == 0
                        and order_index not in assigned_orders
                    ):
                        action["action"][courier_index] = 2
                        action["target"][courier_index] = order_index
                        assigned_orders.add(order_index)
                        break

        return action


class RideHailingAgent(Agent):
    def act(self, observation: dict, info: dict) -> dict:
        n_drivers = len(observation["drivers_status"])
        n_stations = observation["charging_stations_location"].shape[0]
        action = {
            "action": [0] * n_drivers,
            "target": [0] * n_drivers,
            "location": [0.0, 0.0] * n_drivers,
        }

        assigned_rides = set()
        n_rides = observation["n_rides"]
        for driver_index in range(n_drivers):
            if observation["drivers_status"][driver_index] == 0:
                if n_stations >= 1 and observation["drivers_fuel"][driver_index][0] < 0.25:
                    station_index = np.random.randint(0, n_stations)
                    action["action"][driver_index] = 3
                    action["target"][driver_index] = station_index
                else:
                    for ride_index in range(n_rides):
                        if (
                            observation["rides_status"][ride_index] == 0
                            and ride_index not in assigned_rides
                        ):
                            action["action"][driver_index] = 2
                            action["target"][driver_index] = ride_index
                            assigned_rides.add(ride_index)
                            break
        return action


class Runner:
    def run(self, input_file: BytesIO, run_meta: dict, run_folder: pathlib.Path) -> None:
        logger.info("Creating environment")
        if run_meta["parameters"]["logistics_environment"] == "Q_COMMERCE":
            env, agent = self._create_q_commerce_env(input_file, run_meta, run_folder)
        elif run_meta["parameters"]["logistics_environment"] == "RIDE_HAILING":
            env, agent = self._create_ride_hailing_env(input_file, run_meta, run_folder)
        else:
            raise ValueError(
                f"Unknown logistics environment: {run_meta['parameters']['logistics_environment']}"
            )

        logger.info(f"Running environment: {env}")
        options = {
            "simulation_id": run_meta["id"],
        }
        observation, info = env.reset(options=options)
        done = False

        while not done:
            action = agent.act(observation, info)
            observation, reward, done, truncated, info = env.step(action)

        env.close()

        with open(run_folder / "run_report.json", "w") as file:
            json.dump(info, file, indent=4)

        logger.info(f"Finished environment run: {env}")

    def _create_q_commerce_env(
        self, input_file: BytesIO, run_meta: dict, run_folder: pathlib.Path
    ) -> tuple[gym.Env, Agent]:
        # order_data = pd.read_excel(input_file, skiprows=1, sheet_name="Orders")
        mode = LocationMode[run_meta["parameters"]["location_mode"]]
        config = {
            "mode": mode,
            "start_time": 100,
            "end_time": 300,
            "time_step": 1,
            "depot_location": [0.3, 0.5],
            "n_couriers": 3,
            "courier_speed": 0.05,
            "max_orders": 10,
            "order_window_size": 10,
            "order_pickup_time": 2,
            "order_drop_off_time": 3,
            "order_generation_start_time": 100,
            "order_generation_end_time": 110,
            "order_generation_probability": 0.25,
            "max_concurrent_orders": 1,
            "seed": 42,
        }
        env = gym.make("logistics_envs/QCommerce-v0", render_mode=None, **config)
        agent = QCommerceAgent()

        return env, agent

    def _create_ride_hailing_env(
        self, input_file: BytesIO, run_meta: dict, run_folder: pathlib.Path
    ) -> tuple[gym.Env, Agent]:
        mode = LocationMode[run_meta["parameters"]["location_mode"]]
        if run_meta["parameters"]["run_mode"] == "LIVE":
            render_mode = "human"
        else:
            render_mode = None

        config = RideHailingEnvConfig.from_file(
            file_path=str(run_folder / "input_file.xlsx"),
            mode=mode,
            render_mode=render_mode,
            routing_host="172.25.0.1:8002",
            render_host="172.25.0.1:8000",
        )

        env = gym.make("logistics_envs/RideHailing-v0", config=config)
        agent = RideHailingAgent()

        return env, agent
