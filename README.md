# WiFi Password Extractor

This Python script extracts WiFi passwords from Windows systems and uploads them to a specified API endpoint or you can save it into a text file (by uncommenting the script)

## Description

This script utilizes `netsh` and `requests` modules to extract WiFi passwords from the Windows system. It first retrieves a list of WiFi profiles and then extracts passwords associated with those profiles. Finally, it uploads the data to a specified API endpoint.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library installed (`pip install requests`).

## Usage

1. Run the script by executing `python wifi_password_extractor.py`.
2. The script will extract WiFi passwords and attempt to upload them to the specified API endpoint.
3. Check the console for status messages.

## Configuration

- Ensure that the API endpoint URL is correctly set in the `URL` variable within the script.
- If you want to store the data in a text file, uncomment the corresponding code block in the script.

## Note

- This script may require administrative privileges to run.
- Use it responsibly and only on systems where you have permission to extract WiFi passwords.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the script, feel free to open an issue or submit a pull request.
