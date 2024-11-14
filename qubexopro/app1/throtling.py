from rest_framework.throttling import UserRateThrottle

class CustomThrot(UserRateThrottle):
    scope = 'post_tho'