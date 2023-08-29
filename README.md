# 📊 Google Sheets to CSV GitHub Action Template

This repository provides a GitHub Actions template to automatically export data from a Google Sheet to a CSV file and commit the changes to your GitHub repository. This is especially useful for projects that rely on data from Google Sheets and want to keep their repository updated with the latest data.

## 🌟 Features:

* 📝 Automated export of Google Sheet data to CSV.
* 🚀 Commit and push changes to the repository.
* ⏰ Schedule regular data pulls using cron syntax.

## 🚀 Getting Started:

### 1️⃣ Create Your Own Copy:

To use this template:

* Click on the `Use this template` button on the main page of this repository.
* Provide a name for your new repository and click `Create repository from template`.

### 2️⃣ Configure Secrets:

In your newly created repository:

* Navigate to `Settings` ➡️ `Secrets`.
* Add the following secrets:
  * `SHEET_ID`: The ID of your Google Sheet. (Hint: This can be found in the URL of your Google Sheet between `/spreadsheets/d/` and `/edit`).
  * `SERVICE_ACCOUNT_JSON`: The content of the service account JSON key (🔐 make sure to wrap the entire JSON in single quotes).
  * (Optional) `OUTPUT_FILENAME`: The desired name for the output CSV file. If not provided, the default will be `data.csv`.

### 3️⃣ Set Up Regular Pulls:

To set up regular pulls of information from the Google Sheet:

* Visit [crontab.guru](https://crontab.guru/) to help you understand and generate the cron syntax for your desired schedule. 📅
* Edit the `.github/workflows/sheet_to_csv.yml` file in your repository.
* Under the `on` key, replace or add the `schedule` key with your desired cron schedule. For example, to run the action every day at 9 AM, you would add:
 
    ```yaml
    schedule:
      - cron: '0 9 * * *'
    ```

## 📝 Final Notes:

Ensure that the Google Sheet is shared with the email address of the service account (found in the JSON key) to grant it access. 🔒

🎉 Enjoy automating your data workflow and keeping your repository up-to-date with the latest data from your Google Sheet!
