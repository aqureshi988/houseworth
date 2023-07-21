import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_location_names():
    global __locations
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts..")
    global __data_columns
    global __locations

    with open("./artifacts/columns2.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[8:]

    global __model
    with open("./artifacts/mumbai_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Done loading artifacts..")


def get_estimated_price(location, area, bhk, gym, lift, car_parking, security, playground, swimming_pool):
    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bhk
    x[2] = gym
    x[3] = lift
    x[4] = car_parking
    x[5] = security
    x[6] = playground
    x[7] = swimming_pool

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Kharghar', 2000, 1, 0, 0, 0, 0, 0, 0))
    print(get_estimated_price('Kharghar', 1000, 1, 1, 1, 1, 1, 1, 1))
    print(get_estimated_price('Andheri', 1000, 2, 0, 0, 0, 0, 0, 0))
    print(get_estimated_price('Mira Road East', 1000, 2, 0, 0, 0, 0, 0, 0))
