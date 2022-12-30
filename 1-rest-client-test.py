#pytest for the GetLanguage function

#import the GetLanguage function from 1-rest-client.py
import os
import importlib
restclient=importlib.import_module('1-rest-client')


# Test 1: Test the GetLanguage function
def test_GetLanguage():
    # Arrange
    text = "This is a test of the GetLanguage function."
    expected = "English"

    # Act
    actual = restclient.GetLanguage(text)

    # Assert
    assert actual == expected   