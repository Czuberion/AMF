import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

# Set application width
st.set_page_config(layout="wide", page_title="Delivery Prediction App", page_icon="🚚")

# Load the saved model
MODEL_PATH = "data/models"
predictor = TabularPredictor.load(MODEL_PATH)

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/raw/Food_Time_Data_Set.csv")

data = load_data()

def main():
    st.title("Delivery Prediction App")

    st.subheader("Entered Data")

    # Placeholder for input data
    input_data_placeholder = st.empty()

    # Main part of the app: layout in four columns
    col1, col2, col3, col4 = st.columns([1,1,0.5,1])

    with col1:
        # Precipitation
        min_precip, max_precip = data["precipitation"].dropna().min(), data["precipitation"].dropna().max()
        precipitation = st.slider(
            "Precipitation", float(min_precip), float(max_precip), step=0.1, key="precipitation"
        )

        # Restaurant_latitude
        min_lat, max_lat = data["Restaurant_latitude"].dropna().min(), data["Restaurant_latitude"].dropna().max()
        restaurant_latitude = st.slider(
            "Restaurant Latitude", float(min_lat), float(max_lat), step=0.001, key="restaurant_latitude"
        )

        # Delivery_location_latitude
        min_delivery_lat, max_delivery_lat = data["Delivery_location_latitude"].dropna().min(), data["Delivery_location_latitude"].dropna().max()
        delivery_location_latitude = st.slider(
            "Delivery Location Latitude", float(min_delivery_lat), float(max_delivery_lat), step=0.001, key="delivery_location_latitude"
        )

        # Distance
        min_distance, max_distance = data["Distance"].dropna().min(), data["Distance"].dropna().max()
        distance = st.slider(
            "Distance", float(min_distance), float(max_distance), step=1.0, key="distance"
        )

    with col2:
        # Delivery_person_Age
        min_age, max_age = int(data["Delivery_person_Age"].dropna().min()), int(data["Delivery_person_Age"].dropna().max())
        delivery_person_age = st.slider(
            "Delivery Person Age", min_age, max_age, step=1, key="delivery_person_age"
        )

        # Restaurant_longitude
        min_long, max_long = data["Restaurant_longitude"].dropna().min(), data["Restaurant_longitude"].dropna().max()
        restaurant_longitude = st.slider(
            "Restaurant Longitude", float(min_long), float(max_long), step=0.001, key="restaurant_longitude"
        )

        # Delivery_location_longitude
        min_delivery_long, max_delivery_long = data["Delivery_location_longitude"].dropna().min(), data["Delivery_location_longitude"].dropna().max()
        delivery_location_longitude = st.slider(
            "Delivery Location Longitude", float(min_delivery_long), float(max_delivery_long), step=0.001, key="delivery_location_longitude"
        )

        # Delivery_person_Ratings
        delivery_person_ratings = st.slider(
            "Delivery Person Ratings", 1, 6, step=1, key="delivery_person_ratings"
        )

    with col3:
        # Type_of_order
        order_types = data["Type_of_order"].dropna().unique()
        type_of_order = st.radio("Type of Order", options=order_types, key="type_of_order")

        # Type_of_vehicle
        vehicle_types = data["Type_of_vehicle"].dropna().unique()
        type_of_vehicle = st.radio("Type of Vehicle", options=vehicle_types, key="type_of_vehicle")

        # Traffic_Level
        traffic_levels = ['Very Low','Low','Moderate','High','Very High']
        traffic_level = st.radio("Traffic Level", options=traffic_levels, key="traffic_level")

    with col4:
        # Weather_description
        weather_descriptions = data["weather_description"].dropna().unique()
        weather_description = st.selectbox(
            "Weather Description", weather_descriptions, key="weather_description"
        )

        # Delivery_person_ID
        delivery_person_ids = data["Delivery_person_ID"].dropna().unique()
        delivery_person_ids = [""] + list(delivery_person_ids)
        delivery_person_id = st.selectbox(
            "Delivery Person ID", delivery_person_ids, key="delivery_person_id"
        )

        # Temperature
        temperature = st.text_input("Temperature (°C)", value="0", key="temperature")
        try:
            temperature = int(temperature)
            if not -50 <= temperature <= 50:
                st.error("Temperature must be between -50 and 50.")
        except ValueError:
            st.error("Please enter a valid integer for Temperature.")

            # Create a DataFrame from the entered data
        input_data = pd.DataFrame({
            "Delivery_person_ID": [delivery_person_id],
            "Delivery_person_Age": [delivery_person_age],
            "Delivery_person_Ratings": [delivery_person_ratings],
            "Restaurant_latitude": [restaurant_latitude],
            "Restaurant_longitude": [restaurant_longitude],
            "Delivery_location_latitude": [delivery_location_latitude],
            "Delivery_location_longitude": [delivery_location_longitude],
            "Type_of_order": [type_of_order],
            "Type_of_vehicle": [type_of_vehicle],
            "temperature": [temperature],
            "humidity": [st.session_state.get("humidity", 0)],
            "precipitation": [precipitation],
            "weather_description": [weather_description],
            "Traffic_Level": [traffic_level],
            "Distance": [distance],
        })

        # Update the displayed data
        input_data_placeholder.write(input_data)

            # Prediction button
        st.write("---")
        if st.button("Predict"):
            prediction = predictor.predict(input_data)
            st.success(f"Predicted Delivery Time: {prediction[0]} minutes")



if __name__ == "__main__":
    main()
