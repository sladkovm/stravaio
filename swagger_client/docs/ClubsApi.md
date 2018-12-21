# swagger_client.ClubsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club_activities_by_id**](ClubsApi.md#get_club_activities_by_id) | **GET** /clubs/{id}/activities | List Club Activities
[**get_club_admins_by_id**](ClubsApi.md#get_club_admins_by_id) | **GET** /clubs/{id}/admins | List Club Administrators.
[**get_club_by_id**](ClubsApi.md#get_club_by_id) | **GET** /clubs/{id} | Get Club
[**get_club_members_by_id**](ClubsApi.md#get_club_members_by_id) | **GET** /clubs/{id}/members | List Club Members
[**get_logged_in_athlete_clubs**](ClubsApi.md#get_logged_in_athlete_clubs) | **GET** /athlete/clubs | List Athlete Clubs


# **get_club_activities_by_id**
> list[SummaryActivity] get_club_activities_by_id(id, page=page, per_page=per_page)

List Club Activities

Retrieve recent activities from members of a specific club. The authenticated athlete must belong to the requested club in order to hit this endpoint. Pagination is supported. Athlete profile visibility is respected for all activities.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the club.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Club Activities
    api_response = api_instance.get_club_activities_by_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club_activities_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryActivity]**](SummaryActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_admins_by_id**
> list[SummaryAthlete] get_club_admins_by_id(id, page=page, per_page=per_page)

List Club Administrators.

Returns a list of the administrators of a given club.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the club.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Club Administrators.
    api_response = api_instance.get_club_admins_by_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club_admins_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryAthlete]**](SummaryAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_by_id**
> DetailedClub get_club_by_id(id)

Get Club

Returns a given club using its identifier.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the club.

try:
    # Get Club
    api_response = api_instance.get_club_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 

### Return type

[**DetailedClub**](DetailedClub.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_members_by_id**
> list[SummaryAthlete] get_club_members_by_id(id, page=page, per_page=per_page)

List Club Members

Returns a list of the athletes who are members of a given club.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the club.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Club Members
    api_response = api_instance.get_club_members_by_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club_members_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the club. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryAthlete]**](SummaryAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_clubs**
> list[SummaryClub] get_logged_in_athlete_clubs(page=page, per_page=per_page)

List Athlete Clubs

Returns a list of the clubs whose membership includes the authenticated athlete.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Clubs
    api_response = api_instance.get_logged_in_athlete_clubs(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_logged_in_athlete_clubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryClub]**](SummaryClub.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

