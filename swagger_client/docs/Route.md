# Route

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete** | [**SummaryAthlete**](SummaryAthlete.md) |  | [optional] 
**description** | **str** | The description of the route | [optional] 
**distance** | **float** | The route&#39;s distance, in meters | [optional] 
**elevation_gain** | **float** | The route&#39;s elevation gain. | [optional] 
**id** | **int** | The unique identifier of this route | [optional] 
**map** | [**PolylineMap**](PolylineMap.md) |  | [optional] 
**name** | **str** | The name of this route | [optional] 
**private** | **bool** | Whether this route is private | [optional] 
**starred** | **bool** | Whether this route is starred by the logged-in athlete | [optional] 
**timestamp** | **int** |  | [optional] 
**type** | **int** | This route&#39;s type (1 for ride, 2 for runs) | [optional] 
**sub_type** | **int** | This route&#39;s sub-type (1 for road, 2 for mountain bike, 3 for cross, 4 for trail, 5 for mixed) | [optional] 
**segments** | [**list[SummarySegment]**](SummarySegment.md) | The segments traversed by this route | [optional] 
**directions** | [**list[RouteDirection]**](RouteDirection.md) | The directions of this route | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


