FROM python:3.11.11-slim

# Install system dependencies
RUN apt -y update && apt install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
# CMD ["streamlit", "run", "src/suml/pipelines/app/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["kedro", "run"]