# datameta_client_lib.ServicesApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_info**](ServicesApi.md#get_service_info) | **GET** /services | Get Services information
[**post_service**](ServicesApi.md#post_service) | **POST** /services | Create a new service.
[**put_service**](ServicesApi.md#put_service) | **PUT** /services/{id} | Update a specific service.
[**service_set_meta_datum**](ServicesApi.md#service_set_meta_datum) | **POST** /service-execution/{serviceId}/{metadatasetId} | Endpoint to store the result of a service execution for a single metadataset


# **get_service_info**
> Services get_service_info()

Get Services information

Get names and IDs for all services

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import services_api
from datameta_client_lib.model.services import Services
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
    api_instance = services_api.ServicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Services information
        api_response = api_instance.get_service_info()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->get_service_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Services**](Services.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service**
> ServiceResponse post_service()

Create a new service.

Create a new service.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import services_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.service_request import ServiceRequest
from datameta_client_lib.model.service_response import ServiceResponse
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
    api_instance = services_api.ServicesApi(api_client)
    service_request = ServiceRequest(
        name="name_example",
    ) # ServiceRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new service.
        api_response = api_instance.post_service(service_request=service_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->post_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_request** | [**ServiceRequest**](ServiceRequest.md)|  | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service**
> ServiceResponse put_service(id)

Update a specific service.

Update the name and/or the users of this service.  If the name, or the userIds are omitted, those will not be updated upon request. To remove all users, an empty array must be submitted for userIds.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import services_api
from datameta_client_lib.model.service_update_request import ServiceUpdateRequest
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.service_response import ServiceResponse
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
    api_instance = services_api.ServicesApi(api_client)
    id = "id_example" # str | ID of the service
    service_update_request = ServiceUpdateRequest(
        name="name_example",
        user_ids=[
            "user_ids_example",
        ],
    ) # ServiceUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a specific service.
        api_response = api_instance.put_service(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->put_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a specific service.
        api_response = api_instance.put_service(id, service_update_request=service_update_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->put_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the service |
 **service_update_request** | [**ServiceUpdateRequest**](ServiceUpdateRequest.md)|  | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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
**404** | Service does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_set_meta_datum**
> MetaDataSetResponse service_set_meta_datum(service_id, metadataset_id)

Endpoint to store the result of a service execution for a single metadataset

This endpoint is used to report the result of a service execution in the form of metadatum key - value pairs for the service-related metadata and corresponding files if file metadata are involved.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import services_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.meta_data_set_response import MetaDataSetResponse
from datameta_client_lib.model.service_execution import ServiceExecution
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
    api_instance = services_api.ServicesApi(api_client)
    service_id = "serviceId_example" # str | ID of the service
    metadataset_id = "metadatasetId_example" # str | ID of the metadataset
    service_execution = ServiceExecution(
        record={},
        file_ids=[
            "file_ids_example",
        ],
    ) # ServiceExecution | The `records` attribute of the request body must describe the result of the service execution in form of key/value pairs corresponding to the metadata associated with the service. The `fileIds` list must contain all file IDs of files referenced in values of file metadata. It can be empty (`[]`) but not `null` or missing. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to store the result of a service execution for a single metadataset
        api_response = api_instance.service_set_meta_datum(service_id, metadataset_id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->service_set_meta_datum: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint to store the result of a service execution for a single metadataset
        api_response = api_instance.service_set_meta_datum(service_id, metadataset_id, service_execution=service_execution)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServicesApi->service_set_meta_datum: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| ID of the service |
 **metadataset_id** | **str**| ID of the metadataset |
 **service_execution** | [**ServiceExecution**](ServiceExecution.md)| The &#x60;records&#x60; attribute of the request body must describe the result of the service execution in form of key/value pairs corresponding to the metadata associated with the service. The &#x60;fileIds&#x60; list must contain all file IDs of files referenced in values of file metadata. It can be empty (&#x60;[]&#x60;) but not &#x60;null&#x60; or missing. | [optional]

### Return type

[**MetaDataSetResponse**](MetaDataSetResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update successful |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The specified metadataset or service does not exist. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

