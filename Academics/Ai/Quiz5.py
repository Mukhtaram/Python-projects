import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperature = ctrl.Antecedent(np.arange(0, 100, 1), 'temperature')
cloud = ctrl.Antecedent(np.arange(0, 100, 1), 'cloud')
speed = ctrl.Consequent(np.arange(0, 100, 1), 'speed')

temperature.automf(3)
cloud.automf(3)


speed['low'] = fuzz.trimf(speed.universe, [0, 50, 75])
speed['medium'] = fuzz.trimf(speed.universe, [50, 75, 100])
speed['high'] = fuzz.trimf(speed.universe, [75, 100, 100])


rule1 = ctrl.Rule(temperature['poor'] | cloud['poor'], speed['low'])
rule2 = ctrl.Rule(temperature['average'] | cloud['average'],  speed['medium'])
rule3 = ctrl.Rule(temperature['good'] | cloud['good'], speed['high'])


driving_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

driving_speed = ctrl.ControlSystemSimulation(driving_speed_ctrl)

temperature_scale = float(input('How much is the temperature, on the scale between 0 and 100F? '))
cloud_cover_scale = float(input('How much is the cloud cover, on the scale betwenn 0 adn 100%? '))
driving_speed.input['temperature'] = temperature_scale
driving_speed.input['cloud'] = cloud_cover_scale

driving_speed.compute()

print (f'The model suggests you to drive your car {driving_speed.output["speed"]}%.')
driving_speed.view(sim=driving_speed)
plt.show()
