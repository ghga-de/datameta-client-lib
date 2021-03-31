# datameta_client_lib.SettingsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_settings**](SettingsApi.md#app_settings) | **GET** /appsettings | GET all AppSettings
[**update_app_settings**](SettingsApi.md#update_app_settings) | **PUT** /appsettings/{id} | Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.


# **app_settings**
> [AppSettingsResponse] app_settings()

GET all AppSettings

GET all AppSettings. This is an administrative Endpoint that is not accessible for regular users.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import settings_api
from datameta_client_lib.model.app_settings_response import AppSettingsResponse
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
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET all AppSettings
        api_response = api_instance.app_settings()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SettingsApi->app_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AppSettingsResponse]**](AppSettingsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_settings**
> update_app_settings(id)

Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.

Update a specific appsetting

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import settings_api
from datameta_client_lib.model.app_settings_update_request import AppSettingsUpdateRequest
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
    api_instance = settings_api.SettingsApi(api_client)
    id = "id_example" # str | ID of the group
    app_settings_update_request = AppSettingsUpdateRequest(
        value="value_example",
    ) # AppSettingsUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.
        api_instance.update_app_settings(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SettingsApi->update_app_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.
        api_instance.update_app_settings(id, app_settings_update_request=app_settings_update_request)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SettingsApi->update_app_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group |
 **app_settings_update_request** | [**AppSettingsUpdateRequest**](AppSettingsUpdateRequest.md)|  | [optional]

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
**204** | App Settings Updated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Setting does not exist |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

