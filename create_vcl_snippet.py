import argparse
from config import LIST_SNIPPETS, CREATE_SNIPPET

from connector import FastlyConnector
import update_vcl_snippet

def main(api_key,service_id,  version_id=None):
    connector = FastlyConnector(api_key)    

    name = "my_dynamic_snippet_name"
    response = connector.do_request(
        config=CREATE_SNIPPET,
        service_id=service_id,
        version_id=version_id,data=dict(name=name, type='recv', dynamic=1, content='if ( req.url ) {\n set req.http.my-snippet-test-header = "true";')
    )
    if response.status_code == 429:
        print(f"duplicate snippet name {name}")
        update_vcl_snippet.main(
        config=CREATE_SNIPPET,
        service_id=service_id,
        version_id=version_id,data=dict(name=name, type='recv', dynamic=1, content='if ( req.url ) {\n set req.http.my-snippet-test-header = "true";')
    )
    print(response.json())
if __name__ == "__main__":
    main(
        service_id='22LPoUbQohLtn2eRGcv1vY',
        version_id='7',
        api_key='Jt5U7L6mUlv6DiWEpFeg3nHWnRZm0M8h'
    )


# dict(name="my_dynamic_snippet_name", type='recv', dynamic=1, content='if ( req.url ) {\n set req.http.my-snippet-test-header = "true";\n}')