# datameta_client_lib.UserApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_registration_settings**](UserApi.md#get_registration_settings) | **GET** /registrationsettings | Get details for the registration view
[**post_registration**](UserApi.md#post_registration) | **POST** /registrations | Create a new user registration request


# **get_registration_settings**
> RegisterSettingsResponse get_registration_settings()

Get details for the registration view

Get all available groups and the user agreement for the registration view

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import user_api
from datameta_client_lib.model.register_settings_response import RegisterSettingsResponse
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get details for the registration view
        api_response = api_instance.get_registration_settings()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling UserApi->get_registration_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegisterSettingsResponse**](RegisterSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_registration**
> post_registration()

Create a new user registration request

Create a new user registration request

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import user_api
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.registration_request import RegistrationRequest
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
    api_instance = user_api.UserApi(api_client)
    registration_request = RegistrationRequest(
        name="name_example",
        email="email_example",
        org_select="org_select_example",
        org_create="org_create_example",
        org_new_name="org_new_name_example",
        check_user_agreement=True,
    ) # RegistrationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new user registration request
        api_instance.post_registration(registration_request=registration_request)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling UserApi->post_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_request** | [**RegistrationRequest**](RegistrationRequest.md)|  | [optional]

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
**204** | New User Registration Request created |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

