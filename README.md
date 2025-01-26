# SUML

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

DTP (Delivery Time Predictor) is an application designed to improve the functioning of food delivery services. Its main purpose is to predict the time needed to deliver an order, from the moment it is placed by the customer to its arrival at the specified address.

## Running with a script

You can run this app with one of the `.sh` or `.bat` scripts depending on whether you want to run it with Docker or not.

- `Docker.sh` - run with Docker as a bash script
- `Docker.bat` - run with Docker as a bat script
- `Kedro.sh` - run with Kedro as a bash script
- `Kedro.bat` - run with Kedro as a bat script

## Streamlit hosting

This app can be accessed [here](https://czuberion-amf-srcsumlpipelinesappstreamlit-uxx1mn.streamlit.app/).

> [!NOTE]  
> Streamlit apps will go to sleep if not visited regularly, requiring a prompt to reinitialize them. [Docs](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation)

## Docker deployment

To run this project with Docker, you must:

1. Build the Docker Image

   ```
   docker build -t delivery-prediction-app .
   ```

2. Run the Docker Container

   ```
   docker run -p 8501:8501 delivery-prediction-app
   ```

3. Open the website in your browser on port 8501 or serve it.

## Dataset

The dataset used for this project is "[Food Delivery Time: A Multi-Factor Dataset](https://www.kaggle.com/datasets/gautamdeora7/food-delivery-time-a-multi-factor-dataset)".
