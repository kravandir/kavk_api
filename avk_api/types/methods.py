from .base import BaseMethod
from .objects import *
from .responses import *

class Account(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def ban(self, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.ban", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def changePassword(self, restore_sid:Optional[str]=None, change_password_hash:Optional[str]=None, old_password:Optional[str]=None, new_password:Optional[str]=None):
		"""Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.changePassword", **args)
		try: return AccountChangePasswordResponse(**r)
		except: return r


	async def getActiveOffers(self, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of active ads (offers) which executed by the user will bring him/her respective number of votes to his balance in the application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getActiveOffers", **args)
		try: return AccountGetActiveOffersResponse(**r)
		except: return r


	async def getAppPermissions(self, user_id:Optional[int]=None):
		"""Gets settings of the user in this application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getAppPermissions", **args)
		try: return AccountGetAppPermissionsResponse(**r)
		except: return r


	async def getBanned(self, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a user's blacklist."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getBanned", **args)
		try: return AccountGetBannedResponse(**r)
		except: return r


	async def getCounters(self, filter:Optional[list[str]]=None, user_id:Optional[int]=None):
		"""Returns non-null values of user counters."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getCounters", **args)
		try: return AccountGetCountersResponse(**r)
		except: return r


	async def getInfo(self, fields:Optional[list[str]]=None):
		"""Returns current account info."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getInfo", **args)
		try: return AccountGetInfoResponse(**r)
		except: return r


	async def getProfileInfo(self):
		"""Returns the current account info."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getProfileInfo", **args)
		try: return AccountGetProfileInfoResponse(**r)
		except: return r


	async def getPushSettings(self, device_id:Optional[str]=None):
		"""Gets settings of push notifications."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.getPushSettings", **args)
		try: return AccountGetPushSettingsResponse(**r)
		except: return r


	async def registerDevice(self, token:Optional[str]=None, device_model:Optional[str]=None, device_year:Optional[int]=None, device_id:Optional[str]=None, system_version:Optional[str]=None, settings:Optional[str]=None, sandbox:Optional[bool]=None):
		"""Subscribes an iOS/Android/Windows Phone-based device to receive push notifications"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.registerDevice", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def saveProfileInfo(self, first_name:Optional[str]=None, last_name:Optional[str]=None, maiden_name:Optional[str]=None, screen_name:Optional[str]=None, cancel_request_id:Optional[int]=None, sex:Optional[int]=None, relation:Optional[int]=None, relation_partner_id:Optional[int]=None, bdate:Optional[str]=None, bdate_visibility:Optional[int]=None, home_town:Optional[str]=None, country_id:Optional[int]=None, city_id:Optional[int]=None, status:Optional[str]=None):
		"""Edits current profile info."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.saveProfileInfo", **args)
		try: return AccountSaveProfileInfoResponse(**r)
		except: return r


	async def setInfo(self, name:Optional[str]=None, value:Optional[str]=None):
		"""Allows to edit the current account info."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.setInfo", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setOffline(self):
		"""Marks a current user as offline."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.setOffline", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setOnline(self, voip:Optional[bool]=None):
		"""Marks the current user as online for 15 minutes."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.setOnline", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setPushSettings(self, device_id:Optional[str]=None, settings:Optional[str]=None, key:Optional[str]=None, value:Optional[list[str]]=None):
		"""Change push settings."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.setPushSettings", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setSilenceMode(self, device_id:Optional[str]=None, time:Optional[int]=None, peer_id:Optional[int]=None, sound:Optional[int]=None):
		"""Mutes push notifications for the set period of time."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.setSilenceMode", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unban(self, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.unban", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unregisterDevice(self, device_id:Optional[str]=None, sandbox:Optional[bool]=None):
		"""Unsubscribes a device from push notifications."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Account.unregisterDevice", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Ads(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addOfficeUsers(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Adds managers and/or supervisors to advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.addOfficeUsers", **args)
		try: return AdsAddOfficeUsersResponse(**r)
		except: return r


	async def checkLink(self, account_id:Optional[int]=None, link_type:Optional[str]=None, link_url:Optional[str]=None, campaign_id:Optional[int]=None):
		"""Allows to check the ad link."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.checkLink", **args)
		try: return AdsCheckLinkResponse(**r)
		except: return r


	async def createAds(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Creates ads."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.createAds", **args)
		try: return AdsCreateAdsResponse(**r)
		except: return r


	async def createCampaigns(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Creates advertising campaigns."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.createCampaigns", **args)
		try: return AdsCreateCampaignsResponse(**r)
		except: return r


	async def createClients(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Creates clients of an advertising agency."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.createClients", **args)
		try: return AdsCreateClientsResponse(**r)
		except: return r


	async def createTargetGroup(self, account_id:Optional[int]=None, client_id:Optional[int]=None, name:Optional[str]=None, lifetime:Optional[int]=None, target_pixel_id:Optional[int]=None, target_pixel_rules:Optional[str]=None):
		"""Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.)."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.createTargetGroup", **args)
		try: return AdsCreateTargetGroupResponse(**r)
		except: return r


	async def deleteAds(self, account_id:Optional[int]=None, ids:Optional[str]=None):
		"""Archives ads."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.deleteAds", **args)
		try: return AdsDeleteAdsResponse(**r)
		except: return r


	async def deleteCampaigns(self, account_id:Optional[int]=None, ids:Optional[str]=None):
		"""Archives advertising campaigns."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.deleteCampaigns", **args)
		try: return AdsDeleteCampaignsResponse(**r)
		except: return r


	async def deleteClients(self, account_id:Optional[int]=None, ids:Optional[str]=None):
		"""Archives clients of an advertising agency."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.deleteClients", **args)
		try: return AdsDeleteClientsResponse(**r)
		except: return r


	async def deleteTargetGroup(self, account_id:Optional[int]=None, client_id:Optional[int]=None, target_group_id:Optional[int]=None):
		"""Deletes a retarget group."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.deleteTargetGroup", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getAccounts(self):
		"""Returns a list of advertising accounts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getAccounts", **args)
		try: return AdsGetAccountsResponse(**r)
		except: return r


	async def getAds(self, account_id:Optional[int]=None, ad_ids:Optional[str]=None, campaign_ids:Optional[str]=None, client_id:Optional[int]=None, include_deleted:Optional[bool]=None, only_deleted:Optional[bool]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		"""Returns number of ads."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getAds", **args)
		try: return AdsGetAdsResponse(**r)
		except: return r


	async def getAdsLayout(self, account_id:Optional[int]=None, client_id:Optional[int]=None, include_deleted:Optional[bool]=None, only_deleted:Optional[bool]=None, campaign_ids:Optional[str]=None, ad_ids:Optional[str]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		"""Returns descriptions of ad layouts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getAdsLayout", **args)
		try: return AdsGetAdsLayoutResponse(**r)
		except: return r


	async def getAdsTargeting(self, account_id:Optional[int]=None, ad_ids:Optional[str]=None, campaign_ids:Optional[str]=None, client_id:Optional[int]=None, include_deleted:Optional[bool]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		"""Returns ad targeting parameters."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getAdsTargeting", **args)
		try: return AdsGetAdsTargetingResponse(**r)
		except: return r


	async def getBudget(self, account_id:Optional[int]=None):
		"""Returns current budget of the advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getBudget", **args)
		try: return AdsGetBudgetResponse(**r)
		except: return r


	async def getCampaigns(self, account_id:Optional[int]=None, client_id:Optional[int]=None, include_deleted:Optional[bool]=None, campaign_ids:Optional[str]=None, fields:Optional[list[str]]=None):
		"""Returns a list of campaigns in an advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getCampaigns", **args)
		try: return AdsGetCampaignsResponse(**r)
		except: return r


	async def getCategories(self, lang:Optional[str]=None):
		"""Returns a list of possible ad categories."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getCategories", **args)
		try: return AdsGetCategoriesResponse(**r)
		except: return r


	async def getClients(self, account_id:Optional[int]=None):
		"""Returns a list of advertising agency's clients."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getClients", **args)
		try: return AdsGetClientsResponse(**r)
		except: return r


	async def getDemographics(self, account_id:Optional[int]=None, ids_type:Optional[str]=None, ids:Optional[str]=None, period:Optional[str]=None, date_from:Optional[str]=None, date_to:Optional[str]=None):
		"""Returns demographics for ads or campaigns."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getDemographics", **args)
		try: return AdsGetDemographicsResponse(**r)
		except: return r


	async def getFloodStats(self, account_id:Optional[int]=None):
		"""Returns information about current state of a counter — number of remaining runs of methods and time to the next counter nulling in seconds."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getFloodStats", **args)
		try: return AdsGetFloodStatsResponse(**r)
		except: return r


	async def getLookalikeRequests(self, account_id:Optional[int]=None, client_id:Optional[int]=None, requests_ids:Optional[str]=None, offset:Optional[int]=None, limit:Optional[int]=None, sort_by:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getLookalikeRequests", **args)
		try: return AdsGetLookalikeRequestsResponse(**r)
		except: return r


	async def getMusicians(self, artist_name:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getMusicians", **args)
		try: return AdsGetMusiciansResponse(**r)
		except: return r


	async def getMusiciansByIds(self, ids:Optional[list[int]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getMusiciansByIds", **args)
		try: return AdsGetMusiciansResponse(**r)
		except: return r


	async def getOfficeUsers(self, account_id:Optional[int]=None):
		"""Returns a list of managers and supervisors of advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getOfficeUsers", **args)
		try: return AdsGetOfficeUsersResponse(**r)
		except: return r


	async def getPostsReach(self, account_id:Optional[int]=None, ids_type:Optional[str]=None, ids:Optional[str]=None):
		"""Returns detailed statistics of promoted posts reach from campaigns and ads."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getPostsReach", **args)
		try: return AdsGetPostsReachResponse(**r)
		except: return r


	async def getRejectionReason(self, account_id:Optional[int]=None, ad_id:Optional[int]=None):
		"""Returns a reason of ad rejection for pre-moderation."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getRejectionReason", **args)
		try: return AdsGetRejectionReasonResponse(**r)
		except: return r


	async def getStatistics(self, account_id:Optional[int]=None, ids_type:Optional[str]=None, ids:Optional[str]=None, period:Optional[str]=None, date_from:Optional[str]=None, date_to:Optional[str]=None, stats_fields:Optional[list[str]]=None):
		"""Returns statistics of performance indicators for ads, campaigns, clients or the whole account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getStatistics", **args)
		try: return AdsGetStatisticsResponse(**r)
		except: return r


	async def getSuggestions(self, section:Optional[str]=None, ids:Optional[str]=None, q:Optional[str]=None, country:Optional[int]=None, cities:Optional[str]=None, lang:Optional[str]=None):
		"""Returns a set of auto-suggestions for various targeting parameters."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getSuggestions", **args)
		for i in [AdsGetSuggestionsResponse, AdsGetSuggestionsRegionsResponse, AdsGetSuggestionsCitiesResponse, AdsGetSuggestionsSchoolsResponse]:
			try: return i(**r)
			except: return r


	async def getTargetGroups(self, account_id:Optional[int]=None, client_id:Optional[int]=None, extended:Optional[bool]=None):
		"""Returns a list of target groups."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getTargetGroups", **args)
		try: return AdsGetTargetGroupsResponse(**r)
		except: return r


	async def getTargetingStats(self, account_id:Optional[int]=None, client_id:Optional[int]=None, criteria:Optional[str]=None, ad_id:Optional[int]=None, ad_format:Optional[int]=None, ad_platform:Optional[str]=None, ad_platform_no_wall:Optional[str]=None, ad_platform_no_ad_network:Optional[str]=None, publisher_platforms:Optional[str]=None, link_url:Optional[str]=None, link_domain:Optional[str]=None, need_precise:Optional[bool]=None, impressions_limit_period:Optional[int]=None):
		"""Returns the size of targeting audience, and also recommended values for CPC and CPM."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getTargetingStats", **args)
		try: return AdsGetTargetingStatsResponse(**r)
		except: return r


	async def getUploadURL(self, ad_format:Optional[int]=None, icon:Optional[int]=None):
		"""Returns URL to upload an ad photo to."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getUploadURL", **args)
		try: return AdsGetUploadURLResponse(**r)
		except: return r


	async def getVideoUploadURL(self):
		"""Returns URL to upload an ad video to."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.getVideoUploadURL", **args)
		try: return AdsGetVideoUploadURLResponse(**r)
		except: return r


	async def importTargetContacts(self, account_id:Optional[int]=None, client_id:Optional[int]=None, target_group_id:Optional[int]=None, contacts:Optional[str]=None):
		"""Imports a list of advertiser's contacts to count VK registered users against the target group."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.importTargetContacts", **args)
		try: return AdsImportTargetContactsResponse(**r)
		except: return r


	async def removeOfficeUsers(self, account_id:Optional[int]=None, ids:Optional[str]=None):
		"""Removes managers and/or supervisors from advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.removeOfficeUsers", **args)
		try: return AdsRemoveOfficeUsersResponse(**r)
		except: return r


	async def updateAds(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Edits ads."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.updateAds", **args)
		try: return AdsUpdateAdsResponse(**r)
		except: return r


	async def updateCampaigns(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Edits advertising campaigns."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.updateCampaigns", **args)
		try: return AdsUpdateCampaignsResponse(**r)
		except: return r


	async def updateClients(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Edits clients of an advertising agency."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.updateClients", **args)
		try: return AdsUpdateClientsResponse(**r)
		except: return r


	async def updateOfficeUsers(self, account_id:Optional[int]=None, data:Optional[str]=None):
		"""Adds managers and/or supervisors to advertising account."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.updateOfficeUsers", **args)
		try: return AdsUpdateOfficeUsersResponse(**r)
		except: return r


	async def updateTargetGroup(self, account_id:Optional[int]=None, client_id:Optional[int]=None, target_group_id:Optional[int]=None, name:Optional[str]=None, domain:Optional[str]=None, lifetime:Optional[int]=None, target_pixel_id:Optional[int]=None, target_pixel_rules:Optional[str]=None):
		"""Edits a retarget group."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Ads.updateTargetGroup", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Adsweb(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getAdCategories(self, office_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getAdCategories", **args)
		try: return AdswebGetAdCategoriesResponse(**r)
		except: return r


	async def getAdUnitCode(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getAdUnitCode", **args)
		try: return AdswebGetAdUnitCodeResponse(**r)
		except: return r


	async def getAdUnits(self, office_id:Optional[int]=None, sites_ids:Optional[str]=None, ad_units_ids:Optional[str]=None, fields:Optional[str]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getAdUnits", **args)
		try: return AdswebGetAdUnitsResponse(**r)
		except: return r


	async def getFraudHistory(self, office_id:Optional[int]=None, sites_ids:Optional[str]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getFraudHistory", **args)
		try: return AdswebGetFraudHistoryResponse(**r)
		except: return r


	async def getSites(self, office_id:Optional[int]=None, sites_ids:Optional[str]=None, fields:Optional[str]=None, limit:Optional[int]=None, offset:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getSites", **args)
		try: return AdswebGetSitesResponse(**r)
		except: return r


	async def getStatistics(self, office_id:Optional[int]=None, ids_type:Optional[str]=None, ids:Optional[str]=None, period:Optional[str]=None, date_from:Optional[str]=None, date_to:Optional[str]=None, fields:Optional[str]=None, limit:Optional[int]=None, page_id:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Adsweb.getStatistics", **args)
		try: return AdswebGetStatisticsResponse(**r)
		except: return r



class Appwidgets(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getAppImageUploadServer(self, image_type:Optional[str]=None):
		"""Returns a URL for uploading a photo to the community collection for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.getAppImageUploadServer", **args)
		try: return AppWidgetsGetAppImageUploadServerResponse(**r)
		except: return r


	async def getAppImages(self, offset:Optional[int]=None, count:Optional[int]=None, image_type:Optional[str]=None):
		"""Returns an app collection of images for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.getAppImages", **args)
		try: return AppWidgetsGetAppImagesResponse(**r)
		except: return r


	async def getGroupImageUploadServer(self, image_type:Optional[str]=None):
		"""Returns a URL for uploading a photo to the community collection for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.getGroupImageUploadServer", **args)
		try: return AppWidgetsGetGroupImageUploadServerResponse(**r)
		except: return r


	async def getGroupImages(self, offset:Optional[int]=None, count:Optional[int]=None, image_type:Optional[str]=None):
		"""Returns a community collection of images for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.getGroupImages", **args)
		try: return AppWidgetsGetGroupImagesResponse(**r)
		except: return r


	async def getImagesById(self, images:Optional[list[str]]=None):
		"""Returns an image for community app widgets by its ID"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.getImagesById", **args)
		try: return AppWidgetsGetImagesByIdResponse(**r)
		except: return r


	async def saveAppImage(self, hash:Optional[str]=None, image:Optional[str]=None):
		"""Allows to save image into app collection for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.saveAppImage", **args)
		try: return AppWidgetsSaveAppImageResponse(**r)
		except: return r


	async def saveGroupImage(self, hash:Optional[str]=None, image:Optional[str]=None):
		"""Allows to save image into community collection for community app widgets"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.saveGroupImage", **args)
		try: return AppWidgetsSaveGroupImageResponse(**r)
		except: return r


	async def update(self, code:Optional[str]=None, type:Optional[str]=None):
		"""Allows to update community app widget"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Appwidgets.update", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Apps(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def deleteAppRequests(self):
		"""Deletes all request notifications from the current app."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.deleteAppRequests", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, app_id:Optional[int]=None, app_ids:Optional[list[str]]=None, platform:Optional[str]=None, extended:Optional[bool]=None, return_friends:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns applications data."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.get", **args)
		try: return AppsGetResponse(**r)
		except: return r


	async def getCatalog(self, sort:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None, platform:Optional[str]=None, extended:Optional[bool]=None, return_friends:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None, q:Optional[str]=None, genre_id:Optional[int]=None, filter:Optional[str]=None):
		"""Returns a list of applications (apps) available to users in the App Catalog."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getCatalog", **args)
		try: return AppsGetCatalogResponse(**r)
		except: return r


	async def getFriendsList(self, extended:Optional[bool]=None, count:Optional[int]=None, offset:Optional[int]=None, type:Optional[str]=None, fields:Optional[list[UsersFields]]=None):
		"""Creates friends list for requests and invites in current app."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getFriendsList", **args)
		for i in [AppsGetFriendsListResponse, AppsGetFriendsListExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getLeaderboard(self, type:Optional[str]=None, _global:Optional[bool]=None, extended:Optional[bool]=None):
		"""Returns players rating in the game."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getLeaderboard", **args)
		for i in [AppsGetLeaderboardResponse, AppsGetLeaderboardExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getMiniAppPolicies(self, app_id:Optional[int]=None):
		"""Returns policies and terms given to a mini app."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getMiniAppPolicies", **args)
		try: return AppsGetMiniAppPoliciesResponse(**r)
		except: return r


	async def getScopes(self, type:Optional[str]=None):
		"""Returns scopes for auth"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getScopes", **args)
		try: return AppsGetScopesResponse(**r)
		except: return r


	async def getScore(self, user_id:Optional[int]=None):
		"""Returns user score in app"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.getScore", **args)
		try: return AppsGetScoreResponse(**r)
		except: return r


	async def promoHasActiveGift(self, promo_id:Optional[int]=None, user_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.promoHasActiveGift", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def promoUseGift(self, promo_id:Optional[int]=None, user_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.promoUseGift", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def sendRequest(self, user_id:Optional[int]=None, text:Optional[str]=None, type:Optional[str]=None, name:Optional[str]=None, key:Optional[str]=None, separate:Optional[bool]=None):
		"""Sends a request to another user in an app that uses VK authorization."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Apps.sendRequest", **args)
		try: return AppsSendRequestResponse(**r)
		except: return r



class Auth(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def restore(self, phone:Optional[str]=None, last_name:Optional[str]=None):
		"""Allows to restore account access using a code received via SMS. ' This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. '"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Auth.restore", **args)
		try: return AuthRestoreResponse(**r)
		except: return r



class Board(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addTopic(self, group_id:Optional[int]=None, title:Optional[str]=None, text:Optional[str]=None, from_group:Optional[bool]=None, attachments:Optional[list[str]]=None):
		"""Creates a new topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.addTopic", **args)
		try: return BoardAddTopicResponse(**r)
		except: return r


	async def closeTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None):
		"""Closes a topic on a community's discussion board so that comments cannot be posted."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.closeTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def createComment(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, from_group:Optional[bool]=None, sticker_id:Optional[int]=None, guid:Optional[str]=None):
		"""Adds a comment on a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.createComment", **args)
		try: return BoardCreateCommentResponse(**r)
		except: return r


	async def deleteComment(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Deletes a comment on a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.deleteComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None):
		"""Deletes a topic from a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.deleteTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, comment_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None):
		"""Edits a comment on a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, title:Optional[str]=None):
		"""Edits the title of a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.editTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def fixTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None):
		"""Pins a topic (fixes its place) to the top of a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.fixTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getComments(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, need_likes:Optional[bool]=None, start_comment_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, sort:Optional[str]=None):
		"""Returns a list of comments on a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.getComments", **args)
		for i in [BoardGetCommentsResponse, BoardGetCommentsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getTopics(self, group_id:Optional[int]=None, topic_ids:Optional[list[int]]=None, order:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, preview:Optional[int]=None, preview_length:Optional[int]=None):
		"""Returns a list of topics on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.getTopics", **args)
		for i in [BoardGetTopicsResponse, BoardGetTopicsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def openTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None):
		"""Re-opens a previously closed topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.openTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restoreComment(self, group_id:Optional[int]=None, topic_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Restores a comment deleted from a topic on a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.restoreComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unfixTopic(self, group_id:Optional[int]=None, topic_id:Optional[int]=None):
		"""Unpins a pinned topic from the top of a community's discussion board."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Board.unfixTopic", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Database(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getChairs(self, faculty_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns list of chairs on a specified faculty."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getChairs", **args)
		try: return DatabaseGetChairsResponse(**r)
		except: return r


	async def getCities(self, country_id:Optional[int]=None, region_id:Optional[int]=None, q:Optional[str]=None, need_all:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of cities."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getCities", **args)
		try: return DatabaseGetCitiesResponse(**r)
		except: return r


	async def getCitiesById(self, city_ids:Optional[list[int]]=None):
		"""Returns information about cities by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getCitiesById", **args)
		try: return DatabaseGetCitiesByIdResponse(**r)
		except: return r


	async def getCountries(self, need_all:Optional[bool]=None, code:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of countries."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getCountries", **args)
		try: return DatabaseGetCountriesResponse(**r)
		except: return r


	async def getCountriesById(self, country_ids:Optional[list[int]]=None):
		"""Returns information about countries by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getCountriesById", **args)
		try: return DatabaseGetCountriesByIdResponse(**r)
		except: return r


	async def getFaculties(self, university_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of faculties (i.e., university departments)."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getFaculties", **args)
		try: return DatabaseGetFacultiesResponse(**r)
		except: return r


	async def getMetroStations(self, city_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None):
		"""Get metro stations by city"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getMetroStations", **args)
		try: return DatabaseGetMetroStationsResponse(**r)
		except: return r


	async def getMetroStationsById(self, station_ids:Optional[list[int]]=None):
		"""Get metro station by his id"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getMetroStationsById", **args)
		try: return DatabaseGetMetroStationsByIdResponse(**r)
		except: return r


	async def getRegions(self, country_id:Optional[int]=None, q:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of regions."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getRegions", **args)
		try: return DatabaseGetRegionsResponse(**r)
		except: return r


	async def getSchoolClasses(self, country_id:Optional[int]=None):
		"""Returns a list of school classes specified for the country."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getSchoolClasses", **args)
		try: return DatabaseGetSchoolClassesResponse(**r)
		except: return r


	async def getSchools(self, q:Optional[str]=None, city_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of schools."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getSchools", **args)
		try: return DatabaseGetSchoolsResponse(**r)
		except: return r


	async def getUniversities(self, q:Optional[str]=None, country_id:Optional[int]=None, city_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of higher education institutions."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Database.getUniversities", **args)
		try: return DatabaseGetUniversitiesResponse(**r)
		except: return r



class Docs(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, owner_id:Optional[int]=None, doc_id:Optional[int]=None, access_key:Optional[str]=None):
		"""Copies a document to a user's or community's document list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.add", **args)
		try: return DocsAddResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, doc_id:Optional[int]=None):
		"""Deletes a user or community document."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, doc_id:Optional[int]=None, title:Optional[str]=None, tags:Optional[list[str]]=None):
		"""Edits a document."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, count:Optional[int]=None, offset:Optional[int]=None, type:Optional[int]=None, owner_id:Optional[int]=None, return_tags:Optional[bool]=None):
		"""Returns detailed information about user or community documents."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.get", **args)
		try: return DocsGetResponse(**r)
		except: return r


	async def getById(self, docs:Optional[list[str]]=None, return_tags:Optional[bool]=None):
		"""Returns information about documents by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.getById", **args)
		try: return DocsGetByIdResponse(**r)
		except: return r


	async def getMessagesUploadServer(self, type:Optional[str]=None, peer_id:Optional[int]=None):
		"""Returns the server address for document upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.getMessagesUploadServer", **args)
		try: return DocsGetUploadServerResponse(**r)
		except: return r


	async def getTypes(self, owner_id:Optional[int]=None):
		"""Returns documents types available for current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.getTypes", **args)
		try: return DocsGetTypesResponse(**r)
		except: return r


	async def getUploadServer(self, group_id:Optional[int]=None):
		"""Returns the server address for document upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.getUploadServer", **args)
		try: return DocsGetUploadServerResponse(**r)
		except: return r


	async def getWallUploadServer(self, group_id:Optional[int]=None):
		"""Returns the server address for document upload onto a user's or community's wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.getWallUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def save(self, file:Optional[str]=None, title:Optional[str]=None, tags:Optional[str]=None, return_tags:Optional[bool]=None):
		"""Saves a document after [vk.com/dev/upload_files_2|uploading it to a server]."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.save", **args)
		try: return DocsSaveResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, search_own:Optional[bool]=None, count:Optional[int]=None, offset:Optional[int]=None, return_tags:Optional[bool]=None):
		"""Returns a list of documents matching the search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Docs.search", **args)
		try: return DocsSearchResponse(**r)
		except: return r



class Donut(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getFriends(self, owner_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[str]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Donut.getFriends", **args)
		try: return GroupsGetMembersFieldsResponse(**r)
		except: return r


	async def getSubscription(self, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Donut.getSubscription", **args)
		try: return DonutGetSubscriptionResponse(**r)
		except: return r


	async def getSubscriptions(self, fields:Optional[list[BaseUserGroupFields]]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of user's VK Donut subscriptions."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Donut.getSubscriptions", **args)
		try: return DonutGetSubscriptionsResponse(**r)
		except: return r


	async def isDon(self, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Donut.isDon", **args)
		try: return BaseBoolResponse(**r)
		except: return r



class Downloadedgames(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getPaidStatus(self, user_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Downloadedgames.getPaidStatus", **args)
		try: return DownloadedGamesPaidStatusResponse(**r)
		except: return r



class Fave(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addArticle(self, url:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addArticle", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addLink(self, link:Optional[str]=None):
		"""Adds a link to user faves."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addLink", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addPage(self, user_id:Optional[int]=None, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addPage", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addPost(self, owner_id:Optional[int]=None, id:Optional[int]=None, access_key:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addPost", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addProduct(self, owner_id:Optional[int]=None, id:Optional[int]=None, access_key:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addProduct", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addTag(self, name:Optional[str]=None, position:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addTag", **args)
		try: return FaveAddTagResponse(**r)
		except: return r


	async def addVideo(self, owner_id:Optional[int]=None, id:Optional[int]=None, access_key:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.addVideo", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editTag(self, id:Optional[int]=None, name:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.editTag", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, extended:Optional[bool]=None, item_type:Optional[str]=None, tag_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[str]=None, is_from_snackbar:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.get", **args)
		for i in [FaveGetResponse, FaveGetExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getPages(self, offset:Optional[int]=None, count:Optional[int]=None, type:Optional[str]=None, fields:Optional[list[BaseUserGroupFields]]=None, tag_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.getPages", **args)
		try: return FaveGetPagesResponse(**r)
		except: return r


	async def getTags(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.getTags", **args)
		try: return FaveGetTagsResponse(**r)
		except: return r


	async def markSeen(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.markSeen", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def removeArticle(self, owner_id:Optional[int]=None, article_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removeArticle", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def removeLink(self, link_id:Optional[str]=None, link:Optional[str]=None):
		"""Removes link from the user's faves."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removeLink", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removePage(self, user_id:Optional[int]=None, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removePage", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removePost(self, owner_id:Optional[int]=None, id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removePost", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removeProduct(self, owner_id:Optional[int]=None, id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removeProduct", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removeTag(self, id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removeTag", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removeVideo(self, owner_id:Optional[int]=None, id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.removeVideo", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderTags(self, ids:Optional[list[int]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.reorderTags", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setPageTags(self, user_id:Optional[int]=None, group_id:Optional[int]=None, tag_ids:Optional[list[int]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.setPageTags", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setTags(self, item_type:Optional[str]=None, item_owner_id:Optional[int]=None, item_id:Optional[int]=None, tag_ids:Optional[list[int]]=None, link_id:Optional[str]=None, link_url:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.setTags", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def trackPageInteraction(self, user_id:Optional[int]=None, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Fave.trackPageInteraction", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Friends(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, user_id:Optional[int]=None, text:Optional[str]=None, follow:Optional[bool]=None):
		"""Approves or creates a friend request."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.add", **args)
		try: return FriendsAddResponse(**r)
		except: return r


	async def addList(self, name:Optional[str]=None, user_ids:Optional[list[int]]=None):
		"""Creates a new friend list for the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.addList", **args)
		try: return FriendsAddListResponse(**r)
		except: return r


	async def areFriends(self, user_ids:Optional[list[int]]=None, need_sign:Optional[bool]=None, extended:Optional[bool]=None):
		"""Checks the current user's friendship status with other specified users."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.areFriends", **args)
		for i in [FriendsAreFriendsResponse, FriendsAreFriendsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def delete(self, user_id:Optional[int]=None):
		"""Declines a friend request or deletes a user from the current user's friend list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.delete", **args)
		try: return FriendsDeleteResponse(**r)
		except: return r


	async def deleteAllRequests(self):
		"""Marks all incoming friend requests as viewed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.deleteAllRequests", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteList(self, list_id:Optional[int]=None):
		"""Deletes a friend list of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.deleteList", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, user_id:Optional[int]=None, list_ids:Optional[list[int]]=None):
		"""Edits the friend lists of the selected user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editList(self, name:Optional[str]=None, list_id:Optional[int]=None, user_ids:Optional[list[int]]=None, add_user_ids:Optional[list[int]]=None, delete_user_ids:Optional[list[int]]=None):
		"""Edits a friend list of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.editList", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, user_id:Optional[int]=None, order:Optional[str]=None, list_id:Optional[int]=None, count:Optional[int]=None, offset:Optional[int]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None, ref:Optional[str]=None):
		"""Returns a list of user IDs or detailed information about a user's friends."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.get", **args)
		for i in [FriendsGetResponse, FriendsGetFieldsResponse]:
			try: return i(**r)
			except: return r


	async def getAppUsers(self):
		"""Returns a list of IDs of the current user's friends who installed the application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getAppUsers", **args)
		try: return FriendsGetAppUsersResponse(**r)
		except: return r


	async def getByPhones(self, phones:Optional[list[str]]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getByPhones", **args)
		try: return FriendsGetByPhonesResponse(**r)
		except: return r


	async def getLists(self, user_id:Optional[int]=None, return_system:Optional[bool]=None):
		"""Returns a list of the user's friend lists."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getLists", **args)
		try: return FriendsGetListsResponse(**r)
		except: return r


	async def getMutual(self, source_uid:Optional[int]=None, target_uid:Optional[int]=None, target_uids:Optional[list[int]]=None, order:Optional[str]=None, count:Optional[int]=None, offset:Optional[int]=None):
		"""Returns a list of user IDs of the mutual friends of two users."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getMutual", **args)
		for i in [FriendsGetMutualResponse, FriendsGetMutualTargetUidsResponse]:
			try: return i(**r)
			except: return r


	async def getOnline(self, user_id:Optional[int]=None, list_id:Optional[int]=None, online_mobile:Optional[bool]=None, order:Optional[str]=None, count:Optional[int]=None, offset:Optional[int]=None):
		"""Returns a list of user IDs of a user's friends who are online."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getOnline", **args)
		for i in [FriendsGetOnlineResponse, FriendsGetOnlineOnlineMobileResponse]:
			try: return i(**r)
			except: return r


	async def getRecent(self, count:Optional[int]=None):
		"""Returns a list of user IDs of the current user's recently added friends."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getRecent", **args)
		try: return FriendsGetRecentResponse(**r)
		except: return r


	async def getRequests(self, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, need_mutual:Optional[bool]=None, out:Optional[bool]=None, sort:Optional[int]=None, need_viewed:Optional[bool]=None, suggested:Optional[bool]=None, ref:Optional[str]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns information about the current user's incoming and outgoing friend requests."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getRequests", **args)
		for i in [FriendsGetRequestsResponse, FriendsGetRequestsNeedMutualResponse, FriendsGetRequestsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getSuggestions(self, filter:Optional[list[str]]=None, count:Optional[int]=None, offset:Optional[int]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns a list of profiles of users whom the current user may know."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.getSuggestions", **args)
		try: return FriendsGetSuggestionsResponse(**r)
		except: return r


	async def search(self, user_id:Optional[int]=None, q:Optional[str]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of friends matching the search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Friends.search", **args)
		try: return FriendsSearchResponse(**r)
		except: return r



class Gifts(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, user_id:Optional[int]=None, count:Optional[int]=None, offset:Optional[int]=None):
		"""Returns a list of user gifts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Gifts.get", **args)
		try: return GiftsGetResponse(**r)
		except: return r



class Groups(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addAddress(self, group_id:Optional[int]=None, title:Optional[str]=None, address:Optional[str]=None, additional_address:Optional[str]=None, country_id:Optional[int]=None, city_id:Optional[int]=None, metro_id:Optional[int]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, phone:Optional[str]=None, work_info_status:Optional[str]=None, timetable:Optional[str]=None, is_main_address:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.addAddress", **args)
		try: return GroupsAddAddressResponse(**r)
		except: return r


	async def addCallbackServer(self, group_id:Optional[int]=None, url:Optional[str]=None, title:Optional[str]=None, secret_key:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.addCallbackServer", **args)
		try: return GroupsAddCallbackServerResponse(**r)
		except: return r


	async def addLink(self, group_id:Optional[int]=None, link:Optional[str]=None, text:Optional[str]=None):
		"""Allows to add a link to the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.addLink", **args)
		try: return GroupsAddLinkResponse(**r)
		except: return r


	async def approveRequest(self, group_id:Optional[int]=None, user_id:Optional[int]=None):
		"""Allows to approve join request to the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.approveRequest", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def ban(self, group_id:Optional[int]=None, owner_id:Optional[int]=None, end_date:Optional[int]=None, reason:Optional[int]=None, comment:Optional[str]=None, comment_visible:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.ban", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def create(self, title:Optional[str]=None, description:Optional[str]=None, type:Optional[str]=None, public_category:Optional[int]=None, public_subcategory:Optional[int]=None, subtype:Optional[int]=None):
		"""Creates a new community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.create", **args)
		try: return GroupsCreateResponse(**r)
		except: return r


	async def deleteAddress(self, group_id:Optional[int]=None, address_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.deleteAddress", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteCallbackServer(self, group_id:Optional[int]=None, server_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.deleteCallbackServer", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteLink(self, group_id:Optional[int]=None, link_id:Optional[int]=None):
		"""Allows to delete a link from the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.deleteLink", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def disableOnline(self, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.disableOnline", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, group_id:Optional[int]=None, title:Optional[str]=None, description:Optional[str]=None, screen_name:Optional[str]=None, access:Optional[int]=None, website:Optional[str]=None, subject:Optional[str]=None, email:Optional[str]=None, phone:Optional[str]=None, rss:Optional[str]=None, event_start_date:Optional[int]=None, event_finish_date:Optional[int]=None, event_group_id:Optional[int]=None, public_category:Optional[int]=None, public_subcategory:Optional[int]=None, public_date:Optional[str]=None, wall:Optional[int]=None, topics:Optional[int]=None, photos:Optional[int]=None, video:Optional[int]=None, audio:Optional[int]=None, links:Optional[bool]=None, events:Optional[bool]=None, places:Optional[bool]=None, contacts:Optional[bool]=None, docs:Optional[int]=None, wiki:Optional[int]=None, messages:Optional[bool]=None, articles:Optional[bool]=None, addresses:Optional[bool]=None, age_limits:Optional[int]=None, market:Optional[bool]=None, market_comments:Optional[bool]=None, market_country:Optional[list[int]]=None, market_city:Optional[list[int]]=None, market_currency:Optional[int]=None, market_contact:Optional[int]=None, market_wiki:Optional[int]=None, obscene_filter:Optional[bool]=None, obscene_stopwords:Optional[bool]=None, obscene_words:Optional[list[str]]=None, main_section:Optional[int]=None, secondary_section:Optional[int]=None, country:Optional[int]=None, city:Optional[int]=None):
		"""Edits a community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editAddress(self, group_id:Optional[int]=None, address_id:Optional[int]=None, title:Optional[str]=None, address:Optional[str]=None, additional_address:Optional[str]=None, country_id:Optional[int]=None, city_id:Optional[int]=None, metro_id:Optional[int]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, phone:Optional[str]=None, work_info_status:Optional[str]=None, timetable:Optional[str]=None, is_main_address:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.editAddress", **args)
		try: return GroupsEditAddressResponse(**r)
		except: return r


	async def editCallbackServer(self, group_id:Optional[int]=None, server_id:Optional[int]=None, url:Optional[str]=None, title:Optional[str]=None, secret_key:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.editCallbackServer", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editLink(self, group_id:Optional[int]=None, link_id:Optional[int]=None, text:Optional[str]=None):
		"""Allows to edit a link in the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.editLink", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editManager(self, group_id:Optional[int]=None, user_id:Optional[int]=None, role:Optional[str]=None, is_contact:Optional[bool]=None, contact_position:Optional[str]=None, contact_phone:Optional[str]=None, contact_email:Optional[str]=None):
		"""Allows to add, remove or edit the community manager."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.editManager", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def enableOnline(self, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.enableOnline", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, user_id:Optional[int]=None, extended:Optional[bool]=None, filter:Optional[list[GroupsFilter]]=None, fields:Optional[list[GroupsFields]]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of the communities to which a user belongs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.get", **args)
		for i in [GroupsGetResponse, GroupsGetObjectExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getAddresses(self, group_id:Optional[int]=None, address_ids:Optional[list[int]]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[AddressesFields]]=None):
		"""Returns a list of community addresses."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getAddresses", **args)
		try: return GroupsGetAddressesResponse(**r)
		except: return r


	async def getBanned(self, group_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None, owner_id:Optional[int]=None):
		"""Returns a list of users on a community blacklist."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getBanned", **args)
		try: return GroupsGetBannedResponse(**r)
		except: return r


	async def getById(self, group_ids:Optional[list[int|str]]=None, group_id:Optional[list[int|str]]=None, fields:Optional[list[GroupsFields]]=None):
		"""Returns information about communities by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getById", **args)
		try: return GroupsGetByIdObjectLegacyResponse(**r)
		except: return r


	async def getCallbackConfirmationCode(self, group_id:Optional[int]=None):
		"""Returns Callback API confirmation code for the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getCallbackConfirmationCode", **args)
		try: return GroupsGetCallbackConfirmationCodeResponse(**r)
		except: return r


	async def getCallbackServers(self, group_id:Optional[int]=None, server_ids:Optional[list[int]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getCallbackServers", **args)
		try: return GroupsGetCallbackServersResponse(**r)
		except: return r


	async def getCallbackSettings(self, group_id:Optional[int]=None, server_id:Optional[int]=None):
		"""Returns [vk.com/dev/callback_api|Callback API] notifications settings."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getCallbackSettings", **args)
		try: return GroupsGetCallbackSettingsResponse(**r)
		except: return r


	async def getCatalog(self, category_id:Optional[int]=None, subcategory_id:Optional[int]=None):
		"""Returns communities list for a catalog category."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getCatalog", **args)
		try: return GroupsGetCatalogResponse(**r)
		except: return r


	async def getCatalogInfo(self, extended:Optional[bool]=None, subcategories:Optional[bool]=None):
		"""Returns categories list for communities catalog"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getCatalogInfo", **args)
		for i in [GroupsGetCatalogInfoResponse, GroupsGetCatalogInfoExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getInvitedUsers(self, group_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns invited users list of a community"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getInvitedUsers", **args)
		try: return GroupsGetInvitedUsersResponse(**r)
		except: return r


	async def getInvites(self, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None):
		"""Returns a list of invitations to join communities and events."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getInvites", **args)
		for i in [GroupsGetInvitesResponse, GroupsGetInvitesExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getLongPollServer(self, group_id:Optional[int]=None):
		"""Returns the data needed to query a Long Poll server for events"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getLongPollServer", **args)
		try: return GroupsGetLongPollServerResponse(**r)
		except: return r


	async def getLongPollSettings(self, group_id:Optional[int]=None):
		"""Returns Long Poll notification settings"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getLongPollSettings", **args)
		try: return GroupsGetLongPollSettingsResponse(**r)
		except: return r


	async def getMembers(self, group_id:Optional[str]=None, sort:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None, filter:Optional[str]=None):
		"""Returns a list of community members."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getMembers", **args)
		for i in [GroupsGetMembersResponse, GroupsGetMembersFieldsResponse, GroupsGetMembersFilterResponse]:
			try: return i(**r)
			except: return r


	async def getRequests(self, group_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns a list of requests to the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getRequests", **args)
		for i in [GroupsGetRequestsResponse, GroupsGetRequestsFieldsResponse]:
			try: return i(**r)
			except: return r


	async def getSettings(self, group_id:Optional[int]=None):
		"""Returns community settings."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getSettings", **args)
		try: return GroupsGetSettingsResponse(**r)
		except: return r


	async def getTagList(self, group_id:Optional[int]=None):
		"""List of group's tags"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getTagList", **args)
		try: return GroupsGetTagListResponse(**r)
		except: return r


	async def getTokenPermissions(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.getTokenPermissions", **args)
		try: return GroupsGetTokenPermissionsResponse(**r)
		except: return r


	async def invite(self, group_id:Optional[int]=None, user_id:Optional[int]=None):
		"""Allows to invite friends to the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.invite", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def isMember(self, group_id:Optional[str]=None, user_id:Optional[int]=None, user_ids:Optional[list[int]]=None, extended:Optional[bool]=None):
		"""Returns information specifying whether a user is a member of a community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.isMember", **args)
		for i in [GroupsIsMemberResponse, GroupsIsMemberUserIdsResponse, GroupsIsMemberExtendedResponse, GroupsIsMemberUserIdsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def join(self, group_id:Optional[int]=None, not_sure:Optional[str]=None):
		"""With this method you can join the group or public page, and also confirm your participation in an event."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.join", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def leave(self, group_id:Optional[int]=None):
		"""With this method you can leave a group, public page, or event."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.leave", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def removeUser(self, group_id:Optional[int]=None, user_id:Optional[int]=None):
		"""Removes a user from the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.removeUser", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderLink(self, group_id:Optional[int]=None, link_id:Optional[int]=None, after:Optional[int]=None):
		"""Allows to reorder links in the community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.reorderLink", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, type:Optional[str]=None, country_id:Optional[int]=None, city_id:Optional[int]=None, future:Optional[bool]=None, market:Optional[bool]=None, sort:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of communities matching the search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.search", **args)
		try: return GroupsSearchResponse(**r)
		except: return r


	async def setCallbackSettings(self, group_id:Optional[int]=None, server_id:Optional[int]=None, api_version:Optional[str]=None, message_new:Optional[bool]=None, message_reply:Optional[bool]=None, message_allow:Optional[bool]=None, message_edit:Optional[bool]=None, message_deny:Optional[bool]=None, message_typing_state:Optional[bool]=None, photo_new:Optional[bool]=None, audio_new:Optional[bool]=None, video_new:Optional[bool]=None, wall_reply_new:Optional[bool]=None, wall_reply_edit:Optional[bool]=None, wall_reply_delete:Optional[bool]=None, wall_reply_restore:Optional[bool]=None, wall_post_new:Optional[bool]=None, wall_repost:Optional[bool]=None, board_post_new:Optional[bool]=None, board_post_edit:Optional[bool]=None, board_post_restore:Optional[bool]=None, board_post_delete:Optional[bool]=None, photo_comment_new:Optional[bool]=None, photo_comment_edit:Optional[bool]=None, photo_comment_delete:Optional[bool]=None, photo_comment_restore:Optional[bool]=None, video_comment_new:Optional[bool]=None, video_comment_edit:Optional[bool]=None, video_comment_delete:Optional[bool]=None, video_comment_restore:Optional[bool]=None, market_comment_new:Optional[bool]=None, market_comment_edit:Optional[bool]=None, market_comment_delete:Optional[bool]=None, market_comment_restore:Optional[bool]=None, market_order_new:Optional[bool]=None, market_order_edit:Optional[bool]=None, poll_vote_new:Optional[bool]=None, group_join:Optional[bool]=None, group_leave:Optional[bool]=None, group_change_settings:Optional[bool]=None, group_change_photo:Optional[bool]=None, group_officers_edit:Optional[bool]=None, user_block:Optional[bool]=None, user_unblock:Optional[bool]=None, lead_forms_new:Optional[bool]=None, like_add:Optional[bool]=None, like_remove:Optional[bool]=None, message_event:Optional[bool]=None, donut_subscription_create:Optional[bool]=None, donut_subscription_prolonged:Optional[bool]=None, donut_subscription_cancelled:Optional[bool]=None, donut_subscription_price_changed:Optional[bool]=None, donut_subscription_expired:Optional[bool]=None, donut_money_withdraw:Optional[bool]=None, donut_money_withdraw_error:Optional[bool]=None):
		"""Allow to set notifications settings for group."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.setCallbackSettings", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setLongPollSettings(self, group_id:Optional[int]=None, enabled:Optional[bool]=None, api_version:Optional[str]=None, message_new:Optional[bool]=None, message_reply:Optional[bool]=None, message_allow:Optional[bool]=None, message_deny:Optional[bool]=None, message_edit:Optional[bool]=None, message_typing_state:Optional[bool]=None, photo_new:Optional[bool]=None, audio_new:Optional[bool]=None, video_new:Optional[bool]=None, wall_reply_new:Optional[bool]=None, wall_reply_edit:Optional[bool]=None, wall_reply_delete:Optional[bool]=None, wall_reply_restore:Optional[bool]=None, wall_post_new:Optional[bool]=None, wall_repost:Optional[bool]=None, board_post_new:Optional[bool]=None, board_post_edit:Optional[bool]=None, board_post_restore:Optional[bool]=None, board_post_delete:Optional[bool]=None, photo_comment_new:Optional[bool]=None, photo_comment_edit:Optional[bool]=None, photo_comment_delete:Optional[bool]=None, photo_comment_restore:Optional[bool]=None, video_comment_new:Optional[bool]=None, video_comment_edit:Optional[bool]=None, video_comment_delete:Optional[bool]=None, video_comment_restore:Optional[bool]=None, market_comment_new:Optional[bool]=None, market_comment_edit:Optional[bool]=None, market_comment_delete:Optional[bool]=None, market_comment_restore:Optional[bool]=None, poll_vote_new:Optional[bool]=None, group_join:Optional[bool]=None, group_leave:Optional[bool]=None, group_change_settings:Optional[bool]=None, group_change_photo:Optional[bool]=None, group_officers_edit:Optional[bool]=None, user_block:Optional[bool]=None, user_unblock:Optional[bool]=None, like_add:Optional[bool]=None, like_remove:Optional[bool]=None, message_event:Optional[bool]=None, donut_subscription_create:Optional[bool]=None, donut_subscription_prolonged:Optional[bool]=None, donut_subscription_cancelled:Optional[bool]=None, donut_subscription_price_changed:Optional[bool]=None, donut_subscription_expired:Optional[bool]=None, donut_money_withdraw:Optional[bool]=None, donut_money_withdraw_error:Optional[bool]=None):
		"""Sets Long Poll notification settings"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.setLongPollSettings", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setSettings(self, group_id:Optional[int]=None, messages:Optional[bool]=None, bots_capabilities:Optional[bool]=None, bots_start_button:Optional[bool]=None, bots_add_to_chat:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.setSettings", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setUserNote(self, group_id:Optional[int]=None, user_id:Optional[int]=None, note:Optional[str]=None):
		"""In order to save note about group participant"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.setUserNote", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def tagAdd(self, group_id:Optional[int]=None, tag_name:Optional[str]=None, tag_color:Optional[str]=None):
		"""Add new group's tag"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.tagAdd", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def tagBind(self, group_id:Optional[int]=None, tag_id:Optional[int]=None, user_id:Optional[int]=None, act:Optional[str]=None):
		"""Bind or unbind group's tag to user"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.tagBind", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def tagDelete(self, group_id:Optional[int]=None, tag_id:Optional[int]=None):
		"""Delete group's tag"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.tagDelete", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def tagUpdate(self, group_id:Optional[int]=None, tag_id:Optional[int]=None, tag_name:Optional[str]=None):
		"""Update group's tag"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.tagUpdate", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def toggleMarket(self, group_id:Optional[int]=None, state:Optional[str]=None, ref:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.toggleMarket", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unban(self, group_id:Optional[int]=None, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Groups.unban", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Leadforms(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def create(self, group_id:Optional[int]=None, name:Optional[str]=None, title:Optional[str]=None, description:Optional[str]=None, questions:Optional[str]=None, policy_link_url:Optional[str]=None, photo:Optional[str]=None, confirmation:Optional[str]=None, site_link_url:Optional[str]=None, active:Optional[bool]=None, once_per_user:Optional[bool]=None, pixel_code:Optional[str]=None, notify_admins:Optional[list[int]]=None, notify_emails:Optional[list[str]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.create", **args)
		try: return LeadFormsCreateResponse(**r)
		except: return r


	async def delete(self, group_id:Optional[int]=None, form_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.delete", **args)
		try: return LeadFormsDeleteResponse(**r)
		except: return r


	async def get(self, group_id:Optional[int]=None, form_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.get", **args)
		try: return LeadFormsGetResponse(**r)
		except: return r


	async def getLeads(self, group_id:Optional[int]=None, form_id:Optional[int]=None, limit:Optional[int]=None, next_page_token:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.getLeads", **args)
		try: return LeadFormsGetLeadsResponse(**r)
		except: return r


	async def getUploadURL(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.getUploadURL", **args)
		try: return LeadFormsUploadUrlResponse(**r)
		except: return r


	async def _list(self, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms._list", **args)
		try: return LeadFormsListResponse(**r)
		except: return r


	async def update(self, group_id:Optional[int]=None, form_id:Optional[int]=None, name:Optional[str]=None, title:Optional[str]=None, description:Optional[str]=None, questions:Optional[str]=None, policy_link_url:Optional[str]=None, photo:Optional[str]=None, confirmation:Optional[str]=None, site_link_url:Optional[str]=None, active:Optional[bool]=None, once_per_user:Optional[bool]=None, pixel_code:Optional[str]=None, notify_admins:Optional[list[int]]=None, notify_emails:Optional[list[str]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Leadforms.update", **args)
		try: return LeadFormsCreateResponse(**r)
		except: return r



class Likes(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None, access_key:Optional[str]=None):
		"""Adds the specified object to the 'Likes' list of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Likes.add", **args)
		try: return LikesAddResponse(**r)
		except: return r


	async def delete(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None, access_key:Optional[str]=None):
		"""Deletes the specified object from the 'Likes' list of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Likes.delete", **args)
		try: return LikesDeleteResponse(**r)
		except: return r


	async def getList(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None, page_url:Optional[str]=None, filter:Optional[str]=None, friends_only:Optional[int]=None, extended:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None, skip_own:Optional[bool]=None):
		"""Returns a list of IDs of users who added the specified object to their 'Likes' list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Likes.getList", **args)
		for i in [LikesGetListResponse, LikesGetListExtendedResponse]:
			try: return i(**r)
			except: return r


	async def isLiked(self, user_id:Optional[int]=None, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None):
		"""Checks for the object in the 'Likes' list of the specified user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Likes.isLiked", **args)
		try: return LikesIsLikedResponse(**r)
		except: return r



class Market(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, owner_id:Optional[int]=None, name:Optional[str]=None, description:Optional[str]=None, category_id:Optional[int]=None, price:Optional[int]=None, old_price:Optional[int]=None, deleted:Optional[bool]=None, main_photo_id:Optional[int]=None, photo_ids:Optional[list[int]]=None, url:Optional[str]=None, dimension_width:Optional[int]=None, dimension_height:Optional[int]=None, dimension_length:Optional[int]=None, weight:Optional[int]=None, sku:Optional[str]=None):
		"""Ads a new item to the market."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.add", **args)
		try: return MarketAddResponse(**r)
		except: return r


	async def addAlbum(self, owner_id:Optional[int]=None, title:Optional[str]=None, photo_id:Optional[int]=None, main_album:Optional[bool]=None, is_hidden:Optional[bool]=None):
		"""Creates new collection of items"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.addAlbum", **args)
		try: return MarketAddAlbumResponse(**r)
		except: return r


	async def addToAlbum(self, owner_id:Optional[int]=None, item_ids:Optional[list[int]]=None, album_ids:Optional[list[int]]=None):
		"""Adds an item to one or multiple collections."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.addToAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def createComment(self, owner_id:Optional[int]=None, item_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, from_group:Optional[bool]=None, reply_to_comment:Optional[int]=None, sticker_id:Optional[int]=None, guid:Optional[str]=None):
		"""Creates a new comment for an item."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.createComment", **args)
		try: return MarketCreateCommentResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, item_id:Optional[int]=None):
		"""Deletes an item."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteAlbum(self, owner_id:Optional[int]=None, album_id:Optional[int]=None):
		"""Deletes a collection of items."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.deleteAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Deletes an item's comment"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.deleteComment", **args)
		try: return MarketDeleteCommentResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, item_id:Optional[int]=None, name:Optional[str]=None, description:Optional[str]=None, category_id:Optional[int]=None, price:Optional[int]=None, old_price:Optional[int]=None, deleted:Optional[bool]=None, main_photo_id:Optional[int]=None, photo_ids:Optional[list[int]]=None, url:Optional[str]=None, dimension_width:Optional[int]=None, dimension_height:Optional[int]=None, dimension_length:Optional[int]=None, weight:Optional[int]=None, sku:Optional[str]=None):
		"""Edits an item."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editAlbum(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, title:Optional[str]=None, photo_id:Optional[int]=None, main_album:Optional[bool]=None, is_hidden:Optional[bool]=None):
		"""Edits a collection of items"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.editAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None):
		"""Chages item comment's text"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editOrder(self, user_id:Optional[int]=None, order_id:Optional[int]=None, merchant_comment:Optional[str]=None, status:Optional[int]=None, track_number:Optional[str]=None, payment_status:Optional[str]=None, delivery_price:Optional[int]=None, width:Optional[int]=None, length:Optional[int]=None, height:Optional[int]=None, weight:Optional[int]=None):
		"""Edit order"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.editOrder", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, count:Optional[int]=None, offset:Optional[int]=None, extended:Optional[bool]=None, date_from:Optional[str]=None, date_to:Optional[str]=None, need_variants:Optional[bool]=None, with_disabled:Optional[bool]=None):
		"""Returns items list for a community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.get", **args)
		for i in [MarketGetResponse, MarketGetExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getAlbumById(self, owner_id:Optional[int]=None, album_ids:Optional[list[int]]=None):
		"""Returns items album's data"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getAlbumById", **args)
		try: return MarketGetAlbumByIdResponse(**r)
		except: return r


	async def getAlbums(self, owner_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns community's market collections list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getAlbums", **args)
		try: return MarketGetAlbumsResponse(**r)
		except: return r


	async def getById(self, item_ids:Optional[list[str]]=None, extended:Optional[bool]=None):
		"""Returns information about market items by their ids."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getById", **args)
		for i in [MarketGetByIdResponse, MarketGetByIdExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getCategories(self, count:Optional[int]=None, offset:Optional[int]=None):
		"""Returns a list of market categories."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getCategories", **args)
		try: return MarketGetCategoriesResponse(**r)
		except: return r


	async def getComments(self, owner_id:Optional[int]=None, item_id:Optional[int]=None, need_likes:Optional[bool]=None, start_comment_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, sort:Optional[str]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns comments list for an item."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getComments", **args)
		try: return MarketGetCommentsResponse(**r)
		except: return r


	async def getGroupOrders(self, group_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Get market orders"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getGroupOrders", **args)
		try: return MarketGetGroupOrdersResponse(**r)
		except: return r


	async def getOrderById(self, user_id:Optional[int]=None, order_id:Optional[int]=None, extended:Optional[bool]=None):
		"""Get order"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getOrderById", **args)
		try: return MarketGetOrderByIdResponse(**r)
		except: return r


	async def getOrderItems(self, user_id:Optional[int]=None, order_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Get market items in the order"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getOrderItems", **args)
		try: return MarketGetOrderItemsResponse(**r)
		except: return r


	async def getOrders(self, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, date_from:Optional[str]=None, date_to:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.getOrders", **args)
		for i in [MarketGetOrdersResponse, MarketGetOrdersExtendedResponse]:
			try: return i(**r)
			except: return r


	async def removeFromAlbum(self, owner_id:Optional[int]=None, item_id:Optional[int]=None, album_ids:Optional[list[int]]=None):
		"""Removes an item from one or multiple collections."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.removeFromAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderAlbums(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, before:Optional[int]=None, after:Optional[int]=None):
		"""Reorders the collections list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.reorderAlbums", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderItems(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, item_id:Optional[int]=None, before:Optional[int]=None, after:Optional[int]=None):
		"""Changes item place in a collection."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.reorderItems", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def report(self, owner_id:Optional[int]=None, item_id:Optional[int]=None, reason:Optional[int]=None):
		"""Sends a complaint to the item."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.report", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reportComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, reason:Optional[int]=None):
		"""Sends a complaint to the item's comment."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.reportComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restore(self, owner_id:Optional[int]=None, item_id:Optional[int]=None):
		"""Restores recently deleted item"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.restore", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restoreComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Restores a recently deleted comment"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.restoreComment", **args)
		try: return MarketRestoreCommentResponse(**r)
		except: return r


	async def search(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, q:Optional[str]=None, price_from:Optional[int]=None, price_to:Optional[int]=None, sort:Optional[int]=None, rev:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, status:Optional[list[int]]=None, need_variants:Optional[bool]=None):
		"""Searches market items in a community's catalog"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.search", **args)
		for i in [MarketSearchResponse, MarketSearchExtendedResponse]:
			try: return i(**r)
			except: return r


	async def searchItems(self, q:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None, category_id:Optional[int]=None, price_from:Optional[int]=None, price_to:Optional[int]=None, sort_by:Optional[int]=None, sort_direction:Optional[int]=None, country:Optional[int]=None, city:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Market.searchItems", **args)
		try: return MarketSearchResponse(**r)
		except: return r



class Messages(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addChatUser(self, chat_id:Optional[int]=None, user_id:Optional[int]=None, visible_messages_count:Optional[int]=None):
		"""Adds a new user to a chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.addChatUser", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def allowMessagesFromGroup(self, group_id:Optional[int]=None, key:Optional[str]=None):
		"""Allows sending messages from community to the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.allowMessagesFromGroup", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def createChat(self, user_ids:Optional[list[int]]=None, title:Optional[str]=None, group_id:Optional[int]=None):
		"""Creates a chat with several participants."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.createChat", **args)
		try: return MessagesCreateChatResponse(**r)
		except: return r


	async def delete(self, message_ids:Optional[list[int]]=None, spam:Optional[bool]=None, group_id:Optional[int]=None, delete_for_all:Optional[bool]=None, peer_id:Optional[int]=None, cmids:Optional[list[int]]=None):
		"""Deletes one or more messages."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.delete", **args)
		try: return MessagesDeleteResponse(**r)
		except: return r


	async def deleteChatPhoto(self, chat_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Deletes a chat's cover picture."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.deleteChatPhoto", **args)
		try: return MessagesDeleteChatPhotoResponse(**r)
		except: return r


	async def deleteConversation(self, user_id:Optional[int]=None, peer_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Deletes all private messages in a conversation."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.deleteConversation", **args)
		try: return MessagesDeleteConversationResponse(**r)
		except: return r


	async def denyMessagesFromGroup(self, group_id:Optional[int]=None):
		"""Denies sending message from community to the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.denyMessagesFromGroup", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, peer_id:Optional[int]=None, message:Optional[str]=None, lat:Optional[int]=None, long:Optional[int]=None, attachment:Optional[str]=None, keep_forward_messages:Optional[bool]=None, keep_snippets:Optional[bool]=None, group_id:Optional[int]=None, dont_parse_links:Optional[bool]=None, disable_mentions:Optional[bool]=None, message_id:Optional[int]=None, conversation_message_id:Optional[int]=None, template:Optional[str]=None, keyboard:Optional[str]=None):
		"""Edits the message."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.edit", **args)
		try: return MessagesEditResponse(**r)
		except: return r


	async def editChat(self, chat_id:Optional[int]=None, title:Optional[str]=None):
		"""Edits the title of a chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.editChat", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getByConversationMessageId(self, peer_id:Optional[int]=None, conversation_message_ids:Optional[list[int]]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None):
		"""Returns messages by their IDs within the conversation."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getByConversationMessageId", **args)
		for i in [MessagesGetByConversationMessageIdResponse, MessagesGetByConversationMessageIdExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getById(self, message_ids:Optional[list[int]]=None, preview_length:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None):
		"""Returns messages by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getById", **args)
		for i in [MessagesGetByIdResponse, MessagesGetByIdExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getChatPreview(self, peer_id:Optional[int]=None, link:Optional[str]=None, fields:Optional[list[UsersFields]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getChatPreview", **args)
		try: return MessagesGetChatPreviewResponse(**r)
		except: return r


	async def getConversationMembers(self, peer_id:Optional[int]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None):
		"""Returns a list of IDs of users participating in a chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getConversationMembers", **args)
		try: return MessagesGetConversationMembersResponse(**r)
		except: return r


	async def getConversations(self, offset:Optional[int]=None, count:Optional[int]=None, filter:Optional[str]=None, extended:Optional[bool]=None, start_message_id:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None, group_id:Optional[int]=None):
		"""Returns a list of the current user's conversations."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getConversations", **args)
		try: return MessagesGetConversationsResponse(**r)
		except: return r


	async def getConversationsById(self, peer_ids:Optional[list[int]]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None, group_id:Optional[int]=None):
		"""Returns conversations by their IDs"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getConversationsById", **args)
		for i in [MessagesGetConversationsByIdResponse, MessagesGetConversationsByIdExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getHistory(self, offset:Optional[int]=None, count:Optional[int]=None, user_id:Optional[int]=None, peer_id:Optional[int]=None, start_message_id:Optional[int]=None, rev:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None):
		"""Returns message history for the specified user or group chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getHistory", **args)
		for i in [MessagesGetHistoryResponse, MessagesGetHistoryExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getHistoryAttachments(self, peer_id:Optional[int]=None, media_type:Optional[str]=None, start_from:Optional[str]=None, count:Optional[int]=None, photo_sizes:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None, preserve_order:Optional[bool]=None, max_forwards_level:Optional[int]=None):
		"""Returns media files from the dialog or group chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getHistoryAttachments", **args)
		try: return MessagesGetHistoryAttachmentsResponse(**r)
		except: return r


	async def getImportantMessages(self, count:Optional[int]=None, offset:Optional[int]=None, start_message_id:Optional[int]=None, preview_length:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None, extended:Optional[bool]=None, group_id:Optional[int]=None):
		"""Returns a list of user's important messages."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getImportantMessages", **args)
		for i in [MessagesGetImportantMessagesResponse, MessagesGetImportantMessagesExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getIntentUsers(self, intent:Optional[str]=None, subscribe_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, name_case:Optional[list[str]]=None, fields:Optional[list[str]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getIntentUsers", **args)
		try: return MessagesGetIntentUsersResponse(**r)
		except: return r


	async def getInviteLink(self, peer_id:Optional[int]=None, reset:Optional[bool]=None, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getInviteLink", **args)
		try: return MessagesGetInviteLinkResponse(**r)
		except: return r


	async def getLastActivity(self, user_id:Optional[int]=None):
		"""Returns a user's current status and date of last activity."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getLastActivity", **args)
		try: return MessagesGetLastActivityResponse(**r)
		except: return r


	async def getLongPollHistory(self, ts:Optional[int]=None, pts:Optional[int]=None, preview_length:Optional[int]=None, onlines:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, events_limit:Optional[int]=None, msgs_limit:Optional[int]=None, max_msg_id:Optional[int]=None, group_id:Optional[int]=None, lp_version:Optional[int]=None, last_n:Optional[int]=None, credentials:Optional[bool]=None, extended:Optional[bool]=None):
		"""Returns updates in user's private messages."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getLongPollHistory", **args)
		try: return MessagesGetLongPollHistoryResponse(**r)
		except: return r


	async def getLongPollServer(self, need_pts:Optional[bool]=None, group_id:Optional[int]=None, lp_version:Optional[int]=None):
		"""Returns data required for connection to a Long Poll server."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.getLongPollServer", **args)
		try: return MessagesGetLongPollServerResponse(**r)
		except: return r


	async def isMessagesFromGroupAllowed(self, group_id:Optional[int]=None, user_id:Optional[int]=None):
		"""Returns information whether sending messages from the community to current user is allowed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.isMessagesFromGroupAllowed", **args)
		try: return MessagesIsMessagesFromGroupAllowedResponse(**r)
		except: return r


	async def joinChatByInviteLink(self, link:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.joinChatByInviteLink", **args)
		try: return MessagesJoinChatByInviteLinkResponse(**r)
		except: return r


	async def markAsAnsweredConversation(self, peer_id:Optional[int]=None, answered:Optional[bool]=None, group_id:Optional[int]=None):
		"""Marks and unmarks conversations as unanswered."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.markAsAnsweredConversation", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def markAsImportant(self, message_ids:Optional[list[int]]=None, important:Optional[int]=None):
		"""Marks and unmarks messages as important (starred)."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.markAsImportant", **args)
		try: return MessagesMarkAsImportantResponse(**r)
		except: return r


	async def markAsImportantConversation(self, peer_id:Optional[int]=None, important:Optional[bool]=None, group_id:Optional[int]=None):
		"""Marks and unmarks conversations as important."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.markAsImportantConversation", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def markAsRead(self, message_ids:Optional[list[int]]=None, peer_id:Optional[int]=None, start_message_id:Optional[int]=None, group_id:Optional[int]=None, mark_conversation_as_read:Optional[bool]=None):
		"""Marks messages as read."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.markAsRead", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def pin(self, peer_id:Optional[int]=None, message_id:Optional[int]=None, conversation_message_id:Optional[int]=None):
		"""Pin a message."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.pin", **args)
		try: return MessagesPinResponse(**r)
		except: return r


	async def removeChatUser(self, chat_id:Optional[int]=None, user_id:Optional[int]=None, member_id:Optional[int]=None):
		"""Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.removeChatUser", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restore(self, message_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Restores a deleted message."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.restore", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, peer_id:Optional[int]=None, date:Optional[int]=None, preview_length:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[str]]=None, group_id:Optional[int]=None):
		"""Returns a list of the current user's private messages that match search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.search", **args)
		for i in [MessagesSearchResponse, MessagesSearchExtendedResponse]:
			try: return i(**r)
			except: return r


	async def searchConversations(self, q:Optional[str]=None, count:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, group_id:Optional[int]=None):
		"""Returns a list of the current user's conversations that match search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.searchConversations", **args)
		for i in [MessagesSearchConversationsResponse, MessagesSearchConversationsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def send(self, user_id:Optional[int]=None, random_id:Optional[int]=None, peer_id:Optional[int]=None, peer_ids:Optional[list[int]]=None, domain:Optional[str]=None, chat_id:Optional[int]=None, user_ids:Optional[list[int]]=None, message:Optional[str]=None, lat:Optional[int]=None, long:Optional[int]=None, attachment:Optional[str]=None, reply_to:Optional[int]=None, forward_messages:Optional[list[int]]=None, forward:Optional[str]=None, sticker_id:Optional[int]=None, group_id:Optional[int]=None, keyboard:Optional[str]=None, template:Optional[str]=None, payload:Optional[str]=None, content_source:Optional[str]=None, dont_parse_links:Optional[bool]=None, disable_mentions:Optional[bool]=None, intent:Optional[str]=None, subscribe_id:Optional[int]=None):
		"""Sends a message."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.send", **args)
		for i in [MessagesSendResponse, MessagesSendUserIdsResponse]:
			try: return i(**r)
			except: return r


	async def sendMessageEventAnswer(self, event_id:Optional[str]=None, user_id:Optional[int]=None, peer_id:Optional[int]=None, event_data:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.sendMessageEventAnswer", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setActivity(self, user_id:Optional[int]=None, type:Optional[str]=None, peer_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Changes the status of a user as typing in a conversation."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.setActivity", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setChatPhoto(self, file:Optional[str]=None):
		"""Sets a previously-uploaded picture as the cover picture of a chat."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.setChatPhoto", **args)
		try: return MessagesSetChatPhotoResponse(**r)
		except: return r


	async def unpin(self, peer_id:Optional[int]=None, group_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Messages.unpin", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Newsfeed(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addBan(self, user_ids:Optional[list[int]]=None, group_ids:Optional[list[int]]=None):
		"""Prevents news from specified users and communities from appearing in the current user's newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.addBan", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteBan(self, user_ids:Optional[list[int]]=None, group_ids:Optional[list[int]]=None):
		"""Allows news from previously banned users and communities to be shown in the current user's newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.deleteBan", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteList(self, list_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.deleteList", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, filters:Optional[list[NewsfeedNewsfeedItemType]]=None, return_banned:Optional[bool]=None, start_time:Optional[int]=None, end_time:Optional[int]=None, max_photos:Optional[int]=None, source_ids:Optional[str]=None, start_from:Optional[str]=None, count:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None, section:Optional[str]=None):
		"""Returns data required to show newsfeed for the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.get", **args)
		try: return NewsfeedGenericResponse(**r)
		except: return r


	async def getBanned(self, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns a list of users and communities banned from the current user's newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getBanned", **args)
		for i in [NewsfeedGetBannedResponse, NewsfeedGetBannedExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getComments(self, count:Optional[int]=None, filters:Optional[list[NewsfeedCommentsFilters]]=None, reposts:Optional[str]=None, start_time:Optional[int]=None, end_time:Optional[int]=None, last_comments_count:Optional[int]=None, start_from:Optional[str]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns a list of comments in the current user's newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getComments", **args)
		try: return NewsfeedGetCommentsResponse(**r)
		except: return r


	async def getLists(self, list_ids:Optional[list[int]]=None, extended:Optional[bool]=None):
		"""Returns a list of newsfeeds followed by the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getLists", **args)
		for i in [NewsfeedGetListsResponse, NewsfeedGetListsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getMentions(self, owner_id:Optional[int]=None, start_time:Optional[int]=None, end_time:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of posts on user walls in which the current user is mentioned."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getMentions", **args)
		try: return NewsfeedGetMentionsResponse(**r)
		except: return r


	async def getRecommended(self, start_time:Optional[int]=None, end_time:Optional[int]=None, max_photos:Optional[int]=None, start_from:Optional[str]=None, count:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		""", Returns a list of newsfeeds recommended to the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getRecommended", **args)
		try: return NewsfeedGenericResponse(**r)
		except: return r


	async def getSuggestedSources(self, offset:Optional[int]=None, count:Optional[int]=None, shuffle:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns communities and users that current user is suggested to follow."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.getSuggestedSources", **args)
		try: return NewsfeedGetSuggestedSourcesResponse(**r)
		except: return r


	async def ignoreItem(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None):
		"""Hides an item from the newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.ignoreItem", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def saveList(self, list_id:Optional[int]=None, title:Optional[str]=None, source_ids:Optional[list[int]]=None, no_reposts:Optional[bool]=None):
		"""Creates and edits user newsfeed lists"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.saveList", **args)
		try: return NewsfeedSaveListResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, extended:Optional[bool]=None, count:Optional[int]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, start_time:Optional[int]=None, end_time:Optional[int]=None, start_from:Optional[str]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns search results by statuses."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.search", **args)
		for i in [NewsfeedSearchResponse, NewsfeedSearchExtendedResponse]:
			try: return i(**r)
			except: return r


	async def unignoreItem(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None, track_code:Optional[str]=None):
		"""Returns a hidden item to the newsfeed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.unignoreItem", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unsubscribe(self, type:Optional[str]=None, owner_id:Optional[int]=None, item_id:Optional[int]=None):
		"""Unsubscribes the current user from specified newsfeeds."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Newsfeed.unsubscribe", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Notes(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, title:Optional[str]=None, text:Optional[str]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None):
		"""Creates a new note for the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.add", **args)
		try: return NotesAddResponse(**r)
		except: return r


	async def createComment(self, note_id:Optional[int]=None, owner_id:Optional[int]=None, reply_to:Optional[int]=None, message:Optional[str]=None, guid:Optional[str]=None):
		"""Adds a new comment on a note."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.createComment", **args)
		try: return NotesCreateCommentResponse(**r)
		except: return r


	async def delete(self, note_id:Optional[int]=None):
		"""Deletes a note of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteComment(self, comment_id:Optional[int]=None, owner_id:Optional[int]=None):
		"""Deletes a comment on a note."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.deleteComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, note_id:Optional[int]=None, title:Optional[str]=None, text:Optional[str]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None):
		"""Edits a note of the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, comment_id:Optional[int]=None, owner_id:Optional[int]=None, message:Optional[str]=None):
		"""Edits a comment on a note."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, note_ids:Optional[list[int]]=None, user_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, sort:Optional[int]=None):
		"""Returns a list of notes created by a user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.get", **args)
		try: return NotesGetResponse(**r)
		except: return r


	async def getById(self, note_id:Optional[int]=None, owner_id:Optional[int]=None, need_wiki:Optional[bool]=None):
		"""Returns a note by its ID."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.getById", **args)
		try: return NotesGetByIdResponse(**r)
		except: return r


	async def getComments(self, note_id:Optional[int]=None, owner_id:Optional[int]=None, sort:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of comments on a note."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.getComments", **args)
		try: return NotesGetCommentsResponse(**r)
		except: return r


	async def restoreComment(self, comment_id:Optional[int]=None, owner_id:Optional[int]=None):
		"""Restores a deleted comment on a note."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notes.restoreComment", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Notifications(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, count:Optional[int]=None, start_from:Optional[str]=None, filters:Optional[list[str]]=None, start_time:Optional[int]=None, end_time:Optional[int]=None):
		"""Returns a list of notifications about other users' feedback to the current user's wall posts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notifications.get", **args)
		try: return NotificationsGetResponse(**r)
		except: return r


	async def markAsViewed(self):
		"""Resets the counter of new notifications about other users' feedback to the current user's wall posts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notifications.markAsViewed", **args)
		try: return NotificationsMarkAsViewedResponse(**r)
		except: return r


	async def sendMessage(self, user_ids:Optional[list[int]]=None, message:Optional[str]=None, fragment:Optional[str]=None, group_id:Optional[int]=None, random_id:Optional[int]=None, sending_mode:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Notifications.sendMessage", **args)
		try: return NotificationsSendMessageResponse(**r)
		except: return r



class Orders(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def cancelSubscription(self, user_id:Optional[int]=None, subscription_id:Optional[int]=None, pending_cancel:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.cancelSubscription", **args)
		try: return OrdersCancelSubscriptionResponse(**r)
		except: return r


	async def changeState(self, order_id:Optional[int]=None, action:Optional[str]=None, app_order_id:Optional[int]=None, test_mode:Optional[bool]=None):
		"""Changes order status."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.changeState", **args)
		try: return OrdersChangeStateResponse(**r)
		except: return r


	async def get(self, offset:Optional[int]=None, count:Optional[int]=None, test_mode:Optional[bool]=None):
		"""Returns a list of orders."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.get", **args)
		try: return OrdersGetResponse(**r)
		except: return r


	async def getAmount(self, user_id:Optional[int]=None, votes:Optional[list[str]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.getAmount", **args)
		try: return OrdersGetAmountResponse(**r)
		except: return r


	async def getById(self, order_id:Optional[int]=None, order_ids:Optional[list[int]]=None, test_mode:Optional[bool]=None):
		"""Returns information about orders by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.getById", **args)
		try: return OrdersGetByIdResponse(**r)
		except: return r


	async def getUserSubscriptionById(self, user_id:Optional[int]=None, subscription_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.getUserSubscriptionById", **args)
		try: return OrdersGetUserSubscriptionByIdResponse(**r)
		except: return r


	async def getUserSubscriptions(self, user_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.getUserSubscriptions", **args)
		try: return OrdersGetUserSubscriptionsResponse(**r)
		except: return r


	async def updateSubscription(self, user_id:Optional[int]=None, subscription_id:Optional[int]=None, price:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Orders.updateSubscription", **args)
		try: return OrdersUpdateSubscriptionResponse(**r)
		except: return r



class Pages(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def clearCache(self, url:Optional[str]=None):
		"""Allows to clear the cache of particular 'external' pages which may be attached to VK posts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.clearCache", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, page_id:Optional[int]=None, _global:Optional[bool]=None, site_preview:Optional[bool]=None, title:Optional[str]=None, need_source:Optional[bool]=None, need_html:Optional[bool]=None):
		"""Returns information about a wiki page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.get", **args)
		try: return PagesGetResponse(**r)
		except: return r


	async def getHistory(self, page_id:Optional[int]=None, group_id:Optional[int]=None, user_id:Optional[int]=None):
		"""Returns a list of all previous versions of a wiki page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.getHistory", **args)
		try: return PagesGetHistoryResponse(**r)
		except: return r


	async def getTitles(self, group_id:Optional[int]=None):
		"""Returns a list of wiki pages in a group."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.getTitles", **args)
		try: return PagesGetTitlesResponse(**r)
		except: return r


	async def getVersion(self, version_id:Optional[int]=None, group_id:Optional[int]=None, user_id:Optional[int]=None, need_html:Optional[bool]=None):
		"""Returns the text of one of the previous versions of a wiki page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.getVersion", **args)
		try: return PagesGetVersionResponse(**r)
		except: return r


	async def parseWiki(self, text:Optional[str]=None, group_id:Optional[int]=None):
		"""Returns HTML representation of the wiki markup."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.parseWiki", **args)
		try: return PagesParseWikiResponse(**r)
		except: return r


	async def save(self, text:Optional[str]=None, page_id:Optional[int]=None, group_id:Optional[int]=None, user_id:Optional[int]=None, title:Optional[str]=None):
		"""Saves the text of a wiki page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.save", **args)
		try: return PagesSaveResponse(**r)
		except: return r


	async def saveAccess(self, page_id:Optional[int]=None, group_id:Optional[int]=None, user_id:Optional[int]=None, view:Optional[int]=None, edit:Optional[int]=None):
		"""Saves modified read and edit access settings for a wiki page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Pages.saveAccess", **args)
		try: return PagesSaveAccessResponse(**r)
		except: return r



class Photos(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def confirmTag(self, owner_id:Optional[int]=None, photo_id:Optional[str]=None, tag_id:Optional[int]=None):
		"""Confirms a tag on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.confirmTag", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def copy(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, access_key:Optional[str]=None):
		"""Allows to copy a photo to the 'Saved photos' album"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.copy", **args)
		try: return PhotosCopyResponse(**r)
		except: return r


	async def createAlbum(self, title:Optional[str]=None, group_id:Optional[int]=None, description:Optional[str]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None, upload_by_admins_only:Optional[bool]=None, comments_disabled:Optional[bool]=None):
		"""Creates an empty photo album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.createAlbum", **args)
		try: return PhotosCreateAlbumResponse(**r)
		except: return r


	async def createComment(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, from_group:Optional[bool]=None, reply_to_comment:Optional[int]=None, sticker_id:Optional[int]=None, access_key:Optional[str]=None, guid:Optional[str]=None):
		"""Adds a new comment on the photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.createComment", **args)
		try: return PhotosCreateCommentResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None):
		"""Deletes a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteAlbum(self, album_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Deletes a photo album belonging to the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.deleteAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Deletes a comment on the photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.deleteComment", **args)
		try: return PhotosDeleteCommentResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, caption:Optional[str]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, place_str:Optional[str]=None, foursquare_id:Optional[str]=None, delete_place:Optional[bool]=None):
		"""Edits the caption of a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editAlbum(self, album_id:Optional[int]=None, title:Optional[str]=None, description:Optional[str]=None, owner_id:Optional[int]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None, upload_by_admins_only:Optional[bool]=None, comments_disabled:Optional[bool]=None):
		"""Edits information about a photo album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.editAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None):
		"""Edits a comment on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, album_id:Optional[str]=None, photo_ids:Optional[list[str]]=None, rev:Optional[bool]=None, extended:Optional[bool]=None, feed_type:Optional[str]=None, feed:Optional[int]=None, photo_sizes:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of a user's or community's photos."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.get", **args)
		try: return PhotosGetResponse(**r)
		except: return r


	async def getAlbums(self, owner_id:Optional[int]=None, album_ids:Optional[list[int]]=None, offset:Optional[int]=None, count:Optional[int]=None, need_system:Optional[bool]=None, need_covers:Optional[bool]=None, photo_sizes:Optional[bool]=None):
		"""Returns a list of a user's or community's photo albums."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getAlbums", **args)
		try: return PhotosGetAlbumsResponse(**r)
		except: return r


	async def getAlbumsCount(self, user_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Returns the number of photo albums belonging to a user or community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getAlbumsCount", **args)
		try: return PhotosGetAlbumsCountResponse(**r)
		except: return r


	async def getAll(self, owner_id:Optional[int]=None, extended:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None, photo_sizes:Optional[bool]=None, no_service_albums:Optional[bool]=None, need_hidden:Optional[bool]=None, skip_hidden:Optional[bool]=None):
		"""Returns a list of photos belonging to a user or community, in reverse chronological order."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getAll", **args)
		for i in [PhotosGetAllResponse, PhotosGetAllExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getAllComments(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, need_likes:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getAllComments", **args)
		try: return PhotosGetAllCommentsResponse(**r)
		except: return r


	async def getById(self, photos:Optional[list[str]]=None, extended:Optional[bool]=None, photo_sizes:Optional[bool]=None):
		"""Returns information about photos by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getById", **args)
		try: return PhotosGetByIdResponse(**r)
		except: return r


	async def getChatUploadServer(self, chat_id:Optional[int]=None, crop_x:Optional[int]=None, crop_y:Optional[int]=None, crop_width:Optional[int]=None):
		"""Returns an upload link for chat cover pictures."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getChatUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def getComments(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, need_likes:Optional[bool]=None, start_comment_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, sort:Optional[str]=None, access_key:Optional[str]=None, extended:Optional[bool]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns a list of comments on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getComments", **args)
		for i in [PhotosGetCommentsResponse, PhotosGetCommentsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getMarketAlbumUploadServer(self, group_id:Optional[int]=None):
		"""Returns the server address for market album photo upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getMarketAlbumUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def getMarketUploadServer(self, group_id:Optional[int]=None, main_photo:Optional[bool]=None, crop_x:Optional[int]=None, crop_y:Optional[int]=None, crop_width:Optional[int]=None):
		"""Returns the server address for market photo upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getMarketUploadServer", **args)
		try: return PhotosGetMarketUploadServerResponse(**r)
		except: return r


	async def getMessagesUploadServer(self, peer_id:Optional[int]=None):
		"""Returns the server address for photo upload in a private message for a user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getMessagesUploadServer", **args)
		try: return PhotosGetMessagesUploadServerResponse(**r)
		except: return r


	async def getNewTags(self, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns a list of photos with tags that have not been viewed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getNewTags", **args)
		try: return PhotosGetNewTagsResponse(**r)
		except: return r


	async def getOwnerCoverPhotoUploadServer(self, group_id:Optional[int]=None, crop_x:Optional[int]=None, crop_y:Optional[int]=None, crop_x2:Optional[int]=None, crop_y2:Optional[int]=None):
		"""Returns the server address for owner cover upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getOwnerCoverPhotoUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def getOwnerPhotoUploadServer(self, owner_id:Optional[int]=None):
		"""Returns an upload server address for a profile or community photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getOwnerPhotoUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def getTags(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, access_key:Optional[str]=None):
		"""Returns a list of tags on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getTags", **args)
		try: return PhotosGetTagsResponse(**r)
		except: return r


	async def getUploadServer(self, album_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Returns the server address for photo upload."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getUploadServer", **args)
		try: return PhotosGetUploadServerResponse(**r)
		except: return r


	async def getUserPhotos(self, user_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, sort:Optional[str]=None):
		"""Returns a list of photos in which a user is tagged."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getUserPhotos", **args)
		try: return PhotosGetUserPhotosResponse(**r)
		except: return r


	async def getWallUploadServer(self, group_id:Optional[int]=None):
		"""Returns the server address for photo upload onto a user's wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.getWallUploadServer", **args)
		try: return PhotosGetWallUploadServerResponse(**r)
		except: return r


	async def makeCover(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, album_id:Optional[int]=None):
		"""Makes a photo into an album cover."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.makeCover", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def move(self, owner_id:Optional[int]=None, target_album_id:Optional[int]=None, photo_ids:Optional[int]=None):
		"""Moves a photo from one album to another."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.move", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def putTag(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, user_id:Optional[int]=None, x:Optional[int]=None, y:Optional[int]=None, x2:Optional[int]=None, y2:Optional[int]=None):
		"""Adds a tag on the photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.putTag", **args)
		try: return PhotosPutTagResponse(**r)
		except: return r


	async def removeTag(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, tag_id:Optional[int]=None):
		"""Removes a tag from a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.removeTag", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderAlbums(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, before:Optional[int]=None, after:Optional[int]=None):
		"""Reorders the album in the list of user albums."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.reorderAlbums", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderPhotos(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, before:Optional[int]=None, after:Optional[int]=None):
		"""Reorders the photo in the list of photos of the user album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.reorderPhotos", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def report(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None, reason:Optional[int]=None):
		"""Reports (submits a complaint about) a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.report", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reportComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, reason:Optional[int]=None):
		"""Reports (submits a complaint about) a comment on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.reportComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restore(self, owner_id:Optional[int]=None, photo_id:Optional[int]=None):
		"""Restores a deleted photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.restore", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restoreComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Restores a deleted comment on a photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.restoreComment", **args)
		try: return PhotosRestoreCommentResponse(**r)
		except: return r


	async def save(self, album_id:Optional[int]=None, group_id:Optional[int]=None, server:Optional[int]=None, photos_list:Optional[str]=None, hash:Optional[str]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, caption:Optional[str]=None):
		"""Saves photos after successful uploading."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.save", **args)
		try: return PhotosSaveResponse(**r)
		except: return r


	async def saveMarketAlbumPhoto(self, group_id:Optional[int]=None, photo:Optional[str]=None, server:Optional[int]=None, hash:Optional[str]=None):
		"""Saves market album photos after successful uploading."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveMarketAlbumPhoto", **args)
		try: return PhotosSaveMarketAlbumPhotoResponse(**r)
		except: return r


	async def saveMarketPhoto(self, group_id:Optional[int]=None, photo:Optional[str]=None, server:Optional[int]=None, hash:Optional[str]=None, crop_data:Optional[str]=None, crop_hash:Optional[str]=None):
		"""Saves market photos after successful uploading."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveMarketPhoto", **args)
		try: return PhotosSaveMarketPhotoResponse(**r)
		except: return r


	async def saveMessagesPhoto(self, photo:Optional[str]=None, server:Optional[int]=None, hash:Optional[str]=None):
		"""Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveMessagesPhoto", **args)
		try: return PhotosSaveMessagesPhotoResponse(**r)
		except: return r


	async def saveOwnerCoverPhoto(self, hash:Optional[str]=None, photo:Optional[str]=None):
		"""Saves cover photo after successful uploading."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveOwnerCoverPhoto", **args)
		try: return PhotosSaveOwnerCoverPhotoResponse(**r)
		except: return r


	async def saveOwnerPhoto(self, server:Optional[str]=None, hash:Optional[str]=None, photo:Optional[str]=None):
		"""Saves a profile or community photo. Upload URL can be got with the [vk.com/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveOwnerPhoto", **args)
		try: return PhotosSaveOwnerPhotoResponse(**r)
		except: return r


	async def saveWallPhoto(self, user_id:Optional[int]=None, group_id:Optional[int]=None, photo:Optional[str]=None, server:Optional[int]=None, hash:Optional[str]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, caption:Optional[str]=None):
		"""Saves a photo to a user's or community's wall after being uploaded."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.saveWallPhoto", **args)
		try: return PhotosSaveWallPhotoResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, lat:Optional[int]=None, long:Optional[int]=None, start_time:Optional[int]=None, end_time:Optional[int]=None, sort:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, radius:Optional[int]=None):
		"""Returns a list of photos."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Photos.search", **args)
		try: return PhotosSearchResponse(**r)
		except: return r



class Podcasts(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def searchPodcast(self, search_string:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Podcasts.searchPodcast", **args)
		try: return PodcastsSearchPodcastResponse(**r)
		except: return r



class Polls(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addVote(self, owner_id:Optional[int]=None, poll_id:Optional[int]=None, answer_ids:Optional[list[int]]=None, is_board:Optional[bool]=None):
		"""Adds the current user's vote to the selected answer in the poll."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.addVote", **args)
		try: return PollsAddVoteResponse(**r)
		except: return r


	async def create(self, question:Optional[str]=None, is_anonymous:Optional[bool]=None, is_multiple:Optional[bool]=None, end_date:Optional[int]=None, owner_id:Optional[int]=None, app_id:Optional[int]=None, add_answers:Optional[str]=None, photo_id:Optional[int]=None, background_id:Optional[str]=None, disable_unvote:Optional[bool]=None):
		"""Creates polls that can be attached to the users' or communities' posts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.create", **args)
		try: return PollsCreateResponse(**r)
		except: return r


	async def deleteVote(self, owner_id:Optional[int]=None, poll_id:Optional[int]=None, answer_id:Optional[int]=None, is_board:Optional[bool]=None):
		"""Deletes the current user's vote from the selected answer in the poll."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.deleteVote", **args)
		try: return PollsDeleteVoteResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, poll_id:Optional[int]=None, question:Optional[str]=None, add_answers:Optional[str]=None, edit_answers:Optional[str]=None, delete_answers:Optional[str]=None, end_date:Optional[int]=None, photo_id:Optional[int]=None, background_id:Optional[str]=None):
		"""Edits created polls"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getBackgrounds(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.getBackgrounds", **args)
		try: return PollsGetBackgroundsResponse(**r)
		except: return r


	async def getById(self, owner_id:Optional[int]=None, is_board:Optional[bool]=None, poll_id:Optional[int]=None, extended:Optional[bool]=None, friends_count:Optional[int]=None, fields:Optional[list[str]]=None, name_case:Optional[str]=None):
		"""Returns detailed information about a poll by its ID."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.getById", **args)
		try: return PollsGetByIdResponse(**r)
		except: return r


	async def getPhotoUploadServer(self, owner_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.getPhotoUploadServer", **args)
		try: return BaseGetUploadServerResponse(**r)
		except: return r


	async def getVoters(self, owner_id:Optional[int]=None, poll_id:Optional[int]=None, answer_ids:Optional[list[int]]=None, is_board:Optional[bool]=None, friends_only:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns a list of IDs of users who selected specific answers in the poll."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.getVoters", **args)
		try: return PollsGetVotersResponse(**r)
		except: return r


	async def savePhoto(self, photo:Optional[str]=None, hash:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Polls.savePhoto", **args)
		try: return PollsSavePhotoResponse(**r)
		except: return r



class Prettycards(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def create(self, owner_id:Optional[int]=None, photo:Optional[str]=None, title:Optional[str]=None, link:Optional[str]=None, price:Optional[str]=None, price_old:Optional[str]=None, button:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.create", **args)
		try: return PrettyCardsCreateResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, card_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.delete", **args)
		try: return PrettyCardsDeleteResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, card_id:Optional[int]=None, photo:Optional[str]=None, title:Optional[str]=None, link:Optional[str]=None, price:Optional[str]=None, price_old:Optional[str]=None, button:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.edit", **args)
		try: return PrettyCardsEditResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.get", **args)
		try: return PrettyCardsGetResponse(**r)
		except: return r


	async def getById(self, owner_id:Optional[int]=None, card_ids:Optional[list[int]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.getById", **args)
		try: return PrettyCardsGetByIdResponse(**r)
		except: return r


	async def getUploadURL(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Prettycards.getUploadURL", **args)
		try: return PrettyCardsGetUploadURLResponse(**r)
		except: return r



class Search(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getHints(self, q:Optional[str]=None, offset:Optional[int]=None, limit:Optional[int]=None, filters:Optional[list[str]]=None, fields:Optional[list[str]]=None, search_global:Optional[bool]=None):
		"""Allows the programmer to do a quick search for any substring."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Search.getHints", **args)
		try: return SearchGetHintsResponse(**r)
		except: return r



class Secure(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addAppEvent(self, user_id:Optional[int]=None, activity_id:Optional[int]=None, value:Optional[int]=None):
		"""Adds user activity information to an application"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.addAppEvent", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def checkToken(self, token:Optional[str]=None, ip:Optional[str]=None):
		"""Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.checkToken", **args)
		try: return SecureCheckTokenResponse(**r)
		except: return r


	async def getAppBalance(self):
		"""Returns payment balance of the application in hundredth of a vote."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.getAppBalance", **args)
		try: return SecureGetAppBalanceResponse(**r)
		except: return r


	async def getSMSHistory(self, user_id:Optional[int]=None, date_from:Optional[int]=None, date_to:Optional[int]=None, limit:Optional[int]=None):
		"""Shows a list of SMS notifications sent by the application using [vk.com/dev/secure.sendSMSNotification|secure.sendSMSNotification] method."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.getSMSHistory", **args)
		try: return SecureGetSMSHistoryResponse(**r)
		except: return r


	async def getTransactionsHistory(self, type:Optional[int]=None, uid_from:Optional[int]=None, uid_to:Optional[int]=None, date_from:Optional[int]=None, date_to:Optional[int]=None, limit:Optional[int]=None):
		"""Shows history of votes transaction between users and the application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.getTransactionsHistory", **args)
		try: return SecureGetTransactionsHistoryResponse(**r)
		except: return r


	async def getUserLevel(self, user_ids:Optional[list[int]]=None):
		"""Returns one of the previously set game levels of one or more users in the application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.getUserLevel", **args)
		try: return SecureGetUserLevelResponse(**r)
		except: return r


	async def giveEventSticker(self, user_ids:Optional[list[int]]=None, achievement_id:Optional[int]=None):
		"""Opens the game achievement and gives the user a sticker"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.giveEventSticker", **args)
		try: return SecureGiveEventStickerResponse(**r)
		except: return r


	async def sendNotification(self, user_ids:Optional[list[int]]=None, user_id:Optional[int]=None, message:Optional[str]=None):
		"""Sends notification to the user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.sendNotification", **args)
		try: return SecureSendNotificationResponse(**r)
		except: return r


	async def sendSMSNotification(self, user_id:Optional[int]=None, message:Optional[str]=None):
		"""Sends 'SMS' notification to a user's mobile device."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.sendSMSNotification", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def setCounter(self, counters:Optional[list[str]]=None, user_id:Optional[int]=None, counter:Optional[int]=None, increment:Optional[bool]=None):
		"""Sets a counter which is shown to the user in bold in the left menu."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Secure.setCounter", **args)
		for i in [BaseBoolResponse, SecureSetCounterArrayResponse]:
			try: return i(**r)
			except: return r



class Stats(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, group_id:Optional[int]=None, app_id:Optional[int]=None, timestamp_from:Optional[int]=None, timestamp_to:Optional[int]=None, interval:Optional[str]=None, intervals_count:Optional[int]=None, filters:Optional[list[str]]=None, stats_groups:Optional[list[str]]=None, extended:Optional[bool]=None):
		"""Returns statistics of a community or an application."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stats.get", **args)
		try: return StatsGetResponse(**r)
		except: return r


	async def getPostReach(self, owner_id:Optional[str]=None, post_ids:Optional[list[int]]=None):
		"""Returns stats for a wall post."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stats.getPostReach", **args)
		try: return StatsGetPostReachResponse(**r)
		except: return r


	async def trackVisitor(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stats.trackVisitor", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Status(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, user_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Returns data required to show the status of a user or community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Status.get", **args)
		try: return StatusGetResponse(**r)
		except: return r


	async def set(self, text:Optional[str]=None, group_id:Optional[int]=None):
		"""Sets a new status for the current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Status.set", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Storage(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, key:Optional[str]=None, keys:Optional[list[str]]=None, user_id:Optional[int]=None):
		"""Returns a value of variable with the name set by key parameter."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Storage.get", **args)
		try: return StorageGetResponse(**r)
		except: return r


	async def getKeys(self, user_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns the names of all variables."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Storage.getKeys", **args)
		try: return StorageGetKeysResponse(**r)
		except: return r


	async def set(self, key:Optional[str]=None, value:Optional[str]=None, user_id:Optional[int]=None):
		"""Saves a value of variable with the name set by 'key' parameter."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Storage.set", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Store(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def addStickersToFavorite(self, sticker_ids:Optional[list[int]]=None):
		"""Adds given sticker IDs to the list of user's favorite stickers"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Store.addStickersToFavorite", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getFavoriteStickers(self):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Store.getFavoriteStickers", **args)
		try: return StoreGetFavoriteStickersResponse(**r)
		except: return r


	async def getProducts(self, type:Optional[str]=None, merchant:Optional[str]=None, section:Optional[str]=None, product_ids:Optional[list[int]]=None, filters:Optional[list[str]]=None, extended:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Store.getProducts", **args)
		try: return StoreGetProductsResponse(**r)
		except: return r


	async def getStickersKeywords(self, stickers_ids:Optional[list[int]]=None, products_ids:Optional[list[int]]=None, aliases:Optional[bool]=None, all_products:Optional[bool]=None, need_stickers:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Store.getStickersKeywords", **args)
		try: return StoreGetStickersKeywordsResponse(**r)
		except: return r


	async def removeStickersFromFavorite(self, sticker_ids:Optional[list[int]]=None):
		"""Removes given sticker IDs from the list of user's favorite stickers"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Store.removeStickersFromFavorite", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Stories(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def banOwner(self, owners_ids:Optional[list[int]]=None):
		"""Allows to hide stories from chosen sources from current user's feed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.banOwner", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, story_id:Optional[int]=None, stories:Optional[list[str]]=None):
		"""Allows to delete story."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns stories available for current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.get", **args)
		try: return StoriesGetV5113Response(**r)
		except: return r


	async def getBanned(self, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns list of sources hidden from current user's feed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getBanned", **args)
		for i in [StoriesGetBannedResponse, StoriesGetBannedExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getById(self, stories:Optional[list[str]]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns story by its ID."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getById", **args)
		try: return StoriesGetByIdExtendedResponse(**r)
		except: return r


	async def getPhotoUploadServer(self, add_to_news:Optional[bool]=None, user_ids:Optional[list[int]]=None, reply_to_story:Optional[str]=None, link_text:Optional[str]=None, link_url:Optional[str]=None, group_id:Optional[int]=None, clickable_stickers:Optional[str]=None):
		"""Returns URL for uploading a story with photo."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getPhotoUploadServer", **args)
		try: return StoriesGetPhotoUploadServerResponse(**r)
		except: return r


	async def getReplies(self, owner_id:Optional[int]=None, story_id:Optional[int]=None, access_key:Optional[str]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns replies to the story."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getReplies", **args)
		try: return StoriesGetV5113Response(**r)
		except: return r


	async def getStats(self, owner_id:Optional[int]=None, story_id:Optional[int]=None):
		"""Returns stories available for current user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getStats", **args)
		try: return StoriesGetStatsResponse(**r)
		except: return r


	async def getVideoUploadServer(self, add_to_news:Optional[bool]=None, user_ids:Optional[list[int]]=None, reply_to_story:Optional[str]=None, link_text:Optional[str]=None, link_url:Optional[str]=None, group_id:Optional[int]=None, clickable_stickers:Optional[str]=None):
		"""Allows to receive URL for uploading story with video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getVideoUploadServer", **args)
		try: return StoriesGetVideoUploadServerResponse(**r)
		except: return r


	async def getViewers(self, owner_id:Optional[int]=None, story_id:Optional[int]=None, count:Optional[int]=None, offset:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns a list of story viewers."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.getViewers", **args)
		for i in [StoriesGetViewersExtendedV5115Response, StoriesGetViewersExtendedV5115Response]:
			try: return i(**r)
			except: return r


	async def hideAllReplies(self, owner_id:Optional[int]=None, group_id:Optional[int]=None):
		"""Hides all replies in the last 24 hours from the user to current user's stories."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.hideAllReplies", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def hideReply(self, owner_id:Optional[int]=None, story_id:Optional[int]=None):
		"""Hides the reply to the current user's story."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.hideReply", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def save(self, upload_results:Optional[list[str]]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.save", **args)
		try: return StoriesSaveResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, place_id:Optional[int]=None, latitude:Optional[int]=None, longitude:Optional[int]=None, radius:Optional[int]=None, mentioned_id:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.search", **args)
		try: return StoriesGetV5113Response(**r)
		except: return r


	async def sendInteraction(self, access_key:Optional[str]=None, message:Optional[str]=None, is_broadcast:Optional[bool]=None, is_anonymous:Optional[bool]=None, unseen_marker:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.sendInteraction", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def unbanOwner(self, owners_ids:Optional[list[int]]=None):
		"""Allows to show stories from hidden sources in current user's feed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Stories.unbanOwner", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Streaming(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getServerUrl(self):
		"""Allows to receive data for the connection to Streaming API."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Streaming.getServerUrl", **args)
		try: return StreamingGetServerUrlResponse(**r)
		except: return r


	async def setSettings(self, monthly_tier:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Streaming.setSettings", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Users(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def get(self, user_ids:Optional[list[int|str]]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns detailed information on users."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Users.get", **args)
		try: return UsersGetResponse(**r)
		except: return r


	async def getFollowers(self, user_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None, name_case:Optional[str]=None):
		"""Returns a list of IDs of followers of the user in question, sorted by date added, most recent first."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Users.getFollowers", **args)
		for i in [UsersGetFollowersResponse, UsersGetFollowersFieldsResponse]:
			try: return i(**r)
			except: return r


	async def getSubscriptions(self, user_id:Optional[int]=None, extended:Optional[bool]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None):
		"""Returns a list of IDs of users and communities followed by the user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Users.getSubscriptions", **args)
		for i in [UsersGetSubscriptionsResponse, UsersGetSubscriptionsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def report(self, user_id:Optional[int]=None, type:Optional[str]=None, comment:Optional[str]=None):
		"""Reports (submits a complain about) a user."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Users.report", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, sort:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, fields:Optional[list[UsersFields]]=None, city:Optional[int]=None, country:Optional[int]=None, hometown:Optional[str]=None, university_country:Optional[int]=None, university:Optional[int]=None, university_year:Optional[int]=None, university_faculty:Optional[int]=None, university_chair:Optional[int]=None, sex:Optional[int]=None, status:Optional[int]=None, age_from:Optional[int]=None, age_to:Optional[int]=None, birth_day:Optional[int]=None, birth_month:Optional[int]=None, birth_year:Optional[int]=None, online:Optional[bool]=None, has_photo:Optional[bool]=None, school_country:Optional[int]=None, school_city:Optional[int]=None, school_class:Optional[int]=None, school:Optional[int]=None, school_year:Optional[int]=None, religion:Optional[str]=None, company:Optional[str]=None, position:Optional[str]=None, group_id:Optional[int]=None, from_list:Optional[list[str]]=None):
		"""Returns a list of users matching the search criteria."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Users.search", **args)
		try: return UsersSearchResponse(**r)
		except: return r



class Utils(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def checkLink(self, url:Optional[str]=None):
		"""Checks whether a link is blocked in VK."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.checkLink", **args)
		try: return UtilsCheckLinkResponse(**r)
		except: return r


	async def deleteFromLastShortened(self, key:Optional[str]=None):
		"""Deletes shortened link from user's list."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.deleteFromLastShortened", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def getLastShortenedLinks(self, count:Optional[int]=None, offset:Optional[int]=None):
		"""Returns a list of user's shortened links."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.getLastShortenedLinks", **args)
		try: return UtilsGetLastShortenedLinksResponse(**r)
		except: return r


	async def getLinkStats(self, key:Optional[str]=None, source:Optional[str]=None, access_key:Optional[str]=None, interval:Optional[str]=None, intervals_count:Optional[int]=None, extended:Optional[bool]=None):
		"""Returns stats data for shortened link."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.getLinkStats", **args)
		for i in [UtilsGetLinkStatsResponse, UtilsGetLinkStatsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getServerTime(self):
		"""Returns the current time of the VK server."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.getServerTime", **args)
		try: return UtilsGetServerTimeResponse(**r)
		except: return r


	async def getShortLink(self, url:Optional[str]=None, private:Optional[bool]=None):
		"""Allows to receive a link shortened via vk.cc."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.getShortLink", **args)
		try: return UtilsGetShortLinkResponse(**r)
		except: return r


	async def resolveScreenName(self, screen_name:Optional[str]=None):
		"""Detects a type of object (e.g., user, community, application) and its ID by screen name."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Utils.resolveScreenName", **args)
		try: return UtilsResolveScreenNameResponse(**r)
		except: return r



class Video(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def add(self, target_id:Optional[int]=None, video_id:Optional[int]=None, owner_id:Optional[int]=None):
		"""Adds a video to a user or community page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.add", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def addAlbum(self, group_id:Optional[int]=None, title:Optional[str]=None, privacy:Optional[list[str]]=None):
		"""Creates an empty album for videos."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.addAlbum", **args)
		try: return VideoAddAlbumResponse(**r)
		except: return r


	async def addToAlbum(self, target_id:Optional[int]=None, album_id:Optional[int]=None, album_ids:Optional[list[int]]=None, owner_id:Optional[int]=None, video_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.addToAlbum", **args)
		for i in [BaseOkResponse, VideoChangeVideoAlbumsResponse]:
			try: return i(**r)
			except: return r


	async def createComment(self, owner_id:Optional[int]=None, video_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, from_group:Optional[bool]=None, reply_to_comment:Optional[int]=None, sticker_id:Optional[int]=None, guid:Optional[str]=None):
		"""Adds a new comment on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.createComment", **args)
		try: return VideoCreateCommentResponse(**r)
		except: return r


	async def delete(self, video_id:Optional[int]=None, owner_id:Optional[int]=None, target_id:Optional[int]=None):
		"""Deletes a video from a user or community page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteAlbum(self, group_id:Optional[int]=None, album_id:Optional[int]=None):
		"""Deletes a video album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.deleteAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Deletes a comment on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.deleteComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, video_id:Optional[int]=None, name:Optional[str]=None, desc:Optional[str]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None, no_comments:Optional[bool]=None, repeat:Optional[bool]=None):
		"""Edits information about a video on a user or community page."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.edit", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editAlbum(self, group_id:Optional[int]=None, album_id:Optional[int]=None, title:Optional[str]=None, privacy:Optional[list[str]]=None):
		"""Edits the title of a video album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.editAlbum", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None):
		"""Edits the text of a comment on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, videos:Optional[list[str]]=None, album_id:Optional[int]=None, count:Optional[int]=None, offset:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[str]]=None):
		"""Returns detailed information about videos."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.get", **args)
		try: return VideoGetResponse(**r)
		except: return r


	async def getAlbumById(self, owner_id:Optional[int]=None, album_id:Optional[int]=None):
		"""Returns video album info"""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.getAlbumById", **args)
		try: return VideoGetAlbumByIdResponse(**r)
		except: return r


	async def getAlbums(self, owner_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None, need_system:Optional[bool]=None):
		"""Returns a list of video albums owned by a user or community."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.getAlbums", **args)
		for i in [VideoGetAlbumsResponse, VideoGetAlbumsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getAlbumsByVideo(self, target_id:Optional[int]=None, owner_id:Optional[int]=None, video_id:Optional[int]=None, extended:Optional[bool]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.getAlbumsByVideo", **args)
		for i in [VideoGetAlbumsByVideoResponse, VideoGetAlbumsByVideoExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getComments(self, owner_id:Optional[int]=None, video_id:Optional[int]=None, need_likes:Optional[bool]=None, start_comment_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, sort:Optional[str]=None, extended:Optional[bool]=None, fields:Optional[list[str]]=None):
		"""Returns a list of comments on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.getComments", **args)
		for i in [VideoGetCommentsResponse, VideoGetCommentsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def removeFromAlbum(self, target_id:Optional[int]=None, album_id:Optional[int]=None, album_ids:Optional[list[int]]=None, owner_id:Optional[int]=None, video_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.removeFromAlbum", **args)
		for i in [BaseOkResponse, VideoChangeVideoAlbumsResponse]:
			try: return i(**r)
			except: return r


	async def reorderAlbums(self, owner_id:Optional[int]=None, album_id:Optional[int]=None, before:Optional[int]=None, after:Optional[int]=None):
		"""Reorders the album in the list of user video albums."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.reorderAlbums", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reorderVideos(self, target_id:Optional[int]=None, album_id:Optional[int]=None, owner_id:Optional[int]=None, video_id:Optional[int]=None, before_owner_id:Optional[int]=None, before_video_id:Optional[int]=None, after_owner_id:Optional[int]=None, after_video_id:Optional[int]=None):
		"""Reorders the video in the video album."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.reorderVideos", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def report(self, owner_id:Optional[int]=None, video_id:Optional[int]=None, reason:Optional[int]=None, comment:Optional[str]=None, search_query:Optional[str]=None):
		"""Reports (submits a complaint about) a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.report", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reportComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, reason:Optional[int]=None):
		"""Reports (submits a complaint about) a comment on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.reportComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restore(self, video_id:Optional[int]=None, owner_id:Optional[int]=None):
		"""Restores a previously deleted video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.restore", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restoreComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Restores a previously deleted comment on a video."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.restoreComment", **args)
		try: return VideoRestoreCommentResponse(**r)
		except: return r


	async def save(self, name:Optional[str]=None, description:Optional[str]=None, is_private:Optional[bool]=None, wallpost:Optional[bool]=None, link:Optional[str]=None, group_id:Optional[int]=None, album_id:Optional[int]=None, privacy_view:Optional[list[str]]=None, privacy_comment:Optional[list[str]]=None, no_comments:Optional[bool]=None, repeat:Optional[bool]=None, compression:Optional[bool]=None):
		"""Returns a server address (required for upload) and video data."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.save", **args)
		try: return VideoSaveResponse(**r)
		except: return r


	async def search(self, q:Optional[str]=None, sort:Optional[int]=None, hd:Optional[int]=None, adult:Optional[bool]=None, live:Optional[bool]=None, filters:Optional[list[str]]=None, search_own:Optional[bool]=None, offset:Optional[int]=None, longer:Optional[int]=None, shorter:Optional[int]=None, count:Optional[int]=None, extended:Optional[bool]=None):
		"""Returns a list of videos under the set search criterion."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Video.search", **args)
		for i in [VideoSearchResponse, VideoSearchExtendedResponse]:
			try: return i(**r)
			except: return r



class Wall(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def checkCopyrightLink(self, link:Optional[str]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.checkCopyrightLink", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def closeComments(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.closeComments", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def createComment(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, from_group:Optional[int]=None, message:Optional[str]=None, reply_to_comment:Optional[int]=None, attachments:Optional[list[str]]=None, sticker_id:Optional[int]=None, guid:Optional[str]=None):
		"""Adds a comment to a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.createComment", **args)
		try: return WallCreateCommentResponse(**r)
		except: return r


	async def delete(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		"""Deletes a post from a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.delete", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def deleteComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Deletes a comment on a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.deleteComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def edit(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, friends_only:Optional[bool]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, services:Optional[str]=None, signed:Optional[bool]=None, publish_date:Optional[int]=None, lat:Optional[int]=None, long:Optional[int]=None, place_id:Optional[int]=None, mark_as_ads:Optional[bool]=None, close_comments:Optional[bool]=None, donut_paid_duration:Optional[int]=None, poster_bkg_id:Optional[int]=None, poster_bkg_owner_id:Optional[int]=None, poster_bkg_access_hash:Optional[str]=None, copyright:Optional[str]=None, topic_id:Optional[int]=None):
		"""Edits a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.edit", **args)
		try: return WallEditResponse(**r)
		except: return r


	async def editAdsStealth(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, signed:Optional[bool]=None, lat:Optional[int]=None, long:Optional[int]=None, place_id:Optional[int]=None, link_button:Optional[str]=None, link_title:Optional[str]=None, link_image:Optional[str]=None, link_video:Optional[str]=None):
		"""Allows to edit hidden post."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.editAdsStealth", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def editComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None):
		"""Edits a comment on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.editComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def get(self, owner_id:Optional[int]=None, domain:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None, filter:Optional[str]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns a list of posts on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.get", **args)
		for i in [WallGetResponse, WallGetExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getById(self, posts:Optional[list[str]]=None, extended:Optional[bool]=None, copy_history_depth:Optional[int]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns a list of posts from user or community walls by their IDs."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.getById", **args)
		for i in [WallGetByIdLegacyResponse, WallGetByIdExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Returns a comment on a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.getComment", **args)
		for i in [WallGetCommentResponse, WallGetCommentExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getComments(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, need_likes:Optional[bool]=None, start_comment_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None, sort:Optional[str]=None, preview_length:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None, comment_id:Optional[int]=None, thread_items_count:Optional[int]=None):
		"""Returns a list of comments on a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.getComments", **args)
		for i in [WallGetCommentsResponse, WallGetCommentsExtendedResponse]:
			try: return i(**r)
			except: return r


	async def getReposts(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Returns information about reposts of a post on user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.getReposts", **args)
		try: return WallGetRepostsResponse(**r)
		except: return r


	async def openComments(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.openComments", **args)
		try: return BaseBoolResponse(**r)
		except: return r


	async def pin(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		"""Pins the post on wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.pin", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def post(self, owner_id:Optional[int]=None, friends_only:Optional[bool]=None, from_group:Optional[bool]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, services:Optional[str]=None, signed:Optional[bool]=None, publish_date:Optional[int]=None, lat:Optional[int]=None, long:Optional[int]=None, place_id:Optional[int]=None, post_id:Optional[int]=None, guid:Optional[str]=None, mark_as_ads:Optional[bool]=None, close_comments:Optional[bool]=None, donut_paid_duration:Optional[int]=None, mute_notifications:Optional[bool]=None, copyright:Optional[str]=None, topic_id:Optional[int]=None):
		"""Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.post", **args)
		try: return WallPostResponse(**r)
		except: return r


	async def postAdsStealth(self, owner_id:Optional[int]=None, message:Optional[str]=None, attachments:Optional[list[str]]=None, signed:Optional[bool]=None, lat:Optional[int]=None, long:Optional[int]=None, place_id:Optional[int]=None, guid:Optional[str]=None, link_button:Optional[str]=None, link_title:Optional[str]=None, link_image:Optional[str]=None, link_video:Optional[str]=None):
		"""Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type 'Community post'."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.postAdsStealth", **args)
		try: return WallPostAdsStealthResponse(**r)
		except: return r


	async def reportComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None, reason:Optional[int]=None):
		"""Reports (submits a complaint about) a comment on a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.reportComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def reportPost(self, owner_id:Optional[int]=None, post_id:Optional[int]=None, reason:Optional[int]=None):
		"""Reports (submits a complaint about) a post on a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.reportPost", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def repost(self, object:Optional[str]=None, message:Optional[str]=None, group_id:Optional[int]=None, mark_as_ads:Optional[bool]=None, mute_notifications:Optional[bool]=None):
		"""Reposts (copies) an object to a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.repost", **args)
		try: return WallRepostResponse(**r)
		except: return r


	async def restore(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		"""Restores a post deleted from a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.restore", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def restoreComment(self, owner_id:Optional[int]=None, comment_id:Optional[int]=None):
		"""Restores a comment deleted from a user wall or community wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.restoreComment", **args)
		try: return BaseOkResponse(**r)
		except: return r


	async def search(self, owner_id:Optional[int]=None, domain:Optional[str]=None, query:Optional[str]=None, owners_only:Optional[bool]=None, count:Optional[int]=None, offset:Optional[int]=None, extended:Optional[bool]=None, fields:Optional[list[BaseUserGroupFields]]=None):
		"""Allows to search posts on user or community walls."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.search", **args)
		for i in [WallSearchResponse, WallSearchExtendedResponse]:
			try: return i(**r)
			except: return r


	async def unpin(self, owner_id:Optional[int]=None, post_id:Optional[int]=None):
		"""Unpins the post on wall."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Wall.unpin", **args)
		try: return BaseOkResponse(**r)
		except: return r



class Widgets(BaseMethod):
	def __init__(self, vk):
		super().__init__(vk)

	async def getComments(self, widget_api_id:Optional[int]=None, url:Optional[str]=None, page_id:Optional[str]=None, order:Optional[str]=None, fields:Optional[list[UsersFields]]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Gets a list of comments for the page added through the [vk.com/dev/Comments|Comments widget]."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Widgets.getComments", **args)
		try: return WidgetsGetCommentsResponse(**r)
		except: return r


	async def getPages(self, widget_api_id:Optional[int]=None, order:Optional[str]=None, period:Optional[str]=None, offset:Optional[int]=None, count:Optional[int]=None):
		"""Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed."""
		args = locals()
		for i in ('self', '__class__'): args.pop(i)
		r = await super().method("Widgets.getPages", **args)
		try: return WidgetsGetPagesResponse(**r)
		except: return r



