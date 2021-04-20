# datameta_client_lib.RemoteProcedureCallsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_staged_files**](RemoteProcedureCallsApi.md#bulk_delete_staged_files) | **POST** /rpc/delete-files | Bulk-delete Staged Files
[**bulk_delete_staged_meta_data_sets**](RemoteProcedureCallsApi.md#bulk_delete_staged_meta_data_sets) | **POST** /rpc/delete-metadatasets | Bulk-delete Staged MetaDataSets
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

# **get_user_information**
> UserResponse get_user_information()

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
from datameta_client_lib.model.user_response import UserResponse
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

[**UserResponse**](UserResponse.md)

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

