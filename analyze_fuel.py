import pandas as pd
import joblib

# Load the encoders
encoders = joblib.load('encoders.pkl')

print('Ship Types in training data:')
for i, ship_type in enumerate(encoders['SHIP_TYPE_ID'].classes_):
    print(f'{i}: {ship_type}')

print('\nFuel Types:')
print('FUEL_TYPE1 = HFO (Heavy Fuel Oil)')
print('FUEL_TYPE2 = Diesel')

print('\n' + '='*60)
print('Please specify which fuel types each ship type can use:')
print('='*60)
for ship_type in encoders['SHIP_TYPE_ID'].classes_:
    print(f'{ship_type}: ?')
