
import requests

def download_pdf(url, file_name, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)

# Define HTTP Headers
headers = {
    "User-Agent": "Chrome/51.0.2704.103",
}
# Define URL of a PDF
url = "https://www.phytojournal.com/archives/2019/vol8issue2/PartF/8-4-205-517.pdf"
# Define PDF file name
file_name = "file1.pdf"
# Download PDF
download_pdf(url, file_name, headers)

