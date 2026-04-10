# BonjourLaFuite Daily Monitor

A small automation that checks the website **[https://bonjourlafuite.eu.org/](https://bonjourlafuite.eu.org/)** every day and sends newly listed data leak entries to a **Discord channel** via webhook.

The script parses the site's timeline and extracts:

* organization name
* stolen data descriptions
* source links

If the entry was published **yesterday**, it posts the information to Discord.

The workflow runs automatically using **GitHub Actions** every day.

---

# Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Built With](#built-with)
* [Installation](#installation)
* [Usage](#usage)
* [GitHub Actions Automation](#github-actions-automation)
* [Configuration](#configuration)
* [Example Output](#example-output)
* [Contributing](#contributing)
* [License](#license)

---

# About the Project

This project monitors the breach-reporting website **BonjourLaFuite** and automatically sends updates to a Discord server.

It is designed to:

* run automatically once per day
* detect **only the previous day's leaks**
* send formatted messages to Discord

The automation is implemented with **Python + GitHub Actions**.

---

# Features

* Daily monitoring of BonjourLaFuite
* Extracts organization names
* Lists stolen data
* Includes source links
* Automatically posts to Discord
* Fully automated via GitHub Actions
* Lightweight and easy to deploy

---

# Built With

* Python 3.11
* requests
* beautifulsoup4
* GitHub Actions

---

# Installation

Clone the repository:

```bash
git clone https://github.com/theobarrague/bonjourlafuite.git
cd bonjourlafuite
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the script manually:

```bash
python main.py
```

The script will:

1. Fetch the BonjourLaFuite timeline
2. Extract entries from **yesterday**
3. Send the results to the configured Discord webhook

---

# GitHub Actions Automation

The project includes a GitHub Actions workflow that runs the script **daily at 08:00 UTC**.

Workflow trigger:

```yaml
on:
  schedule:
    - cron: "0 8 * * *"
  workflow_dispatch:
```

This allows:

* automatic daily runs
* manual triggering from GitHub

---

# Configuration

You must configure a **Discord webhook URL**.

### 1. Create a Discord Webhook

In your Discord server:

```
Server Settings → Integrations → Webhooks → New Webhook
```

Copy the webhook URL.

---

### 2. Add the GitHub Secret

In your repository:

```
Settings → Secrets and variables → Actions → New repository secret
```

Create:

```
DISCORD_WEBHOOK_URL
```

Paste your webhook URL as the value.

---

# Example Output

Example message sent to Discord:

```
2026-04-09 — Example Organization

- Emails and passwords
- Customer database
- Internal documents

Sources:
- https://bonjourlafuite.eu.org/example-link
```

---

# Contributing

Contributions are welcome.

You can help by:

* improving parsing reliability
* adding filtering options
* adding logging
* supporting more data leak sources

Pull requests are welcome.

---

# License

This project is licensed under the MIT License.
