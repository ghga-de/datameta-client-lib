# datameta_client_lib.GroupsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_group_name**](GroupsApi.md#change_group_name) | **PUT** /groups/{id} | Change the name of a group.
[**get_group_submissions**](GroupsApi.md#get_group_submissions) | **GET** /groups/{id}/submissions | Get A List of All Submissions of A Group.


# **change_group_name**
> change_group_name(id)

Change the name of a group.

Change the name of a group.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import groups_api
from datameta_client_lib.model.group_update_request import GroupUpdateRequest
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | ID of the group
    group_update_request = GroupUpdateRequest(
        name="name_example",
    ) # GroupUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change the name of a group.
        api_instance.change_group_name(id)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling GroupsApi->change_group_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change the name of a group.
        api_instance.change_group_name(id, group_update_request=group_update_request)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling GroupsApi->change_group_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group |
 **group_update_request** | [**GroupUpdateRequest**](GroupUpdateRequest.md)|  | [optional]

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The specified group does not exist. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_submissions**
> GroupSubmissions get_group_submissions(id)

Get A List of All Submissions of A Group.

Get a list of all submissions of a group.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import groups_api
from datameta_client_lib.model.group_submissions import GroupSubmissions
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | ID of the group

    # example passing only required values which don't have defaults set
    try:
        # Get A List of All Submissions of A Group.
        api_response = api_instance.get_group_submissions(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling GroupsApi->get_group_submissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group |

### Return type

[**GroupSubmissions**](GroupSubmissions.md)

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
**404** | The specified group does not exist. |  -  |
**400** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

