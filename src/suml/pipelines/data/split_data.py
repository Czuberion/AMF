from sklearn.model_selection import train_test_split


def split_data(data, parameters):

    # Declare columns
    x = data.drop(columns=["TARGET"])
    y = data["TARGET"]

    # Split data
    x_train, x_temp, y_train, y_temp = train_test_split(
        x, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    x_dev, x_test, y_dev, y_test = train_test_split(
        x_temp, y_temp, test_size=0.5, random_state=parameters["random_state"]
    )

    return x_train, x_dev, x_test, y_train, y_dev, y_test
