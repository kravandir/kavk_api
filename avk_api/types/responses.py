from .objects import *
from .base import BM

class AccountChangePasswordResponse(BM):
	token:str
	secret:str

class AccountGetActiveOffersResponse(BM):
	count:int
	items:list[AccountOffer]

AccountGetAppPermissionsResponse = int

class AccountGetBannedResponse(BM):
	count:int
	items:list[int]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroup]

AccountGetCountersResponse = AccountAccountCounters

AccountGetInfoResponse = AccountInfo

AccountGetProfileInfoResponse = AccountUserSettings

AccountGetPushSettingsResponse = AccountPushSettings

class AccountSaveProfileInfoResponse(BM):
	changed:bool
	name_request:AccountNameRequest


AdsAddOfficeUsersResponse = bool

AdsCheckLinkResponse = AdsLinkStatus

AdsCreateAdsResponse = list[AdsCreateAdStatus]

AdsCreateCampaignsResponse = list[AdsCreateCampaignStatus]

AdsCreateClientsResponse = list[int]

class AdsCreateTargetGroupResponse(BM):
	id:int
	pixel:str

AdsDeleteAdsResponse = list[int]

AdsDeleteCampaignsResponse = list[int]

AdsDeleteClientsResponse = list[int]

AdsGetAccountsResponse = list[AdsAccount]

AdsGetAdsLayoutResponse = list[AdsAdLayout]

AdsGetAdsTargetingResponse = list[AdsTargSettings]

AdsGetAdsResponse = list[AdsAd]

AdsGetBudgetResponse = int

AdsGetCampaignsResponse = list[AdsCampaign]

class AdsGetCategoriesResponse(BM):
	v1:list[AdsCategory]
	v2:list[AdsCategory]

AdsGetClientsResponse = list[AdsClient]

AdsGetDemographicsResponse = list[AdsDemoStats]

AdsGetFloodStatsResponse = AdsFloodStats

class AdsGetLookalikeRequestsResponse(BM):
	count:int
	items:list[AdsLookalikeRequest]

class AdsGetMusiciansResponse(BM):
	items:list[AdsMusician]

AdsGetOfficeUsersResponse = list[AdsUsers]

AdsGetPostsReachResponse = list[AdsPromotedPostReach]

AdsGetRejectionReasonResponse = AdsRejectReason

AdsGetStatisticsResponse = list[AdsStats]

AdsGetSuggestionsCitiesResponse = list[AdsTargSuggestionsCities]

AdsGetSuggestionsRegionsResponse = list[AdsTargSuggestionsRegions]

AdsGetSuggestionsResponse = list[AdsTargSuggestions]

AdsGetSuggestionsSchoolsResponse = list[AdsTargSuggestionsSchools]

AdsGetTargetGroupsResponse = list[AdsTargetGroup]

AdsGetTargetingStatsResponse = AdsTargStats

AdsGetUploadURLResponse = str

AdsGetVideoUploadURLResponse = str

AdsImportTargetContactsResponse = int

AdsRemoveOfficeUsersResponse = bool

AdsUpdateAdsResponse = list[int]

AdsUpdateCampaignsResponse = int

AdsUpdateClientsResponse = int

AdsUpdateOfficeUsersResponse = list[AdsUpdateOfficeUsersResult]


class AdswebGetAdCategoriesResponse(BM):
	categories:list[AdswebGetAdCategoriesResponseCategoriesCategory]

class AdswebGetAdUnitCodeResponse(BM):
	html:str

class AdswebGetAdUnitsResponse(BM):
	count:int
	ad_units:list[AdswebGetAdUnitsResponseAdUnitsAdUnit]

class AdswebGetFraudHistoryResponse(BM):
	count:int
	entries:list[AdswebGetFraudHistoryResponseEntriesEntry]

class AdswebGetSitesResponse(BM):
	count:int
	sites:list[AdswebGetSitesResponseSitesSite]

class AdswebGetStatisticsResponse(BM):
	next_page_id:str
	items:list[AdswebGetStatisticsResponseItemsItem]


class AppWidgetsGetAppImageUploadServerResponse(BM):
	upload_url:str

AppWidgetsGetAppImagesResponse = AppWidgetsPhotos

class AppWidgetsGetGroupImageUploadServerResponse(BM):
	upload_url:str

AppWidgetsGetGroupImagesResponse = AppWidgetsPhotos

AppWidgetsGetImagesByIdResponse = list[AppWidgetsPhoto]

AppWidgetsSaveAppImageResponse = AppWidgetsPhoto

AppWidgetsSaveGroupImageResponse = AppWidgetsPhoto


AppsGetCatalogResponse = AppsCatalogList

class AppsGetFriendsListExtendedResponse(BM):
	count:int
	items:list[UsersUserFull]

class AppsGetFriendsListResponse(BM):
	count:int
	items:list[int]

class AppsGetLeaderboardExtendedResponse(BM):
	count:int
	items:list[AppsLeaderboard]
	profiles:list[UsersUser]

class AppsGetLeaderboardResponse(BM):
	count:int
	items:list[AppsLeaderboard]

class AppsGetMiniAppPoliciesResponse(BM):
	privacy_policy:str
	terms:str

class AppsGetScopesResponse(BM):
	count:int
	items:list[AppsScope]

AppsGetScoreResponse = int

class AppsGetResponse(BM):
	count:int
	items:list[AppsApp]

class AppsImageUploadResponse(BM):
	hash:str
	image:str

AppsSendRequestResponse = int


class AuthRestoreResponse(BM):
	success:int
	sid:str


BaseBoolResponse = bool

BaseGetUploadServerResponse = BaseUploadServer

BaseOkResponse = int


BoardAddTopicResponse = int

BoardCreateCommentResponse = int

class BoardGetCommentsExtendedResponse(BM):
	count:int
	items:list[BoardTopicComment]
	poll:object
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	real_offset:int

class BoardGetCommentsResponse(BM):
	count:int
	items:list[BoardTopicComment]
	poll:object
	real_offset:int

class BoardGetTopicsExtendedResponse(BM):
	count:int
	items:list[BoardTopic]
	default_order:BoardDefaultOrder
	can_add_topics:bool
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class BoardGetTopicsResponse(BM):
	count:int
	items:list[BoardTopic]
	default_order:BoardDefaultOrder
	can_add_topics:bool


class DatabaseGetChairsResponse(BM):
	count:int
	items:list[BaseObject]

DatabaseGetCitiesByIdResponse = list[DatabaseCityById]

class DatabaseGetCitiesResponse(BM):
	count:int
	items:list[DatabaseCity]

DatabaseGetCountriesByIdResponse = list[BaseCountry]

class DatabaseGetCountriesResponse(BM):
	count:int
	items:list[BaseCountry]

class DatabaseGetFacultiesResponse(BM):
	count:int
	items:list[DatabaseFaculty]

DatabaseGetMetroStationsByIdResponse = list[DatabaseStation]

class DatabaseGetMetroStationsResponse(BM):
	count:int
	items:list[DatabaseStation]

class DatabaseGetRegionsResponse(BM):
	count:int
	items:list[DatabaseRegion]

DatabaseGetSchoolClassesResponse = list[list]

class DatabaseGetSchoolsResponse(BM):
	count:int
	items:list[DatabaseSchool]

class DatabaseGetUniversitiesResponse(BM):
	count:int
	items:list[DatabaseUniversity]


DocsAddResponse = int

class DocsDocUploadResponse(BM):
	file:str

DocsGetByIdResponse = list[DocsDoc]

class DocsGetTypesResponse(BM):
	count:int
	items:list[DocsDocTypes]

DocsGetUploadServerResponse = BaseUploadServer

class DocsGetResponse(BM):
	count:int
	items:list[DocsDoc]

class DocsSaveResponse(BM):
	type:DocsDocAttachmentType
	audio_message:MessagesAudioMessage
	doc:DocsDoc
	graffiti:MessagesGraffiti

class DocsSearchResponse(BM):
	count:int
	items:list[DocsDoc]


DonutGetSubscriptionResponse = DonutDonatorSubscriptionInfo

class DonutGetSubscriptionsResponse(BM):
	subscriptions:list[DonutDonatorSubscriptionInfo]
	count:int
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]


class DownloadedGamesPaidStatusResponse(BM):
	is_paid:bool


FaveAddTagResponse = FaveTag

class FaveGetPagesResponse(BM):
	count:int
	items:list[FavePage]

class FaveGetTagsResponse(BM):
	count:int
	items:list[FaveTag]

class FaveGetExtendedResponse(BM):
	count:int
	items:list[FaveBookmark]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroup]

class FaveGetResponse(BM):
	count:int
	items:list[FaveBookmark]


class FriendsAddListResponse(BM):
	list_id:int

FriendsAddResponse = int

FriendsAreFriendsExtendedResponse = list[FriendsFriendExtendedStatus]

FriendsAreFriendsResponse = list[FriendsFriendStatus]

class FriendsDeleteResponse(BM):
	success:int
	friend_deleted:int
	out_request_deleted:int
	in_request_deleted:int
	suggestion_deleted:int

FriendsGetAppUsersResponse = list[int]

FriendsGetByPhonesResponse = list[FriendsUserXtrPhone]

class FriendsGetListsResponse(BM):
	count:int
	items:list[FriendsFriendsList]

FriendsGetMutualResponse = list[int]

FriendsGetMutualTargetUidsResponse = list[FriendsMutualFriend]

class FriendsGetOnlineOnlineMobileResponse(BM):
	online:list[int]
	online_mobile:list[int]

FriendsGetOnlineResponse = list[int]

FriendsGetRecentResponse = list[int]

class FriendsGetRequestsExtendedResponse(BM):
	count:int
	items:list[FriendsRequestsXtrMessage]

class FriendsGetRequestsNeedMutualResponse(BM):
	count:int
	items:list[FriendsRequests]

class FriendsGetRequestsResponse(BM):
	count:int
	items:list[int]
	count_unread:int

class FriendsGetSuggestionsResponse(BM):
	count:int
	items:list[UsersUserFull]

class FriendsGetFieldsResponse(BM):
	count:int
	items:list[UsersUserFull]

class FriendsGetResponse(BM):
	count:int
	items:list[int]

class FriendsSearchResponse(BM):
	count:int
	items:list[UsersUserFull]


class GiftsGetResponse(BM):
	count:int
	items:list[GiftsGift]


GroupsAddAddressResponse = GroupsAddress

class GroupsAddCallbackServerResponse(BM):
	server_id:int

GroupsAddLinkResponse = GroupsLinksItem

GroupsCreateResponse = GroupsGroup

GroupsEditAddressResponse = GroupsAddress

class GroupsGetAddressesResponse(BM):
	count:int
	items:list[GroupsAddress]

class GroupsGetBannedResponse(BM):
	count:int
	items:list[GroupsBannedItem]

GroupsGetByIdObjectLegacyResponse = list[GroupsGroupFull]

class GroupsGetCallbackConfirmationCodeResponse(BM):
	code:str

class GroupsGetCallbackServersResponse(BM):
	count:int
	items:list[GroupsCallbackServer]

GroupsGetCallbackSettingsResponse = GroupsCallbackSettings

class GroupsGetCatalogInfoExtendedResponse(BM):
	enabled:bool
	categories:list[GroupsGroupCategoryFull]

class GroupsGetCatalogInfoResponse(BM):
	enabled:bool
	categories:list[GroupsGroupCategory]

class GroupsGetCatalogResponse(BM):
	count:int
	items:list[GroupsGroup]

class GroupsGetInvitedUsersResponse(BM):
	count:int
	items:list[UsersUserFull]

class GroupsGetInvitesExtendedResponse(BM):
	count:int
	items:list[GroupsGroupFull]
	profiles:list[UsersUserMin]
	groups:list[GroupsGroupFull]

class GroupsGetInvitesResponse(BM):
	count:int
	items:list[GroupsGroupFull]

GroupsGetLongPollServerResponse = GroupsLongPollServer

GroupsGetLongPollSettingsResponse = GroupsLongPollSettings

class GroupsGetMembersFieldsResponse(BM):
	count:int
	items:list[GroupsUserXtrRole]

class GroupsGetMembersFilterResponse(BM):
	count:int
	items:list[GroupsMemberRole]

class GroupsGetMembersResponse(BM):
	count:int
	items:list[int]

class GroupsGetRequestsFieldsResponse(BM):
	count:int
	items:list[UsersUserFull]

class GroupsGetRequestsResponse(BM):
	count:int
	items:list[int]

class GroupsGetSettingsResponse(BM):
	access:GroupsGroupAccess
	address:str
	audio:GroupsGroupAudio
	articles:int
	recognize_photo:int
	city_id:int
	city_name:str
	contacts:bool
	links:bool
	sections_list:list[GroupsSectionsListItem]
	main_section:GroupsGroupFullSection
	secondary_section:GroupsGroupFullSection
	age_limits:GroupsGroupAgeLimits
	country_id:int
	country_name:str
	description:str
	docs:GroupsGroupDocs
	events:bool
	obscene_filter:bool
	obscene_stopwords:bool
	obscene_words:list[str]
	event_group_id:int
	photos:GroupsGroupPhotos
	public_category:int
	public_category_list:list[GroupsGroupPublicCategoryList]
	public_date:str
	public_date_label:str
	public_subcategory:int
	rss:str
	start_date:int
	finish_date:int
	subject:int
	subject_list:list[GroupsSubjectItem]
	suggested_privacy:GroupsGroupSuggestedPrivacy
	title:str
	topics:GroupsGroupTopics
	twitter:GroupsSettingsTwitter
	video:GroupsGroupVideo
	wall:GroupsGroupWall
	website:str
	phone:str
	email:str
	wiki:GroupsGroupWiki

GroupsGetTagListResponse = list[GroupsGroupTag]

class GroupsGetTokenPermissionsResponse(BM):
	mask:int
	permissions:list[GroupsTokenPermissionSetting]

class GroupsGetObjectExtendedResponse(BM):
	count:int
	items:list[GroupsGroupFull]

class GroupsGetResponse(BM):
	count:int
	items:list[int]

class GroupsIsMemberExtendedResponse(BM):
	member:bool
	invitation:bool
	can_invite:bool
	can_recall:bool
	request:bool

GroupsIsMemberResponse = bool

GroupsIsMemberUserIdsExtendedResponse = list[GroupsMemberStatusFull]

GroupsIsMemberUserIdsResponse = list[GroupsMemberStatus]

class GroupsSearchResponse(BM):
	count:int
	items:list[GroupsGroup]


class LeadFormsCreateResponse(BM):
	form_id:int
	url:str

class LeadFormsDeleteResponse(BM):
	form_id:int

class LeadFormsGetLeadsResponse(BM):
	leads:list[LeadFormsLead]
	next_page_token:str

LeadFormsGetResponse = LeadFormsForm

LeadFormsListResponse = list[LeadFormsForm]

LeadFormsUploadUrlResponse = str


class LikesAddResponse(BM):
	likes:int

class LikesDeleteResponse(BM):
	likes:int

class LikesGetListExtendedResponse(BM):
	count:int
	items:list[UsersUserMin]

class LikesGetListResponse(BM):
	count:int
	items:list[int]

class LikesIsLikedResponse(BM):
	liked:bool
	copied:bool


class MarketAddAlbumResponse(BM):
	market_album_id:int
	albums_count:int

class MarketAddResponse(BM):
	market_item_id:int

MarketCreateCommentResponse = int

MarketDeleteCommentResponse = bool

class MarketGetAlbumByIdResponse(BM):
	count:int
	items:list[MarketMarketAlbum]

class MarketGetAlbumsResponse(BM):
	count:int
	items:list[MarketMarketAlbum]

class MarketGetByIdExtendedResponse(BM):
	count:int
	items:list[MarketMarketItemFull]

class MarketGetByIdResponse(BM):
	count:int
	items:list[MarketMarketItem]

class MarketGetCategoriesNewResponse(BM):
	items:list[MarketMarketCategoryTree]

class MarketGetCategoriesResponse(BM):
	count:int
	items:list[MarketMarketCategory]

class MarketGetCommentsResponse(BM):
	count:int
	items:list[WallWallComment]

class MarketGetGroupOrdersResponse(BM):
	count:int
	items:list[MarketOrder]

class MarketGetOrderByIdResponse(BM):
	order:MarketOrder

class MarketGetOrderItemsResponse(BM):
	count:int
	items:list[MarketOrderItem]

class MarketGetOrdersExtendedResponse(BM):
	count:int
	items:list[MarketOrder]
	groups:list[GroupsGroupFull]

class MarketGetOrdersResponse(BM):
	count:int
	items:list[MarketOrder]

class MarketGetExtendedResponse(BM):
	count:int
	items:list[MarketMarketItemFull]
	variants:list[MarketMarketItemFull]

class MarketGetResponse(BM):
	count:int
	items:list[MarketMarketItem]
	variants:list[MarketMarketItem]

MarketRestoreCommentResponse = bool

class MarketSearchExtendedResponse(BM):
	count:int
	view_type:MarketServicesViewType
	items:list[MarketMarketItemFull]
	variants:list[MarketMarketItemFull]

class MarketSearchResponse(BM):
	count:int
	view_type:MarketServicesViewType
	items:list[MarketMarketItem]
	variants:list[MarketMarketItem]
	groups:list[GroupsGroupFull]


MessagesCreateChatResponse = int

class MessagesDeleteChatPhotoResponse(BM):
	message_id:int
	chat:MessagesChat

class MessagesDeleteConversationResponse(BM):
	last_deleted_id:int

MessagesDeleteResponse = bool

MessagesEditResponse = bool

class MessagesGetByConversationMessageIdExtendedResponse(BM):
	count:int
	items:list[MessagesMessage]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class MessagesGetByConversationMessageIdResponse(BM):
	count:int
	items:list[MessagesMessage]

class MessagesGetByIdExtendedResponse(BM):
	count:int
	items:list[MessagesMessage]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class MessagesGetByIdResponse(BM):
	count:int
	items:list[MessagesMessage]

class MessagesGetChatPreviewResponse(BM):
	preview:MessagesChatPreview
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

MessagesGetChatChatIdsFieldsResponse = list[MessagesChatFull]

MessagesGetChatChatIdsResponse = list[MessagesChat]

MessagesGetChatFieldsResponse = MessagesChatFull

MessagesGetChatResponse = MessagesChat

MessagesGetConversationMembersResponse = MessagesGetConversationMembers

MessagesGetConversationsByIdExtendedResponse = MessagesGetConversationByIdExtended

MessagesGetConversationsByIdResponse = MessagesGetConversationById

class MessagesGetConversationsResponse(BM):
	count:int
	unread_count:int
	items:list[MessagesConversationWithMessage]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class MessagesGetHistoryAttachmentsResponse(BM):
	items:list[MessagesHistoryAttachment]
	next_from:str
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class MessagesGetHistoryExtendedResponse(BM):
	count:int
	items:list[MessagesMessage]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	conversations:list[MessagesConversation]

class MessagesGetHistoryResponse(BM):
	count:int
	items:list[MessagesMessage]

class MessagesGetImportantMessagesExtendedResponse(BM):
	messages:MessagesMessagesArray
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	conversations:list[MessagesConversation]

class MessagesGetImportantMessagesResponse(BM):
	messages:MessagesMessagesArray
	profiles:list[UsersUser]
	groups:list[GroupsGroupFull]
	conversations:list[MessagesConversation]

class MessagesGetIntentUsersResponse(BM):
	count:int
	items:list[int]
	profiles:list[UsersUserFull]

class MessagesGetInviteLinkResponse(BM):
	link:str

MessagesGetLastActivityResponse = MessagesLastActivity

class MessagesGetLongPollHistoryResponse(BM):
	history:list[list]
	messages:MessagesLongpollMessages
	credentials:MessagesLongpollParams
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	chats:list[MessagesChat]
	new_pts:int
	from_pts:int
	more:bool
	conversations:list[MessagesConversation]

MessagesGetLongPollServerResponse = MessagesLongpollParams

class MessagesIsMessagesFromGroupAllowedResponse(BM):
	is_allowed:bool

class MessagesJoinChatByInviteLinkResponse(BM):
	chat_id:int

MessagesMarkAsImportantResponse = list[int]

MessagesPinResponse = MessagesPinnedMessage

class MessagesSearchConversationsExtendedResponse(BM):
	count:int
	items:list[MessagesConversation]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class MessagesSearchConversationsResponse(BM):
	count:int
	items:list[MessagesConversation]

class MessagesSearchExtendedResponse(BM):
	count:int
	items:list[MessagesMessage]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	conversations:list[MessagesConversation]

class MessagesSearchResponse(BM):
	count:int
	items:list[MessagesMessage]

MessagesSendResponse = int

MessagesSendUserIdsResponse = list[MessagesSendUserIdsResponseItem]

class MessagesSetChatPhotoResponse(BM):
	message_id:int
	chat:MessagesChat


class NewsfeedGenericResponse(BM):
	items:list[NewsfeedNewsfeedItem]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	new_returned_news_items_count:int

class NewsfeedGetBannedExtendedResponse(BM):
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class NewsfeedGetBannedResponse(BM):
	groups:list[int]
	members:list[int]

class NewsfeedGetCommentsResponse(BM):
	items:list[NewsfeedNewsfeedItem]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	next_from:str

class NewsfeedGetListsExtendedResponse(BM):
	count:int
	items:list[NewsfeedListFull]

class NewsfeedGetListsResponse(BM):
	count:int
	items:list[NewsfeedList]

class NewsfeedGetMentionsResponse(BM):
	count:int
	items:list[WallWallpostToId]

class NewsfeedGetSuggestedSourcesResponse(BM):
	count:int
	items:list[UsersSubscriptionsItem]

class NewsfeedIgnoreItemResponse(BM):
	status:bool

NewsfeedSaveListResponse = int

class NewsfeedSearchExtendedResponse(BM):
	items:list[WallWallpostFull]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]
	suggested_queries:list[str]
	next_from:str
	count:int
	total_count:int

class NewsfeedSearchResponse(BM):
	items:list[WallWallpostFull]
	suggested_queries:list[str]
	next_from:str
	count:int
	total_count:int


NotesAddResponse = int

NotesCreateCommentResponse = int

NotesGetByIdResponse = NotesNote

class NotesGetCommentsResponse(BM):
	count:int
	items:list[NotesNoteComment]

class NotesGetResponse(BM):
	count:int
	items:list[NotesNote]


class NotificationsGetResponse(BM):
	count:int
	items:list[NotificationsNotificationItem]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]
	last_viewed:int
	photos:list[PhotosPhoto]
	videos:list[VideoVideo]
	apps:list[AppsApp]
	next_from:str
	ttl:int

NotificationsMarkAsViewedResponse = bool

NotificationsSendMessageResponse = list[NotificationsSendMessageItem]


OrdersCancelSubscriptionResponse = bool

OrdersChangeStateResponse = str

OrdersGetAmountResponse = list[OrdersAmount]

OrdersGetByIdResponse = list[OrdersOrder]

OrdersGetUserSubscriptionByIdResponse = OrdersSubscription

class OrdersGetUserSubscriptionsResponse(BM):
	count:int
	items:list[OrdersSubscription]

OrdersGetResponse = list[OrdersOrder]

OrdersUpdateSubscriptionResponse = bool


PagesGetHistoryResponse = list[PagesWikipageHistory]

PagesGetTitlesResponse = list[PagesWikipage]

PagesGetVersionResponse = PagesWikipageFull

PagesGetResponse = PagesWikipageFull

PagesParseWikiResponse = str

PagesSaveAccessResponse = int

PagesSaveResponse = int


PhotosCopyResponse = int

PhotosCreateAlbumResponse = PhotosPhotoAlbumFull

PhotosCreateCommentResponse = int

PhotosDeleteCommentResponse = bool

PhotosGetAlbumsCountResponse = int

class PhotosGetAlbumsResponse(BM):
	count:int
	items:list[PhotosPhotoAlbumFull]

class PhotosGetAllCommentsResponse(BM):
	count:int
	items:list[WallWallComment]

class PhotosGetAllExtendedResponse(BM):
	count:int
	items:list[PhotosPhotoFullXtrRealOffset]
	more:bool

class PhotosGetAllResponse(BM):
	count:int
	items:list[PhotosPhotoXtrRealOffset]
	more:bool

PhotosGetByIdResponse = list[PhotosPhoto]

class PhotosGetCommentsExtendedResponse(BM):
	count:int
	real_offset:int
	items:list[WallWallComment]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class PhotosGetCommentsResponse(BM):
	count:int
	real_offset:int
	items:list[WallWallComment]

PhotosGetMarketUploadServerResponse = BaseUploadServer

PhotosGetMessagesUploadServerResponse = PhotosPhotoUpload

class PhotosGetNewTagsResponse(BM):
	count:int
	items:list[PhotosPhotoXtrTagInfo]

PhotosGetTagsResponse = list[PhotosPhotoTag]

PhotosGetUploadServerResponse = PhotosPhotoUpload

class PhotosGetUserPhotosResponse(BM):
	count:int
	items:list[PhotosPhoto]

PhotosGetWallUploadServerResponse = PhotosPhotoUpload

class PhotosGetResponse(BM):
	count:int
	items:list[PhotosPhoto]

class PhotosMarketAlbumUploadResponse(BM):
	gid:int
	hash:str
	photo:str
	server:int

class PhotosMarketUploadResponse(BM):
	crop_data:str
	crop_hash:str
	group_id:int
	hash:str
	photo:str
	server:int

class PhotosMessageUploadResponse(BM):
	hash:str
	photo:str
	server:int

class PhotosOwnerCoverUploadResponse(BM):
	hash:str
	photo:str

class PhotosOwnerUploadResponse(BM):
	hash:str
	photo:str
	server:int

class PhotosPhotoUploadResponse(BM):
	aid:int
	hash:str
	photo:str
	photos_list:str
	server:int

PhotosPutTagResponse = int

PhotosRestoreCommentResponse = bool

PhotosSaveMarketAlbumPhotoResponse = list[PhotosPhoto]

PhotosSaveMarketPhotoResponse = list[PhotosPhoto]

PhotosSaveMessagesPhotoResponse = list[PhotosPhoto]

class PhotosSaveOwnerCoverPhotoResponse(BM):
	images:list[BaseImage]

class PhotosSaveOwnerPhotoResponse(BM):
	photo_hash:str
	photo_src:str
	photo_src_big:str
	photo_src_small:str
	saved:int
	post_id:int

PhotosSaveWallPhotoResponse = list[PhotosPhoto]

PhotosSaveResponse = list[PhotosPhoto]

class PhotosSearchResponse(BM):
	count:int
	items:list[PhotosPhoto]

class PhotosWallUploadResponse(BM):
	hash:str
	photo:str
	server:int


class PodcastsSearchPodcastResponse(BM):
	podcasts:list[PodcastExternalData]
	results_total:int


PollsAddVoteResponse = bool

PollsCreateResponse = PollsPoll

PollsDeleteVoteResponse = bool

PollsGetBackgroundsResponse = list[PollsBackground]

PollsGetByIdResponse = PollsPoll

PollsGetVotersResponse = list[PollsVoters]

PollsSavePhotoResponse = PollsBackground


class PrettyCardsCreateResponse(BM):
	owner_id:int
	card_id:str

class PrettyCardsDeleteResponse(BM):
	owner_id:int
	card_id:str
	error:str

class PrettyCardsEditResponse(BM):
	owner_id:int
	card_id:str

PrettyCardsGetByIdResponse = list[PrettyCardsPrettyCardOrError]

PrettyCardsGetUploadURLResponse = str

class PrettyCardsGetResponse(BM):
	count:int
	items:list[PrettyCardsPrettyCard]


class SearchGetHintsResponse(BM):
	count:int
	items:list[SearchHint]
	suggested_queries:list[str]


SecureCheckTokenResponse = SecureTokenChecked

SecureGetAppBalanceResponse = int

SecureGetSMSHistoryResponse = list[SecureSmsNotification]

SecureGetTransactionsHistoryResponse = list[SecureTransaction]

SecureGetUserLevelResponse = list[SecureLevel]

SecureGiveEventStickerResponse = list[SecureGiveEventStickerItem]

SecureSendNotificationResponse = list[int]

SecureSetCounterArrayResponse = list[SecureSetCounterItem]


StatsGetPostReachResponse = list[StatsWallpostStat]

StatsGetResponse = list[StatsPeriod]


StatusGetResponse = StatusStatus


StorageGetKeysResponse = list[str]

StorageGetResponse = list[StorageValue]


StoreGetFavoriteStickersResponse = list[BaseSticker]

StoreGetProductsResponse = list[StoreProduct]

class StoreGetStickersKeywordsResponse(BM):
	count:int
	dictionary:list[StoreStickersKeyword]
	chunks_count:int
	chunks_hash:str


class StoriesGetBannedExtendedResponse(BM):
	count:int
	items:list[int]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class StoriesGetBannedResponse(BM):
	count:int
	items:list[int]

class StoriesGetByIdExtendedResponse(BM):
	count:int
	items:list[StoriesStory]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class StoriesGetPhotoUploadServerResponse(BM):
	upload_url:str
	user_ids:list[int]

StoriesGetStatsResponse = StoriesStoryStats

class StoriesGetVideoUploadServerResponse(BM):
	upload_url:str
	user_ids:list[int]

class StoriesGetViewersExtendedV5115Response(BM):
	count:int
	items:list[StoriesViewersItem]
	hidden_reason:str
	next_from:str

class StoriesGetViewersExtendedResponse(BM):
	count:int
	items:list[UsersUserFull]

class StoriesGetV5113Response(BM):
	count:int
	items:list[StoriesFeedItem]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroup]
	need_upload_screen:bool

class StoriesGetResponse(BM):
	count:int
	items:list[list]
	promo_data:StoriesPromoBlock
	profiles:list[UsersUserFull]
	groups:list[GroupsGroup]
	need_upload_screen:bool

class StoriesSaveResponse(BM):
	count:int
	items:list[StoriesStory]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]

class StoriesUploadResponse(BM):
	upload_result:str


class StreamingGetServerUrlResponse(BM):
	endpoint:str
	key:str


class UsersGetFollowersFieldsResponse(BM):
	count:int
	items:list[UsersUserFull]

class UsersGetFollowersResponse(BM):
	count:int
	items:list[int]

class UsersGetSubscriptionsExtendedResponse(BM):
	count:int
	items:list[UsersSubscriptionsItem]

class UsersGetSubscriptionsResponse(BM):
	users:UsersUsersArray
	groups:GroupsGroupsArray

UsersGetResponse = list[UsersUserFull]

class UsersSearchResponse(BM):
	count:int
	items:list[UsersUserFull]


UtilsCheckLinkResponse = UtilsLinkChecked

class UtilsGetLastShortenedLinksResponse(BM):
	count:int
	items:list[UtilsLastShortenedLink]

UtilsGetLinkStatsExtendedResponse = UtilsLinkStatsExtended

UtilsGetLinkStatsResponse = UtilsLinkStats

UtilsGetServerTimeResponse = int

UtilsGetShortLinkResponse = UtilsShortLink

UtilsResolveScreenNameResponse = UtilsDomainResolved


class VideoAddAlbumResponse(BM):
	album_id:int

VideoChangeVideoAlbumsResponse = list[int]

VideoCreateCommentResponse = int

VideoGetAlbumByIdResponse = VideoVideoAlbumFull

class VideoGetAlbumsByVideoExtendedResponse(BM):
	count:int
	items:list[VideoVideoAlbumFull]

VideoGetAlbumsByVideoResponse = list[int]

class VideoGetAlbumsExtendedResponse(BM):
	count:int
	items:list[VideoVideoAlbumFull]

class VideoGetAlbumsResponse(BM):
	count:int
	items:list[VideoVideoAlbum]

class VideoGetCommentsExtendedResponse(BM):
	count:int
	items:list[WallWallComment]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]
	current_level_count:int
	can_post:bool
	show_reply_button:bool
	groups_can_post:bool
	real_offset:int

class VideoGetCommentsResponse(BM):
	count:int
	items:list[WallWallComment]
	current_level_count:int
	can_post:bool
	show_reply_button:bool
	groups_can_post:bool
	real_offset:int

class VideoGetResponse(BM):
	count:int
	items:list[VideoVideoFull]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

VideoRestoreCommentResponse = bool

VideoSaveResponse = VideoSaveResult

class VideoSearchExtendedResponse(BM):
	count:int
	items:list[VideoVideoFull]
	profiles:list[UsersUser]
	groups:list[GroupsGroupFull]

class VideoSearchResponse(BM):
	count:int
	items:list[VideoVideoFull]

class VideoUploadResponse(BM):
	size:int
	video_id:int


class WallCreateCommentResponse(BM):
	comment_id:int

class WallEditResponse(BM):
	post_id:int

class WallGetByIdExtendedResponse(BM):
	items:list[WallWallpostFull]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

WallGetByIdLegacyResponse = list[WallWallpostFull]

class WallGetByIdResponse(BM):
	items:list[WallWallpostFull]

class WallGetCommentExtendedResponse(BM):
	items:list[WallWallComment]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]

class WallGetCommentResponse(BM):
	items:list[WallWallComment]

class WallGetCommentsExtendedResponse(BM):
	count:int
	items:list[WallWallComment]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]
	current_level_count:int
	can_post:bool
	show_reply_button:bool
	groups_can_post:bool

class WallGetCommentsResponse(BM):
	count:int
	items:list[WallWallComment]
	current_level_count:int
	can_post:bool
	show_reply_button:bool
	groups_can_post:bool

class WallGetRepostsResponse(BM):
	items:list[WallWallpostFull]
	profiles:list[UsersUser]
	groups:list[GroupsGroup]

class WallGetExtendedResponse(BM):
	count:int
	items:list[WallWallpostFull]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class WallGetResponse(BM):
	count:int
	items:list[WallWallpostFull]

class WallPostAdsStealthResponse(BM):
	post_id:int

class WallPostResponse(BM):
	post_id:int

class WallRepostResponse(BM):
	success:int
	post_id:int
	reposts_count:int
	wall_repost_count:int
	mail_repost_count:int
	likes_count:int

class WallSearchExtendedResponse(BM):
	count:int
	items:list[WallWallpostFull]
	profiles:list[UsersUserFull]
	groups:list[GroupsGroupFull]

class WallSearchResponse(BM):
	count:int
	items:list[WallWallpostFull]


class WidgetsGetCommentsResponse(BM):
	count:int
	posts:list[WidgetsWidgetComment]

class WidgetsGetPagesResponse(BM):
	count:int
	pages:list[WidgetsWidgetPage]


