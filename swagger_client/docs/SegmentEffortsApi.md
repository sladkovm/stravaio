# swagger_client.SegmentEffortsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_efforts_by_segment_id**](SegmentEffortsApi.md#get_efforts_by_segment_id) | **GET** /segments/{id}/all_efforts | List Segment Efforts
[**get_segment_effort_by_id**](SegmentEffortsApi.md#get_segment_effort_by_id) | **GET** /segment_efforts/{id} | Get Segment Effort


# **get_efforts_by_segment_id**
> list[DetailedSegmentEffort] get_efforts_by_segment_id(id, page=page, per_page=per_page)

List Segment Efforts

Returns a set of the authenticated athlete's segment efforts for a given segment.

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
api_instance = swagger_client.SegmentEffortsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the segment.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Segment Efforts
    api_response = api_instance.get_efforts_by_segment_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEffortsApi->get_efforts_by_segment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[DetailedSegmentEffort]**](DetailedSegmentEffort.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_effort_by_id**
> DetailedSegmentEffort get_segment_effort_by_id(id)

Get Segment Effort

Returns a segment effort from an activity that is owned by the authenticated athlete.

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
api_instance = swagger_client.SegmentEffortsApi(swagger_client.ApiClient(configuration))
id = 789 # int | The identifier of the segment effort.

try:
    # Get Segment Effort
    api_response = api_instance.get_segment_effort_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEffortsApi->get_segment_effort_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment effort. | 

### Return type

[**DetailedSegmentEffort**](DetailedSegmentEffort.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

