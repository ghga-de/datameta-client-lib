# datameta_client_lib.ServerApi

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_info**](ServerApi.md#get_server_info) | **GET** /server | Get DataMeta server information


# **get_server_info**
> ServerInfoResponse get_server_info()

Get DataMeta server information

Get information about the DataMeta server serving this API

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import server_api
from datameta_client_lib.model.server_info_response import ServerInfoResponse
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get DataMeta server information
        api_response = api_instance.get_server_info()
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling ServerApi->get_server_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfoResponse**](ServerInfoResponse.md)

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

