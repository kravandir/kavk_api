from enum import Enum
from typing import Optional
from .base import BM

class AccountNameRequestStatus(Enum):
	SUCCESS = "success"
	PROCESSING = "processing"
	DECLINED = "declined"
	WAS_ACCEPTED = "was_accepted"
	WAS_DECLINED = "was_declined"
	DECLINED_WITH_LINK = "declined_with_link"
	RESPONSE = "response"
	RESPONSE_WITH_LINK = "response_with_link"

class AccountPushParamsMode(Enum):
	ON = "on"
	OFF = "off"
	NO_SOUND = "no_sound"
	NO_TEXT = "no_text"

class AccountPushParamsOnoff(Enum):
	ON = "on"
	OFF = "off"

class AccountPushParamsSettings(Enum):
	ON = "on"
	OFF = "off"
	FR_OF_FR = "fr_of_fr"

class AccountAccountCounters(BM):
	app_requests:Optional[int] = None
	events:Optional[int] = None
	faves:Optional[int] = None
	friends:Optional[int] = None
	friends_suggestions:Optional[int] = None
	friends_recommendations:Optional[int] = None
	gifts:Optional[int] = None
	groups:Optional[int] = None
	menu_discover_badge:Optional[int] = None
	menu_clips_badge:Optional[int] = None
	messages:Optional[int] = None
	memories:Optional[int] = None
	notes:Optional[int] = None
	notifications:Optional[int] = None
	photos:Optional[int] = None
	sdk:Optional[int] = None


class AccountInfo(BM):
	wishlists_ae_promo_banner_show:Optional[bool] = None
	_2fa_required:Optional[bool] = None
	country:Optional[str] = None
	https_required:Optional[bool] = None
	intro:Optional[bool] = None
	show_vk_apps_intro:Optional[bool] = None
	mini_apps_ads_slot_id:Optional[int] = None
	qr_promotion:Optional[int] = None
	link_redirects:Optional[object] = None
	lang:Optional[int] = None
	no_wall_replies:Optional[bool] = None
	own_posts_default:Optional[bool] = None
	subscriptions:Optional[object] = None


class AccountNameRequest(BM):
	first_name:Optional[str] = None
	id:Optional[int] = None
	last_name:Optional[str] = None
	status:Optional["AccountNameRequestStatus"] = None
	lang:Optional[str] = None
	link_href:Optional[str] = None
	link_label:Optional[str] = None


class AccountOffer(BM):
	description:Optional[str] = None
	id:Optional[int] = None
	img:Optional[str] = None
	instruction:Optional[str] = None
	instruction_html:Optional[str] = None
	price:Optional[int] = None
	short_description:Optional[str] = None
	tag:Optional[str] = None
	title:Optional[str] = None
	currency_amount:Optional[int] = None
	link_id:Optional[int] = None
	link_type:Optional[str] = None


class AccountPushConversations(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class AccountPushConversationsItem(BM):
	disabled_until:Optional[int] = None
	peer_id:Optional[int] = None
	sound:Optional[bool] = None
	disabled_mentions:Optional[bool] = None
	disabled_mass_mentions:Optional[bool] = None


class AccountPushParams(BM):
	msg:Optional[list[list]] = None
	chat:Optional[list[list]] = None
	like:Optional[list[list]] = None
	repost:Optional[list[list]] = None
	comment:Optional[list[list]] = None
	mention:Optional[list[list]] = None
	reply:Optional[list[list]] = None
	new_post:Optional[list[list]] = None
	wall_post:Optional[list[list]] = None
	wall_publish:Optional[list[list]] = None
	friend:Optional[list[list]] = None
	friend_found:Optional[list[list]] = None
	friend_accepted:Optional[list[list]] = None
	group_invite:Optional[list[list]] = None
	group_accepted:Optional[list[list]] = None
	birthday:Optional[list[list]] = None
	event_soon:Optional[list[list]] = None
	app_request:Optional[list[list]] = None
	sdk_open:Optional[list[list]] = None


class AccountPushSettings(BM):
	disabled:Optional[bool] = None
	disabled_until:Optional[int] = None
	settings:Optional["AccountPushParams"] = None
	conversations:Optional["AccountPushConversations"] = None


class AccountSubscriptions(BM):
	pass

class AccountUserSettingsInterest(BM):
	title:Optional[str] = None
	value:Optional[str] = None


class AccountUserSettingsInterests(BM):
	activities:Optional["AccountUserSettingsInterest"] = None
	interests:Optional["AccountUserSettingsInterest"] = None
	music:Optional["AccountUserSettingsInterest"] = None
	tv:Optional["AccountUserSettingsInterest"] = None
	movies:Optional["AccountUserSettingsInterest"] = None
	books:Optional["AccountUserSettingsInterest"] = None
	games:Optional["AccountUserSettingsInterest"] = None
	quotes:Optional["AccountUserSettingsInterest"] = None
	about:Optional["AccountUserSettingsInterest"] = None




class AddressesFields(Enum):
	ID = "id"
	TITLE = "title"
	ADDRESS = "address"
	ADDITIONAL_ADDRESS = "additional_address"
	COUNTRY_ID = "country_id"
	CITY_ID = "city_id"
	METRO_STATION_ID = "metro_station_id"
	LATITUDE = "latitude"
	LONGITUDE = "longitude"
	DISTANCE = "distance"
	WORK_INFO_STATUS = "work_info_status"
	TIMETABLE = "timetable"
	PHONE = "phone"
	TIME_OFFSET = "time_offset"



class AdsAccessRole(Enum):
	ADMIN = "admin"
	MANAGER = "manager"
	REPORTS = "reports"

class AdsAccessRolePublic(Enum):
	MANAGER = "manager"
	REPORTS = "reports"

class AdsAccountType(Enum):
	GENERAL = "general"
	AGENCY = "agency"

class AdsAdApproved(Enum):
	NOT_MODERATED = 0
	PENDING_MODERATION = 1
	APPROVED = 2
	REJECTED = 3

class AdsAdCostType(Enum):
	PER_CLICKS = 0
	PER_IMPRESSIONS = 1
	PER_ACTIONS = 2
	PER_IMPRESSIONS_OPTIMIZED = 3

class AdsAdStatus(Enum):
	STOPPED = 0
	STARTED = 1
	DELETED = 2

class AdsCampaignStatus(Enum):
	STOPPED = 0
	STARTED = 1
	DELETED = 2

class AdsCampaignType(Enum):
	NORMAL = "normal"
	VK_APPS_MANAGED = "vk_apps_managed"
	MOBILE_APPS = "mobile_apps"
	PROMOTED_POSTS = "promoted_posts"
	ADAPTIVE_ADS = "adaptive_ads"
	STORIES = "stories"

class AdsCriteriaSex(Enum):
	ANY = 0
	MALE = 1
	FEMALE = 2

class AdsObjectType(Enum):
	AD = "ad"
	CAMPAIGN = "campaign"
	CLIENT = "client"
	OFFICE = "office"

class AdsStatsSexValue(Enum):
	FEMALE = "f"
	MALE = "m"

class AdsTargSuggestionsSchoolsType(Enum):
	SCHOOL = "school"
	UNIVERSITY = "university"
	FACULTY = "faculty"
	CHAIR = "chair"

class AdsAccesses(BM):
	client_id:Optional[str] = None
	role:Optional["AdsAccessRole"] = None


class AdsAccount(BM):
	access_role:Optional["AdsAccessRole"] = None
	account_id:Optional[int] = None
	account_status:Optional[bool] = None
	account_type:Optional["AdsAccountType"] = None
	account_name:Optional[str] = None
	can_view_budget:Optional[bool] = None


class AdsAd(BM):
	ad_format:Optional[int] = None
	ad_platform:Optional[list[int|str]] = None
	all_limit:Optional[int] = None
	approved:Optional["AdsAdApproved"] = None
	campaign_id:Optional[int] = None
	category1_id:Optional[int] = None
	category2_id:Optional[int] = None
	cost_type:Optional["AdsAdCostType"] = None
	cpc:Optional[int] = None
	cpm:Optional[int] = None
	cpa:Optional[int] = None
	ocpm:Optional[int] = None
	autobidding_max_cost:Optional[int] = None
	disclaimer_medical:Optional[bool] = None
	disclaimer_specialist:Optional[bool] = None
	disclaimer_supplements:Optional[bool] = None
	id:Optional[int] = None
	impressions_limit:Optional[int] = None
	impressions_limited:Optional[bool] = None
	name:Optional[str] = None
	status:Optional["AdsAdStatus"] = None
	video:Optional[bool] = None


class AdsAdLayout(BM):
	ad_format:Optional[int] = None
	campaign_id:Optional[int] = None
	cost_type:Optional["AdsAdCostType"] = None
	description:Optional[str] = None
	id:Optional[str] = None
	image_src:Optional[str] = None
	image_src_2x:Optional[str] = None
	link_domain:Optional[str] = None
	link_url:Optional[str] = None
	preview_link:Optional[str] = None
	title:Optional[str] = None
	video:Optional[bool] = None


class AdsCampaign(BM):
	ads_count:Optional[int] = None
	all_limit:Optional[str] = None
	create_time:Optional[int] = None
	goal_type:Optional[int] = None
	user_goal_type:Optional[int] = None
	is_cbo_enabled:Optional[bool] = None
	day_limit:Optional[str] = None
	id:Optional[int] = None
	name:Optional[str] = None
	start_time:Optional[int] = None
	status:Optional["AdsCampaignStatus"] = None
	stop_time:Optional[int] = None
	type:Optional["AdsCampaignType"] = None
	update_time:Optional[int] = None
	views_limit:Optional[int] = None


class AdsCategory(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	subcategories:Optional[list[list]] = None


class AdsClient(BM):
	all_limit:Optional[str] = None
	day_limit:Optional[str] = None
	id:Optional[int] = None
	name:Optional[str] = None


class AdsCreateAdStatus(BM):
	id:Optional[int] = None
	post_id:Optional[int] = None
	error_code:Optional[int] = None
	error_desc:Optional[str] = None


class AdsCreateCampaignStatus(BM):
	id:Optional[int] = None
	error_code:Optional[int] = None
	error_desc:Optional[str] = None


class AdsCriteria(BM):
	age_from:Optional[int] = None
	age_to:Optional[int] = None
	apps:Optional[str] = None
	apps_not:Optional[str] = None
	birthday:Optional[int] = None
	cities:Optional[str] = None
	cities_not:Optional[str] = None
	country:Optional[int] = None
	districts:Optional[str] = None
	groups:Optional[str] = None
	interest_categories:Optional[str] = None
	interests:Optional[str] = None
	paying:Optional[bool] = None
	positions:Optional[str] = None
	religions:Optional[str] = None
	retargeting_groups:Optional[str] = None
	retargeting_groups_not:Optional[str] = None
	school_from:Optional[int] = None
	school_to:Optional[int] = None
	schools:Optional[str] = None
	sex:Optional["AdsCriteriaSex"] = None
	stations:Optional[str] = None
	statuses:Optional[str] = None
	streets:Optional[str] = None
	travellers:Optional["BasePropertyExists"] = None
	uni_from:Optional[int] = None
	uni_to:Optional[int] = None
	user_browsers:Optional[str] = None
	user_devices:Optional[str] = None
	user_os:Optional[str] = None


class AdsDemoStats(BM):
	id:Optional[int] = None
	stats:Optional["AdsDemostatsFormat"] = None
	type:Optional["AdsObjectType"] = None


class AdsDemostatsFormat(BM):
	age:Optional[list[list]] = None
	cities:Optional[list[list]] = None
	day:Optional[str] = None
	month:Optional[str] = None
	overall:Optional[int] = None
	sex:Optional[list[list]] = None
	sex_age:Optional[list[list]] = None


class AdsFloodStats(BM):
	left:Optional[int] = None
	refresh:Optional[int] = None


class AdsLinkStatus(BM):
	description:Optional[str] = None
	redirect_url:Optional[str] = None
	status:Optional[str] = None


class AdsLookalikeRequest(BM):
	id:Optional[int] = None
	create_time:Optional[int] = None
	update_time:Optional[int] = None
	scheduled_delete_time:Optional[int] = None
	status:Optional[str] = None
	source_type:Optional[str] = None
	source_retargeting_group_id:Optional[int] = None
	source_name:Optional[str] = None
	audience_count:Optional[int] = None
	save_audience_levels:Optional[list[list]] = None


class AdsLookalikeRequestSaveAudienceLevel(BM):
	level:Optional[int] = None
	audience_count:Optional[int] = None


class AdsMusician(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	avatar:Optional[str] = None


class AdsParagraphs(BM):
	paragraph:Optional[str] = None


class AdsPromotedPostReach(BM):
	hide:Optional[int] = None
	id:Optional[int] = None
	join_group:Optional[int] = None
	links:Optional[int] = None
	reach_subscribers:Optional[int] = None
	reach_total:Optional[int] = None
	report:Optional[int] = None
	to_group:Optional[int] = None
	unsubscribe:Optional[int] = None
	video_views_100p:Optional[int] = None
	video_views_25p:Optional[int] = None
	video_views_3s:Optional[int] = None
	video_views_50p:Optional[int] = None
	video_views_75p:Optional[int] = None
	video_views_start:Optional[int] = None


class AdsRejectReason(BM):
	comment:Optional[str] = None
	rules:Optional[list[list]] = None


class AdsRules(BM):
	paragraphs:Optional[list[list]] = None
	title:Optional[str] = None


class AdsStats(BM):
	id:Optional[int] = None
	stats:Optional["AdsStatsFormat"] = None
	type:Optional["AdsObjectType"] = None
	views_times:Optional["AdsStatsViewsTimes"] = None


class AdsStatsAge(BM):
	clicks_rate:Optional[int] = None
	impressions_rate:Optional[int] = None
	value:Optional[str] = None


class AdsStatsCities(BM):
	clicks_rate:Optional[int] = None
	impressions_rate:Optional[int] = None
	name:Optional[str] = None
	value:Optional[int] = None


class AdsStatsFormat(BM):
	clicks:Optional[int] = None
	link_external_clicks:Optional[int] = None
	day:Optional[str] = None
	impressions:Optional[int] = None
	join_rate:Optional[int] = None
	month:Optional[str] = None
	overall:Optional[int] = None
	reach:Optional[int] = None
	spent:Optional[int] = None
	video_clicks_site:Optional[int] = None
	video_views:Optional[int] = None
	video_views_full:Optional[int] = None
	video_views_half:Optional[int] = None


class AdsStatsSex(BM):
	clicks_rate:Optional[int] = None
	impressions_rate:Optional[int] = None
	value:Optional["AdsStatsSexValue"] = None


class AdsStatsSexAge(BM):
	clicks_rate:Optional[int] = None
	impressions_rate:Optional[int] = None
	value:Optional[str] = None


class AdsStatsViewsTimes(BM):
	views_ads_times_1:Optional[int] = None
	views_ads_times_2:Optional[int] = None
	views_ads_times_3:Optional[int] = None
	views_ads_times_4:Optional[int] = None
	views_ads_times_5:Optional[str] = None
	views_ads_times_6:Optional[int] = None
	views_ads_times_7:Optional[int] = None
	views_ads_times_8:Optional[int] = None
	views_ads_times_9:Optional[int] = None
	views_ads_times_10:Optional[int] = None
	views_ads_times_11_plus:Optional[int] = None


class AdsTargStats(BM):
	audience_count:Optional[int] = None
	recommended_cpc:Optional[int] = None
	recommended_cpm:Optional[int] = None
	recommended_cpc_50:Optional[int] = None
	recommended_cpm_50:Optional[int] = None
	recommended_cpc_70:Optional[int] = None
	recommended_cpm_70:Optional[int] = None
	recommended_cpc_90:Optional[int] = None
	recommended_cpm_90:Optional[int] = None


class AdsTargSuggestions(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class AdsTargSuggestionsCities(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	parent:Optional[str] = None


class AdsTargSuggestionsRegions(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	type:Optional[str] = None


class AdsTargSuggestionsSchools(BM):
	desc:Optional[str] = None
	id:Optional[int] = None
	name:Optional[str] = None
	parent:Optional[str] = None
	type:Optional["AdsTargSuggestionsSchoolsType"] = None


class AdsTargetGroup(BM):
	audience_count:Optional[int] = None
	domain:Optional[str] = None
	id:Optional[int] = None
	lifetime:Optional[int] = None
	name:Optional[str] = None
	pixel:Optional[str] = None


class AdsUpdateOfficeUsersResult(BM):
	user_id:Optional[int] = None
	is_success:Optional[bool] = None
	error:Optional["BaseError"] = None


class AdsUserSpecification(BM):
	user_id:Optional[int] = None
	role:Optional["AdsAccessRolePublic"] = None
	grant_access_to_all_clients:Optional[bool] = None
	client_ids:Optional[list[list]] = None
	view_budget:Optional[bool] = None


class AdsUserSpecificationCutted(BM):
	user_id:Optional[int] = None
	role:Optional["AdsAccessRolePublic"] = None
	client_id:Optional[int] = None
	view_budget:Optional[bool] = None


class AdsUsers(BM):
	accesses:Optional[list[list]] = None
	user_id:Optional[int] = None




class AdswebGetAdCategoriesResponseCategoriesCategory(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class AdswebGetAdUnitsResponseAdUnitsAdUnit(BM):
	id:Optional[int] = None
	site_id:Optional[int] = None
	name:Optional[str] = None


class AdswebGetFraudHistoryResponseEntriesEntry(BM):
	site_id:Optional[int] = None
	day:Optional[str] = None


class AdswebGetSitesResponseSitesSite(BM):
	id:Optional[int] = None
	status_user:Optional[str] = None
	status_moder:Optional[str] = None
	domains:Optional[str] = None


class AdswebGetStatisticsResponseItemsItem(BM):
	site_id:Optional[int] = None
	ad_unit_id:Optional[int] = None
	overall_count:Optional[int] = None
	months_count:Optional[int] = None
	month_min:Optional[str] = None
	month_max:Optional[str] = None
	days_count:Optional[int] = None
	day_min:Optional[str] = None
	day_max:Optional[str] = None
	hours_count:Optional[int] = None
	hour_min:Optional[str] = None
	hour_max:Optional[str] = None




class AppWidgetsPhoto(BM):
	id:Optional[str] = None
	images:Optional[list[list]] = None


class AppWidgetsPhotos(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None




class AppsAppLeaderboardType(Enum):
	NOT_SUPPORTED = 0
	LEVELS = 1
	POINTS = 2

class AppsAppType(Enum):
	APP = "app"
	GAME = "game"
	SITE = "site"
	STANDALONE = "standalone"
	VK_APP = "vk_app"
	COMMUNITY_APP = "community_app"
	HTML5_GAME = "html5_game"
	MINI_APP = "mini_app"

class AppsAppMin(BM):
	type:Optional["AppsAppType"] = None
	id:Optional[int] = None
	title:Optional[str] = None
	author_owner_id:Optional[int] = None
	is_installed:Optional[bool] = None
	icon_139:Optional[str] = None
	icon_150:Optional[str] = None
	icon_278:Optional[str] = None
	icon_576:Optional[str] = None
	background_loader_color:Optional[str] = None
	loader_icon:Optional[str] = None
	icon_75:Optional[str] = None


class AppsCatalogList(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None
	profiles:Optional[list[list]] = None


class AppsLeaderboard(BM):
	level:Optional[int] = None
	points:Optional[int] = None
	score:Optional[int] = None
	user_id:Optional[int] = None


class AppsScope(BM):
	name:Optional[str] = None
	title:Optional[str] = None




class AudioAudio(BM):
	access_key:Optional[str] = None
	artist:Optional[str] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None
	url:Optional[str] = None
	duration:Optional[int] = None
	date:Optional[int] = None
	album_id:Optional[int] = None
	genre_id:Optional[int] = None
	performer:Optional[str] = None




class bool(Enum):
	NO = 0
	YES = 1

class BaseLinkButtonActionType(Enum):
	OPEN_URL = "open_url"

class BaseLinkButtonStyle(Enum):
	PRIMARY = "primary"
	SECONDARY = "secondary"

class BaseLinkProductStatus(Enum):
	ACTIVE = "active"
	BLOCKED = "blocked"
	SOLD = "sold"
	DELETED = "deleted"
	ARCHIVED = "archived"

class BasePropertyExists(Enum):
	PROPERTY_EXISTS = 1

class BaseSex(Enum):
	UNKNOWN = 0
	FEMALE = 1
	MALE = 2

class BaseUserGroupFields(Enum):
	ABOUT = "about"
	ACTION_BUTTON = "action_button"
	ACTIVITIES = "activities"
	ACTIVITY = "activity"
	ADDRESSES = "addresses"
	ADMIN_LEVEL = "admin_level"
	AGE_LIMITS = "age_limits"
	AUTHOR_ID = "author_id"
	BAN_INFO = "ban_info"
	BDATE = "bdate"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	BOOKS = "books"
	CAN_CREATE_TOPIC = "can_create_topic"
	CAN_MESSAGE = "can_message"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAREER = "career"
	CITY = "city"
	COMMON_COUNT = "common_count"
	CONNECTIONS = "connections"
	CONTACTS = "contacts"
	COUNTERS = "counters"
	COUNTRY = "country"
	COVER = "cover"
	CROP_PHOTO = "crop_photo"
	DEACTIVATED = "deactivated"
	DESCRIPTION = "description"
	DOMAIN = "domain"
	EDUCATION = "education"
	EXPORTS = "exports"
	FINISH_DATE = "finish_date"
	FIXED_POST = "fixed_post"
	FOLLOWERS_COUNT = "followers_count"
	FRIEND_STATUS = "friend_status"
	GAMES = "games"
	HAS_MARKET_APP = "has_market_app"
	HAS_MOBILE = "has_mobile"
	HAS_PHOTO = "has_photo"
	HOME_TOWN = "home_town"
	ID = "id"
	INTERESTS = "interests"
	IS_ADMIN = "is_admin"
	IS_CLOSED = "is_closed"
	IS_FAVORITE = "is_favorite"
	IS_FRIEND = "is_friend"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	IS_MEMBER = "is_member"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	IS_SUBSCRIBED = "is_subscribed"
	LAST_SEEN = "last_seen"
	LINKS = "links"
	LISTS = "lists"
	MAIDEN_NAME = "maiden_name"
	MAIN_ALBUM_ID = "main_album_id"
	MAIN_SECTION = "main_section"
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	MEMBERS_COUNT = "members_count"
	MILITARY = "military"
	MOVIES = "movies"
	MUSIC = "music"
	NAME = "name"
	NICKNAME = "nickname"
	OCCUPATION = "occupation"
	ONLINE = "online"
	ONLINE_STATUS = "online_status"
	PERSONAL = "personal"
	PHONE = "phone"
	PHOTO_100 = "photo_100"
	PHOTO_200 = "photo_200"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_50 = "photo_50"
	PHOTO_ID = "photo_id"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	QUOTES = "quotes"
	RELATION = "relation"
	RELATIVES = "relatives"
	SCHOOLS = "schools"
	SCREEN_NAME = "screen_name"
	SEX = "sex"
	SITE = "site"
	START_DATE = "start_date"
	STATUS = "status"
	TIMEZONE = "timezone"
	TRENDING = "trending"
	TV = "tv"
	TYPE = "type"
	UNIVERSITIES = "universities"
	VERIFIED = "verified"
	WALL_COMMENTS = "wall_comments"
	WIKI_PAGE = "wiki_page"
	FIRST_NAME = "first_name"
	FIRST_NAME_ACC = "first_name_acc"
	FIRST_NAME_DAT = "first_name_dat"
	FIRST_NAME_GEN = "first_name_gen"
	LAST_NAME = "last_name"
	LAST_NAME_ACC = "last_name_acc"
	LAST_NAME_DAT = "last_name_dat"
	LAST_NAME_GEN = "last_name_gen"
	CAN_SUBSCRIBE_STORIES = "can_subscribe_stories"
	IS_SUBSCRIBED_STORIES = "is_subscribed_stories"
	VK_ADMIN_STATUS = "vk_admin_status"
	CAN_UPLOAD_STORY = "can_upload_story"

class BaseCity(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class BaseCommentsInfo(BM):
	can_post:Optional[bool] = None
	can_open:Optional[bool] = None
	can_close:Optional[bool] = None
	count:Optional[int] = None
	groups_can_post:Optional[bool] = None
	donut:Optional["WallWallpostCommentsDonut"] = None


class BaseCountry(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class BaseCropPhoto(BM):
	photo:Optional["PhotosPhoto"] = None
	crop:Optional["BaseCropPhotoCrop"] = None
	rect:Optional["BaseCropPhotoRect"] = None


class BaseCropPhotoCrop(BM):
	x:Optional[int] = None
	y:Optional[int] = None
	x2:Optional[int] = None
	y2:Optional[int] = None


class BaseCropPhotoRect(BM):
	x:Optional[int] = None
	y:Optional[int] = None
	x2:Optional[int] = None
	y2:Optional[int] = None


class BaseError(BM):
	error_code:Optional[int] = None
	error_subcode:Optional[int] = None
	error_msg:Optional[str] = None
	error_text:Optional[str] = None
	request_params:Optional[list[list]] = None


class BaseGeo(BM):
	coordinates:Optional["BaseGeoCoordinates"] = None
	place:Optional["BasePlace"] = None
	showmap:Optional[int] = None
	type:Optional[str] = None


class BaseGeoCoordinates(BM):
	latitude:Optional[int] = None
	longitude:Optional[int] = None


class BaseGradientPoint(BM):
	color:Optional[str] = None
	position:Optional[int] = None


class BaseImage(BM):
	id:Optional[str] = None
	url:Optional[str] = None
	width:Optional[int] = None
	height:Optional[int] = None


class BaseLikes(BM):
	count:Optional[int] = None
	user_likes:Optional[bool] = None


class BaseLikesInfo(BM):
	can_like:Optional[bool] = None
	can_publish:Optional[bool] = None
	count:Optional[int] = None
	user_likes:Optional[int] = None


class BaseLink(BM):
	application:Optional["BaseLinkApplication"] = None
	button:Optional["BaseLinkButton"] = None
	caption:Optional[str] = None
	description:Optional[str] = None
	id:Optional[str] = None
	is_favorite:Optional[bool] = None
	photo:Optional["PhotosPhoto"] = None
	preview_page:Optional[str] = None
	preview_url:Optional[str] = None
	product:Optional["BaseLinkProduct"] = None
	rating:Optional["BaseLinkRating"] = None
	title:Optional[str] = None
	url:Optional[str] = None
	target_object:Optional["LinkTargetObject"] = None
	is_external:Optional[bool] = None
	video:Optional["VideoVideo"] = None


class BaseLinkApplication(BM):
	app_id:Optional[int] = None
	store:Optional["BaseLinkApplicationStore"] = None


class BaseLinkApplicationStore(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class BaseLinkButton(BM):
	action:Optional["BaseLinkButtonAction"] = None
	title:Optional[str] = None
	block_id:Optional[str] = None
	section_id:Optional[str] = None
	curator_id:Optional[int] = None
	album_id:Optional[int] = None
	owner_id:Optional[int] = None
	icon:Optional[str] = None
	style:Optional["BaseLinkButtonStyle"] = None


class BaseLinkButtonAction(BM):
	type:Optional["BaseLinkButtonActionType"] = None
	url:Optional[str] = None
	consume_reason:Optional[str] = None


class BaseLinkProduct(BM):
	price:Optional["MarketPrice"] = None
	merchant:Optional[str] = None
	orders_count:Optional[int] = None


class BaseLinkProductCategory(BM):
	pass

class BaseLinkRating(BM):
	reviews_count:Optional[int] = None
	stars:Optional[int] = None


class BaseMessageError(BM):
	code:Optional[int] = None
	description:Optional[str] = None


class BaseObject(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class BaseObjectCount(BM):
	count:Optional[int] = None


class BaseObjectWithName(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class BasePlace(BM):
	address:Optional[str] = None
	checkins:Optional[int] = None
	city:Optional[str] = None
	country:Optional[str] = None
	created:Optional[int] = None
	icon:Optional[str] = None
	id:Optional[int] = None
	latitude:Optional[int] = None
	longitude:Optional[int] = None
	title:Optional[str] = None
	type:Optional[str] = None


class BaseRepostsInfo(BM):
	count:Optional[int] = None
	wall_count:Optional[int] = None
	mail_count:Optional[int] = None
	user_reposted:Optional[int] = None


class BaseRequestParam(BM):
	key:Optional[str] = None
	value:Optional[str] = None


class BaseSticker(BM):
	pass

class BaseStickerAnimation(BM):
	type:Optional[str] = None
	url:Optional[str] = None


class BaseStickerNew(BM):
	sticker_id:Optional[int] = None
	product_id:Optional[int] = None
	images:Optional[list[list]] = None
	images_with_background:Optional[list[list]] = None
	animation_url:Optional[str] = None
	animations:Optional[list[list]] = None
	is_allowed:Optional[bool] = None


class BaseStickerOld(BM):
	id:Optional[int] = None
	product_id:Optional[int] = None
	width:Optional[int] = None
	height:Optional[int] = None
	photo_128:Optional[str] = None
	photo_256:Optional[str] = None
	photo_352:Optional[str] = None
	photo_512:Optional[str] = None
	photo_64:Optional[str] = None
	is_allowed:Optional[bool] = None


class BaseStickersList(BM):
	pass

class BaseUploadServer(BM):
	upload_url:Optional[str] = None


class BaseUserId(BM):
	user_id:Optional[int] = None




class BoardDefaultOrder(Enum):
	DESC_UPDATED = 1
	DESC_CREATED = 2
	ASC_UPDATED = -1
	ASC_CREATED = -2

class BoardTopic(BM):
	comments:Optional[int] = None
	created:Optional[int] = None
	created_by:Optional[int] = None
	id:Optional[int] = None
	is_closed:Optional[bool] = None
	is_fixed:Optional[bool] = None
	title:Optional[str] = None
	updated:Optional[int] = None
	updated_by:Optional[int] = None
	first_comment:Optional[str] = None
	last_comment:Optional[str] = None


class BoardTopicComment(BM):
	attachments:Optional[list[list]] = None
	date:Optional[int] = None
	from_id:Optional[int] = None
	id:Optional[int] = None
	real_offset:Optional[int] = None
	text:Optional[str] = None
	can_edit:Optional[bool] = None
	likes:Optional["BaseLikesInfo"] = None




class CallbackGroupJoinType(Enum):
	JOIN = "join"
	UNSURE = "unsure"
	ACCEPTED = "accepted"
	APPROVED = "approved"
	REQUEST = "request"

class CallbackGroupMarket(Enum):
	DISABLED = 0
	OPEN = 1

class CallbackGroupOfficerRole(Enum):
	NONE = 0
	MODERATOR = 1
	EDITOR = 2
	ADMINISTRATOR = 3

class CallbackType(Enum):
	AUDIO_NEW = "audio_new"
	BOARD_POST_NEW = "board_post_new"
	BOARD_POST_EDIT = "board_post_edit"
	BOARD_POST_RESTORE = "board_post_restore"
	BOARD_POST_DELETE = "board_post_delete"
	CONFIRMATION = "confirmation"
	GROUP_LEAVE = "group_leave"
	GROUP_JOIN = "group_join"
	GROUP_CHANGE_PHOTO = "group_change_photo"
	GROUP_CHANGE_SETTINGS = "group_change_settings"
	GROUP_OFFICERS_EDIT = "group_officers_edit"
	LEAD_FORMS_NEW = "lead_forms_new"
	MARKET_COMMENT_NEW = "market_comment_new"
	MARKET_COMMENT_DELETE = "market_comment_delete"
	MARKET_COMMENT_EDIT = "market_comment_edit"
	MARKET_COMMENT_RESTORE = "market_comment_restore"
	MESSAGE_NEW = "message_new"
	MESSAGE_REPLY = "message_reply"
	MESSAGE_EDIT = "message_edit"
	MESSAGE_ALLOW = "message_allow"
	MESSAGE_DENY = "message_deny"
	MESSAGE_READ = "message_read"
	MESSAGE_TYPING_STATE = "message_typing_state"
	MESSAGES_EDIT = "messages_edit"
	PHOTO_NEW = "photo_new"
	PHOTO_COMMENT_NEW = "photo_comment_new"
	PHOTO_COMMENT_DELETE = "photo_comment_delete"
	PHOTO_COMMENT_EDIT = "photo_comment_edit"
	PHOTO_COMMENT_RESTORE = "photo_comment_restore"
	POLL_VOTE_NEW = "poll_vote_new"
	USER_BLOCK = "user_block"
	USER_UNBLOCK = "user_unblock"
	VIDEO_NEW = "video_new"
	VIDEO_COMMENT_NEW = "video_comment_new"
	VIDEO_COMMENT_DELETE = "video_comment_delete"
	VIDEO_COMMENT_EDIT = "video_comment_edit"
	VIDEO_COMMENT_RESTORE = "video_comment_restore"
	WALL_POST_NEW = "wall_post_new"
	WALL_REPLY_NEW = "wall_reply_new"
	WALL_REPLY_EDIT = "wall_reply_edit"
	WALL_REPLY_DELETE = "wall_reply_delete"
	WALL_REPLY_RESTORE = "wall_reply_restore"
	WALL_REPOST = "wall_repost"

class CallbackBase(BM):
	type:Optional[str] = None
	group_id:Optional[int] = None
	event_id:Optional[str] = None
	secret:Optional[str] = None


class CallbackBoardPostDelete(BM):
	topic_owner_id:Optional[int] = None
	topic_id:Optional[int] = None
	id:Optional[int] = None


class CallbackDonutMoneyWithdraw(BM):
	amount:Optional[int] = None
	amount_without_fee:Optional[int] = None


class CallbackDonutMoneyWithdrawError(BM):
	reason:Optional[str] = None


class CallbackDonutSubscriptionCancelled(BM):
	user_id:Optional[int] = None


class CallbackDonutSubscriptionCreate(BM):
	user_id:Optional[int] = None
	amount:Optional[int] = None
	amount_without_fee:Optional[int] = None


class CallbackDonutSubscriptionExpired(BM):
	user_id:Optional[int] = None


class CallbackDonutSubscriptionPriceChanged(BM):
	user_id:Optional[int] = None
	amount_old:Optional[int] = None
	amount_new:Optional[int] = None
	amount_diff:Optional[int] = None
	amount_diff_without_fee:Optional[int] = None


class CallbackDonutSubscriptionProlonged(BM):
	user_id:Optional[int] = None
	amount:Optional[int] = None
	amount_without_fee:Optional[int] = None


class CallbackGroupChangePhoto(BM):
	user_id:Optional[int] = None
	photo:Optional["PhotosPhoto"] = None


class CallbackGroupChangeSettings(BM):
	user_id:Optional[int] = None
	self:Optional[bool] = None


class CallbackGroupJoin(BM):
	user_id:Optional[int] = None
	join_type:Optional["CallbackGroupJoinType"] = None


class CallbackGroupLeave(BM):
	user_id:Optional[int] = None
	self:Optional[bool] = None


class CallbackGroupOfficersEdit(BM):
	admin_id:Optional[int] = None
	user_id:Optional[int] = None
	level_old:Optional["CallbackGroupOfficerRole"] = None
	level_new:Optional["CallbackGroupOfficerRole"] = None


class CallbackGroupSettingsChanges(BM):
	title:Optional[str] = None
	description:Optional[str] = None
	access:Optional["GroupsGroupIsClosed"] = None
	screen_name:Optional[str] = None
	public_category:Optional[int] = None
	public_subcategory:Optional[int] = None
	age_limits:Optional["GroupsGroupFullAgeLimits"] = None
	website:Optional[str] = None
	enable_status_default:Optional["GroupsGroupWall"] = None
	enable_audio:Optional["GroupsGroupAudio"] = None
	enable_video:Optional["GroupsGroupVideo"] = None
	enable_photo:Optional["GroupsGroupPhotos"] = None
	enable_market:Optional["CallbackGroupMarket"] = None


class CallbackLikeAddRemove(BM):
	liker_id:Optional[int] = None
	object_type:Optional[str] = None
	object_owner_id:Optional[int] = None
	object_id:Optional[int] = None
	post_id:Optional[int] = None
	thread_reply_id:Optional[int] = None


class CallbackMarketComment(BM):
	id:Optional[int] = None
	from_id:Optional[int] = None
	date:Optional[int] = None
	text:Optional[str] = None
	market_owner_id:Optional[int] = None
	photo_id:Optional[int] = None


class CallbackMarketCommentDelete(BM):
	owner_id:Optional[int] = None
	id:Optional[int] = None
	user_id:Optional[int] = None
	item_id:Optional[int] = None


class CallbackMessageAllowObject(BM):
	user_id:Optional[int] = None
	key:Optional[str] = None


class CallbackMessageDeny(BM):
	user_id:Optional[int] = None


class CallbackMessageObject(BM):
	client_info:Optional["ClientInfoForBots"] = None
	message:Optional["MessagesMessage"] = None


class CallbackPhotoComment(BM):
	id:Optional[int] = None
	from_id:Optional[int] = None
	date:Optional[int] = None
	text:Optional[str] = None
	photo_owner_id:Optional[int] = None


class CallbackPhotoCommentDelete(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	user_id:Optional[int] = None
	photo_id:Optional[int] = None


class CallbackPollVoteNew(BM):
	owner_id:Optional[int] = None
	poll_id:Optional[int] = None
	option_id:Optional[int] = None
	user_id:Optional[int] = None


class CallbackQrScan(BM):
	user_id:Optional[int] = None
	data:Optional[str] = None
	type:Optional[str] = None
	subtype:Optional[str] = None
	reread:Optional[bool] = None


class CallbackUserBlock(BM):
	admin_id:Optional[int] = None
	user_id:Optional[int] = None
	unblock_date:Optional[int] = None
	reason:Optional[int] = None
	comment:Optional[str] = None


class CallbackUserUnblock(BM):
	admin_id:Optional[int] = None
	user_id:Optional[int] = None
	by_end_date:Optional[int] = None


class CallbackVideoComment(BM):
	id:Optional[int] = None
	from_id:Optional[int] = None
	date:Optional[int] = None
	text:Optional[str] = None
	video_owner_id:Optional[int] = None


class CallbackVideoCommentDelete(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	user_id:Optional[int] = None
	video_id:Optional[int] = None


class CallbackWallCommentDelete(BM):
	owner_id:Optional[int] = None
	id:Optional[int] = None
	user_id:Optional[int] = None
	post_id:Optional[int] = None




class CallsEndState(Enum):
	CANCELED_BY_INITIATOR = "canceled_by_initiator"
	CANCELED_BY_RECEIVER = "canceled_by_receiver"
	REACHED = "reached"

class CallsCall(BM):
	duration:Optional[int] = None
	initiator_id:Optional[int] = None
	receiver_id:Optional[int] = None
	state:Optional["CallsEndState"] = None
	time:Optional[int] = None
	video:Optional[bool] = None
	participants:Optional["CallsParticipants"] = None


class CallsParticipants(BM):
	_list:Optional[list[list]] = None
	count:Optional[int] = None




class ClientInfoForBots(BM):
	button_actions:Optional[list[list]] = None
	keyboard:Optional[bool] = None
	inline_keyboard:Optional[bool] = None
	carousel:Optional[bool] = None
	lang_id:Optional[int] = None




class CommentThread(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None
	can_post:Optional[bool] = None
	show_reply_button:Optional[bool] = None
	groups_can_post:Optional[bool] = None




class DatabaseCityById(BM):
	pass

class DatabaseFaculty(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class DatabaseRegion(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class DatabaseSchool(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class DatabaseStation(BM):
	city_id:Optional[int] = None
	color:Optional[str] = None
	id:Optional[int] = None
	name:Optional[str] = None


class DatabaseUniversity(BM):
	id:Optional[int] = None
	title:Optional[str] = None




class DocsDocAttachmentType(Enum):
	DOC = "doc"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"

class DocsDoc(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None
	size:Optional[int] = None
	ext:Optional[str] = None
	url:Optional[str] = None
	date:Optional[int] = None
	type:Optional[int] = None
	preview:Optional["DocsDocPreview"] = None
	is_licensed:Optional[bool] = None
	access_key:Optional[str] = None
	tags:Optional[list[list]] = None


class DocsDocPreview(BM):
	audio_msg:Optional["DocsDocPreviewAudioMsg"] = None
	graffiti:Optional["DocsDocPreviewGraffiti"] = None
	photo:Optional["DocsDocPreviewPhoto"] = None
	video:Optional["DocsDocPreviewVideo"] = None


class DocsDocPreviewAudioMsg(BM):
	duration:Optional[int] = None
	link_mp3:Optional[str] = None
	link_ogg:Optional[str] = None
	waveform:Optional[list[list]] = None


class DocsDocPreviewGraffiti(BM):
	src:Optional[str] = None
	width:Optional[int] = None
	height:Optional[int] = None


class DocsDocPreviewPhoto(BM):
	sizes:Optional[list[list]] = None


class DocsDocPreviewPhotoSizes(BM):
	src:Optional[str] = None
	width:Optional[int] = None
	height:Optional[int] = None
	type:Optional["PhotosPhotoSizesType"] = None


class DocsDocPreviewVideo(BM):
	src:Optional[str] = None
	width:Optional[int] = None
	height:Optional[int] = None
	file_size:Optional[int] = None


class DocsDocTypes(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	count:Optional[int] = None




class DonutDonatorSubscriptionInfo(BM):
	owner_id:Optional[int] = None
	next_payment_date:Optional[int] = None
	amount:Optional[int] = None
	status:Optional[str] = None




class EventsEventAttach(BM):
	address:Optional[str] = None
	button_text:Optional[str] = None
	friends:Optional[list[list]] = None
	id:Optional[int] = None
	is_favorite:Optional[bool] = None
	member_status:Optional["GroupsGroupFullMemberStatus"] = None
	text:Optional[str] = None
	time:Optional[int] = None




class FaveBookmarkType(Enum):
	POST = "post"
	VIDEO = "video"
	PRODUCT = "product"
	ARTICLE = "article"
	LINK = "link"

class FavePageType(Enum):
	USER = "user"
	GROUP = "group"
	HINTS = "hints"

class FaveBookmark(BM):
	added_date:Optional[int] = None
	link:Optional["BaseLink"] = None
	post:Optional["WallWallpostFull"] = None
	product:Optional["MarketMarketItem"] = None
	seen:Optional[bool] = None
	tags:Optional[list[list]] = None
	type:Optional["FaveBookmarkType"] = None
	video:Optional["VideoVideoFull"] = None


class FavePage(BM):
	description:Optional[str] = None
	group:Optional["GroupsGroupFull"] = None
	tags:Optional[list[list]] = None
	type:Optional["FavePageType"] = None
	updated_date:Optional[int] = None
	user:Optional["UsersUserFull"] = None


class FaveTag(BM):
	id:Optional[int] = None
	name:Optional[str] = None




class FriendsFriendStatusStatus(Enum):
	NOT_A_FRIEND = 0
	OUTCOMING_REQUEST = 1
	INCOMING_REQUEST = 2
	IS_FRIEND = 3

class FriendsFriendStatus(BM):
	friend_status:Optional["FriendsFriendStatusStatus"] = None
	sign:Optional[str] = None
	user_id:Optional[int] = None


class FriendsFriendsList(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class FriendsMutualFriend(BM):
	common_count:Optional[int] = None
	common_friends:Optional[list[list]] = None
	id:Optional[int] = None


class FriendsRequests(BM):
	_from:Optional[str] = None
	mutual:Optional["FriendsRequestsMutual"] = None
	user_id:Optional[int] = None


class FriendsRequestsMutual(BM):
	count:Optional[int] = None
	users:Optional[list[list]] = None


class FriendsRequestsXtrMessage(BM):
	_from:Optional[str] = None
	message:Optional[str] = None
	mutual:Optional["FriendsRequestsMutual"] = None
	user_id:Optional[int] = None




class GiftsGiftPrivacy(Enum):
	NAME_AND_MESSAGE_FOR_ALL = 0
	NAME_FOR_ALL = 1
	NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2

class GiftsGift(BM):
	date:Optional[int] = None
	from_id:Optional[int] = None
	gift:Optional["GiftsLayout"] = None
	gift_hash:Optional[str] = None
	id:Optional[int] = None
	message:Optional[str] = None
	privacy:Optional["GiftsGiftPrivacy"] = None


class GiftsLayout(BM):
	id:Optional[int] = None
	thumb_512:Optional[str] = None
	thumb_256:Optional[str] = None
	thumb_48:Optional[str] = None
	thumb_96:Optional[str] = None
	stickers_product_id:Optional[int] = None
	is_stickers_style:Optional[bool] = None
	build_id:Optional[str] = None
	keywords:Optional[str] = None




class GroupsAddressWorkInfoStatus(Enum):
	NO_INFORMATION = "no_information"
	TEMPORARILY_CLOSED = "temporarily_closed"
	ALWAYS_OPENED = "always_opened"
	TIMETABLE = "timetable"
	FOREVER_CLOSED = "forever_closed"

class GroupsBanInfoReason(Enum):
	OTHER = 0
	SPAM = 1
	VERBAL_ABUSE = 2
	STRONG_LANGUAGE = 3
	FLOOD = 4

class GroupsFields(Enum):
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	IS_FAVORITE = "is_favorite"
	IS_SUBSCRIBED = "is_subscribed"
	IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
	CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
	CITY = "city"
	COUNTRY = "country"
	VERIFIED = "verified"
	DESCRIPTION = "description"
	WIKI_PAGE = "wiki_page"
	MEMBERS_COUNT = "members_count"
	REQUESTS_COUNT = "requests_count"
	COUNTERS = "counters"
	COVER = "cover"
	CAN_POST = "can_post"
	CAN_SUGGEST = "can_suggest"
	CAN_UPLOAD_STORY = "can_upload_story"
	CAN_UPLOAD_DOC = "can_upload_doc"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_UPLOAD_CLIP = "can_upload_clip"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_CREATE_TOPIC = "can_create_topic"
	CROP_PHOTO = "crop_photo"
	ACTIVITY = "activity"
	FIXED_POST = "fixed_post"
	HAS_PHOTO = "has_photo"
	STATUS = "status"
	MAIN_ALBUM_ID = "main_album_id"
	LINKS = "links"
	CONTACTS = "contacts"
	SITE = "site"
	MAIN_SECTION = "main_section"
	SECONDARY_SECTION = "secondary_section"
	WALL = "wall"
	TRENDING = "trending"
	CAN_MESSAGE = "can_message"
	IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	HAS_GROUP_CHANNEL = "has_group_channel"
	GROUP_CHANNEL = "group_channel"
	ONLINE_STATUS = "online_status"
	START_DATE = "start_date"
	FINISH_DATE = "finish_date"
	AGE_LIMITS = "age_limits"
	BAN_INFO = "ban_info"
	ACTION_BUTTON = "action_button"
	AUTHOR_ID = "author_id"
	PHONE = "phone"
	HAS_MARKET_APP = "has_market_app"
	ADDRESSES = "addresses"
	LIVE_COVERS = "live_covers"
	IS_ADULT = "is_adult"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	WARNING_NOTIFICATION = "warning_notification"
	MSG_PUSH_ALLOWED = "msg_push_allowed"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	HAS_UNSEEN_STORIES = "has_unseen_stories"
	IS_BUSINESS = "is_business"
	TEXTLIVES_COUNT = "textlives_count"
	MEMBERS_COUNT_TEXT = "members_count_text"

class GroupsFilter(Enum):
	ADMIN = "admin"
	EDITOR = "editor"
	MODER = "moder"
	ADVERTISER = "advertiser"
	GROUPS = "groups"
	PUBLICS = "publics"
	EVENTS = "events"
	HAS_ADDRESSES = "has_addresses"

class GroupsGroupAccess(Enum):
	OPEN = 0
	CLOSED = 1
	PRIVATE = 2

class GroupsGroupAdminLevel(Enum):
	MODERATOR = 1
	EDITOR = 2
	ADMINISTRATOR = 3

class GroupsGroupAgeLimits(Enum):
	UNLIMITED = 1
	_16_PLUS = 2
	_18_PLUS = 3

class GroupsGroupAudio(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsGroupDocs(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsGroupFullAgeLimits(Enum):
	NO = 1
	OVER_16 = 2
	OVER_18 = 3

class GroupsGroupFullMemberStatus(Enum):
	NOT_A_MEMBER = 0
	MEMBER = 1
	NOT_SURE = 2
	DECLINED = 3
	HAS_SENT_A_REQUEST = 4
	INVITED = 5

class GroupsGroupFullSection(Enum):
	NONE = 0
	PHOTOS = 1
	TOPICS = 2
	AUDIOS = 3
	VIDEOS = 4
	MARKET = 5
	STORIES = 6
	APPS = 7
	FOLLOWERS = 8
	LINKS = 9
	EVENTS = 10
	PLACES = 11
	CONTACTS = 12
	APP_BTNS = 13
	DOCS = 14
	EVENT_COUNTERS = 15
	GROUP_MESSAGES = 16
	ALBUMS = 24
	CATEGORIES = 26
	ADMIN_HELP = 27
	APP_WIDGET = 31
	PUBLIC_HELP = 32
	HS_DONATION_APP = 33
	HS_MARKET_APP = 34
	ADDRESSES = 35
	ARTIST_PAGE = 36
	PODCAST = 37
	ARTICLES = 39
	ADMIN_TIPS = 40
	MENU = 41
	FIXED_POST = 42
	CHATS = 43
	EVERGREEN_NOTICE = 44
	MUSICIANS = 45
	NARRATIVES = 46
	DONUT_DONATE = 47
	CLIPS = 48
	MARKET_CART = 49
	CURATORS = 50
	MARKET_SERVICES = 51
	CLASSIFIEDS = 53
	TEXTLIVES = 54
	DONUT_FOR_DONS = 55
	BADGES = 57
	CHATS_CREATION = 58

class GroupsGroupIsClosed(Enum):
	OPEN = 0
	CLOSED = 1
	PRIVATE = 2

class GroupsGroupMarketCurrency(Enum):
	RUSSIAN_RUBLES = 643
	UKRAINIAN_HRYVNIA = 980
	KAZAKH_TENGE = 398
	EURO = 978
	US_DOLLARS = 840

class GroupsGroupPhotos(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsGroupRole(Enum):
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	ADVERTISER = "advertiser"

class GroupsGroupSubject(Enum):
	AUTO = 1
	ACTIVITY_HOLIDAYS = 2
	BUSINESS = 3
	PETS = 4
	HEALTH = 5
	DATING_AND_COMMUNICATION = 6
	GAMES = 7
	IT = 8
	CINEMA = 9
	BEAUTY_AND_FASHION = 10
	COOKING = 11
	ART_AND_CULTURE = 12
	LITERATURE = 13
	MOBILE_SERVICES_AND_INTERNET = 14
	MUSIC = 15
	SCIENCE_AND_TECHNOLOGY = 16
	REAL_ESTATE = 17
	NEWS_AND_MEDIA = 18
	SECURITY = 19
	EDUCATION = 20
	HOME_AND_RENOVATIONS = 21
	POLITICS = 22
	FOOD = 23
	INDUSTRY = 24
	TRAVEL = 25
	WORK = 26
	ENTERTAINMENT = 27
	RELIGION = 28
	FAMILY = 29
	SPORTS = 30
	INSURANCE = 31
	TELEVISION = 32
	GOODS_AND_SERVICES = 33
	HOBBIES = 34
	FINANCE = 35
	PHOTO = 36
	ESOTERICS = 37
	ELECTRONICS_AND_APPLIANCES = 38
	EROTIC = 39
	HUMOR = 40
	SOCIETY_HUMANITIES = 41
	DESIGN_AND_GRAPHICS = 42

class GroupsGroupSuggestedPrivacy(Enum):
	NONE = 0
	ALL = 1
	SUBSCRIBERS = 2

class GroupsGroupTopics(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsGroupType(Enum):
	GROUP = "group"
	PAGE = "page"
	EVENT = "event"

class GroupsGroupVideo(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsGroupWall(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2
	CLOSED = 3

class GroupsGroupWiki(Enum):
	DISABLED = 0
	OPEN = 1
	LIMITED = 2

class GroupsMarketState(Enum):
	NONE = "none"
	BASIC = "basic"
	ADVANCED = "advanced"

class GroupsMemberRolePermission(Enum):
	ADS = "ads"

class GroupsMemberRoleStatus(Enum):
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"
	ADVERTISER = "advertiser"

class GroupsOnlineStatusType(Enum):
	NONE = "none"
	ONLINE = "online"
	ANSWER_MARK = "answer_mark"

class GroupsOwnerXtrBanInfoType(Enum):
	GROUP = "group"
	PROFILE = "profile"

class GroupsRoleOptions(Enum):
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"

class GroupsAddress(BM):
	additional_address:Optional[str] = None
	address:Optional[str] = None
	city_id:Optional[int] = None
	country_id:Optional[int] = None
	distance:Optional[int] = None
	id:Optional[int] = None
	latitude:Optional[int] = None
	longitude:Optional[int] = None
	metro_station_id:Optional[int] = None
	phone:Optional[str] = None
	time_offset:Optional[int] = None
	timetable:Optional["GroupsAddressTimetable"] = None
	title:Optional[str] = None
	work_info_status:Optional["GroupsAddressWorkInfoStatus"] = None
	place_id:Optional[int] = None


class GroupsAddressTimetable(BM):
	fri:Optional["GroupsAddressTimetableDay"] = None
	mon:Optional["GroupsAddressTimetableDay"] = None
	sat:Optional["GroupsAddressTimetableDay"] = None
	sun:Optional["GroupsAddressTimetableDay"] = None
	thu:Optional["GroupsAddressTimetableDay"] = None
	tue:Optional["GroupsAddressTimetableDay"] = None
	wed:Optional["GroupsAddressTimetableDay"] = None


class GroupsAddressTimetableDay(BM):
	break_close_time:Optional[int] = None
	break_open_time:Optional[int] = None
	close_time:Optional[int] = None
	open_time:Optional[int] = None


class GroupsAddressesInfo(BM):
	is_enabled:Optional[bool] = None
	main_address_id:Optional[int] = None


class GroupsBanInfo(BM):
	admin_id:Optional[int] = None
	comment:Optional[str] = None
	comment_visible:Optional[bool] = None
	is_closed:Optional[bool] = None
	date:Optional[int] = None
	end_date:Optional[int] = None
	reason:Optional["GroupsBanInfoReason"] = None


class GroupsBannedItem(BM):
	pass

class GroupsCallbackServer(BM):
	id:Optional[int] = None
	title:Optional[str] = None
	creator_id:Optional[int] = None
	url:Optional[str] = None
	secret_key:Optional[str] = None
	status:Optional[str] = None


class GroupsCallbackSettings(BM):
	api_version:Optional[str] = None
	events:Optional["GroupsLongPollEvents"] = None


class GroupsContactsItem(BM):
	user_id:Optional[int] = None
	desc:Optional[str] = None
	phone:Optional[str] = None
	email:Optional[str] = None


class GroupsCountersGroup(BM):
	addresses:Optional[int] = None
	albums:Optional[int] = None
	audios:Optional[int] = None
	audio_playlists:Optional[int] = None
	docs:Optional[int] = None
	market:Optional[int] = None
	photos:Optional[int] = None
	topics:Optional[int] = None
	videos:Optional[int] = None
	market_services:Optional[int] = None
	podcasts:Optional[int] = None
	articles:Optional[int] = None
	narratives:Optional[int] = None
	clips:Optional[int] = None
	clips_followers:Optional[int] = None


class GroupsCover(BM):
	enabled:Optional[bool] = None
	images:Optional[list[list]] = None


class GroupsGroup(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	screen_name:Optional[str] = None
	is_closed:Optional["GroupsGroupIsClosed"] = None
	type:Optional["GroupsGroupType"] = None
	is_admin:Optional[bool] = None
	admin_level:Optional["GroupsGroupAdminLevel"] = None
	is_member:Optional[bool] = None
	is_advertiser:Optional[bool] = None
	start_date:Optional[int] = None
	finish_date:Optional[int] = None
	deactivated:Optional[str] = None
	photo_50:Optional[str] = None
	photo_100:Optional[str] = None
	photo_200:Optional[str] = None
	photo_200_orig:Optional[str] = None
	photo_400:Optional[str] = None
	photo_400_orig:Optional[str] = None
	photo_max:Optional[str] = None
	photo_max_orig:Optional[str] = None
	est_date:Optional[str] = None
	public_date_label:Optional[str] = None
	photo_max_size:Optional["GroupsPhotoSize"] = None
	is_video_live_notifications_blocked:Optional[bool] = None
	video_live:Optional["VideoLiveInfo"] = None


class GroupsGroupAttach(BM):
	id:Optional[int] = None
	text:Optional[str] = None
	status:Optional[str] = None
	size:Optional[int] = None
	is_favorite:Optional[bool] = None


class GroupsGroupBanInfo(BM):
	comment:Optional[str] = None
	end_date:Optional[int] = None
	reason:Optional["GroupsBanInfoReason"] = None


class GroupsGroupCategory(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	subcategories:Optional[list[list]] = None


class GroupsGroupCategoryFull(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	page_count:Optional[int] = None
	page_previews:Optional[list[list]] = None
	subcategories:Optional[list[list]] = None


class GroupsGroupCategoryType(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class GroupsGroupPublicCategoryList(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	subcategories:Optional[list[list]] = None


class GroupsGroupTag(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	color:Optional[str] = None
	uses:Optional[int] = None


class GroupsGroupsArray(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class GroupsLinksItem(BM):
	name:Optional[str] = None
	desc:Optional[str] = None
	edit_title:Optional[bool] = None
	id:Optional[int] = None
	photo_100:Optional[str] = None
	photo_50:Optional[str] = None
	url:Optional[str] = None
	image_processing:Optional[bool] = None


class GroupsLiveCovers(BM):
	is_enabled:Optional[bool] = None
	is_scalable:Optional[bool] = None
	story_ids:Optional[list[list]] = None


class GroupsLongPollEvents(BM):
	audio_new:Optional[bool] = None
	board_post_delete:Optional[bool] = None
	board_post_edit:Optional[bool] = None
	board_post_new:Optional[bool] = None
	board_post_restore:Optional[bool] = None
	group_change_photo:Optional[bool] = None
	group_change_settings:Optional[bool] = None
	group_join:Optional[bool] = None
	group_leave:Optional[bool] = None
	group_officers_edit:Optional[bool] = None
	lead_forms_new:Optional[bool] = None
	market_comment_delete:Optional[bool] = None
	market_comment_edit:Optional[bool] = None
	market_comment_new:Optional[bool] = None
	market_comment_restore:Optional[bool] = None
	market_order_new:Optional[bool] = None
	market_order_edit:Optional[bool] = None
	message_allow:Optional[bool] = None
	message_deny:Optional[bool] = None
	message_new:Optional[bool] = None
	message_read:Optional[bool] = None
	message_reply:Optional[bool] = None
	message_typing_state:Optional[bool] = None
	message_edit:Optional[bool] = None
	photo_comment_delete:Optional[bool] = None
	photo_comment_edit:Optional[bool] = None
	photo_comment_new:Optional[bool] = None
	photo_comment_restore:Optional[bool] = None
	photo_new:Optional[bool] = None
	poll_vote_new:Optional[bool] = None
	user_block:Optional[bool] = None
	user_unblock:Optional[bool] = None
	video_comment_delete:Optional[bool] = None
	video_comment_edit:Optional[bool] = None
	video_comment_new:Optional[bool] = None
	video_comment_restore:Optional[bool] = None
	video_new:Optional[bool] = None
	wall_post_new:Optional[bool] = None
	wall_reply_delete:Optional[bool] = None
	wall_reply_edit:Optional[bool] = None
	wall_reply_new:Optional[bool] = None
	wall_reply_restore:Optional[bool] = None
	wall_repost:Optional[bool] = None
	donut_subscription_create:Optional[bool] = None
	donut_subscription_prolonged:Optional[bool] = None
	donut_subscription_cancelled:Optional[bool] = None
	donut_subscription_expired:Optional[bool] = None
	donut_subscription_price_changed:Optional[bool] = None
	donut_money_withdraw:Optional[bool] = None
	donut_money_withdraw_error:Optional[bool] = None


class GroupsLongPollServer(BM):
	key:Optional[str] = None
	server:Optional[str] = None
	ts:Optional[str] = None


class GroupsLongPollSettings(BM):
	api_version:Optional[str] = None
	events:Optional["GroupsLongPollEvents"] = None
	is_enabled:Optional[bool] = None


class GroupsMarketInfo(BM):
	type:Optional[str] = None
	contact_id:Optional[int] = None
	currency:Optional["MarketCurrency"] = None
	currency_text:Optional[str] = None
	enabled:Optional[bool] = None
	main_album_id:Optional[int] = None
	price_max:Optional[str] = None
	price_min:Optional[str] = None
	min_order_price:Optional["MarketPrice"] = None


class GroupsMemberRole(BM):
	id:Optional[int] = None
	permissions:Optional[list[list]] = None
	role:Optional["GroupsMemberRoleStatus"] = None


class GroupsMemberStatus(BM):
	member:Optional[bool] = None
	user_id:Optional[int] = None


class GroupsMemberStatusFull(BM):
	can_invite:Optional[bool] = None
	can_recall:Optional[bool] = None
	invitation:Optional[bool] = None
	member:Optional[bool] = None
	request:Optional[bool] = None
	user_id:Optional[int] = None


class GroupsOnlineStatus(BM):
	minutes:Optional[int] = None
	status:Optional["GroupsOnlineStatusType"] = None


class GroupsOwnerXtrBanInfo(BM):
	ban_info:Optional["GroupsBanInfo"] = None
	group:Optional["GroupsGroup"] = None
	profile:Optional["UsersUser"] = None
	type:Optional["GroupsOwnerXtrBanInfoType"] = None


class GroupsPhotoSize(BM):
	height:Optional[int] = None
	width:Optional[int] = None


class GroupsSectionsListItem(BM):
	pass

class GroupsSettingsTwitter(BM):
	status:Optional[str] = None
	name:Optional[str] = None


class GroupsSubjectItem(BM):
	id:Optional[int] = None
	name:Optional[str] = None


class GroupsTokenPermissionSetting(BM):
	name:Optional[str] = None
	setting:Optional[int] = None




class LeadFormsAnswer(BM):
	key:Optional[str] = None
	answer:Optional["Any"] = None


class LeadFormsAnswerItem(BM):
	key:Optional[str] = None
	value:Optional[str] = None


class LeadFormsForm(BM):
	form_id:Optional[int] = None
	group_id:Optional[int] = None
	photo:Optional[str] = None
	name:Optional[str] = None
	title:Optional[str] = None
	description:Optional[str] = None
	confirmation:Optional[str] = None
	site_link_url:Optional[str] = None
	policy_link_url:Optional[str] = None
	questions:Optional[list[list]] = None
	active:Optional[bool] = None
	leads_count:Optional[int] = None
	pixel_code:Optional[str] = None
	once_per_user:Optional[int] = None
	notify_admins:Optional[str] = None
	notify_emails:Optional[str] = None
	url:Optional[str] = None


class LeadFormsLead(BM):
	lead_id:Optional[int] = None
	user_id:Optional[int] = None
	date:Optional[int] = None
	answers:Optional[list[list]] = None
	ad_id:Optional[int] = None


class LeadFormsQuestionItem(BM):
	key:Optional[str] = None
	type:Optional[str] = None
	label:Optional[str] = None
	options:Optional[list[list]] = None


class LeadFormsQuestionItemOption(BM):
	key:Optional[str] = None
	label:Optional[str] = None




class LikesType(Enum):
	POST = "post"
	COMMENT = "comment"
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	NOTE = "note"
	MARKET = "market"
	PHOTO_COMMENT = "photo_comment"
	VIDEO_COMMENT = "video_comment"
	TOPIC_COMMENT = "topic_comment"
	MARKET_COMMENT = "market_comment"
	SITEPAGE = "sitepage"
	TEXTPOST = "textpost"



class LinkTargetObject(BM):
	type:Optional[str] = None
	owner_id:Optional[int] = None
	item_id:Optional[int] = None




class MarketMarketItemAvailability(Enum):
	AVAILABLE = 0
	REMOVED = 1
	UNAVAILABLE = 2

class MarketServicesViewType(Enum):
	CARDS = 1
	ROWS = 2

class MarketCurrency(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	title:Optional[str] = None


class MarketMarketAlbum(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None
	count:Optional[int] = None
	is_main:Optional[bool] = None
	is_hidden:Optional[bool] = None
	photo:Optional["PhotosPhoto"] = None
	updated_time:Optional[int] = None


class MarketMarketCategory(BM):
	pass

class MarketMarketCategoryNested(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	parent:Optional["MarketMarketCategoryNested"] = None


class MarketMarketCategoryOld(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	section:Optional["MarketSection"] = None


class MarketMarketCategoryTree(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	children:Optional[list[list]] = None


class MarketMarketItem(BM):
	access_key:Optional[str] = None
	availability:Optional["MarketMarketItemAvailability"] = None
	button_title:Optional[str] = None
	category:Optional["MarketMarketCategory"] = None
	date:Optional[int] = None
	description:Optional[str] = None
	external_id:Optional[str] = None
	id:Optional[int] = None
	is_favorite:Optional[bool] = None
	owner_id:Optional[int] = None
	price:Optional["MarketPrice"] = None
	thumb_photo:Optional[str] = None
	title:Optional[str] = None
	url:Optional[str] = None
	variants_grouping_id:Optional[int] = None
	is_main_variant:Optional[bool] = None
	sku:Optional[str] = None


class MarketOrder(BM):
	id:Optional[int] = None
	group_id:Optional[int] = None
	user_id:Optional[int] = None
	display_order_id:Optional[str] = None
	date:Optional[int] = None
	status:Optional[int] = None
	items_count:Optional[int] = None
	track_number:Optional[str] = None
	track_link:Optional[str] = None
	comment:Optional[str] = None
	address:Optional[str] = None
	merchant_comment:Optional[str] = None
	weight:Optional[int] = None
	total_price:Optional["MarketPrice"] = None
	preview_order_items:Optional[list[list]] = None
	cancel_info:Optional["BaseLink"] = None


class MarketOrderItem(BM):
	owner_id:Optional[int] = None
	item_id:Optional[int] = None
	price:Optional["MarketPrice"] = None
	quantity:Optional[int] = None
	item:Optional["MarketMarketItem"] = None
	title:Optional[str] = None
	photo:Optional["PhotosPhoto"] = None
	variants:Optional[list[list]] = None


class MarketPrice(BM):
	amount:Optional[str] = None
	currency:Optional["MarketCurrency"] = None
	discount_rate:Optional[int] = None
	old_amount:Optional[str] = None
	text:Optional[str] = None
	old_amount_text:Optional[str] = None


class MarketSection(BM):
	id:Optional[int] = None
	name:Optional[str] = None




class MessagesChatSettingsState(Enum):
	_IN = "in"
	KICKED = "kicked"
	LEFT = "left"

class MessagesConversationPeerType(Enum):
	CHAT = "chat"
	EMAIL = "email"
	USER = "user"
	GROUP = "group"

class MessagesHistoryMessageAttachmentType(Enum):
	PHOTO = "photo"
	VIDEO = "video"
	AUDIO = "audio"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	WALL = "wall"
	SHARE = "share"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"

class MessagesMessageActionStatus(Enum):
	CHAT_PHOTO_UPDATE = "chat_photo_update"
	CHAT_PHOTO_REMOVE = "chat_photo_remove"
	CHAT_CREATE = "chat_create"
	CHAT_TITLE_UPDATE = "chat_title_update"
	CHAT_INVITE_USER = "chat_invite_user"
	CHAT_KICK_USER = "chat_kick_user"
	CHAT_PIN_MESSAGE = "chat_pin_message"
	CHAT_UNPIN_MESSAGE = "chat_unpin_message"
	CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
	CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
	CHAT_SCREENSHOT = "chat_screenshot"

class MessagesMessageAttachmentType(Enum):
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	MARKET_ALBUM = "market_album"
	GIFT = "gift"
	STICKER = "sticker"
	WALL = "wall"
	WALL_REPLY = "wall_reply"
	ARTICLE = "article"
	POLL = "poll"
	CALL = "call"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"

class MessagesTemplateActionTypeNames(Enum):
	TEXT = "text"
	START = "start"
	LOCATION = "location"
	VKPAY = "vkpay"
	OPEN_APP = "open_app"
	OPEN_PHOTO = "open_photo"
	OPEN_LINK = "open_link"
	CALLBACK = "callback"
	INTENT_SUBSCRIBE = "intent_subscribe"
	INTENT_UNSUBSCRIBE = "intent_unsubscribe"

class MessagesAudioMessage(BM):
	access_key:Optional[str] = None
	transcript_error:Optional[int] = None
	duration:Optional[int] = None
	id:Optional[int] = None
	link_mp3:Optional[str] = None
	link_ogg:Optional[str] = None
	owner_id:Optional[int] = None
	waveform:Optional[list[list]] = None


class MessagesChat(BM):
	admin_id:Optional[int] = None
	id:Optional[int] = None
	kicked:Optional[bool] = None
	left:Optional[bool] = None
	photo_100:Optional[str] = None
	photo_200:Optional[str] = None
	photo_50:Optional[str] = None
	push_settings:Optional["MessagesChatPushSettings"] = None
	title:Optional[str] = None
	type:Optional[str] = None
	users:Optional[list[list]] = None
	is_default_photo:Optional[bool] = None
	members_count:Optional[int] = None
	is_group_channel:Optional[bool] = None


class MessagesChatFull(BM):
	admin_id:Optional[int] = None
	id:Optional[int] = None
	kicked:Optional[bool] = None
	left:Optional[bool] = None
	photo_100:Optional[str] = None
	photo_200:Optional[str] = None
	photo_50:Optional[str] = None
	push_settings:Optional["MessagesChatPushSettings"] = None
	title:Optional[str] = None
	type:Optional[str] = None
	users:Optional[list[list]] = None


class MessagesChatPreview(BM):
	admin_id:Optional[int] = None
	joined:Optional[bool] = None
	local_id:Optional[int] = None
	members:Optional[list[list]] = None
	members_count:Optional[int] = None
	title:Optional[str] = None
	is_member:Optional[bool] = None
	photo:Optional["MessagesChatSettingsPhoto"] = None
	is_don:Optional[bool] = None
	is_group_channel:Optional[bool] = None
	button:Optional["BaseLinkButton"] = None


class MessagesChatPushSettings(BM):
	disabled_until:Optional[int] = None
	sound:Optional[bool] = None


class MessagesChatRestrictions(BM):
	admins_promote_users:Optional[bool] = None
	only_admins_edit_info:Optional[bool] = None
	only_admins_edit_pin:Optional[bool] = None
	only_admins_invite:Optional[bool] = None
	only_admins_kick:Optional[bool] = None


class MessagesChatSettings(BM):
	members_count:Optional[int] = None
	friends_count:Optional[int] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None
	pinned_message:Optional["MessagesPinnedMessage"] = None
	state:Optional["MessagesChatSettingsState"] = None
	photo:Optional["MessagesChatSettingsPhoto"] = None
	admin_ids:Optional[list[list]] = None
	active_ids:Optional[list[list]] = None
	is_group_channel:Optional[bool] = None
	acl:Optional["MessagesChatSettingsAcl"] = None
	permissions:Optional["MessagesChatSettingsPermissions"] = None
	is_disappearing:Optional[bool] = None
	theme:Optional[str] = None
	disappearing_chat_link:Optional[str] = None
	is_service:Optional[bool] = None


class MessagesChatSettingsAcl(BM):
	can_change_info:Optional[bool] = None
	can_change_invite_link:Optional[bool] = None
	can_change_pin:Optional[bool] = None
	can_invite:Optional[bool] = None
	can_promote_users:Optional[bool] = None
	can_see_invite_link:Optional[bool] = None
	can_moderate:Optional[bool] = None
	can_copy_chat:Optional[bool] = None
	can_call:Optional[bool] = None
	can_use_mass_mentions:Optional[bool] = None
	can_change_service_type:Optional[bool] = None


class MessagesChatSettingsPermissions(BM):
	invite:Optional[str] = None
	change_info:Optional[str] = None
	change_pin:Optional[str] = None
	use_mass_mentions:Optional[str] = None
	see_invite_link:Optional[str] = None
	call:Optional[str] = None
	change_admins:Optional[str] = None


class MessagesChatSettingsPhoto(BM):
	photo_50:Optional[str] = None
	photo_100:Optional[str] = None
	photo_200:Optional[str] = None
	is_default_photo:Optional[bool] = None
	is_default_call_photo:Optional[bool] = None


class MessagesConversation(BM):
	peer:Optional["MessagesConversationPeer"] = None
	sort_id:Optional["MessagesConversationSortId"] = None
	last_message_id:Optional[int] = None
	last_conversation_message_id:Optional[int] = None
	in_read:Optional[int] = None
	out_read:Optional[int] = None
	unread_count:Optional[int] = None
	is_marked_unread:Optional[bool] = None
	out_read_by:Optional["MessagesOutReadBy"] = None
	important:Optional[bool] = None
	unanswered:Optional[bool] = None
	special_service_type:Optional[str] = None
	message_request_data:Optional["MessagesMessageRequestData"] = None
	mentions:Optional[list[list]] = None
	current_keyboard:Optional["MessagesKeyboard"] = None
	push_settings:Optional["MessagesPushSettings"] = None
	can_write:Optional["MessagesConversationCanWrite"] = None
	chat_settings:Optional["MessagesChatSettings"] = None


class MessagesConversationCanWrite(BM):
	allowed:Optional[bool] = None
	reason:Optional[int] = None


class MessagesConversationMember(BM):
	can_kick:Optional[bool] = None
	invited_by:Optional[int] = None
	is_admin:Optional[bool] = None
	is_owner:Optional[bool] = None
	is_message_request:Optional[bool] = None
	join_date:Optional[int] = None
	request_date:Optional[int] = None
	member_id:Optional[int] = None


class MessagesConversationPeer(BM):
	id:Optional[int] = None
	local_id:Optional[int] = None
	type:Optional["MessagesConversationPeerType"] = None


class MessagesConversationSortId(BM):
	major_id:Optional[int] = None
	minor_id:Optional[int] = None


class MessagesConversationWithMessage(BM):
	conversation:Optional["MessagesConversation"] = None
	last_message:Optional["MessagesMessage"] = None


class MessagesForeignMessage(BM):
	attachments:Optional[list[list]] = None
	conversation_message_id:Optional[int] = None
	date:Optional[int] = None
	from_id:Optional[int] = None
	fwd_messages:Optional[list[list]] = None
	geo:Optional["BaseGeo"] = None
	id:Optional[int] = None
	peer_id:Optional[int] = None
	reply_message:Optional["MessagesForeignMessage"] = None
	text:Optional[str] = None
	update_time:Optional[int] = None
	was_listened:Optional[bool] = None
	payload:Optional[str] = None


class MessagesForward(BM):
	owner_id:Optional[int] = None
	peer_id:Optional[int] = None
	conversation_message_ids:Optional[list[list]] = None
	message_ids:Optional[list[list]] = None
	is_reply:Optional[bool] = None


class MessagesGetConversationById(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class MessagesGetConversationMembers(BM):
	items:Optional[list[list]] = None
	count:Optional[int] = None
	chat_restrictions:Optional["MessagesChatRestrictions"] = None
	profiles:Optional[list[list]] = None
	groups:Optional[list[list]] = None


class MessagesGraffiti(BM):
	access_key:Optional[str] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	url:Optional[str] = None
	width:Optional[int] = None
	height:Optional[int] = None


class MessagesHistoryAttachment(BM):
	attachment:Optional["MessagesHistoryMessageAttachment"] = None
	message_id:Optional[int] = None
	from_id:Optional[int] = None
	forward_level:Optional[int] = None
	was_listened:Optional[bool] = None


class MessagesHistoryMessageAttachment(BM):
	audio:Optional["AudioAudio"] = None
	audio_message:Optional["MessagesAudioMessage"] = None
	doc:Optional["DocsDoc"] = None
	graffiti:Optional["MessagesGraffiti"] = None
	link:Optional["BaseLink"] = None
	market:Optional["MarketMarketItem"] = None
	photo:Optional["PhotosPhoto"] = None
	type:Optional["MessagesHistoryMessageAttachmentType"] = None
	video:Optional["VideoVideo"] = None
	wall:Optional["WallWallpostFull"] = None


class MessagesKeyboard(BM):
	one_time:Optional[bool] = None
	buttons:Optional[list[list]] = None
	author_id:Optional[int] = None
	inline:Optional[bool] = None


class MessagesKeyboardButton(BM):
	action:Optional["MessagesKeyboardButtonPropertyAction"] = None
	color:Optional[str] = None


class MessagesKeyboardButtonActionCallback(BM):
	label:Optional[str] = None
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonActionLocation(BM):
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonActionOpenApp(BM):
	app_id:Optional[int] = None
	hash:Optional[str] = None
	label:Optional[str] = None
	owner_id:Optional[int] = None
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonActionOpenLink(BM):
	label:Optional[str] = None
	link:Optional[str] = None
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonActionOpenPhoto(BM):
	type:Optional[str] = None


class MessagesKeyboardButtonActionText(BM):
	label:Optional[str] = None
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonActionVkpay(BM):
	hash:Optional[str] = None
	payload:Optional[str] = None
	type:Optional[str] = None


class MessagesKeyboardButtonPropertyAction(BM):
	pass

class MessagesLastActivity(BM):
	online:Optional[bool] = None
	time:Optional[int] = None


class MessagesLongpollMessages(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class MessagesLongpollParams(BM):
	server:Optional[str] = None
	key:Optional[str] = None
	ts:Optional[int] = None
	pts:Optional[int] = None


class MessagesMessage(BM):
	action:Optional["MessagesMessageAction"] = None
	admin_author_id:Optional[int] = None
	attachments:Optional[list[list]] = None
	conversation_message_id:Optional[int] = None
	date:Optional[int] = None
	deleted:Optional[bool] = None
	from_id:Optional[int] = None
	fwd_messages:Optional[list[list]] = None
	geo:Optional["BaseGeo"] = None
	id:Optional[int] = None
	important:Optional[bool] = None
	is_hidden:Optional[bool] = None
	is_cropped:Optional[bool] = None
	keyboard:Optional["MessagesKeyboard"] = None
	members_count:Optional[int] = None
	out:Optional[bool] = None
	payload:Optional[str] = None
	peer_id:Optional[int] = None
	random_id:Optional[int] = None
	ref:Optional[str] = None
	ref_source:Optional[str] = None
	reply_message:Optional["MessagesForeignMessage"] = None
	text:Optional[str] = None
	update_time:Optional[int] = None
	was_listened:Optional[bool] = None
	pinned_at:Optional[int] = None
	is_silent:Optional[bool] = None


class MessagesMessageAction(BM):
	conversation_message_id:Optional[int] = None
	email:Optional[str] = None
	member_id:Optional[int] = None
	message:Optional[str] = None
	photo:Optional["MessagesMessageActionPhoto"] = None
	text:Optional[str] = None
	type:Optional["MessagesMessageActionStatus"] = None


class MessagesMessageActionPhoto(BM):
	photo_50:Optional[str] = None
	photo_100:Optional[str] = None
	photo_200:Optional[str] = None


class MessagesMessageAttachment(BM):
	audio:Optional["AudioAudio"] = None
	audio_message:Optional["MessagesAudioMessage"] = None
	call:Optional["CallsCall"] = None
	doc:Optional["DocsDoc"] = None
	gift:Optional["GiftsLayout"] = None
	graffiti:Optional["MessagesGraffiti"] = None
	market:Optional["MarketMarketItem"] = None
	market_market_album:Optional["MarketMarketAlbum"] = None
	photo:Optional["PhotosPhoto"] = None
	sticker:Optional["BaseSticker"] = None
	story:Optional["StoriesStory"] = None
	type:Optional["MessagesMessageAttachmentType"] = None
	video:Optional["VideoVideoFull"] = None
	wall_reply:Optional["WallWallComment"] = None
	poll:Optional["PollsPoll"] = None


class MessagesMessageRequestData(BM):
	status:Optional[str] = None
	inviter_id:Optional[int] = None
	request_date:Optional[int] = None


class MessagesMessagesArray(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class MessagesOutReadBy(BM):
	count:Optional[int] = None
	member_ids:Optional[list[list]] = None


class MessagesPinnedMessage(BM):
	attachments:Optional[list[list]] = None
	conversation_message_id:Optional[int] = None
	id:Optional[int] = None
	date:Optional[int] = None
	from_id:Optional[int] = None
	fwd_messages:Optional[list[list]] = None
	geo:Optional["BaseGeo"] = None
	peer_id:Optional[int] = None
	reply_message:Optional["MessagesForeignMessage"] = None
	text:Optional[str] = None
	keyboard:Optional["MessagesKeyboard"] = None


class MessagesPushSettings(BM):
	disabled_forever:Optional[bool] = None
	disabled_until:Optional[int] = None
	no_sound:Optional[bool] = None
	disabled_mentions:Optional[bool] = None
	disabled_mass_mentions:Optional[bool] = None


class MessagesSendUserIdsResponseItem(BM):
	peer_id:Optional[int] = None
	message_id:Optional[int] = None
	conversation_message_id:Optional[int] = None
	error:Optional["BaseMessageError"] = None




class NewsfeedCommentsFilters(Enum):
	POST = "post"
	PHOTO = "photo"
	VIDEO = "video"
	TOPIC = "topic"
	NOTE = "note"

class NewsfeedIgnoreItemType(Enum):
	POST_ON_THE_WALL = "wall"
	TAG_ON_A_PHOTO = "tag"
	PROFILE_PHOTO = "profilephoto"
	VIDEO = "video"
	PHOTO = "photo"
	AUDIO = "audio"

class NewsfeedItemWallpostFeedbackType(Enum):
	BUTTONS = "buttons"
	STARS = "stars"

class NewsfeedNewsfeedItemType(Enum):
	POST = "post"
	PHOTO = "photo"
	PHOTO_TAG = "photo_tag"
	WALL_PHOTO = "wall_photo"
	FRIEND = "friend"
	AUDIO = "audio"
	VIDEO = "video"
	TOPIC = "topic"
	DIGEST = "digest"
	STORIES = "stories"
	NOTE = "note"
	AUDIO_PLAYLIST = "audio_playlist"
	CLIP = "clip"

class NewsfeedItemAudioAudio(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class NewsfeedItemBase(BM):
	type:Optional["NewsfeedNewsfeedItemType"] = None
	source_id:Optional[int] = None
	date:Optional[int] = None


class NewsfeedItemDigestButton(BM):
	title:Optional[str] = None
	style:Optional[str] = None


class NewsfeedItemDigestFooter(BM):
	style:Optional[str] = None
	text:Optional[str] = None
	button:Optional["NewsfeedItemDigestButton"] = None


class NewsfeedItemDigestFullItem(BM):
	text:Optional[str] = None
	source_name:Optional[str] = None
	attachment_index:Optional[int] = None
	attachment:Optional["WallWallpostAttachment"] = None
	style:Optional[str] = None
	post:Optional["WallWallpost"] = None


class NewsfeedItemDigestHeader(BM):
	title:Optional[str] = None
	subtitle:Optional[str] = None
	style:Optional[str] = None
	button:Optional["NewsfeedItemDigestButton"] = None


class NewsfeedItemDigestItem(BM):
	pass

class NewsfeedItemFriendFriends(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class NewsfeedItemHolidayRecommendationsBlockHeader(BM):
	title:Optional[str] = None
	subtitle:Optional[str] = None
	image:Optional[list[list]] = None
	action:Optional["BaseLinkButtonAction"] = None


class NewsfeedItemPhotoPhotos(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class NewsfeedItemPhotoTagPhotoTags(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class NewsfeedItemPromoButtonAction(BM):
	url:Optional[str] = None
	type:Optional[str] = None
	target:Optional[str] = None


class NewsfeedItemPromoButtonImage(BM):
	width:Optional[int] = None
	height:Optional[int] = None
	url:Optional[str] = None


class NewsfeedItemVideoVideo(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None


class NewsfeedItemWallpostFeedback(BM):
	type:Optional["NewsfeedItemWallpostFeedbackType"] = None
	question:Optional[str] = None
	answers:Optional[list[list]] = None
	stars_count:Optional[int] = None
	gratitude:Optional[str] = None


class NewsfeedItemWallpostFeedbackAnswer(BM):
	title:Optional[str] = None
	id:Optional[str] = None


class NewsfeedList(BM):
	id:Optional[int] = None
	title:Optional[str] = None


class NewsfeedNewsfeedItem(BM):
	pass



class NotesNote(BM):
	read_comments:Optional[int] = None
	can_comment:Optional[bool] = None
	comments:Optional[int] = None
	date:Optional[int] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	text:Optional[str] = None
	text_wiki:Optional[str] = None
	title:Optional[str] = None
	view_url:Optional[str] = None
	privacy_view:Optional[list[list]] = None
	privacy_comment:Optional[list[list]] = None


class NotesNoteComment(BM):
	date:Optional[int] = None
	id:Optional[int] = None
	message:Optional[str] = None
	nid:Optional[int] = None
	oid:Optional[int] = None
	reply_to:Optional[int] = None
	uid:Optional[int] = None




class NotificationsFeedback(BM):
	attachments:Optional[list[list]] = None
	from_id:Optional[int] = None
	geo:Optional["BaseGeo"] = None
	id:Optional[int] = None
	likes:Optional["BaseLikesInfo"] = None
	text:Optional[str] = None
	to_id:Optional[int] = None


class NotificationsNotification(BM):
	date:Optional[int] = None
	feedback:Optional["NotificationsFeedback"] = None
	parent:Optional["NotificationsNotification"] = None
	reply:Optional["NotificationsReply"] = None
	type:Optional[str] = None


class NotificationsNotificationItem(BM):
	pass

class NotificationsNotificationsComment(BM):
	date:Optional[int] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	photo:Optional["PhotosPhoto"] = None
	post:Optional["WallWallpost"] = None
	text:Optional[str] = None
	topic:Optional["BoardTopic"] = None
	video:Optional["VideoVideo"] = None


class NotificationsReply(BM):
	date:Optional[int] = None
	id:Optional[int] = None
	text:Optional[int] = None


class NotificationsSendMessageError(BM):
	code:Optional[int] = None
	description:Optional[str] = None


class NotificationsSendMessageItem(BM):
	user_id:Optional[int] = None
	status:Optional[bool] = None
	error:Optional["NotificationsSendMessageError"] = None




class OauthError(BM):
	error:Optional[str] = None
	error_description:Optional[str] = None
	redirect_uri:Optional[str] = None




class OrdersAmount(BM):
	amounts:Optional[list[list]] = None
	currency:Optional[str] = None


class OrdersAmountItem(BM):
	amount:Optional[int] = None
	description:Optional[str] = None
	votes:Optional[str] = None


class OrdersOrder(BM):
	amount:Optional[str] = None
	app_order_id:Optional[str] = None
	cancel_transaction_id:Optional[str] = None
	date:Optional[str] = None
	id:Optional[str] = None
	item:Optional[str] = None
	receiver_id:Optional[str] = None
	status:Optional[str] = None
	transaction_id:Optional[str] = None
	user_id:Optional[str] = None


class OrdersSubscription(BM):
	cancel_reason:Optional[str] = None
	create_time:Optional[int] = None
	id:Optional[int] = None
	item_id:Optional[str] = None
	next_bill_time:Optional[int] = None
	expire_time:Optional[int] = None
	pending_cancel:Optional[bool] = None
	period:Optional[int] = None
	period_start_time:Optional[int] = None
	price:Optional[int] = None
	title:Optional[str] = None
	app_id:Optional[int] = None
	application_name:Optional[str] = None
	photo_url:Optional[str] = None
	status:Optional[str] = None
	test_mode:Optional[bool] = None
	trial_expire_time:Optional[int] = None
	update_time:Optional[int] = None




class OwnerState(BM):
	state:Optional[int] = None
	description:Optional[str] = None




class PagesPrivacySettings(Enum):
	COMMUNITY_MANAGERS_ONLY = 0
	COMMUNITY_MEMBERS_ONLY = 1
	EVERYONE = 2

class PagesWikipage(BM):
	creator_id:Optional[int] = None
	creator_name:Optional[str] = None
	editor_id:Optional[int] = None
	editor_name:Optional[str] = None
	group_id:Optional[int] = None
	id:Optional[int] = None
	title:Optional[str] = None
	views:Optional[int] = None
	who_can_edit:Optional["PagesPrivacySettings"] = None
	who_can_view:Optional["PagesPrivacySettings"] = None


class PagesWikipageFull(BM):
	created:Optional[int] = None
	creator_id:Optional[int] = None
	current_user_can_edit:Optional[bool] = None
	current_user_can_edit_access:Optional[bool] = None
	edited:Optional[int] = None
	editor_id:Optional[int] = None
	group_id:Optional[int] = None
	html:Optional[str] = None
	id:Optional[int] = None
	source:Optional[str] = None
	title:Optional[str] = None
	view_url:Optional[str] = None
	views:Optional[int] = None
	who_can_edit:Optional["PagesPrivacySettings"] = None
	who_can_view:Optional["PagesPrivacySettings"] = None
	url:Optional[str] = None
	parent:Optional[str] = None
	parent2:Optional[str] = None
	owner_id:Optional[int] = None


class PagesWikipageHistory(BM):
	id:Optional[int] = None
	length:Optional[int] = None
	date:Optional[int] = None
	editor_id:Optional[int] = None
	editor_name:Optional[str] = None




class PhotosImageType(Enum):
	S = "s"
	M = "m"
	X = "x"
	L = "l"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	Y = "y"
	Z = "z"
	W = "w"

class PhotosPhotoSizesType(Enum):
	S = "s"
	M = "m"
	X = "x"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	K = "k"
	L = "l"
	Y = "y"
	Z = "z"
	C = "c"
	W = "w"
	A = "a"
	B = "b"
	E = "e"
	I = "i"
	D = "d"
	J = "j"
	TEMP = "temp"
	H = "h"
	G = "g"
	N = "n"
	F = "f"
	MAX = "max"

class PhotosImage(BM):
	height:Optional[int] = None
	type:Optional["PhotosImageType"] = None
	url:Optional[str] = None
	width:Optional[int] = None


class PhotosPhoto(BM):
	access_key:Optional[str] = None
	album_id:Optional[int] = None
	date:Optional[int] = None
	height:Optional[int] = None
	id:Optional[int] = None
	images:Optional[list[list]] = None
	lat:Optional[int] = None
	long:Optional[int] = None
	owner_id:Optional[int] = None
	photo_256:Optional[str] = None
	can_comment:Optional[bool] = None
	place:Optional[str] = None
	post_id:Optional[int] = None
	sizes:Optional[list[list]] = None
	text:Optional[str] = None
	user_id:Optional[int] = None
	width:Optional[int] = None
	has_tags:Optional[bool] = None
	likes:Optional["BaseLikes"] = None
	comments:Optional["BaseObjectCount"] = None
	reposts:Optional["BaseRepostsInfo"] = None
	tags:Optional["BaseObjectCount"] = None


class PhotosPhotoAlbum(BM):
	created:Optional[int] = None
	description:Optional[str] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	size:Optional[int] = None
	thumb:Optional["PhotosPhoto"] = None
	title:Optional[str] = None
	updated:Optional[int] = None


class PhotosPhotoAlbumFull(BM):
	can_upload:Optional[bool] = None
	comments_disabled:Optional[bool] = None
	created:Optional[int] = None
	description:Optional[str] = None
	can_delete:Optional[bool] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	size:Optional[int] = None
	sizes:Optional[list[list]] = None
	thumb_id:Optional[int] = None
	thumb_is_last:Optional[bool] = None
	thumb_src:Optional[str] = None
	title:Optional[str] = None
	updated:Optional[int] = None
	upload_by_admins_only:Optional[bool] = None


class PhotosPhotoFalseable(BM):
	pass

class PhotosPhotoFullXtrRealOffset(BM):
	access_key:Optional[str] = None
	album_id:Optional[int] = None
	can_comment:Optional[bool] = None
	comments:Optional["BaseObjectCount"] = None
	date:Optional[int] = None
	height:Optional[int] = None
	hidden:Optional["BasePropertyExists"] = None
	id:Optional[int] = None
	lat:Optional[int] = None
	likes:Optional["BaseLikes"] = None
	long:Optional[int] = None
	owner_id:Optional[int] = None
	photo_1280:Optional[str] = None
	photo_130:Optional[str] = None
	photo_2560:Optional[str] = None
	photo_604:Optional[str] = None
	photo_75:Optional[str] = None
	photo_807:Optional[str] = None
	post_id:Optional[int] = None
	real_offset:Optional[int] = None
	reposts:Optional["BaseObjectCount"] = None
	sizes:Optional[list[list]] = None
	tags:Optional["BaseObjectCount"] = None
	text:Optional[str] = None
	user_id:Optional[int] = None
	width:Optional[int] = None


class PhotosPhotoSizes(BM):
	height:Optional[int] = None
	url:Optional[str] = None
	src:Optional[str] = None
	type:Optional["PhotosPhotoSizesType"] = None
	width:Optional[int] = None


class PhotosPhotoTag(BM):
	date:Optional[int] = None
	id:Optional[int] = None
	placer_id:Optional[int] = None
	tagged_name:Optional[str] = None
	description:Optional[str] = None
	user_id:Optional[int] = None
	viewed:Optional[bool] = None
	x:Optional[int] = None
	x2:Optional[int] = None
	y:Optional[int] = None
	y2:Optional[int] = None


class PhotosPhotoUpload(BM):
	album_id:Optional[int] = None
	upload_url:Optional[str] = None
	fallback_upload_url:Optional[str] = None
	user_id:Optional[int] = None
	group_id:Optional[int] = None


class PhotosPhotoXtrRealOffset(BM):
	access_key:Optional[str] = None
	album_id:Optional[int] = None
	date:Optional[int] = None
	height:Optional[int] = None
	hidden:Optional["BasePropertyExists"] = None
	id:Optional[int] = None
	lat:Optional[int] = None
	long:Optional[int] = None
	owner_id:Optional[int] = None
	photo_1280:Optional[str] = None
	photo_130:Optional[str] = None
	photo_2560:Optional[str] = None
	photo_604:Optional[str] = None
	photo_75:Optional[str] = None
	photo_807:Optional[str] = None
	post_id:Optional[int] = None
	real_offset:Optional[int] = None
	sizes:Optional[list[list]] = None
	text:Optional[str] = None
	user_id:Optional[int] = None
	width:Optional[int] = None


class PhotosPhotoXtrTagInfo(BM):
	access_key:Optional[str] = None
	album_id:Optional[int] = None
	date:Optional[int] = None
	height:Optional[int] = None
	id:Optional[int] = None
	lat:Optional[int] = None
	long:Optional[int] = None
	owner_id:Optional[int] = None
	photo_1280:Optional[str] = None
	photo_130:Optional[str] = None
	photo_2560:Optional[str] = None
	photo_604:Optional[str] = None
	photo_75:Optional[str] = None
	photo_807:Optional[str] = None
	placer_id:Optional[int] = None
	post_id:Optional[int] = None
	sizes:Optional[list[list]] = None
	tag_created:Optional[int] = None
	tag_id:Optional[int] = None
	text:Optional[str] = None
	user_id:Optional[int] = None
	width:Optional[int] = None


class PhotosTagsSuggestionItem(BM):
	title:Optional[str] = None
	caption:Optional[str] = None
	type:Optional[str] = None
	buttons:Optional[list[list]] = None
	photo:Optional["PhotosPhoto"] = None
	tags:Optional[list[list]] = None
	track_code:Optional[str] = None


class PhotosTagsSuggestionItemButton(BM):
	title:Optional[str] = None
	action:Optional[str] = None
	style:Optional[str] = None




class PodcastCover(BM):
	sizes:Optional[list[list]] = None


class PodcastExternalData(BM):
	url:Optional[str] = None
	owner_url:Optional[str] = None
	title:Optional[str] = None
	owner_name:Optional[str] = None
	cover:Optional["PodcastCover"] = None




class PollsAnswer(BM):
	id:Optional[int] = None
	rate:Optional[int] = None
	text:Optional[str] = None
	votes:Optional[int] = None


class PollsBackground(BM):
	angle:Optional[int] = None
	color:Optional[str] = None
	height:Optional[int] = None
	id:Optional[int] = None
	name:Optional[str] = None
	images:Optional[list[list]] = None
	points:Optional[list[list]] = None
	type:Optional[str] = None
	width:Optional[int] = None


class PollsFriend(BM):
	id:Optional[int] = None


class PollsPoll(BM):
	anonymous:Optional["PollsPollAnonymous"] = None
	friends:Optional[list[list]] = None
	multiple:Optional[bool] = None
	answer_id:Optional[int] = None
	end_date:Optional[int] = None
	answer_ids:Optional[list[list]] = None
	closed:Optional[bool] = None
	is_board:Optional[bool] = None
	can_edit:Optional[bool] = None
	can_vote:Optional[bool] = None
	can_report:Optional[bool] = None
	can_share:Optional[bool] = None
	embed_hash:Optional[str] = None
	photo:Optional["PollsBackground"] = None
	answers:Optional[list[list]] = None
	created:Optional[int] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	author_id:Optional[int] = None
	question:Optional[str] = None
	background:Optional["PollsBackground"] = None
	votes:Optional[int] = None
	disable_unvote:Optional[bool] = None


class PollsPollAnonymous(BM):
	pass

class PollsVoters(BM):
	answer_id:Optional[int] = None
	users:Optional["PollsVotersUsers"] = None


class PollsVotersUsers(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None




class PrettyCardsPrettyCard(BM):
	button:Optional["Any"] = None
	button_text:Optional[str] = None
	card_id:Optional[str] = None
	images:Optional[list[list]] = None
	link_url:Optional[str] = None
	photo:Optional[str] = None
	price:Optional[str] = None
	price_old:Optional[str] = None
	title:Optional[str] = None


class PrettyCardsPrettyCardOrError(BM):
	pass



class SearchHintSection(Enum):
	GROUPS = "groups"
	EVENTS = "events"
	PUBLICS = "publics"
	CORRESPONDENTS = "correspondents"
	PEOPLE = "people"
	FRIENDS = "friends"
	MUTUAL_FRIENDS = "mutual_friends"
	PROMO = "promo"

class SearchHintType(Enum):
	GROUP = "group"
	PROFILE = "profile"
	VK_APP = "vk_app"
	APP = "app"
	HTML5_GAME = "html5_game"
	LINK = "link"

class SearchHint(BM):
	app:Optional["AppsApp"] = None
	description:Optional[str] = None
	_global:Optional[bool] = None
	group:Optional["GroupsGroup"] = None
	profile:Optional["UsersUserMin"] = None
	section:Optional["SearchHintSection"] = None
	type:Optional["SearchHintType"] = None
	link:Optional["BaseLink"] = None




class SecureGiveEventStickerItem(BM):
	user_id:Optional[int] = None
	status:Optional[str] = None


class SecureLevel(BM):
	level:Optional[int] = None
	uid:Optional[int] = None


class SecureSetCounterItem(BM):
	id:Optional[int] = None
	result:Optional[bool] = None


class SecureSmsNotification(BM):
	app_id:Optional[str] = None
	date:Optional[str] = None
	id:Optional[str] = None
	message:Optional[str] = None
	user_id:Optional[str] = None


class SecureTokenChecked(BM):
	date:Optional[int] = None
	expire:Optional[int] = None
	success:Optional[int] = None
	user_id:Optional[int] = None


class SecureTransaction(BM):
	date:Optional[int] = None
	id:Optional[int] = None
	uid_from:Optional[int] = None
	uid_to:Optional[int] = None
	votes:Optional[int] = None




class StatsActivity(BM):
	comments:Optional[int] = None
	copies:Optional[int] = None
	hidden:Optional[int] = None
	likes:Optional[int] = None
	subscribed:Optional[int] = None
	unsubscribed:Optional[int] = None


class StatsCity(BM):
	count:Optional[int] = None
	name:Optional[str] = None
	value:Optional[int] = None


class StatsCountry(BM):
	code:Optional[str] = None
	count:Optional[int] = None
	name:Optional[str] = None
	value:Optional[int] = None


class StatsPeriod(BM):
	activity:Optional["StatsActivity"] = None
	period_from:Optional[int] = None
	period_to:Optional[int] = None
	reach:Optional["StatsReach"] = None
	visitors:Optional["StatsViews"] = None


class StatsReach(BM):
	age:Optional[list[list]] = None
	cities:Optional[list[list]] = None
	countries:Optional[list[list]] = None
	mobile_reach:Optional[int] = None
	reach:Optional[int] = None
	reach_subscribers:Optional[int] = None
	sex:Optional[list[list]] = None
	sex_age:Optional[list[list]] = None


class StatsSexAge(BM):
	count:Optional[int] = None
	value:Optional[str] = None
	reach:Optional[int] = None
	reach_subscribers:Optional[int] = None
	count_subscribers:Optional[int] = None


class StatsViews(BM):
	age:Optional[list[list]] = None
	cities:Optional[list[list]] = None
	countries:Optional[list[list]] = None
	mobile_views:Optional[int] = None
	sex:Optional[list[list]] = None
	sex_age:Optional[list[list]] = None
	views:Optional[int] = None
	visitors:Optional[int] = None


class StatsWallpostStat(BM):
	post_id:Optional[int] = None
	hide:Optional[int] = None
	join_group:Optional[int] = None
	links:Optional[int] = None
	reach_subscribers:Optional[int] = None
	reach_subscribers_count:Optional[int] = None
	reach_total:Optional[int] = None
	reach_total_count:Optional[int] = None
	reach_viral:Optional[int] = None
	reach_ads:Optional[int] = None
	report:Optional[int] = None
	to_group:Optional[int] = None
	unsubscribe:Optional[int] = None
	sex_age:Optional[list[list]] = None




class StatusStatus(BM):
	text:Optional[str] = None
	audio:Optional["AudioAudio"] = None




class StickersImageSet(BM):
	base_url:Optional[str] = None
	version:Optional[int] = None




class StorageValue(BM):
	key:Optional[str] = None
	value:Optional[str] = None




class StoreProduct(BM):
	id:Optional[int] = None
	type:Optional[str] = None
	is_new:Optional[bool] = None
	purchased:Optional[bool] = None
	active:Optional[bool] = None
	promoted:Optional[bool] = None
	purchase_date:Optional[int] = None
	title:Optional[str] = None
	stickers:Optional["BaseStickersList"] = None
	style_sticker_ids:Optional[list[list]] = None
	icon:Optional["StoreProductIcon"] = None
	previews:Optional[list[list]] = None
	has_animation:Optional[bool] = None
	subtitle:Optional[str] = None
	payment_region:Optional[str] = None


class StoreProductIcon(BM):
	pass

class StoreStickersKeyword(BM):
	words:Optional[list[list]] = None
	user_stickers:Optional["StoreStickersKeywordStickers"] = None
	promoted_stickers:Optional["StoreStickersKeywordStickers"] = None
	stickers:Optional[list[list]] = None


class StoreStickersKeywordSticker(BM):
	pack_id:Optional[int] = None
	sticker_id:Optional[int] = None


class StoreStickersKeywordStickers(BM):
	pass



class StoriesStoryStatsState(Enum):
	ON = "on"
	OFF = "off"
	HIDDEN = "hidden"

class StoriesStoryType(Enum):
	PHOTO = "photo"
	VIDEO = "video"
	LIVE_ACTIVE = "live_active"
	LIVE_FINISHED = "live_finished"
	BIRTHDAY_INVITE = "birthday_invite"

class StoriesUploadLinkText(Enum):
	TO_STORE = "to_store"
	VOTE = "vote"
	MORE = "more"
	BOOK = "book"
	ORDER = "order"
	ENROLL = "enroll"
	FILL = "fill"
	SIGNUP = "signup"
	BUY = "buy"
	TICKET = "ticket"
	WRITE = "write"
	OPEN = "open"
	LEARN_MORE = "learn_more"
	VIEW = "view"
	GO_TO = "go_to"
	CONTACT = "contact"
	WATCH = "watch"
	PLAY = "play"
	INSTALL = "install"
	READ = "read"
	CALENDAR = "calendar"

class StoriesClickableArea(BM):
	x:Optional[int] = None
	y:Optional[int] = None


class StoriesClickableSticker(BM):
	clickable_area:Optional[list[list]] = None
	id:Optional[int] = None
	hashtag:Optional[str] = None
	link_object:Optional["BaseLink"] = None
	mention:Optional[str] = None
	tooltip_text:Optional[str] = None
	owner_id:Optional[int] = None
	story_id:Optional[int] = None
	question:Optional[str] = None
	question_button:Optional[str] = None
	place_id:Optional[int] = None
	market_item:Optional["MarketMarketItem"] = None
	audio:Optional["AudioAudio"] = None
	audio_start_time:Optional[int] = None
	style:Optional[str] = None
	type:Optional[str] = None
	subtype:Optional[str] = None
	post_owner_id:Optional[int] = None
	post_id:Optional[int] = None
	poll:Optional["PollsPoll"] = None
	color:Optional[str] = None
	sticker_id:Optional[int] = None
	sticker_pack_id:Optional[int] = None
	app:Optional["AppsAppMin"] = None
	app_context:Optional[str] = None
	has_new_interactions:Optional[bool] = None
	is_broadcast_notify_allowed:Optional[bool] = None
	situational_theme_id:Optional[int] = None
	situational_app_url:Optional[str] = None


class StoriesClickableStickers(BM):
	clickable_stickers:Optional[list[list]] = None
	original_height:Optional[int] = None
	original_width:Optional[int] = None


class StoriesFeedItem(BM):
	type:Optional[str] = None
	id:Optional[str] = None
	stories:Optional[list[list]] = None
	grouped:Optional[list[list]] = None
	app:Optional["AppsAppMin"] = None
	promo_data:Optional["StoriesPromoBlock"] = None
	birthday_user_id:Optional[int] = None
	track_code:Optional[str] = None
	has_unseen:Optional[bool] = None
	name:Optional[str] = None


class StoriesPromoBlock(BM):
	name:Optional[str] = None
	photo_50:Optional[str] = None
	photo_100:Optional[str] = None
	not_animated:Optional[bool] = None


class StoriesReplies(BM):
	count:Optional[int] = None
	new:Optional[int] = None


class StoriesStatLine(BM):
	name:Optional[str] = None
	counter:Optional[int] = None
	is_unavailable:Optional[bool] = None


class StoriesStory(BM):
	access_key:Optional[str] = None
	can_comment:Optional[bool] = None
	can_reply:Optional[bool] = None
	can_see:Optional[bool] = None
	can_like:Optional[bool] = None
	can_share:Optional[bool] = None
	can_hide:Optional[bool] = None
	date:Optional[int] = None
	expires_at:Optional[int] = None
	id:Optional[int] = None
	is_deleted:Optional[bool] = None
	is_expired:Optional[bool] = None
	link:Optional["StoriesStoryLink"] = None
	owner_id:Optional[int] = None
	parent_story:Optional["StoriesStory"] = None
	parent_story_access_key:Optional[str] = None
	parent_story_id:Optional[int] = None
	parent_story_owner_id:Optional[int] = None
	photo:Optional["PhotosPhoto"] = None
	replies:Optional["StoriesReplies"] = None
	seen:Optional[bool] = None
	type:Optional["StoriesStoryType"] = None
	clickable_stickers:Optional["StoriesClickableStickers"] = None
	video:Optional["VideoVideoFull"] = None
	views:Optional[int] = None
	can_ask:Optional[bool] = None
	can_ask_anonymous:Optional[bool] = None
	narratives_count:Optional[int] = None
	first_narrative_title:Optional[str] = None
	birthday_wish_user_id:Optional[int] = None
	can_use_in_narrative:Optional[bool] = None


class StoriesStoryLink(BM):
	text:Optional[str] = None
	url:Optional[str] = None
	link_url_target:Optional[str] = None


class StoriesStoryStats(BM):
	answer:Optional["StoriesStoryStatsStat"] = None
	bans:Optional["StoriesStoryStatsStat"] = None
	open_link:Optional["StoriesStoryStatsStat"] = None
	replies:Optional["StoriesStoryStatsStat"] = None
	shares:Optional["StoriesStoryStatsStat"] = None
	subscribers:Optional["StoriesStoryStatsStat"] = None
	views:Optional["StoriesStoryStatsStat"] = None
	likes:Optional["StoriesStoryStatsStat"] = None


class StoriesStoryStatsStat(BM):
	count:Optional[int] = None
	state:Optional["StoriesStoryStatsState"] = None


class StoriesViewersItem(BM):
	is_liked:Optional[bool] = None
	user_id:Optional[int] = None
	user:Optional["UsersUserFull"] = None




class UsersFields(Enum):
	FIRST_NAME_NOM = "first_name_nom"
	FIRST_NAME_GEN = "first_name_gen"
	FIRST_NAME_DAT = "first_name_dat"
	FIRST_NAME_ACC = "first_name_acc"
	FIRST_NAME_INS = "first_name_ins"
	FIRST_NAME_ABL = "first_name_abl"
	LAST_NAME_NOM = "last_name_nom"
	LAST_NAME_GEN = "last_name_gen"
	LAST_NAME_DAT = "last_name_dat"
	LAST_NAME_ACC = "last_name_acc"
	LAST_NAME_INS = "last_name_ins"
	LAST_NAME_ABL = "last_name_abl"
	PHOTO_ID = "photo_id"
	VERIFIED = "verified"
	SEX = "sex"
	BDATE = "bdate"
	BDATE_VISIBILITY = "bdate_visibility"
	CITY = "city"
	COUNTRY = "country"
	HOME_TOWN = "home_town"
	HAS_PHOTO = "has_photo"
	PHOTO = "photo"
	PHOTO_REC = "photo_rec"
	PHOTO_50 = "photo_50"
	PHOTO_100 = "photo_100"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_200 = "photo_200"
	PHOTO_400 = "photo_400"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_BIG = "photo_big"
	PHOTO_MEDIUM = "photo_medium"
	PHOTO_MEDIUM_REC = "photo_medium_rec"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	PHOTO_MAX_SIZE = "photo_max_size"
	THIRD_PARTY_BUTTONS = "third_party_buttons"
	ONLINE = "online"
	LISTS = "lists"
	DOMAIN = "domain"
	HAS_MOBILE = "has_mobile"
	CONTACTS = "contacts"
	LANGUAGE = "language"
	SITE = "site"
	EDUCATION = "education"
	UNIVERSITIES = "universities"
	SCHOOLS = "schools"
	STATUS = "status"
	LAST_SEEN = "last_seen"
	FOLLOWERS_COUNT = "followers_count"
	COUNTERS = "counters"
	COMMON_COUNT = "common_count"
	ONLINE_INFO = "online_info"
	OCCUPATION = "occupation"
	NICKNAME = "nickname"
	RELATIVES = "relatives"
	RELATION = "relation"
	PERSONAL = "personal"
	CONNECTIONS = "connections"
	EXPORTS = "exports"
	WALL_COMMENTS = "wall_comments"
	WALL_DEFAULT = "wall_default"
	ACTIVITIES = "activities"
	ACTIVITY = "activity"
	INTERESTS = "interests"
	MUSIC = "music"
	MOVIES = "movies"
	TV = "tv"
	BOOKS = "books"
	IS_NO_INDEX = "is_no_index"
	GAMES = "games"
	ABOUT = "about"
	QUOTES = "quotes"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_SEE_GIFTS = "can_see_gifts"
	WORK = "work"
	PLACES = "places"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	CAN_UPLOAD_DOC = "can_upload_doc"
	IS_FAVORITE = "is_favorite"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	TIMEZONE = "timezone"
	SCREEN_NAME = "screen_name"
	MAIDEN_NAME = "maiden_name"
	CROP_PHOTO = "crop_photo"
	IS_FRIEND = "is_friend"
	FRIEND_STATUS = "friend_status"
	CAREER = "career"
	MILITARY = "military"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	DESCRIPTIONS = "descriptions"
	TRENDING = "trending"
	MUTUAL = "mutual"
	FRIENDSHIP_WEEKS = "friendship_weeks"
	CAN_INVITE_TO_CHATS = "can_invite_to_chats"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	HAS_UNSEEN_STORIES = "has_unseen_stories"
	VIDEO_LIVE = "video_live"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	SERVICE_DESCRIPTION = "service_description"
	CAN_SEE_WISHES = "can_see_wishes"
	IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
	CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"

class UsersUserRelation(Enum):
	NOT_SPECIFIED = 0
	SINGLE = 1
	IN_A_RELATIONSHIP = 2
	ENGAGED = 3
	MARRIED = 4
	COMPLICATED = 5
	ACTIVELY_SEARCHING = 6
	IN_LOVE = 7
	IN_A_CIVIL_UNION = 8

class UsersUserType(Enum):
	PROFILE = "profile"

class UsersCareer(BM):
	city_id:Optional[int] = None
	city_name:Optional[str] = None
	company:Optional[str] = None
	country_id:Optional[int] = None
	_from:Optional[int] = None
	group_id:Optional[int] = None
	id:Optional[int] = None
	position:Optional[str] = None
	until:Optional[int] = None


class UsersExports(BM):
	facebook:Optional[int] = None
	livejournal:Optional[int] = None
	twitter:Optional[int] = None


class UsersLastSeen(BM):
	platform:Optional[int] = None
	time:Optional[int] = None


class UsersMilitary(BM):
	country_id:Optional[int] = None
	_from:Optional[int] = None
	id:Optional[int] = None
	unit:Optional[str] = None
	unit_id:Optional[int] = None
	until:Optional[int] = None


class UsersOccupation(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	type:Optional[str] = None


class UsersOnlineInfo(BM):
	visible:Optional[bool] = None
	last_seen:Optional[int] = None
	is_online:Optional[bool] = None
	app_id:Optional[int] = None
	is_mobile:Optional[bool] = None
	status:Optional[str] = None


class UsersPersonal(BM):
	alcohol:Optional[int] = None
	inspired_by:Optional[str] = None
	langs:Optional[list[list]] = None
	life_main:Optional[int] = None
	people_main:Optional[int] = None
	political:Optional[int] = None
	religion:Optional[str] = None
	religion_id:Optional[int] = None
	smoking:Optional[int] = None


class UsersRelative(BM):
	birth_date:Optional[str] = None
	id:Optional[int] = None
	name:Optional[str] = None
	type:Optional[str] = None


class UsersSchool(BM):
	city:Optional[int] = None
	_class:Optional[str] = None
	country:Optional[int] = None
	id:Optional[str] = None
	name:Optional[str] = None
	type:Optional[int] = None
	type_str:Optional[str] = None
	year_from:Optional[int] = None
	year_graduated:Optional[int] = None
	year_to:Optional[int] = None
	speciality:Optional[str] = None


class UsersSubscriptionsItem(BM):
	pass

class UsersUniversity(BM):
	chair:Optional[int] = None
	chair_name:Optional[str] = None
	city:Optional[int] = None
	country:Optional[int] = None
	education_form:Optional[str] = None
	education_status:Optional[str] = None
	faculty:Optional[int] = None
	faculty_name:Optional[str] = None
	graduation:Optional[int] = None
	id:Optional[int] = None
	name:Optional[str] = None
	university_group_id:Optional[int] = None


class UsersUserConnections(BM):
	skype:Optional[str] = None
	facebook:Optional[str] = None
	facebook_name:Optional[str] = None
	twitter:Optional[str] = None
	livejournal:Optional[str] = None
	instagram:Optional[str] = None


class UsersUserCounters(BM):
	albums:Optional[int] = None
	badges:Optional[int] = None
	audios:Optional[int] = None
	followers:Optional[int] = None
	friends:Optional[int] = None
	gifts:Optional[int] = None
	groups:Optional[int] = None
	notes:Optional[int] = None
	online_friends:Optional[int] = None
	pages:Optional[int] = None
	photos:Optional[int] = None
	subscriptions:Optional[int] = None
	user_photos:Optional[int] = None
	user_videos:Optional[int] = None
	videos:Optional[int] = None
	new_photo_tags:Optional[int] = None
	new_recognition_tags:Optional[int] = None
	mutual_friends:Optional[int] = None
	posts:Optional[int] = None
	articles:Optional[int] = None
	wishes:Optional[int] = None
	podcasts:Optional[int] = None
	clips:Optional[int] = None
	clips_followers:Optional[int] = None


class UsersUserMin(BM):
	deactivated:Optional[str] = None
	first_name:Optional[str] = None
	hidden:Optional[int] = None
	id:Optional[int] = None
	last_name:Optional[str] = None
	can_access_closed:Optional[bool] = None
	is_closed:Optional[bool] = None


class UsersUserSettingsXtr(BM):
	connections:Optional["UsersUserConnections"] = None
	bdate:Optional[str] = None
	bdate_visibility:Optional[int] = None
	city:Optional["BaseCity"] = None
	country:Optional["BaseCountry"] = None
	first_name:Optional[str] = None
	home_town:Optional[str] = None
	last_name:Optional[str] = None
	maiden_name:Optional[str] = None
	name_request:Optional["AccountNameRequest"] = None
	personal:Optional["UsersPersonal"] = None
	phone:Optional[str] = None
	relation:Optional["UsersUserRelation"] = None
	relation_partner:Optional["UsersUserMin"] = None
	relation_pending:Optional[bool] = None
	relation_requests:Optional[list[list]] = None
	screen_name:Optional[str] = None
	sex:Optional["BaseSex"] = None
	status:Optional[str] = None
	status_audio:Optional["AudioAudio"] = None
	interests:Optional["AccountUserSettingsInterests"] = None
	languages:Optional[list[list]] = None


class UsersUsersArray(BM):
	count:Optional[int] = None
	items:Optional[list[list]] = None




class UtilsDomainResolvedType(Enum):
	USER = "user"
	GROUP = "group"
	APPLICATION = "application"
	PAGE = "page"
	VK_APP = "vk_app"
	COMMUNITY_APPLICATION = "community_application"

class UtilsLinkCheckedStatus(Enum):
	NOT_BANNED = "not_banned"
	BANNED = "banned"
	PROCESSING = "processing"

class UtilsDomainResolved(BM):
	object_id:Optional[int] = None
	group_id:Optional[int] = None
	type:Optional["UtilsDomainResolvedType"] = None


class UtilsLastShortenedLink(BM):
	access_key:Optional[str] = None
	key:Optional[str] = None
	short_url:Optional[str] = None
	timestamp:Optional[int] = None
	url:Optional[str] = None
	views:Optional[int] = None


class UtilsLinkChecked(BM):
	link:Optional[str] = None
	status:Optional["UtilsLinkCheckedStatus"] = None


class UtilsLinkStats(BM):
	key:Optional[str] = None
	stats:Optional[list[list]] = None


class UtilsLinkStatsExtended(BM):
	key:Optional[str] = None
	stats:Optional[list[list]] = None


class UtilsShortLink(BM):
	access_key:Optional[str] = None
	key:Optional[str] = None
	short_url:Optional[str] = None
	url:Optional[str] = None


class UtilsStats(BM):
	timestamp:Optional[int] = None
	views:Optional[int] = None


class UtilsStatsCity(BM):
	city_id:Optional[int] = None
	views:Optional[int] = None


class UtilsStatsCountry(BM):
	country_id:Optional[int] = None
	views:Optional[int] = None


class UtilsStatsExtended(BM):
	cities:Optional[list[list]] = None
	countries:Optional[list[list]] = None
	sex_age:Optional[list[list]] = None
	timestamp:Optional[int] = None
	views:Optional[int] = None


class UtilsStatsSexAge(BM):
	age_range:Optional[str] = None
	female:Optional[int] = None
	male:Optional[int] = None




class VideoLiveInfo(BM):
	enabled:Optional[bool] = None
	is_notifications_blocked:Optional[bool] = None


class VideoLiveSettings(BM):
	can_rewind:Optional[bool] = None
	is_endless:Optional[bool] = None
	max_duration:Optional[int] = None


class VideoSaveResult(BM):
	access_key:Optional[str] = None
	description:Optional[str] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None
	upload_url:Optional[str] = None
	video_id:Optional[int] = None


class VideoVideo(BM):
	access_key:Optional[str] = None
	adding_date:Optional[int] = None
	can_comment:Optional[bool] = None
	can_edit:Optional[bool] = None
	can_like:Optional[bool] = None
	can_repost:Optional[bool] = None
	can_subscribe:Optional[bool] = None
	can_add_to_faves:Optional[bool] = None
	can_add:Optional[bool] = None
	can_attach_link:Optional[bool] = None
	is_private:Optional[bool] = None
	comments:Optional[int] = None
	date:Optional[int] = None
	description:Optional[str] = None
	duration:Optional[int] = None
	image:Optional[list[list]] = None
	first_frame:Optional[list[list]] = None
	width:Optional[int] = None
	height:Optional[int] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	user_id:Optional[int] = None
	title:Optional[str] = None
	is_favorite:Optional[bool] = None
	player:Optional[str] = None
	processing:Optional["BasePropertyExists"] = None
	converting:Optional[bool] = None
	added:Optional[bool] = None
	is_subscribed:Optional[bool] = None
	track_code:Optional[str] = None
	repeat:Optional["BasePropertyExists"] = None
	type:Optional[str] = None
	views:Optional[int] = None
	local_views:Optional[int] = None
	content_restricted:Optional[int] = None
	content_restricted_message:Optional[str] = None
	balance:Optional[int] = None
	live_status:Optional[str] = None
	live:Optional["BasePropertyExists"] = None
	upcoming:Optional["BasePropertyExists"] = None
	live_start_time:Optional[int] = None
	live_notify:Optional[bool] = None
	spectators:Optional[int] = None
	platform:Optional[str] = None
	likes:Optional["BaseLikes"] = None
	reposts:Optional["BaseRepostsInfo"] = None


class VideoVideoAlbum(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	title:Optional[str] = None


class VideoVideoFiles(BM):
	external:Optional[str] = None
	mp4_144:Optional[str] = None
	mp4_240:Optional[str] = None
	mp4_360:Optional[str] = None
	mp4_480:Optional[str] = None
	mp4_720:Optional[str] = None
	mp4_1080:Optional[str] = None
	mp4_1440:Optional[str] = None
	mp4_2160:Optional[str] = None
	flv_320:Optional[str] = None




class WallCommentAttachmentType(Enum):
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	NOTE = "note"
	PAGE = "page"
	MARKET_MARKET_ALBUM = "market_market_album"
	MARKET = "market"
	STICKER = "sticker"

class WallGetFilter(Enum):
	OWNER = "owner"
	OTHERS = "others"
	ALL = "all"
	POSTPONED = "postponed"
	SUGGESTS = "suggests"
	ARCHIVED = "archived"
	DONUT = "donut"

class WallPostSourceType(Enum):
	VK = "vk"
	WIDGET = "widget"
	API = "api"
	RSS = "rss"
	SMS = "sms"
	MVK = "mvk"

class WallPostType(Enum):
	POST = "post"
	COPY = "copy"
	REPLY = "reply"
	POSTPONE = "postpone"
	SUGGEST = "suggest"
	POST_ADS = "post_ads"
	PHOTO = "photo"
	VIDEO = "video"

class WallWallpostAttachmentType(Enum):
	PHOTO = "photo"
	PHOTOS_LIST = "photos_list"
	POSTED_PHOTO = "posted_photo"
	AUDIO = "audio"
	AUDIO_PLAYLIST = "audio_playlist"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	GRAFFITI = "graffiti"
	NOTE = "note"
	APP = "app"
	POLL = "poll"
	PAGE = "page"
	ALBUM = "album"
	MARKET_ALBUM = "market_album"
	MARKET = "market"
	EVENT = "event"
	DONUT_LINK = "donut_link"
	ARTICLE = "article"
	TEXTLIVE = "textlive"
	TEXTPOST = "textpost"
	TEXTPOST_PUBLISH = "textpost_publish"
	SITUATIONAL_THEME = "situational_theme"
	GROUP = "group"
	STICKER = "sticker"
	PODCAST = "podcast"

class WallAppPost(BM):
	id:Optional[int] = None
	name:Optional[str] = None
	photo_130:Optional[str] = None
	photo_604:Optional[str] = None


class WallAttachedNote(BM):
	comments:Optional[int] = None
	date:Optional[int] = None
	id:Optional[int] = None
	owner_id:Optional[int] = None
	read_comments:Optional[int] = None
	title:Optional[str] = None
	text:Optional[str] = None
	privacy_view:Optional[list[list]] = None
	privacy_comment:Optional[list[list]] = None
	can_comment:Optional[int] = None
	text_wiki:Optional[str] = None
	view_url:Optional[str] = None


class WallCarouselBase(BM):
	carousel_offset:Optional[int] = None


class WallCommentAttachment(BM):
	audio:Optional["AudioAudio"] = None
	doc:Optional["DocsDoc"] = None
	link:Optional["BaseLink"] = None
	market:Optional["MarketMarketItem"] = None
	market_market_album:Optional["MarketMarketAlbum"] = None
	note:Optional["WallAttachedNote"] = None
	page:Optional["PagesWikipageFull"] = None
	photo:Optional["PhotosPhoto"] = None
	sticker:Optional["BaseSticker"] = None
	type:Optional["WallCommentAttachmentType"] = None
	video:Optional["VideoVideo"] = None


class WallGeo(BM):
	coordinates:Optional[str] = None
	place:Optional["BasePlace"] = None
	showmap:Optional[int] = None
	type:Optional[str] = None


class WallGraffiti(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	photo_200:Optional[str] = None
	photo_586:Optional[str] = None
	height:Optional[int] = None
	url:Optional[str] = None
	width:Optional[int] = None
	access_key:Optional[str] = None


class WallPostCopyright(BM):
	id:Optional[int] = None
	link:Optional[str] = None
	name:Optional[str] = None
	type:Optional[str] = None


class WallPostSource(BM):
	data:Optional[str] = None
	platform:Optional[str] = None
	type:Optional["WallPostSourceType"] = None
	url:Optional[str] = None
	link:Optional["BaseLink"] = None


class WallPostedPhoto(BM):
	id:Optional[int] = None
	owner_id:Optional[int] = None
	photo_130:Optional[str] = None
	photo_604:Optional[str] = None


class WallViews(BM):
	count:Optional[int] = None


class WallWallComment(BM):
	id:Optional[int] = None
	from_id:Optional[int] = None
	can_edit:Optional[bool] = None
	post_id:Optional[int] = None
	owner_id:Optional[int] = None
	parents_stack:Optional[list[list]] = None
	photo_id:Optional[int] = None
	video_id:Optional[int] = None
	date:Optional[int] = None
	text:Optional[str] = None
	attachments:Optional[list[list]] = None
	donut:Optional["WallWallCommentDonut"] = None
	likes:Optional["BaseLikesInfo"] = None
	real_offset:Optional[int] = None
	reply_to_user:Optional[int] = None
	reply_to_comment:Optional[int] = None
	thread:Optional["CommentThread"] = None
	deleted:Optional[bool] = None
	pid:Optional[int] = None


class WallWallCommentDonut(BM):
	is_don:Optional[bool] = None
	placeholder:Optional["WallWallCommentDonutPlaceholder"] = None


class WallWallCommentDonutPlaceholder(BM):
	text:Optional[str] = None


class WallWallpost(BM):
	access_key:Optional[str] = None
	is_deleted:Optional[bool] = None
	attachments:Optional[list[list]] = None
	copyright:Optional["WallPostCopyright"] = None
	date:Optional[int] = None
	edited:Optional[int] = None
	from_id:Optional[int] = None
	geo:Optional["WallGeo"] = None
	id:Optional[int] = None
	is_archived:Optional[bool] = None
	is_favorite:Optional[bool] = None
	likes:Optional["BaseLikesInfo"] = None
	owner_id:Optional[int] = None
	post_id:Optional[int] = None
	parents_stack:Optional[list[list]] = None
	post_source:Optional["WallPostSource"] = None
	post_type:Optional["WallPostType"] = None
	reposts:Optional["BaseRepostsInfo"] = None
	signer_id:Optional[int] = None
	text:Optional[str] = None
	views:Optional["WallViews"] = None


class WallWallpostAttachment(BM):
	access_key:Optional[str] = None
	album:Optional["PhotosPhotoAlbum"] = None
	app:Optional["WallAppPost"] = None
	audio:Optional["AudioAudio"] = None
	doc:Optional["DocsDoc"] = None
	event:Optional["EventsEventAttach"] = None
	group:Optional["GroupsGroupAttach"] = None
	graffiti:Optional["WallGraffiti"] = None
	link:Optional["BaseLink"] = None
	market:Optional["MarketMarketItem"] = None
	market_album:Optional["MarketMarketAlbum"] = None
	note:Optional["NotesNote"] = None
	page:Optional["PagesWikipageFull"] = None
	photo:Optional["PhotosPhoto"] = None
	poll:Optional["PollsPoll"] = None
	posted_photo:Optional["WallPostedPhoto"] = None
	type:Optional["WallWallpostAttachmentType"] = None
	video:Optional["VideoVideoFull"] = None


class WallWallpostCommentsDonut(BM):
	placeholder:Optional["WallWallpostCommentsDonutPlaceholder"] = None


class WallWallpostCommentsDonutPlaceholder(BM):
	text:Optional[str] = None


class WallWallpostDonut(BM):
	is_donut:Optional[bool] = None
	paid_duration:Optional[int] = None
	placeholder:Optional["WallWallpostDonutPlaceholder"] = None
	can_publish_free_copy:Optional[bool] = None
	edit_mode:Optional[str] = None


class WallWallpostDonutPlaceholder(BM):
	text:Optional[str] = None


class WallWallpostToId(BM):
	attachments:Optional[list[list]] = None
	comments:Optional["BaseCommentsInfo"] = None
	copy_owner_id:Optional[int] = None
	copy_post_id:Optional[int] = None
	date:Optional[int] = None
	from_id:Optional[int] = None
	geo:Optional["WallGeo"] = None
	id:Optional[int] = None
	is_favorite:Optional[bool] = None
	likes:Optional["BaseLikesInfo"] = None
	post_id:Optional[int] = None
	post_source:Optional["WallPostSource"] = None
	post_type:Optional["WallPostType"] = None
	reposts:Optional["BaseRepostsInfo"] = None
	signer_id:Optional[int] = None
	text:Optional[str] = None
	to_id:Optional[int] = None




class WidgetsCommentMediaType(Enum):
	AUDIO = "audio"
	PHOTO = "photo"
	VIDEO = "video"

class WidgetsCommentMedia(BM):
	item_id:Optional[int] = None
	owner_id:Optional[int] = None
	thumb_src:Optional[str] = None
	type:Optional["WidgetsCommentMediaType"] = None


class WidgetsCommentReplies(BM):
	can_post:Optional[bool] = None
	count:Optional[int] = None
	replies:Optional[list[list]] = None


class WidgetsCommentRepliesItem(BM):
	cid:Optional[int] = None
	date:Optional[int] = None
	likes:Optional["WidgetsWidgetLikes"] = None
	text:Optional[str] = None
	uid:Optional[int] = None
	user:Optional["UsersUserFull"] = None


class WidgetsWidgetComment(BM):
	attachments:Optional[list[list]] = None
	can_delete:Optional[bool] = None
	comments:Optional["WidgetsCommentReplies"] = None
	date:Optional[int] = None
	from_id:Optional[int] = None
	id:Optional[int] = None
	likes:Optional["BaseLikesInfo"] = None
	media:Optional["WidgetsCommentMedia"] = None
	post_source:Optional["WallPostSource"] = None
	post_type:Optional[int] = None
	reposts:Optional["BaseRepostsInfo"] = None
	text:Optional[str] = None
	to_id:Optional[int] = None
	user:Optional["UsersUserFull"] = None


class WidgetsWidgetLikes(BM):
	count:Optional[int] = None


class WidgetsWidgetPage(BM):
	comments:Optional["BaseObjectCount"] = None
	date:Optional[int] = None
	description:Optional[str] = None
	id:Optional[int] = None
	likes:Optional["BaseObjectCount"] = None
	page_id:Optional[str] = None
	photo:Optional[str] = None
	title:Optional[str] = None
	url:Optional[str] = None




class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
	photo_200:Optional[str] = None
	is_service_account:Optional[bool] = None

class AdsTargSettings(AdsCriteria):
	id:Optional[int] = None
	campaign_id:Optional[int] = None

class AppsApp(AppsAppMin):
	author_url:Optional[str] = None
	banner_1120:Optional[str] = None
	banner_560:Optional[str] = None
	icon_16:Optional[str] = None
	is_new:Optional[bool] = None
	push_enabled:Optional[bool] = None
	screen_orientation:Optional[int] = None
	friends:Optional[list[list]] = None
	catalog_position:Optional[int] = None
	description:Optional[str] = None
	genre:Optional[str] = None
	genre_id:Optional[int] = None
	international:Optional[bool] = None
	is_in_catalog:Optional[int] = None
	leaderboard_type:Optional["AppsAppLeaderboardType"] = None
	members_count:Optional[int] = None
	platform_id:Optional[str] = None
	published_date:Optional[int] = None
	screen_name:Optional[str] = None
	section:Optional[str] = None

class CallbackConfirmation(CallbackBase):
	type:Optional[str] = None

class CallbackMessageAllow(CallbackBase):
	type:Optional[str] = None
	object:Optional["CallbackMessageAllowObject"] = None

class CallbackMessageEdit(CallbackBase):
	type:Optional[str] = None
	object:Optional["MessagesMessage"] = None

class CallbackMessageNew(CallbackBase):
	type:Optional[str] = None
	object:Optional[object] = None

class CallbackMessageReply(CallbackBase):
	type:Optional[str] = None
	object:Optional["MessagesMessage"] = None

class DatabaseCity(BaseObject):
	area:Optional[str] = None
	region:Optional[str] = None
	important:Optional[bool] = None

class FriendsFriendExtendedStatus(FriendsFriendStatus):
	is_request_unread:Optional[bool] = None

class GroupsGroupFull(GroupsGroup):
	market:Optional["GroupsMarketInfo"] = None
	member_status:Optional["GroupsGroupFullMemberStatus"] = None
	is_adult:Optional[bool] = None
	is_hidden_from_feed:Optional[bool] = None
	is_favorite:Optional[bool] = None
	is_subscribed:Optional[bool] = None
	city:Optional["BaseObject"] = None
	country:Optional["BaseCountry"] = None
	verified:Optional[bool] = None
	description:Optional[str] = None
	wiki_page:Optional[str] = None
	members_count:Optional[int] = None
	members_count_text:Optional[str] = None
	requests_count:Optional[int] = None
	video_live_level:Optional[int] = None
	video_live_count:Optional[int] = None
	clips_count:Optional[int] = None
	counters:Optional["GroupsCountersGroup"] = None
	cover:Optional["GroupsCover"] = None
	can_post:Optional[bool] = None
	can_suggest:Optional[bool] = None
	can_upload_story:Optional[bool] = None
	can_upload_doc:Optional[bool] = None
	can_upload_video:Optional[bool] = None
	can_see_all_posts:Optional[bool] = None
	can_create_topic:Optional[bool] = None
	activity:Optional[str] = None
	fixed_post:Optional[int] = None
	has_photo:Optional[bool] = None
	crop_photo:Optional["BaseCropPhoto"] = None
	status:Optional[str] = None
	status_audio:Optional["AudioAudio"] = None
	main_album_id:Optional[int] = None
	links:Optional[list[list]] = None
	contacts:Optional[list[list]] = None
	wall:Optional[int] = None
	site:Optional[str] = None
	main_section:Optional["GroupsGroupFullSection"] = None
	secondary_section:Optional["GroupsGroupFullSection"] = None
	trending:Optional[bool] = None
	can_message:Optional[bool] = None
	is_messages_blocked:Optional[bool] = None
	can_send_notify:Optional[bool] = None
	online_status:Optional["GroupsOnlineStatus"] = None
	invited_by:Optional[int] = None
	age_limits:Optional["GroupsGroupFullAgeLimits"] = None
	ban_info:Optional["GroupsGroupBanInfo"] = None
	has_market_app:Optional[bool] = None
	using_vkpay_market_app:Optional[bool] = None
	has_group_channel:Optional[bool] = None
	addresses:Optional["GroupsAddressesInfo"] = None
	is_subscribed_podcasts:Optional[bool] = None
	can_subscribe_podcasts:Optional[bool] = None
	can_subscribe_posts:Optional[bool] = None
	live_covers:Optional["GroupsLiveCovers"] = None
	stories_archive_count:Optional[int] = None
	has_unseen_stories:Optional[bool] = None

class MarketMarketItemFull(MarketMarketItem):
	albums_ids:Optional[list[list]] = None
	photos:Optional[list[list]] = None
	can_comment:Optional[bool] = None
	can_repost:Optional[bool] = None
	likes:Optional["BaseLikes"] = None
	reposts:Optional["BaseRepostsInfo"] = None
	views_count:Optional[int] = None
	wishlist_item_id:Optional[int] = None
	cancel_info:Optional["BaseLink"] = None
	user_agreement_info:Optional[str] = None
	ad_id:Optional[int] = None

class MessagesGetConversationByIdExtended(MessagesGetConversationById):
	profiles:Optional[list[list]] = None
	groups:Optional[list[list]] = None

class NewsfeedItemAudio(NewsfeedItemBase):
	audio:Optional["NewsfeedItemAudioAudio"] = None
	post_id:Optional[int] = None

class NewsfeedItemDigest(NewsfeedItemBase):
	feed_id:Optional[str] = None
	items:Optional[list[list]] = None
	main_post_ids:Optional[list[list]] = None
	template:Optional[str] = None
	header:Optional["NewsfeedItemDigestHeader"] = None
	footer:Optional["NewsfeedItemDigestFooter"] = None
	track_code:Optional[str] = None

class NewsfeedItemFriend(NewsfeedItemBase):
	friends:Optional["NewsfeedItemFriendFriends"] = None

class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
	photos:Optional["NewsfeedItemPhotoPhotos"] = None
	post_id:Optional[int] = None

class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
	photo_tags:Optional["NewsfeedItemPhotoTagPhotoTags"] = None
	post_id:Optional[int] = None

class NewsfeedItemPromoButton(NewsfeedItemBase):
	text:Optional[str] = None
	title:Optional[str] = None
	action:Optional["NewsfeedItemPromoButtonAction"] = None
	images:Optional[list[list]] = None
	track_code:Optional[str] = None

class NewsfeedItemTopic(NewsfeedItemBase):
	comments:Optional["BaseCommentsInfo"] = None
	likes:Optional["BaseLikesInfo"] = None
	post_id:Optional[int] = None
	text:Optional[str] = None

class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
	video:Optional["NewsfeedItemVideoVideo"] = None

class NewsfeedListFull(NewsfeedList):
	no_reposts:Optional[bool] = None
	source_ids:Optional[list[list]] = None

class NewsfeedNewsfeedPhoto(PhotosPhoto):
	likes:Optional["BaseLikes"] = None
	comments:Optional["BaseObjectCount"] = None
	can_repost:Optional[bool] = None

class NotificationsNotificationParent(WallWallpostToId, PhotosPhoto, BoardTopic, VideoVideo, NotificationsNotificationsComment):
	pass
class UsersUser(UsersUserMin):
	sex:Optional["BaseSex"] = None
	screen_name:Optional[str] = None
	photo_50:Optional[str] = None
	photo_100:Optional[str] = None
	online_info:Optional["UsersOnlineInfo"] = None
	online:Optional[bool] = None
	online_mobile:Optional[bool] = None
	online_app:Optional[int] = None
	verified:Optional[bool] = None
	trending:Optional[bool] = None
	friend_status:Optional["FriendsFriendStatusStatus"] = None
	mutual:Optional["FriendsRequestsMutual"] = None

class UsersUserFull(UsersUser):
	first_name_nom:Optional[str] = None
	first_name_gen:Optional[str] = None
	first_name_dat:Optional[str] = None
	first_name_acc:Optional[str] = None
	first_name_ins:Optional[str] = None
	first_name_abl:Optional[str] = None
	last_name_nom:Optional[str] = None
	last_name_gen:Optional[str] = None
	last_name_dat:Optional[str] = None
	last_name_acc:Optional[str] = None
	last_name_ins:Optional[str] = None
	last_name_abl:Optional[str] = None
	nickname:Optional[str] = None
	maiden_name:Optional[str] = None
	contact_name:Optional[str] = None
	domain:Optional[str] = None
	bdate:Optional[str] = None
	city:Optional["BaseCity"] = None
	country:Optional["BaseCountry"] = None
	timezone:Optional[int] = None
	owner_state:Optional["OwnerState"] = None
	photo_200:Optional[str] = None
	photo_max:Optional[str] = None
	photo_200_orig:Optional[str] = None
	photo_400_orig:Optional[str] = None
	photo_max_orig:Optional[str] = None
	photo_id:Optional[str] = None
	has_photo:Optional[bool] = None
	has_mobile:Optional[bool] = None
	is_friend:Optional[bool] = None
	wall_comments:Optional[bool] = None
	can_post:Optional[bool] = None
	can_see_all_posts:Optional[bool] = None
	can_see_audio:Optional[bool] = None
	type:Optional["UsersUserType"] = None
	email:Optional[str] = None
	skype:Optional[str] = None
	facebook:Optional[str] = None
	facebook_name:Optional[str] = None
	twitter:Optional[str] = None
	livejournal:Optional[str] = None
	instagram:Optional[str] = None
	test:Optional[bool] = None
	video_live:Optional["VideoLiveInfo"] = None
	is_video_live_notifications_blocked:Optional[bool] = None
	is_service:Optional[bool] = None
	service_description:Optional[str] = None
	photo_rec:Optional["PhotosPhotoFalseable"] = None
	photo_medium:Optional["PhotosPhotoFalseable"] = None
	photo_medium_rec:Optional["PhotosPhotoFalseable"] = None
	photo:Optional[str] = None
	photo_big:Optional[str] = None
	photo_400:Optional[str] = None
	photo_max_size:Optional["PhotosPhoto"] = None
	language:Optional[str] = None
	stories_archive_count:Optional[int] = None
	has_unseen_stories:Optional[bool] = None
	wall_default:Optional[str] = None
	can_call:Optional[bool] = None
	can_call_from_group:Optional[bool] = None
	can_see_wishes:Optional[bool] = None
	can_see_gifts:Optional[bool] = None
	interests:Optional[str] = None
	books:Optional[str] = None
	tv:Optional[str] = None
	quotes:Optional[str] = None
	about:Optional[str] = None
	games:Optional[str] = None
	movies:Optional[str] = None
	activities:Optional[str] = None
	music:Optional[str] = None
	can_write_private_message:Optional[bool] = None
	can_send_friend_request:Optional[bool] = None
	can_be_invited_group:Optional[bool] = None
	mobile_phone:Optional[str] = None
	home_phone:Optional[str] = None
	site:Optional[str] = None
	status_audio:Optional["AudioAudio"] = None
	status:Optional[str] = None
	activity:Optional[str] = None
	last_seen:Optional["UsersLastSeen"] = None
	exports:Optional["UsersExports"] = None
	crop_photo:Optional["BaseCropPhoto"] = None
	followers_count:Optional[int] = None
	video_live_level:Optional[int] = None
	video_live_count:Optional[int] = None
	clips_count:Optional[int] = None
	blacklisted:Optional[bool] = None
	blacklisted_by_me:Optional[bool] = None
	is_favorite:Optional[bool] = None
	is_hidden_from_feed:Optional[bool] = None
	common_count:Optional[int] = None
	occupation:Optional["UsersOccupation"] = None
	career:Optional[list[list]] = None
	military:Optional[list[list]] = None
	university:Optional[int] = None
	university_name:Optional[str] = None
	university_group_id:Optional[int] = None
	faculty:Optional[int] = None
	faculty_name:Optional[str] = None
	graduation:Optional[int] = None
	education_form:Optional[str] = None
	education_status:Optional[str] = None
	home_town:Optional[str] = None
	relation:Optional["UsersUserRelation"] = None
	relation_partner:Optional["UsersUserMin"] = None
	personal:Optional["UsersPersonal"] = None
	universities:Optional[list[list]] = None
	schools:Optional[list[list]] = None
	relatives:Optional[list[list]] = None
	is_subscribed_podcasts:Optional[bool] = None
	can_subscribe_podcasts:Optional[bool] = None
	can_subscribe_posts:Optional[bool] = None
	counters:Optional["UsersUserCounters"] = None
	access_key:Optional[str] = None
	can_upload_doc:Optional[bool] = None
	hash:Optional[str] = None
	is_no_index:Optional[bool] = None
	contact_id:Optional[int] = None
	is_message_request:Optional[bool] = None
	descriptions:Optional[list[list]] = None
	lists:Optional[list[list]] = None

class UsersUserXtrType(UsersUser):
	type:Optional["UsersUserType"] = None

class VideoVideoAlbumFull(VideoVideoAlbum):
	count:Optional[int] = None
	image:Optional[list[list]] = None
	image_blur:Optional["BasePropertyExists"] = None
	is_system:Optional["BasePropertyExists"] = None
	updated_time:Optional[int] = None

class VideoVideoFull(VideoVideo):
	files:Optional["VideoVideoFiles"] = None
	trailer:Optional["VideoVideoFiles"] = None
	live_settings:Optional["VideoLiveSettings"] = None

class VideoVideoImage(BaseImage):
	with_padding:Optional["BasePropertyExists"] = None

class WallWallpostFull(WallCarouselBase, WallWallpost):
	copy_history:Optional[list[list]] = None
	can_edit:Optional[bool] = None
	created_by:Optional[int] = None
	can_delete:Optional[bool] = None
	can_pin:Optional[bool] = None
	donut:Optional["WallWallpostDonut"] = None
	is_pinned:Optional[int] = None
	comments:Optional["BaseCommentsInfo"] = None
	marked_as_ads:Optional[bool] = None
	topic_id:Optional[int] = None
	short_text_rate:Optional[int] = None
	hash:Optional[str] = None


class FriendsUserXtrPhone(UsersUserFull):
	phone:Optional[str] = None



class GroupsUserXtrRole(UsersUserFull):
	role:Optional["GroupsRoleOptions"] = None


class NewsfeedItemWallpost(NewsfeedItemBase, WallWallpostFull):
	feedback:Optional["NewsfeedItemWallpostFeedback"] = None

class MessagesUserXtrInvitedBy(UsersUserXtrType):
	invited_by:Optional[int] = None
