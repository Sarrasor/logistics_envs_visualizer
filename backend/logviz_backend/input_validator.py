from io import BytesIO

import pandas as pd

from logviz_backend.schema import InputValidationResponse


class InputValidator:
    def validate(self, input_file: bytes) -> InputValidationResponse:
        input_file_data = BytesIO(input_file)
        bounds = {"min": {"lat": 90.0, "lon": 180.0}, "max": {"lat": -90.0, "lon": -180.0}}
        workers = []
        service_stations = []
        orders = []

        rides_data = pd.read_excel(input_file_data, sheet_name="rides")
        for _, row in rides_data.iterrows():
            self._update_bounds(bounds, row["from_lat"], row["from_lon"])
            self._update_bounds(bounds, row["to_lat"], row["to_lon"])
            orders.append(
                {
                    "id": row["id"],
                    "client_id": row["client_id"],
                    "from_location": {
                        "lat": row["from_lat"],
                        "lon": row["from_lon"],
                    },
                    "to_location": {
                        "lat": row["to_lat"],
                        "lon": row["to_lon"],
                    },
                    "creation_time": row["creation_time"],
                    "time_window": [(row["creation_time"], row["creation_time"])],
                    "status": "CREATED",
                }
            )

        workers_data = pd.read_excel(input_file_data, sheet_name="drivers")
        for _, row in workers_data.iterrows():
            self._update_bounds(bounds, row["lat"], row["lon"])
            workers.append(
                {
                    "id": row["id"],
                    "location": {
                        "lat": row["lat"],
                        "lon": row["lon"],
                    },
                    "travel_type": row["travel_type"],
                    "speed": row["speed"],
                    "fuel": 1.0,
                    "path": None,
                    "remaining_path_index": None,
                    "status": "IDLE",
                    "color": "#ff0000",
                }
            )

        service_stations_data = pd.read_excel(input_file_data, sheet_name="charging_stations")
        for _, row in service_stations_data.iterrows():
            self._update_bounds(bounds, row["lat"], row["lon"])
            service_stations.append(
                {
                    "id": row["id"],
                    "location": {
                        "lat": row["lat"],
                        "lon": row["lon"],
                    },
                }
            )

        status = "ok"
        observation = {
            "current_time": 0,
            "bounds": bounds,
            "workers": workers,
            "orders": orders,
            "service_stations": service_stations,
        }
        response = {
            "status": status,
            "observation": observation,
        }
        return InputValidationResponse(**response)

    def _update_bounds(self, bounds: dict, lat, lon) -> None:
        bounds["min"]["lat"] = min(bounds["min"]["lat"], lat)
        bounds["min"]["lon"] = min(bounds["min"]["lon"], lon)
        bounds["max"]["lat"] = max(bounds["max"]["lat"], lat)
        bounds["max"]["lon"] = max(bounds["max"]["lon"], lon)
