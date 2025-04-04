import requests
import json

# from .logger import setup_logger
# print = setup_logger('request')

def response_handler(response, raw_response=False):

    if response == None:
        return {}, False

    result_json = {}
    success = False

    print(response.request.method, response.url, "status_code", response.status_code)
    if response.status_code < 200 and response.status_code > 300:
        print(response.request.method, response.url, "status_code", response.status_code)

    if response.status_code == 404:
        result_json = {"error": "Not Found"}
        success = False
        # return {"error": "Not Found"}, False
    elif response.status_code == 401 or response.status_code == 403:
        result_json = {"error": "Authentication Failed"}
        success = False
        # return {"error": "Authentication Failed"}, False
    elif response.status_code == 400:
        try:
            result_json = response.json()
            success = False
            # return response.json(), False
        except Exception as e:
            # return response.text, False
            result_json = response.text #double check  { "body": response.text} better
            success = False

    elif response.status_code > 400 and response.status_code < 500:
        result_json = response.json()
        success = False
        # return response.json(), False
    elif response.status_code >= 500:
        result_json = {"error": "Provider Server Down"}
        success = False
        # return {"error": "Provider Server Down"}, False
    elif response.status_code >= 204:
        result_json = {"message": "success"}
        success = True
        # return {"message": "success"}, True
    # elif raw_response:
    #     return response, True


    elif response.status_code >= 200 and response.status_code < 300:
        result_json = response.json()
        success = True
        # return response.json(), True

    if raw_response:
        return response, result_json, success

    return result_json, success

def raw_request(request: requests.Request) -> str:
    request = request.prepare()
    output = f"{request.method} {request.path_url} HTTP/1.1\r\n"
    output += '\r\n'.join(f'{k}: {v}' for k, v in request.headers.items())
    output += "\r\n\r\n"
    if request.body is not None:
        output += request.body.decode() if isinstance(request.body, bytes) else request.body
    return output

def make_get(url, headers=None, params=None, timeout=5):

    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    return response_handler(response)

def make_long_get(url, headers=None, params=None, timeout=30):
    print('make_long_get', url)
    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    return response_handler(response)

def make_raw_get(url, headers=None, params=None, timeout=5):

    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    return response_handler(response, raw_response=True)

def download_file(url, headers=None, params=None, random_name=True):
    # from utils.image import download_image_and_get_image_file_obj
    return False

def make_post(url, payload, headers=None, params=None, timeout=10, verify=True):
    response = requests.post(url, data=json.dumps(payload), headers=headers, params=params, timeout=timeout, verify=verify)
    return response_handler(response)

def make_raw_post(url, payload, headers=None, params=None, timeout=10, verify=True):
    data_payload = json.dumps(payload)
    if headers and headers.get('Content-Type') and "www-form-urlencoded" in headers.get('Content-Type'):
        data_payload = payload

    response = requests.post(url, data=data_payload, headers=headers, params=params, timeout=timeout, verify=verify)
    return response_handler(response, raw_response=True)

def make_post_form_data(url, payload, headers=None, params=None, timeout=10, verify=True):
    # import http.client
    # from utils.string import query_dict_to_query_string
    # # working
    # conn = http.client.HTTPSConnection("crm.filinglounge.com")
    # # payload = 'status=Interested'
    # headers = {
    #   'Content-Type': 'application/x-www-form-urlencoded'
    # }
    # conn.request("POST", "/api/social-media-leads.php", query_dict_to_query_string(payload), headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payload, headers=headers, params=params, timeout=timeout, verify=verify)
    # request = requests.Request("POST", url, data=payload, headers=headers, params=params)
    # print(raw_request(request))
    return response_handler(response)

def make_post_string(url, payload, headers=None, params=None, timeout=10, verify=True):
    # print(url, payload, headers, params)
    response = requests.post(url, data=payload, headers=headers, params=params, timeout=timeout, verify=verify)
    return response_handler(response)

def make_post_files(url, payload, headers=None, files=None, timeout=60):
    # print(payload, headers, files)
    # response = requests.post(url, data=payload, headers=headers, files=files, stream=True)
    response = requests.post(url, data=payload, headers=headers, files=files, timeout=timeout, stream=True)
    return response_handler(response)


def make_patch(url, payload, headers=None, params=None, timeout=20):
    response = requests.patch(url, data=json.dumps(payload), headers=headers, params=params, timeout=timeout)
    return response_handler(response)

def make_delete(url, headers=None):
    response = requests.delete(url, headers=headers)
    return response_handler(response)
