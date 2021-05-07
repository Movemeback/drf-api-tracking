from .base_models import BaseAPIRequestLog

'''
Removing default model to be replaced by model in parent code
Example:
class AnalyticsAPIRequestTracking(BaseAPIRequestLog):
    class Meta:
        db_table = 'analytics_api_request_tracking'
        verbose_name = 'Analytics API Request Tracking'
'''
#class APIRequestLog(BaseAPIRequestLog):
#    pass
