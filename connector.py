import datetime
import os
import requests
 
from config import BASE_URL, DOWNLOAD_VCL_FILES, GET_SERVICES_DATA
from exceptions import StatusError


class FastlyConnector:
    def __init__(self, api_key):
        self.api_key = api_key
 
    @property
    def headers(self):
        return {"Fastly-Key": self.api_key}
 
    def do_get_request(self, url):
        response = requests.get(BASE_URL + url, headers=self.headers)
        return response
 
    def do_post_request(self, url, **kwargs):
        response = requests.post(
            BASE_URL + url, headers=self.headers, data=kwargs.get("data")
        )
        import pdb;pdb.set_trace()
        return response
 
    def do_put_request(self, url, **kwargs):
        if kwargs.get("data"):
            response = requests.put(
                BASE_URL + url, headers=self.headers, data=kwargs.get("data")
            )
            return response
        response = requests.put(BASE_URL + url, headers=self.headers)
        return response
 
    def do_delete_request(self, url):
        response = requests.delete(BASE_URL + url, headers=self.headers)
        return response
 
    def do_request(self, config, **kwargs):
        _url = config.get("url")
        _method = config.get("method", "").upper()
        _arguments = config.get("arguments")
        final_url = self.format_the_url_with_data(_url, _arguments, **kwargs)
        if _method == "GET":
            _response = self.do_get_request(final_url)
 
        elif _method == "POST":
            _response = self.do_post_request(final_url, **kwargs)
 
        elif _method == "PUT":
            _response = self.do_put_request(final_url, **kwargs)
        elif _method == "DELETE":
            _response = self.do_delete_request(final_url)
        import pdb;pdb.set_trace()
        return self.status_checker(_response)
 
    @staticmethod
    def format_the_url_with_data(__url, __arguments, **kwargs):
        format_data = {}
 
        for _i in __arguments:
            format_data.update({_i: kwargs.get(_i)})
        formatted_url = __url.format_map(format_data)
        return formatted_url
 
    @staticmethod
    def dump_into_a_file(file_name, file_data):
        with open(file_name, "w") as file:
            file.write(file_data)
 
    @staticmethod
    def random_file_name_generator():
        basename = "vcl"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S%f")
        filename = (
            "_".join([basename, suffix]) + ".vlc"
        )  # e.g. 'vcl_210509_135017893702.vlc'
        return filename
 
    @staticmethod
    def status_checker(response):
        if response.status_code not in [200, 201, 409]:
            print(response.status_code)
            raise StatusError(response.content)
        return response