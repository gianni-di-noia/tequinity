import io

from google.cloud import vision
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "cdn-dinoia-505c22038a4f.json",
    scopes=["https://www.googleapis.com/auth/cloud-vision"],
)


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts
