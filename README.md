# Automated Daily Email Report
![Screenshot 2024-08-22 205746](https://github.com/user-attachments/assets/ab0eff18-b68b-4a0b-bd8e-79c21a56dd95)
## Overview


The Automated Daily Email Report project simplifies the process of summarizing and emailing daily reports. Using Python and Natural Language Processing (NLP), it condenses lengthy reports into key highlights and sends them via email to specified recipients.

## Key Features

- **Automated Summarization:** Utilizes a pretrained NLP model to generate concise summaries of daily reports.
- **Email Automation:** Sends summarized reports through SMTP, supporting multiple recipients and attachments.
- **Secure Credential Management:** Uses a `.env` file to securely manage email credentials and server details.
- **Retry Mechanism:** Implements retries to ensure emails are sent even if initial attempts fail.
- **Logging:** Logs activities and errors for easy troubleshooting and auditing.

## Technologies Used

- Python
- Transformers (for NLP)
- python-dotenv
- smtplib
- logging

## Setup and Usage

### Prerequisites

- Python 3.6 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/automated-daily-email-report.git
   cd automated-daily-email-report
   ```

2. **Create and Activate a Virtual Environment:**

   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```sh
   pip install dotenv transformers torch
   ```

### Configuration

1. **Create a `.env` File:**

   In the root directory, create a file named `.env` and add your email configuration details:

   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   FROM_EMAIL=youremail@gmail.com
   FROM_PASSWORD=yourpassword
   ```

2. **Create a `report.txt` File:**

   Add your daily report content in a file named `report.txt` in the root directory.

### Running the Script

1. **Run the Script:**

   ```sh
   python extract_content.py
   ```

   This will summarize the content of `report.txt` and send an email with the summarized content.

### Setting Up Task Scheduler (Windows)

To automate the daily execution of the script, you can set up a task in Task Scheduler on Windows:

1. **Open Task Scheduler:**

   - Press `Win + R`, type `taskschd.msc`, and press Enter.

2. **Create a New Task:**

   - Click on "Create Basic Task" in the Actions pane.
   - Name the task (e.g., "Daily Email Report") and provide a description if desired.

3. **Set the Trigger:**

   - Choose "Daily" and click "Next."
   - Set the start date and time for when you want the script to run daily.

4. **Set the Action:**

   - Choose "Start a program" and click "Next."
   - Browse to the path of your Python executable (e.g., `C:\Users\yourusername\myenv\Scripts\python.exe`).
   - In the "Add arguments" field, enter the path to `extract_content.py` (e.g., `C:\path\to\your\project\extract_content.py`).

5. **Finish:**

   - Click "Finish" to create the task.


### `.env`

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FROM_EMAIL=youremail@gmail.com
FROM_PASSWORD=yourpassword
```

### `report.txt`

```txt
This is a sample daily report.
It contains various details about the day's activities and achievements.
- Item 1: Description of the first item.
- Item 2: Description of the second item.
- Summary: This is the summary of the daily report.
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

