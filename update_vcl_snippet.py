import argparse
from config import GET_SNIPPET_INFO, UPDATE_SNIPPET

from connector import FastlyConnector
import update_vcl_snippet

def main(api_key,service_id,  version_id=None):
    connector = FastlyConnector(api_key)    

    name = "my_dynamic_snippet_name"
    response = connector.do_request(
        config=GET_SNIPPET_INFO,
        service_id=service_id,
        version_id=version_id,
        snippet_name=name
    )
    if response.status_code == 200:
        print("we have successfully got the snippet id we will use this to update the snippet content")
        response = connector.do_request(
            config=UPDATE_SNIPPET,
            service_id=service_id,
            version_id=version_id,
            snippet_id=response.json()['id'],
            data=dict(content='if ( req.url ) {\n set req.http.my-snippet-test-header = \"affirmative\";\n}')
        ) 
    print(response.json())


if __name__ == "__main__":
    main(
        service_id='22LPoUbQohLtn2eRGcv1vY',
        version_id='7',
        api_key='Jt5U7L6mUlv6DiWEpFeg3nHWnRZm0M8h'
    )

