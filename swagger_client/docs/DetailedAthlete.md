# DetailedAthlete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the athlete | [optional] 
**resource_state** | **int** | Resource state, indicates level of detail. Possible values: 1 -&gt; \&quot;meta\&quot;, 2 -&gt; \&quot;summary\&quot;, 3 -&gt; \&quot;detail\&quot; | [optional] 
**firstname** | **str** | The athlete&#39;s first name. | [optional] 
**lastname** | **str** | The athlete&#39;s last name. | [optional] 
**profile_medium** | **str** | URL to a 62x62 pixel profile picture. | [optional] 
**profile** | **str** | URL to a 124x124 pixel profile picture. | [optional] 
**city** | **str** | The athlete&#39;s city. | [optional] 
**state** | **str** | The athlete&#39;s state or geographical region. | [optional] 
**country** | **str** | The athlete&#39;s country. | [optional] 
**sex** | **str** | The athlete&#39;s sex. | [optional] 
**friend** | **str** | Whether the currently logged-in athlete follows this athlete. | [optional] 
**follower** | **str** | Whether this athlete follows the currently logged-in athlete. | [optional] 
**premium** | **bool** | Deprecated.  Use summit field instead. Whether the athlete has any Summit subscription. | [optional] 
**summit** | **bool** | Whether the athlete has any Summit subscription. | [optional] 
**created_at** | **datetime** | The time at which the athlete was created. | [optional] 
**updated_at** | **datetime** | The time at which the athlete was last updated. | [optional] 
**follower_count** | **int** | The athlete&#39;s follower count. | [optional] 
**friend_count** | **int** | The athlete&#39;s friend count. | [optional] 
**mutual_friend_count** | **int** | The number or athletes mutually followed by this athlete and the currently logged-in athlete. | [optional] 
**measurement_preference** | **str** | The athlete&#39;s preferred unit system. | [optional] 
**ftp** | **int** | The athlete&#39;s FTP (Functional Threshold Power). | [optional] 
**weight** | **float** | The athlete&#39;s weight. | [optional] 
**clubs** | [**list[SummaryClub]**](SummaryClub.md) | The athlete&#39;s clubs. | [optional] 
**bikes** | [**list[SummaryGear]**](SummaryGear.md) | The athlete&#39;s bikes. | [optional] 
**shoes** | [**list[SummaryGear]**](SummaryGear.md) | The athlete&#39;s shoes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


