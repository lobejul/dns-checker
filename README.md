# dns-checker
A simple cli tool for checking whether a domain is free or not.

## Installation
Please ensure that python3 and pip3 is installed.

Install the required python dependencies with the following command:
```bash
pip3 install -r requirements.txt
```

## Configuration
First of all create your custom settings file from the example.

```bash
mv settings.example.py settings.py
```

Then tailor the settings to your needs.
Important is the *watched_domains* property. It describes which domains are watched.

## Use
You can simply run the *main.py*-file without any parameters.
```bash
python3 main.py
```

You can automate the execution of the script with a crontab to make sure you stay up to date.
