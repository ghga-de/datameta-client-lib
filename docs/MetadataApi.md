# datameta_client_lib.MetadataApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meta_data_set**](MetadataApi.md#create_meta_data_set) | **POST** /metadatasets | Create a New MetaDataSet
[**create_meta_datum**](MetadataApi.md#create_meta_datum) | **POST** /metadata | Create a New MetaDatum
[**delete_metadata_set**](MetadataApi.md#delete_metadata_set) | **DELETE** /metadatasets/{id} | Delete Not-Submitted Metadataset
[**get_meta_data**](MetadataApi.md#get_meta_data) | **GET** /metadata | Get metadata definitions
[**get_meta_data_set**](MetadataApi.md#get_meta_data_set) | **GET** /metadatasets/{id} | Get Details for a MetaDataSet
[**update_meta_datum**](MetadataApi.md#update_meta_datum) | **PUT** /metadata/{id} | Update a MetaDatum


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
from datameta_client_lib.model.error_model import ErrorModel
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
    ) # MetaDataSet | Provide all properties for one MetaDataSet. (optional)

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
 **meta_data_set** | [**MetaDataSet**](MetaDataSet.md)| Provide all properties for one MetaDataSet. | [optional]

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
**401** | Unauthorized |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_meta_datum**
> create_meta_datum()

Create a New MetaDatum

Create a new MetaDatum. This is an administrative Endpoint that is not accessible for regular users.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.meta_datum import MetaDatum
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
    api_instance = metadata_api.MetadataApi(api_client)
    meta_datum = MetaDatum(
        name="name_example",
        regex_description="regex_description_example",
        long_description="long_description_example",
        example="example_example",
        reg_exp="reg_exp_example",
        date_time_fmt="date_time_fmt_example",
        is_mandatory=True,
        order=1,
        is_file=True,
        is_submission_unique=True,
        is_site_unique=True,
    ) # MetaDatum | Provide all properties for one MetaDatum. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New MetaDatum
        api_instance.create_meta_datum(meta_datum=meta_datum)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->create_meta_datum: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_datum** | [**MetaDatum**](MetaDatum.md)| Provide all properties for one MetaDatum. | [optional]

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
**204** | Metadatum added successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The specified metadataset does not exist. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_set**
> delete_metadata_set(id)

Delete Not-Submitted Metadataset

Delete File. Please note: This is only allowed if the metadataset has not been part of a Submission, yet.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
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
    api_instance = metadata_api.MetadataApi(api_client)
    id = "id_example" # str | ID of the Metadataset

    # example passing only required values which don't have defaults set
    try:
        # Delete Not-Submitted Metadataset
        api_instance.delete_metadata_set(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->delete_metadata_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Metadataset |

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
**403** | Either forbidden or the resource is not modifiable |  -  |
**404** | The specified metadataset does not exist. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_data**
> MetaDataResponse get_meta_data()

Get metadata definitions

Get the metadata definitions that are configured for this site.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.meta_data_response import MetaDataResponse
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

    # example, this endpoint has no required or optional parameters
    try:
        # Get metadata definitions
        api_response = api_instance.get_meta_data()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->get_meta_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MetaDataResponse**](MetaDataResponse.md)

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

# **get_meta_data_set**
> MetaDataSetResponse get_meta_data_set(id)

Get Details for a MetaDataSet

Get details for a metadataset.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.error_model import ErrorModel
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
        # Get Details for a MetaDataSet
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
**404** | The specified metadataset does not exist. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta_datum**
> update_meta_datum(id)

Update a MetaDatum

Update a MetaDatum. This is an administrative Endpoint that is not accessible for regular users.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import metadata_api
from datameta_client_lib.model.meta_datum import MetaDatum
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
    api_instance = metadata_api.MetadataApi(api_client)
    id = "id_example" # str | User ID
    meta_datum = MetaDatum(
        name="name_example",
        regex_description="regex_description_example",
        long_description="long_description_example",
        example="example_example",
        reg_exp="reg_exp_example",
        date_time_fmt="date_time_fmt_example",
        is_mandatory=True,
        order=1,
        is_file=True,
        is_submission_unique=True,
        is_site_unique=True,
    ) # MetaDatum |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a MetaDatum
        api_instance.update_meta_datum(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->update_meta_datum: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a MetaDatum
        api_instance.update_meta_datum(id, meta_datum=meta_datum)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling MetadataApi->update_meta_datum: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID |
 **meta_datum** | [**MetaDatum**](MetaDatum.md)|  | [optional]

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
**204** | Metadatum updated successful |  -  |
**401** | Unauthorized |  -  |
**403** | This user does not have the rights to perform this action. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

