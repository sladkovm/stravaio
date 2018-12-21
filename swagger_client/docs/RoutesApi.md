# swagger_client.RoutesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_as_gpx**](RoutesApi.md#get_route_as_gpx) | **GET** /routes/{id}/export_gpx | Export Route GPX
[**get_route_as_tcx**](RoutesApi.md#get_route_as_tcx) | **GET** /routes/{id}/export_tcx | Export Route TCX
[**get_route_by_id**](RoutesApi.md#get_route_by_id) | **GET** /routes/{id} | Get Route
[**get_routes_by_athlete_id**](RoutesApi.md#get_routes_by_athlete_id) | **GET** /athletes/{id}/routes | List Athlete Routes


# **get_route_as_gpx**
> get_route_as_gpx(id)

Export Route GPX

Returns a GPX file of the route. Requires read_all scope for private routes.

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the route.

try:
    # Export Route GPX
    api_instance.get_route_as_gpx(id)
except ApiException as e:
    print("Exception when calling RoutesApi->get_route_as_gpx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

void (empty response body)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_as_tcx**
> get_route_as_tcx(id)

Export Route TCX

Returns a TCX file of the route. Requires read_all scope for private routes.

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the route.

try:
    # Export Route TCX
    api_instance.get_route_as_tcx(id)
except ApiException as e:
    print("Exception when calling RoutesApi->get_route_as_tcx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

void (empty response body)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_by_id**
> Route get_route_by_id(id)

Get Route

Returns a route using its identifier. Requires read_all scope for private routes.

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the route.

try:
    # Get Route
    api_response = api_instance.get_route_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->get_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

[**Route**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes_by_athlete_id**
> list[Route] get_routes_by_athlete_id(id, page=page, per_page=per_page)

List Athlete Routes

Returns a list of the routes created by the authenticated athlete using their athlete ID. Private routes are filtered out unless requested by a token with read_all scope.

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the athlete.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Routes
    api_response = api_instance.get_routes_by_athlete_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->get_routes_by_athlete_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the athlete. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[Route]**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

