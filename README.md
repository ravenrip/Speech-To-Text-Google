# Speech-To-Text-Google

The project was created initial by using the 'Running the Speech to Text Google samples' - codelabs
<https://codelabs.developers.google.com/codelabs/cloud-speech-text-python3/#0>

Also asked ChatGPT how to do it locally with this question:
*"How do I setup my windows vscode environment to support a python project that uses google service account"*

**TODO:**
Create a new file called os_environ_util.py
This file will contain the following code:

```python
    import io
    import os

    # setting Google credentials
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"
    ] = "[PATH TO GOOGLE SERVICE AUTHENTICATION JSON FILE]"

```

Please note that this code assumes that you have already set up the necessary authentication and authorization for accessing the Google Cloud Storage API. You can find more information about this in the documentation for the google-auth and google-api-python-client libraries.
