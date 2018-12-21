# SummaryActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the activity | [optional] 
**external_id** | **str** | The identifier provided at upload time | [optional] 
**upload_id** | **int** | The identifier of the upload that resulted in this activity | [optional] 
**athlete** | [**MetaAthlete**](MetaAthlete.md) |  | [optional] 
**name** | **str** | The name of the activity | [optional] 
**distance** | **float** | The activity&#39;s distance, in meters | [optional] 
**moving_time** | **int** | The activity&#39;s moving time, in seconds | [optional] 
**elapsed_time** | **int** | The activity&#39;s elapsed time, in seconds | [optional] 
**total_elevation_gain** | **float** | The activity&#39;s total elevation gain. | [optional] 
**elev_high** | **float** | The activity&#39;s highest elevation, in meters | [optional] 
**elev_low** | **float** | The activity&#39;s lowest elevation, in meters | [optional] 
**type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**start_date** | **datetime** | The time at which the activity was started. | [optional] 
**start_date_local** | **datetime** | The time at which the activity was started in the local timezone. | [optional] 
**timezone** | **str** | The timezone of the activity | [optional] 
**start_latlng** | [**LatLng**](LatLng.md) |  | [optional] 
**end_latlng** | [**LatLng**](LatLng.md) |  | [optional] 
**achievement_count** | **int** | The number of achievements gained during this activity | [optional] 
**kudos_count** | **int** | The number of kudos given for this activity | [optional] 
**comment_count** | **int** | The number of comments for this activity | [optional] 
**athlete_count** | **int** | The number of athletes for taking part in a group activity | [optional] 
**photo_count** | **int** | The number of Instagram photos for this activity | [optional] 
**total_photo_count** | **int** | The number of Instagram and Strava photos for this activity | [optional] 
**map** | [**PolylineMap**](PolylineMap.md) |  | [optional] 
**trainer** | **bool** | Whether this activity was recorded on a training machine | [optional] 
**commute** | **bool** | Whether this activity is a commute | [optional] 
**manual** | **bool** | Whether this activity was created manually | [optional] 
**private** | **bool** | Whether this activity is private | [optional] 
**flagged** | **bool** | Whether this activity is flagged | [optional] 
**workout_type** | **int** | The activity&#39;s workout type | [optional] 
**average_speed** | **float** | The activity&#39;s average speed, in meters per second | [optional] 
**max_speed** | **float** | The activity&#39;s max speed, in meters per second | [optional] 
**has_kudoed** | **bool** | Whether the logged-in athlete has kudoed this activity | [optional] 
**gear_id** | **str** | The id of the gear for the activity | [optional] 
**kilojoules** | **float** | The total work done in kilojoules during this activity. Rides only | [optional] 
**average_watts** | **float** | Average power output in watts during this activity. Rides only | [optional] 
**device_watts** | **bool** | Whether the watts are from a power meter, false if estimated | [optional] 
**max_watts** | **int** | Rides with power meter data only | [optional] 
**weighted_average_watts** | **int** | Similar to Normalized Power. Rides with power meter data only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


