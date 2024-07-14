# Traffic Light Simulation: Determine the action (stop, ready, go) based on the current state of a traffic light.

traffic_light=input("Tell me about traffic light color \n").strip().capitalize()

if traffic_light=="Red":
    Action="Stop"
elif traffic_light=="Yellow":
    Action="Ready"
elif traffic_light=="Green":
    Action="Go"
else:
    Action="You have provide wrong traffic light color"

print(Action)