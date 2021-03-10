# datameta_client_lib.UsersApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](UsersApi.md#create_api_key) | **POST** /keys | Create new API Key/Token
[**delete_api_key**](UsersApi.md#delete_api_key) | **DELETE** /keys/{id} | Delete ApiKey by label
[**register_user**](UsersApi.md#register_user) | **POST** /users | Register a New User


# **create_api_key**
> UserSession create_api_key()

Create new API Key/Token

Create new API Key/Token

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import users_api
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
from datameta_client_lib.model.create_token_request import CreateTokenRequest
from datameta_client_lib.model.user_session import UserSession
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
    api_instance = users_api.UsersApi(api_client)
    create_token_request = CreateTokenRequest(
        email="email_example",
        password="password_example",
        label="label_example",
        expires="expires_example",
    ) # CreateTokenRequest | Credentials to use (optional when using cookie sessions), a label for the ApiKey to be created and the date it expires. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create new API Key/Token
        api_response = api_instance.create_api_key(create_token_request=create_token_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling UsersApi->create_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_request** | [**CreateTokenRequest**](CreateTokenRequest.md)| Credentials to use (optional when using cookie sessions), a label for the ApiKey to be created and the date it expires. | [optional]

### Return type

[**UserSession**](UserSession.md)

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
**403** | Forbidden |  -  |
**400** | Validation Error |  -  |
**500** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(id)

Delete ApiKey by label

Delete ApiKey by label.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import users_api
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
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
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | ID (not label) of Apikey

    # example passing only required values which don't have defaults set
    try:
        # Delete ApiKey by label
        api_instance.delete_api_key(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling UsersApi->delete_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID (not label) of Apikey |

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Validation Error |  -  |
**500** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> RegRequest register_user()

Register a New User

Register a new user. The password will be set later, after an admin has approved the registration.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import users_api
from datameta_client_lib.model.reg_request import RegRequest
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
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
    api_instance = users_api.UsersApi(api_client)
    reg_request = RegRequest(
        fullname="fullname_example",
        email="email_example",
        group_id="group_id_example",
        new_group_name="new_group_name_example",
    ) # RegRequest | Information required for registration. Please provide either a \"newGroupName\" or a \"groupId\" but not both: If you are the first member of your group to register, please provide a descriptive name of the new group  using the \"newGroupName\" property. If your group already exists, please refer to it using its \"groupId\" (not name). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register a New User
        api_response = api_instance.register_user(reg_request=reg_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling UsersApi->register_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg_request** | [**RegRequest**](RegRequest.md)| Information required for registration. Please provide either a \&quot;newGroupName\&quot; or a \&quot;groupId\&quot; but not both: If you are the first member of your group to register, please provide a descriptive name of the new group  using the \&quot;newGroupName\&quot; property. If your group already exists, please refer to it using its \&quot;groupId\&quot; (not name). | [optional]

### Return type

[**RegRequest**](RegRequest.md)

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

