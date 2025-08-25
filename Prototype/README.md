# Prototype Setup and Usage

This document provides instructions on how to set up, configure, and run the AgapAI prototype.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hvillapando/AgapAI.git
    cd AgapAI/Prototype
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file contains:
    ```
    Flask==3.1.2
    numpy==2.3.2
    pandas==2.3.2
    joblib==1.5.1
    ```

## Configuration

Currently, there are no specific configuration steps required beyond installing the dependencies. The application is designed to run with its default settings.

## Running the Prototype

To start the Flask application, ensure your virtual environment is activated, then execute the following command from within the `Prototype` directory:

```bash
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
python app.py
```

Once the server is running, you can access the prototype by opening your web browser and navigating to the address provided in the terminal (usually `http://127.0.0.1:5000/`).
