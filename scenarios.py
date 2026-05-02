# scenarios.py
#
# Sign convention:
# lane_offset_m:
#   negative = vehicle is left of lane center
#   positive = vehicle is right of lane center
#
# heading_error_deg:
#   negative = vehicle heading points left of desired direction
#   positive = vehicle heading points right of desired direction

scenarios = [
    # ── Critical overrides ──────────────────────────────────────────────────────
    {
        "name": "Invalid Sensor",
        "inputs": {
            "obstacle_distance_m": 0.5,
            "lane_offset_m": 0.5,
            "heading_error_deg": 20.0,
            "speed_mps": 4.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": False
        }
    },
    {
        "name": "Emergency Stop — No Obstacle",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": True,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── Danger zone (distance <= 1.0 m) ─────────────────────────────────────────
    {
        "name": "Danger Obstacle — Both Sides Blocked",
        "inputs": {
            "obstacle_distance_m": 0.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.5,
            "e_stop": False,
            "left_clear": False,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Danger Obstacle — Left Clear",
        "inputs": {
            "obstacle_distance_m": 0.5,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Danger Obstacle — Right Clear",
        "inputs": {
            "obstacle_distance_m": 0.5,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": False,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Danger Obstacle — Both Sides Clear",
        "inputs": {
            "obstacle_distance_m": 0.9,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── Caution zone (1.0 m < distance <= 2.0 m) ────────────────────────────────
    {
        "name": "Caution Obstacle — Both Sides Blocked",
        "inputs": {
            "obstacle_distance_m": 1.5,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.5,
            "e_stop": False,
            "left_clear": False,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Caution Obstacle — Left Clear",
        "inputs": {
            "obstacle_distance_m": 1.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 3.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Caution Obstacle — Right Clear",
        "inputs": {
            "obstacle_distance_m": 1.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 3.0,
            "e_stop": False,
            "left_clear": False,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Caution Obstacle — Both Sides Clear",
        "inputs": {
            "obstacle_distance_m": 1.5,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── High speed (>= 3.0 m/s), no close obstacle ──────────────────────────────
    {
        "name": "High Speed — Large Right Error (heading)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.1,
            "heading_error_deg": 22.0,
            "speed_mps": 4.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "High Speed — Large Left Error (heading)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": -0.1,
            "heading_error_deg": -22.0,
            "speed_mps": 4.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "High Speed — Large Right Error (offset)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.5,
            "heading_error_deg": 5.0,
            "speed_mps": 3.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "High Speed — Large Left Error (offset)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": -0.5,
            "heading_error_deg": -5.0,
            "speed_mps": 3.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "High Speed — Centered (small errors)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.05,
            "heading_error_deg": 1.0,
            "speed_mps": 3.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── Low speed, no obstacle — large errors ────────────────────────────────────
    {
        "name": "Low Speed — Large Right Error (heading)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.1,
            "heading_error_deg": 20.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Low Speed — Large Left Error (heading)",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": -0.1,
            "heading_error_deg": -20.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Low Speed — Large Right Offset",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.5,
            "heading_error_deg": 2.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Low Speed — Large Left Offset",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": -0.5,
            "heading_error_deg": -2.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── Low speed, no obstacle — mild errors ─────────────────────────────────────
    {
        "name": "Low Speed — Mild Right Drift",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.25,
            "heading_error_deg": 5.0,
            "speed_mps": 2.2,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Low Speed — Mild Left Drift",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": -0.25,
            "heading_error_deg": -5.0,
            "speed_mps": 2.2,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    # ── Nominal — perfectly centred ───────────────────────────────────────────────
    {
        "name": "Clear Path, Centered",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Close Obstacle Ahead, No Safe Side",
        "inputs": {
            "obstacle_distance_m": 0.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 2.5,
            "e_stop": False,
            "left_clear": False,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Obstacle Ahead, Left Clear",
        "inputs": {
            "obstacle_distance_m": 1.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 3.0,
            "e_stop": False,
            "left_clear": True,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Obstacle Ahead, Right Clear",
        "inputs": {
            "obstacle_distance_m": 1.8,
            "lane_offset_m": 0.0,
            "heading_error_deg": 0.0,
            "speed_mps": 3.0,
            "e_stop": False,
            "left_clear": False,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Large Heading Error at Speed",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.1,
            "heading_error_deg": 22.0,
            "speed_mps": 4.5,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Emergency Stop Active",
        "inputs": {
            "obstacle_distance_m": 2.0,
            "lane_offset_m": -0.4,
            "heading_error_deg": -12.0,
            "speed_mps": 3.0,
            "e_stop": True,
            "left_clear": True,
            "right_clear": False,
            "sensor_valid": True
        }
    },
    {
        "name": "Obstacle Plus Heading Conflict",
        "inputs": {
            "obstacle_distance_m": 1.7,
            "lane_offset_m": -0.2,
            "heading_error_deg": 18.0,
            "speed_mps": 3.5,
            "e_stop": False,
            "left_clear": False,
            "right_clear": True,
            "sensor_valid": True
        }
    },
    {
        "name": "Mild Drift, No Obstacle",
        "inputs": {
            "obstacle_distance_m": 999.0,
            "lane_offset_m": 0.25,
            "heading_error_deg": 5.0,
            "speed_mps": 2.2,
            "e_stop": False,
            "left_clear": True,
            "right_clear": True,
            "sensor_valid": True
        }
    }
]
