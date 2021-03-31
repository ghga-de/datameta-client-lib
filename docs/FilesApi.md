# datameta_client_lib.FilesApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /files | Create a New File
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files/{id} | Delete Not-Submitted File
[**get_file**](FilesApi.md#get_file) | **GET** /files/{id} | Get Details for A File
[**update_file**](FilesApi.md#update_file) | **PUT** /files/{id} | Update File Details


# **create_file**
> FileUploadResponse create_file()

Create a New File

Creates a new empty file object. Attention: this endpoint does not take the file content for upload. Instead, it will respond with a presigned URL which you can use to upload (PUT) your file content.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import files_api
from datameta_client_lib.model.file_upload_response import FileUploadResponse
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.file_announcement import FileAnnouncement
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = datameta_client_lib.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datameta_client_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file_announcement = FileAnnouncement(
        name="name_example",
        checksum="checksum_example",
    ) # FileAnnouncement | Provide essential properties of the file that shall be uploaded (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New File
        api_response = api_instance.create_file(file_announcement=file_announcement)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_announcement** | [**FileAnnouncement**](FileAnnouncement.md)| Provide essential properties of the file that shall be uploaded | [optional]

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(id)

Delete Not-Submitted File

Delete File. Please note: This is only allowed if the File has not been part of a Submission, yet.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import files_api
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = datameta_client_lib.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datameta_client_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | ID of the File

    # example passing only required values which don't have defaults set
    try:
        # Delete Not-Submitted File
        api_instance.delete_file(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the File |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletion successful |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | File not found |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> FileResponse get_file(id)

Get Details for A File

Get details for a file.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import files_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.file_response import FileResponse
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = datameta_client_lib.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datameta_client_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | ID of the File

    # example passing only required values which don't have defaults set
    try:
        # Get Details for A File
        api_response = api_instance.get_file(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the File |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Either forbidden or the resource is not modifiable |  -  |
**404** | File not found |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileResponse update_file(id)

Update File Details

Update details for a File. E.g. to indicate that the File content has been uploaded (set contentUploaded=true). Please note: this only works for Files that have not been submitted, yet. Other file attributes (checksum and name) can only be updated until contentUploaded has been set to 'true'.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import files_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.file_response import FileResponse
from datameta_client_lib.model.file_update_request import FileUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = datameta_client_lib.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with datameta_client_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    id = "id_example" # str | ID of the File
    file_update_request = FileUpdateRequest(
        name="name_example",
        content_uploaded=True,
        checksum="checksum_example",
    ) # FileUpdateRequest | Provide properties of the file that shall be updated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update File Details
        api_response = api_instance.update_file(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update File Details
        api_response = api_instance.update_file(id, file_update_request=file_update_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the File |
 **file_update_request** | [**FileUpdateRequest**](FileUpdateRequest.md)| Provide properties of the file that shall be updated. | [optional]

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Either forbidden or the resource is not modifiable |  -  |
**404** | File not found |  -  |
**409** | Mismatch between uploaded data checksum and announced checksum |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

