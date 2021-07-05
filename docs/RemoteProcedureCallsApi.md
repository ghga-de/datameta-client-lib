# datameta_client_lib.RemoteProcedureCallsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_staged_files**](RemoteProcedureCallsApi.md#bulk_delete_staged_files) | **POST** /rpc/delete-files | Bulk-delete Staged Files
[**bulk_delete_staged_meta_data_sets**](RemoteProcedureCallsApi.md#bulk_delete_staged_meta_data_sets) | **POST** /rpc/delete-metadatasets | Bulk-delete Staged MetaDataSets
[**get_file_url**](RemoteProcedureCallsApi.md#get_file_url) | **GET** /rpc/get-file-url/{id} | [Not RESTful]: Redirects to a temporary, pre-signed HTTP-URL for downloading a file.
[**get_user_information**](RemoteProcedureCallsApi.md#get_user_information) | **GET** /rpc/whoami | [Not RESTful]: Returns information about the authenticated user


# **bulk_delete_staged_files**
> bulk_delete_staged_files()

Bulk-delete Staged Files

Bulk-delete Staged Files.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import remote_procedure_calls_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.staged_files import StagedFiles
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = remote_procedure_calls_api.RemoteProcedureCallsApi(api_client)
    staged_files = StagedFiles(
        file_ids=[
            "file_ids_example",
        ],
    ) # StagedFiles | Provide a list of staged files to be deleted. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk-delete Staged Files
        api_instance.bulk_delete_staged_files(staged_files=staged_files)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling RemoteProcedureCallsApi->bulk_delete_staged_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staged_files** | [**StagedFiles**](StagedFiles.md)| Provide a list of staged files to be deleted. | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **bulk_delete_staged_meta_data_sets**
> bulk_delete_staged_meta_data_sets()

Bulk-delete Staged MetaDataSets

Bulk-delete Staged MetaDataSets.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import remote_procedure_calls_api
from datameta_client_lib.model.staged_meta_data_sets import StagedMetaDataSets
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = remote_procedure_calls_api.RemoteProcedureCallsApi(api_client)
    staged_meta_data_sets = StagedMetaDataSets(
        metadataset_ids=[
            "metadataset_ids_example",
        ],
    ) # StagedMetaDataSets | Provide a list of staged MetaDataSets to be deleted. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk-delete Staged MetaDataSets
        api_instance.bulk_delete_staged_meta_data_sets(staged_meta_data_sets=staged_meta_data_sets)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling RemoteProcedureCallsApi->bulk_delete_staged_meta_data_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staged_meta_data_sets** | [**StagedMetaDataSets**](StagedMetaDataSets.md)| Provide a list of staged MetaDataSets to be deleted. | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_file_url**
> FileUrl get_file_url(id)

[Not RESTful]: Redirects to a temporary, pre-signed HTTP-URL for downloading a file.

For the file with the given ID, this enpoint will redirect to a pre-signed HTTP URL for downloading the requested file. The pre-signed URL times out after a certain amount of time which can be configured with the \"expires\" query string. [Attention this endpoint is not RESTful, the result should not be cached.]

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import remote_procedure_calls_api
from datameta_client_lib.model.file_url import FileUrl
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = remote_procedure_calls_api.RemoteProcedureCallsApi(api_client)
    id = "id_example" # str | ID of the file
    expires = 1 # int | Minutes until the pre-signed URL will expire, defaults to 1 (optional) if omitted the server will use the default value of 1
    redirect = False # bool | If set to true, the endpoint will return a 307 response, otherwise a 200 response. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # [Not RESTful]: Redirects to a temporary, pre-signed HTTP-URL for downloading a file.
        api_response = api_instance.get_file_url(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling RemoteProcedureCallsApi->get_file_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [Not RESTful]: Redirects to a temporary, pre-signed HTTP-URL for downloading a file.
        api_response = api_instance.get_file_url(id, expires=expires, redirect=redirect)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling RemoteProcedureCallsApi->get_file_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the file |
 **expires** | **int**| Minutes until the pre-signed URL will expire, defaults to 1 | [optional] if omitted the server will use the default value of 1
 **redirect** | **bool**| If set to true, the endpoint will return a 307 response, otherwise a 200 response. | [optional] if omitted the server will use the default value of False

### Return type

[**FileUrl**](FileUrl.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**307** | Redirecting to the pre-signed URL of the file |  * location - Location to redirect to <br>  |
**400** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The specified file does not exist. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_information**
> WhoamiResponse get_user_information()

[Not RESTful]: Returns information about the authenticated user

Returns the ids, name, groupAdmin, siteAdmin, email and groupName attributes for the logged in user. [Attention this endpoint is not RESTful, the result should not be cached.]

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import remote_procedure_calls_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.whoami_response import WhoamiResponse
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = remote_procedure_calls_api.RemoteProcedureCallsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # [Not RESTful]: Returns information about the authenticated user
        api_response = api_instance.get_user_information()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling RemoteProcedureCallsApi->get_user_information: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WhoamiResponse**](WhoamiResponse.md)

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
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

