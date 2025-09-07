# Ubuntu_Requests

## Project Description
Ubuntu-Inspired Image Fetcher Assignment

The Wisdom of Ubuntu: "I am because we are"

In the spirit of Ubuntu, which emphasizes community and sharing, this project is a Python script that connects to the global community of the internet, respectfully fetches shared image resources, and organizes them for later appreciation.

## Your Task
The script:
- Prompts the user for a URL containing an image
- Creates a directory called `Fetched_Images` if it doesn't exist
- Downloads the image from the provided URL
- Saves it to the `Fetched_Images` directory with an appropriate filename
- Handles errors gracefully, respecting that not all connections succeed

## Requirements
- Uses the `requests` library to fetch the image
- Checks for HTTP errors and handles them appropriately
- Creates the directory if it doesn't exist using `os.makedirs()` with `exist_ok=True`
- Extracts the filename from the URL or generates one if not available
- Saves the image in binary mode

## Ubuntu Principles Implemented
- **Community**: The program connects to the wider web community
- **Respect**: Errors are handled gracefully without crashing
- **Sharing**: Fetched images are organized for later sharing
- **Practicality**: The tool serves a real need by simplifying image fetching

## How to Run
1. Ensure Python is installed on your system.
2. Install the `requests` library if not already installed:

3. Run the Python script:

4. Follow the prompt to enter an image URL.

## Repository Structure

## Submission
Save your work in a GitHub repository named "Ubuntu_Requests" and submit the URL of this repository to complete the assignment.

---

*Inspired by Ubuntu's philosophy: "I am because we are."*

