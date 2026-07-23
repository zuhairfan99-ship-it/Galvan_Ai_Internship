# Google Sheet Integration using Python
This project demonstrates how to connect a Python application with **Google Sheets API** to perform various spreadsheet operations such as reading, writing, updating, and managing data programmatically.
## Features
- Connect Python with Google Sheets
- Authenticate using a Google Service Account
- Read data from Google Sheets
- Insert new rows
- Update existing records
- Delete records
- Search specific data
- Handle errors gracefully
- Automate spreadsheet operations
## Technologies Used
- Python 3
- Google Sheets API
- Google Cloud Console
- gspread
- google-auth
## Project Structure
```
Google_Sheet_Integration/
│
├── Google_Sheet_Integration.ipynb
├── credentials.json
├── README.md
└── requirements.txt
```
## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/Google_Sheet_Integration.git
```
Move into the project directory:
```bash
cd Google_Sheet_Integration
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Or install manually:
```bash
pip install gspread google-auth
```
## Google Sheets Setup
1. Create a project in Google Cloud Console.
2. Enable the **Google Sheets API**.
3. Create a **Service Account**.
4. Download the `credentials.json` file.
5. Share your Google Sheet with the Service Account email.
6. Place `credentials.json` inside the project folder.
## Usage
Open the Jupyter Notebook:
```bash
jupyter notebook Google_Sheet_Integration.ipynb
```
Run the notebook cells sequentially to connect with your Google Sheet and perform CRUD operations.
## Learning Outcomes
After completing this project, you will understand:
- Google Sheets API Authentication
- Service Account Configuration
- Reading and Writing Spreadsheet Data
- Updating Existing Records
- Deleting Records
- Data Automation using Python
- Exception Handling
## Requirements
- Python 3.10+
- Google Account
- Google Cloud Project
- Google Sheets API Enabled
- Internet Connection
## Author
**Zuha Irfan**  
**Bachelor of Software Engineering (BSE)**
<br>
**Fatima Jinnah Women University (FJWU)**
