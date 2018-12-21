# swagger_client.StreamsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_streams**](StreamsApi.md#get_activity_streams) | **GET** /activities/{id}/streams | Get Activity Streams
[**get_segment_effort_streams**](StreamsApi.md#get_segment_effort_streams) | **GET** /segment_efforts/{id}/streams | Get segment effort streams
[**get_segment_streams**](StreamsApi.md#get_segment_streams) | **GET** /segments/{id}/streams | Get Segment Streams


# **get_activity_streams**
> StreamSet get_activity_streams(id, keys, key_by_type)

Get Activity Streams

Returns the given activity's streams. Requires activity:read scope. Requires activity:read_all scope for Only Me activities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StreamsApi(swagger_client.ApiClient(configuration))
id = 789 # int | The identifier of the activity.
keys = ['keys_example'] # list[str] | Desired stream types.
key_by_type = true # bool | Must be true. (default to true)

try:
    # Get Activity Streams
    api_response = api_instance.get_activity_streams(id, keys, key_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_activity_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **keys** | [**list[str]**](str.md)| Desired stream types. | 
 **key_by_type** | **bool**| Must be true. | [default to true]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_effort_streams**
> StreamSet get_segment_effort_streams(id, keys, key_by_type)

Get segment effort streams

Returns a set of streams for a segment effort completed by the authenticated athlete. Requires read_all scope.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StreamsApi(swagger_client.ApiClient(configuration))
id = 789 # int | The identifier of the segment effort.
keys = ['keys_example'] # list[str] | The types of streams to return.
key_by_type = true # bool | Must be true. (default to true)

try:
    # Get segment effort streams
    api_response = api_instance.get_segment_effort_streams(id, keys, key_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_segment_effort_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment effort. | 
 **keys** | [**list[str]**](str.md)| The types of streams to return. | 
 **key_by_type** | **bool**| Must be true. | [default to true]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_streams**
> StreamSet get_segment_streams(id, keys, key_by_type)

Get Segment Streams

Returns the given segment's streams. Requires read_all scope for private segments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StreamsApi(swagger_client.ApiClient(configuration))
id = 789 # int | The identifier of the segment.
keys = ['keys_example'] # list[str] | The types of streams to return.
key_by_type = true # bool | Must be true. (default to true)

try:
    # Get Segment Streams
    api_response = api_instance.get_segment_streams(id, keys, key_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_segment_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment. | 
 **keys** | [**list[str]**](str.md)| The types of streams to return. | 
 **key_by_type** | **bool**| Must be true. | [default to true]

### Return type

[**StreamSet**](StreamSet.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

