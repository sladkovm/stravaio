# swagger_client.GearsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gear_by_id**](GearsApi.md#get_gear_by_id) | **GET** /gear/{id} | Get Equipment


# **get_gear_by_id**
> DetailedGear get_gear_by_id(id)

Get Equipment

Returns an equipment using its identifier.

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
api_instance = swagger_client.GearsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the gear.

try:
    # Get Equipment
    api_response = api_instance.get_gear_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GearsApi->get_gear_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the gear. | 

### Return type

[**DetailedGear**](DetailedGear.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

