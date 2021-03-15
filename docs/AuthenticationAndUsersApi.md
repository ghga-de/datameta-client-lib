# datameta_client_lib.AuthenticationAndUsersApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](AuthenticationAndUsersApi.md#create_api_key) | **POST** /keys | Create new API Key/Token
[**delete_api_key**](AuthenticationAndUsersApi.md#delete_api_key) | **DELETE** /keys/{id} | Delete ApiKey by label
[**get_user_api_keys**](AuthenticationAndUsersApi.md#get_user_api_keys) | **GET** /users/{id}/keys | All API keys for a user
[**set_user_password**](AuthenticationAndUsersApi.md#set_user_password) | **PUT** /users/{id}/password | Update a user&#39;s password


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
from datameta_client_lib.api import authentication_and_users_api
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
    api_instance = authentication_and_users_api.AuthenticationAndUsersApi(api_client)
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
        print("Exception when calling AuthenticationAndUsersApi->create_api_key: %s\n" % e)
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
**500** | Internal Server Error |  -  |

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
from datameta_client_lib.api import authentication_and_users_api
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
    api_instance = authentication_and_users_api.AuthenticationAndUsersApi(api_client)
    id = "id_example" # str | ID (not label) of Apikey

    # example passing only required values which don't have defaults set
    try:
        # Delete ApiKey by label
        api_instance.delete_api_key(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling AuthenticationAndUsersApi->delete_api_key: %s\n" % e)
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_keys**
> ApiKeyList get_user_api_keys(id)

All API keys for a user

Get a list of all API keys for a user. Please note that you cannot retrieve the tokens themselves because they are stored in a hashed format in our database as only the respective user is allowed to know them.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import authentication_and_users_api
from datameta_client_lib.model.api_key_list import ApiKeyList
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
    api_instance = authentication_and_users_api.AuthenticationAndUsersApi(api_client)
    id = "id_example" # str | ID of the User

    # example passing only required values which don't have defaults set
    try:
        # All API keys for a user
        api_response = api_instance.get_user_api_keys(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling AuthenticationAndUsersApi->get_user_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the User |

### Return type

[**ApiKeyList**](ApiKeyList.md)

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

# **set_user_password**
> set_user_password(id)

Update a user's password

Update a user's password. The user ID can be specified either as a UUID or as a site ID.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import authentication_and_users_api
from datameta_client_lib.model.validation_error_model import ValidationErrorModel
from datameta_client_lib.model.password_change import PasswordChange
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
    api_instance = authentication_and_users_api.AuthenticationAndUsersApi(api_client)
    id = "id_example" # str | User ID, either as UUID or as site ID. '0' for password reset token based access.
    password_change = PasswordChange(
        password_change_credential="password_change_credential_example",
        new_password="new_password_example",
    ) # PasswordChange | Old and new password (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user's password
        api_instance.set_user_password(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling AuthenticationAndUsersApi->set_user_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user's password
        api_instance.set_user_password(id, password_change=password_change)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling AuthenticationAndUsersApi->set_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID, either as UUID or as site ID. &#39;0&#39; for password reset token based access. |
 **password_change** | [**PasswordChange**](PasswordChange.md)| Old and new password | [optional]

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
**204** | Password update successful |  -  |
**401** | Unauthorized |  -  |
**403** | The specified user does not exist or is not the same user as the authorized user. |  -  |
**404** | Password reset token not found |  -  |
**410** | Password reset token expired |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

