# datameta_client_lib.SubmissionsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_submission**](SubmissionsApi.md#create_submission) | **POST** /submissions | Create a New Submission
[**get_group_submissions**](SubmissionsApi.md#get_group_submissions) | **GET** /groups/{id}/submissions | Get A List of All Submissions of A Group.
[**prevalidate_submission**](SubmissionsApi.md#prevalidate_submission) | **POST** /presubvalidation | Pre-validate a submission


# **create_submission**
> SubmissionResponse create_submission()

Create a New Submission

Creates a new Submission. A submission consists of a list of metadatasets and a list of files.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import submissions_api
from datameta_client_lib.model.submission_response import SubmissionResponse
from datameta_client_lib.model.submission_request import SubmissionRequest
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_request = SubmissionRequest(
        metadataset_ids=[
            "metadataset_ids_example",
        ],
        file_ids=[],
        label="label_example",
    ) # SubmissionRequest | Provide a list of metadatasets and a list of files. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New Submission
        api_response = api_instance.create_submission(submission_request=submission_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SubmissionsApi->create_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_request** | [**SubmissionRequest**](SubmissionRequest.md)| Provide a list of metadatasets and a list of files. | [optional]

### Return type

[**SubmissionResponse**](SubmissionResponse.md)

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
from datameta_client_lib.api import submissions_api
from datameta_client_lib.model.group_submissions import GroupSubmissions
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    id = "id_example" # str | ID of the group

    # example passing only required values which don't have defaults set
    try:
        # Get A List of All Submissions of A Group.
        api_response = api_instance.get_group_submissions(id)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SubmissionsApi->get_group_submissions: %s\n" % e)
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

# **prevalidate_submission**
> prevalidate_submission()

Pre-validate a submission

Pre-validates a submission request without actually creating a submission.  A submission request consists of a list of metadatasets and a list of files.

### Example

* Bearer Authentication (bearerAuth):
* Api Key Authentication (cookieAuth):
```python
import time
import datameta_client_lib
from datameta_client_lib.api import submissions_api
from datameta_client_lib.model.submission_request import SubmissionRequest
from datameta_client_lib.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v1"
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
    api_instance = submissions_api.SubmissionsApi(api_client)
    submission_request = SubmissionRequest(
        metadataset_ids=[
            "metadataset_ids_example",
        ],
        file_ids=[
            "file_ids_example",
        ],
        label="label_example",
    ) # SubmissionRequest | Provide a list of metadatasets and a list of files. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pre-validate a submission
        api_instance.prevalidate_submission(submission_request=submission_request)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling SubmissionsApi->prevalidate_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_request** | [**SubmissionRequest**](SubmissionRequest.md)| Provide a list of metadatasets and a list of files. | [optional]

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
**204** | OK |  -  |
**400** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

