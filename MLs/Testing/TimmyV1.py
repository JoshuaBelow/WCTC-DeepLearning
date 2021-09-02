#    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
#    "heading": float,                      # agent's yaw in degrees
#    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track'] #Boolean
    heading = params['heading'] #Float
    is_left_of_center = params['is_left_of_center'] #Boolean
    steering_angle = params['steering_angle']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = -.5  # likely crashed/ close to off track

    if all_wheels_on_track:
        reward += .5
    
    if is_left_of_center:
        reward += .01

    if steering_angle < 60 > -60
        reward += .02

    return float(reward)