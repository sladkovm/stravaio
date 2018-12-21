# DetailedSegment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this segment | [optional] 
**name** | **str** | The name of this segment | [optional] 
**activity_type** | **str** |  | [optional] 
**distance** | **float** | The segment&#39;s distance, in meters | [optional] 
**average_grade** | **float** | The segment&#39;s average grade, in percents | [optional] 
**maximum_grade** | **float** | The segments&#39;s maximum grade, in percents | [optional] 
**elevation_high** | **float** | The segments&#39;s highest elevation, in meters | [optional] 
**elevation_low** | **float** | The segments&#39;s lowest elevation, in meters | [optional] 
**start_latlng** | [**LatLng**](LatLng.md) |  | [optional] 
**end_latlng** | [**LatLng**](LatLng.md) |  | [optional] 
**climb_category** | **int** | The category of the climb | [optional] 
**city** | **str** | The segments&#39;s city. | [optional] 
**state** | **str** | The segments&#39;s state or geographical region. | [optional] 
**country** | **str** | The segment&#39;s country. | [optional] 
**private** | **bool** | Whether this segment is private. | [optional] 
**athlete_pr_effort** | [**SummarySegmentEffort**](SummarySegmentEffort.md) |  | [optional] 
**created_at** | **datetime** | The time at which the segment was created. | [optional] 
**updated_at** | **datetime** | The time at which the segment was last updated. | [optional] 
**total_elevation_gain** | **float** | The segment&#39;s total elevation gain. | [optional] 
**map** | [**PolylineMap**](PolylineMap.md) |  | [optional] 
**effort_count** | **int** | The total number of efforts for this segment | [optional] 
**athlete_count** | **int** | The number of unique athletes who have an effort for this segment | [optional] 
**hazardous** | **bool** | Whether this segment is considered hazardous | [optional] 
**star_count** | **int** | The number of stars for this segment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


