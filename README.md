# Steganography API using FastAPI

This API allows you to encode and decode messages using steganography techniques. It enables you to hide messages within images and send them via email. With this API, you can send secret messages by embedding them in images, making it difficult for unauthorized individuals to detect the hidden content.

## Features
Encode a message within an image using steganography.
Send an email with the encoded image containing the hidden message.
Decode a message from a steganographically encoded image.
## How to Run the API
Clone the repository to your local machine:

```
git clone https://github.com/your-username/steganography-api.git
```
Navigate to the project directory:

```
py -m pip install uvicorn
py -m pip install fastapi
py -m pip install python-multipart
py -m pip install Pillow
py -m pip install cryptography
```
### Set up the necessary configuration:

Open the config.py file and provide the required email credentials and SMTP server information.
Adjust any other configuration parameters according to your needs.
### Run the FastAPI server:

```
uvicorn main:app --reload
```
The API will now be accessible at http://localhost:8000. Documentation will be accessible at http://localhost:8000/docs 