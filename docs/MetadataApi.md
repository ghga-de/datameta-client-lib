# datameta_client_lib.MetadataApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meta_data_set**](MetadataApi.md#create_meta_data_set) | **POST** /metadatasets | Create a New MetaDataSet
[**get_meta_data_set**](MetadataApi.md#get_meta_data_set) | **GET** /metadatasets/{id} | Get Details for A MetaDataSet


# **create_meta_data_set**
> MetaDataSetResponse create_meta_data_set()

Create a New MetaDataSet

Create a new MetaDataSet

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
from datameta_client_lib.model.meta_data_set_response import MetaDataSetResponse
from datameta_client_lib.model.meta_data_set import MetaDataSet
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
    api_instance = metadata_api.MetadataApi(api_client)
    meta_data_set = MetaDataSet(
        record={},
    ) # MetaDataSet | Provide all properties for of one MetaDataSet. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New MetaDataSet
        api_response = api_instance.create_meta_data_set(meta_data_set=meta_data_set)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->create_meta_data_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_data_set** | [**MetaDataSet**](MetaDataSet.md)| Provide all properties for of one MetaDataSet. | [optional]

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
**200** | OK |  -  |
**400** | Validation Error |  -  |
**500** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_data_set**
> MetaDataSetResponse get_meta_data_set(id)

Get Details for A MetaDataSet

Get details for a metadataset.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
from datameta_client_lib.model.meta_data_set_response import MetaDataSetResponse
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
    api_instance = metadata_api.MetadataApi(api_client)
    id = "id_example" # str | ID of the MetaDataSet

    # example passing only required values which don't have defaults set
    try:
        # Get Details for A MetaDataSet
        api_response = api_instance.get_meta_data_set(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->get_meta_data_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the MetaDataSet |

### Return type

[**MetaDataSetResponse**](MetaDataSetResponse.md)

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
**403** | Forbidden |  -  |
**400** | Validation Error |  -  |
**500** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

