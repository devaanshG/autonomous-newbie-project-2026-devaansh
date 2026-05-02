# controller.py
#
# Faulty decision logic for the 2026 Autonomous Newbie Project.
# Recruits will mainly modify this file.
#
# Sign convention:
# lane_offset_m:
#   negative = vehicle is left of lane center
#   positive = vehicle is right of lane center
#
# heading_error_deg:
#   negative = vehicle heading points left of desired direction
#   positive = vehicle heading points right of desired direction
#
# Steering output semantics:
# "LEFT" means command the vehicle to steer / move left.
# "RIGHT" means command the vehicle to steer / move right.
# Therefore:
# - positive lane_offset_m means vehicle is right of center, so LEFT is corrective
# - positive heading_error_deg means vehicle points right of desired direction, so LEFT is corrective

VALID_STEERING = {"LEFT", "RIGHT", "STRAIGHT"}
VALID_SPEED = {"ACCELERATE", "SLOW", "STOP"}

_state = "LANE_FOLLOW"   # "LANE_FOLLOW" | "AVOIDING"
_avoidance_side = "LEFT"


def controller(
    obstacle_distance_m,
    lane_offset_m,
    heading_error_deg,
    speed_mps,
    e_stop,
    left_clear,
    right_clear,
    sensor_valid
):
    """
    Returns:
        (steering, speed_action)

        steering:
            "LEFT", "RIGHT", "STRAIGHT"

        speed_action:
            "ACCELERATE", "SLOW", "STOP"
    """
    global _state, _avoidance_side

    DANGER_OBSTACLE_M = 2.0
    CAUTION_OBSTACLE_M = 5.0

    MILD_HEADING_DEG = 3.0
    LARGE_HEADING_DEG = 15.0

    MILD_OFFSET_M = 0.15
    LARGE_OFFSET_M = 0.40

    HIGH_SPEED_MPS = 3.0

    # -------- Critical overrides -------

    if not sensor_valid:
        _state = "LANE_FOLLOW"
        return "STRAIGHT", "STOP"

    if e_stop:
        _state = "LANE_FOLLOW"
        return "STRAIGHT", "STOP"

    # -------- AVOIDING state: commit to chosen side until obstacle is clear -------

    if _state == "AVOIDING":
        if obstacle_distance_m > CAUTION_OBSTACLE_M:
            _state = "LANE_FOLLOW"
        else:
            if not left_clear and not right_clear:
                return "STRAIGHT", "STOP"
            return _avoidance_side, "SLOW"

    # -------- LANE_FOLLOW state -------

    centered = abs(lane_offset_m) <= MILD_OFFSET_M
    small_heading_error = abs(heading_error_deg) <= MILD_HEADING_DEG

    if obstacle_distance_m <= DANGER_OBSTACLE_M:
        if not left_clear and not right_clear:
            return "STRAIGHT", "STOP"
        elif left_clear and not right_clear:
            _avoidance_side = "LEFT"
        elif right_clear and not left_clear:
            _avoidance_side = "RIGHT"
        else:
            _avoidance_side = "LEFT"
        _state = "AVOIDING"
        return _avoidance_side, "SLOW"

    elif obstacle_distance_m <= CAUTION_OBSTACLE_M:
        if not left_clear and not right_clear:
            return "STRAIGHT", "STOP"
        elif left_clear and not right_clear:
            return "LEFT", "SLOW"
        elif right_clear and not left_clear:
            return "RIGHT", "SLOW"
        else:
            return "STRAIGHT", "SLOW"

    elif speed_mps >= HIGH_SPEED_MPS:
        if heading_error_deg > LARGE_HEADING_DEG or lane_offset_m > LARGE_OFFSET_M:
            return "LEFT", "SLOW"
        elif heading_error_deg < -LARGE_HEADING_DEG or lane_offset_m < -LARGE_OFFSET_M:
            return "RIGHT", "SLOW"

    elif heading_error_deg > LARGE_HEADING_DEG or lane_offset_m > LARGE_OFFSET_M:
        return "LEFT", "ACCELERATE"

    elif heading_error_deg < -LARGE_HEADING_DEG or lane_offset_m < -LARGE_OFFSET_M:
        return "RIGHT", "ACCELERATE"

    elif heading_error_deg > MILD_HEADING_DEG or lane_offset_m > MILD_OFFSET_M:
        return "LEFT", "SLOW"

    elif heading_error_deg < -MILD_HEADING_DEG or lane_offset_m < -MILD_OFFSET_M:
        return "RIGHT", "SLOW"

    elif centered and small_heading_error:
        return "STRAIGHT", "ACCELERATE"

    return "STRAIGHT", "ACCELERATE"
