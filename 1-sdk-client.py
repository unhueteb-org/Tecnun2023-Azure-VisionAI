from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main():
    global cog_endpoint
    global cog_key

    try:
        # Get Configuration Settings
        # load_dotenv()
        # cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        # cog_key = os.getenv('COG_SERVICE_KEY')

        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                language = GetLanguage(userText)
                print('Language:', language)

    except Exception as ex:
        print(ex)

def GetLanguage(text):

    # Get Configuration Settings from environment variables instead of .env file
    cog_endpoint = os.environ['COG_SERVICE_ENDPOINT']
    cog_key = os.environ['COG_SERVICE_KEY']

    # Create client using endpoint and key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name

# Test 2: Test the GetLanguage function
def test_GetLanguage():
    # Arrange
    text = "This is a test of the GetLanguage function."
    expected = "English"

    # Act
    actual = GetLanguage(text)

    # Assert
    assert actual == expected

if __name__ == "__main__":
    main()