import os
import dialogflow_v2 as dialogflow

from google.api_core.exceptions import InvalidArgument

def do_dialogflow_analysis(enquiry):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './SystemCode/project_key.json'

    # This field need to be changed to your actual dialogFlow project ID
    DIALOGFLOW_PROJECT_ID = 'oscres-wcbhwc'

    DIALOGFLOW_LANGUAGE_CODE = 'en'
    SESSION_ID = 'me'


    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    print('Session path: {}\n'.format(session))
    text_input = dialogflow.types.TextInput(text=enquiry, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        print(response)

    except InvalidArgument:
        raise
    except:
        raise Exception('Sorry I am not able to connect to the internet at the moment. Please try again later. Or use our recommendation system to help you.')
    return response
