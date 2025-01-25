from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def split_data(data, parameters):


    X = data[['Delivery_person_ID','Delivery_person_Age','Delivery_person_Ratings','Restaurant_latitude','Restaurant_longitude','Delivery_location_latitude','Delivery_location_longitude','Type_of_order','Type_of_vehicle','temperature','humidity','precipitation','weather_description','Traffic_Level','Distance']]
    Y = data['TARGET']

    X_train, X_temp, Y_train, Y_temp = train_test_split(
        X, Y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    X_dev, X_test, Y_dev, Y_test = train_test_split(
        X_temp, Y_temp, test_size=0.5, random_state=parameters["random_state"]
    )


    return X_train, X_dev, X_test, Y_train, Y_dev, Y_test
