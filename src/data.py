
MEMBERSHIP_PLANS = {
    "Basic": {"cost": 50, "available": True},
    "Premium": {"cost": 100, "available": True},
    "Family": {"cost": 150, "available": True}
}

ADDITIONAL_FEATURES = {
    "Personal Training": {"cost": 50, "available": True},
    "Group Classes": {"cost": 30, "available": True},
    "Nutritionist": {"cost": 40, "available": True}
}


def get_plan(name):
    return MEMBERSHIP_PLANS.get(name)


def get_feature(name):
    return ADDITIONAL_FEATURES.get(name)