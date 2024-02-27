import argparse
from config import LIST_SNIPPETS

from connector import FastlyConnector

def main(api_key,service_id,  version_id=None):
    connector = FastlyConnector(api_key)    
    response = connector.do_request(
        config=LIST_SNIPPETS,
        service_id=service_id,
        version_id=version_id
    )
    print(response)
    print(response.json())
if __name__ == "__main__":
    main(
        service_id='22LPoUbQohLtn2eRGcv1vY',
        version_id='7',
        api_key='Jt5U7L6mUlv6DiWEpFeg3nHWnRZm0M8h'
    )
