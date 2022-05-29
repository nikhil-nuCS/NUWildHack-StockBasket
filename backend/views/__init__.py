
def initialize_routes(api, firebase_config):
    from .tickerdata import initialize_routes as init_tickerdata_routes
    from .signup import initialize_routes as init_signup_routes
    from .login import initialize_routes as init_login_routes
    from .baskets import initialize_routes as init_baskets_routes
    from .userprofile import initialize_routes as init_userprofile_routes
    from .investedbaskets import initialize_routes as init_investbasket_routes
    from .managerprofile import initialize_routes as init_managerprofile_routes
    from .usercreatedbasket import initialize_routes as init_usercreatedbasket_routes

    init_tickerdata_routes(api, firebase_config)
    init_signup_routes(api, firebase_config)
    init_login_routes(api, firebase_config)
    init_baskets_routes(api, firebase_config)
    init_userprofile_routes(api, firebase_config)
    init_investbasket_routes(api, firebase_config)
    init_managerprofile_routes(api, firebase_config)
    init_usercreatedbasket_routes(api, firebase_config)
    
        