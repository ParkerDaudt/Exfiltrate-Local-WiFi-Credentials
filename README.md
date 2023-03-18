## Wi-Fi Profile Exporter

This script exports the Wi-Fi profiles with their passwords from a Windows machine and sends them to a webhook URL.

## Code Overview

1. Import required modules.

   - Import `subprocess`, `os`, `sys`, `requests`, and `xmltodict`.

2. Define the webhook URL and create a payload dictionary.

   - Set `url` to the target webhook URL.
   - Create a payload dictionary with a 'WAP' key, and an empty list as its value.

3. Run the 'netsh' command to export Wi-Fi profiles with passwords.

   - Use the `subprocess.run()` method to run the 'netsh' command, capturing its output.

4. Print the command output and get the current working directory.

   - Print the output of the 'netsh' command.
   - Store the current working directory path in the `path` variable.

5. Process the exported Wi-Fi profiles.

   - Iterate over the files in the current working directory.
   - If a file has a name starting with "Wi-Fi" and ending with ".xml":
     - Open the file and parse its content as an XML document using `xmltodict.parse()`.
     - Close the opened file.
     - Append a string containing the access point name and password to the 'WAP' key in the payload dictionary.
     - (Optional) Uncomment `os.remove(filename)` to delete the XML file after processing.

6. Check if any Wi-Fi profiles have been found.

   - If there is at least one Wi-Fi profile in the payload, print a message indicating that Wi-Fi profiles have been found.
   - If there are no Wi-Fi profiles in the payload, print a message indicating that no Wi-Fi profiles were found and exit the script.

7. Prepare the final payload and send it to the webhook URL.

   - Create an empty string called `final_payload`.
   - Iterate over the 'WAP' key in the payload dictionary, appending each access point name and password string to `final_payload`.
   - Send a POST request to the webhook URL with the `final_payload` as data.

