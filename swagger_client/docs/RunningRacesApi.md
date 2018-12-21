# swagger_client.RunningRacesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_running_race_by_id**](RunningRacesApi.md#get_running_race_by_id) | **GET** /running_races/{id} | Get Running Race
[**get_running_races**](RunningRacesApi.md#get_running_races) | **GET** /running_races | List Running Races


# **get_running_race_by_id**
> RunningRace get_running_race_by_id(id)

Get Running Race

Returns a running race for a given identifier.

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
api_instance = swagger_client.RunningRacesApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the running race.

try:
    # Get Running Race
    api_response = api_instance.get_running_race_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningRacesApi->get_running_race_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the running race. | 

### Return type

[**RunningRace**](RunningRace.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_races**
> list[RunningRace] get_running_races(year=year)

List Running Races

Returns a list running races based on a set of search criteria.

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
api_instance = swagger_client.RunningRacesApi(swagger_client.ApiClient(configuration))
year = 56 # int | Filters the list by a given year. (optional)

try:
    # List Running Races
    api_response = api_instance.get_running_races(year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningRacesApi->get_running_races: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Filters the list by a given year. | [optional] 

### Return type

[**list[RunningRace]**](RunningRace.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

