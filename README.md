A simple dashboard application built within Streamlit:

![image](https://github.com/AkbarBunyad/Streamlit-Dashboard/assets/114834354/8312c7cf-6a73-4f42-b439-b0f11e59ee57)

## Features

- Display data from an Excel file
- Add new records to the Excel file
- Perform basic data analytics (total purchasing price, total selling price, and expected profit)
- Filter and view specific columns
- Cross-tabulation for category and type analysis

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AkbarBunyad/Streamlit-Dashboard.git
    cd Streamlit-Dashboard
    ```
    
2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run main.py
    ```

2. **Navigate to the provided URL (usually http://localhost:8501) to view the dashboard.**

## File Structure

```plaintext
Streamlit-Dashboard/
├── data.xlsx                 # The Excel file containing the data
├── main.py                   # The main Streamlit application script
├── template.py               # Contains the HTML and CSS for UI
├── requirements.txt          # The required Python packages
└── README.md                 # This README file
