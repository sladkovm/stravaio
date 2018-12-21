# DetailedSegmentEffort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this effort | [optional] 
**elapsed_time** | **int** | The effort&#39;s elapsed time | [optional] 
**start_date** | **datetime** | The time at which the effort was started. | [optional] 
**start_date_local** | **datetime** | The time at which the effort was started in the local timezone. | [optional] 
**distance** | **float** | The effort&#39;s distance in meters | [optional] 
**is_kom** | **bool** | Whether this effort is the current best on the leaderboard | [optional] 
**name** | **str** | The name of the segment on which this effort was performed | [optional] 
**activity** | [**MetaActivity**](MetaActivity.md) |  | [optional] 
**athlete** | [**MetaAthlete**](MetaAthlete.md) |  | [optional] 
**moving_time** | **int** | The effort&#39;s moving time | [optional] 
**start_index** | **int** | The start index of this effort in its activity&#39;s stream | [optional] 
**end_index** | **int** | The end index of this effort in its activity&#39;s stream | [optional] 
**average_cadence** | **float** | The effort&#39;s average cadence | [optional] 
**average_watts** | **float** | The average wattage of this effort | [optional] 
**device_watts** | **bool** | For riding efforts, whether the wattage was reported by a dedicated recording device | [optional] 
**average_heartrate** | **float** | The heart heart rate of the athlete during this effort | [optional] 
**max_heartrate** | **float** | The maximum heart rate of the athlete during this effort | [optional] 
**segment** | [**SummarySegment**](SummarySegment.md) |  | [optional] 
**kom_rank** | **int** | The rank of the effort on the global leaderboard if it belongs in the top 10 at the time of upload | [optional] 
**pr_rank** | **int** | The rank of the effort on the athlete&#39;s leaderboard if it belongs in the top 3 at the time of upload | [optional] 
**hidden** | **bool** | Whether this effort should be hidden when viewed within an activity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


