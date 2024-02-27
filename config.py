BASE_URL = "https://api.fastly.com"
WEBHOOK_URL = ""
DOWNLOADED_VCL_FILES = "downloaded_vcl_files/"
VCL_FILE_FOLDER = "upload_vcl_files/"
SAN_SERVICEID =""
 
DOWNLOAD_VCL_FILES = {
    "url": "/service/{service_id}/version/{version_id}/vcl",
    "method": "GET",
    "arguments": ["service_id", "version_id"],
}
 
DOWNLOAD_SINGLE_VCL_FILE = {
    "url": "/service/{service_id}/version/{version_id}/vcl/{vcl_name}/download",
    "method": "GET",
    "arguments": ["service_id", "version_id", "vcl_name"],
}
 
GET_SERVICES_DATA = {
    "url": "/service/{service_id}/version",
    "method": "GET",
    "arguments": ["service_id"],
}
 
ACTIVATE_SERVICE = {
    "url": "/service/{service_id}/version/{version_id}/activate",
    "method": "PUT",
    "arguments": ["service_id", "version_id"],
}
 
UPLOAD_VCL = {
    "url": "/service/{service_id}/version/{version_id}/vcl",
    "method": "POST",
    "arguments": ["service_id", "version_id"],
}
 
CLONE_SERVICE = {
    "url": "/service/{service_id}/version/{version_id}/clone",
    "method": "PUT",
    "arguments": ["service_id", "version_id"],
}
 
SERVICES_LIST = {"url": "/service", "method": "GET", "arguments": []}
 
UPDATE_VCL = {
    "url": "/service/{service_id}/version/{version_id}/vcl/{vcl_name}",
    "method": "PUT",
    "arguments": ["service_id", "version_id", "vcl_name"],
}
 
COMMENTS = {
    "url": "/service/{service_id}/version/{version_id}",
    "method": "PUT",
    "arguments": ["service_id", "version_id"],
}
 
VALIDATE_VERSION = {
    "url": "/service/{service_id}/version/{version_id}/validate",
    "method": "GET",
    "arguments": ["service_id", "version_id"],
}

LIST_SNIPPETS = {
    "url": "/service/{service_id}/version/{version_id}/snippet",
    "method": "GET",
    "arguments": ["service_id", "version_id"],
}

GET_SNIPPET_INFO = {
    'url': '/service/{service_id}/version/{version_id}/snippet/{snippet_name}',
    "method": "GET",
    "arguments": ["service_id", "version_id", "snippet_name"],
}

UPDATE_SNIPPET = {
    "url": "/service/{service_id}/version/{version_id}/snippet/{snippet_id}",
    "method": "PUT",
    "arguments": ["service_id", "version_id", "snippet_id"],
}

CREATE_SNIPPET = {
    "url": "/service/{service_id}/version/{version_id}/snippet",
    "method": "POST",
    "arguments": ["service_id", "version_id"],
}

DOWNLOAD_SNIPPET = {
    "url": "/service/{service_id}/version/{version_id}/snippet/{snippet_name}",
    "method": "DELETE",
    "arguments": ["service_id", "version_id", "snippet_name"],
}
