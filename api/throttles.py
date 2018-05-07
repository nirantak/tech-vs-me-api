from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonBurst(AnonRateThrottle):
    '''
    Anonymous client burst rate throttling (reqs/min)
    '''
    scope = 'anon_burst'


class AnonSustained(AnonRateThrottle):
    '''
    Anonymous client sustained rate throttling (reqs/day)
    '''
    scope = 'anon_sustained'


class UserBurst(UserRateThrottle):
    '''
    Logged in user burst rate throttling (reqs/min)
    '''
    scope = 'user_burst'


class UserSustained(UserRateThrottle):
    '''
    Logged in user sustained rate throttling (reqs/day)
    '''
    scope = 'user_sustained'
