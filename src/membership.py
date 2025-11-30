"""Module providing membership plan management, feature selection,
discounts, and total cost calculations."""

from src.data import get_plan, get_feature, MEMBERSHIP_PLANS, ADDITIONAL_FEATURES


class MembershipManager:
    """Manage membership plan selection, additional features,
    premium surcharges, group discounts, and total membership cost."""

    def __init__(self):
        """Initialize the manager with no selected plan, no features,
        and default member count of one."""
        self.selected_plan = None
        self.features = []
        self.members_count = 1

    def select_plan(self, name):
        """Select a membership plan by name.

        Args:
            name (str): Name of the membership plan.

        Returns:
            bool: True if the plan exists and is available, otherwise False.
        """
        plan = get_plan(name)
        if not plan or not plan.get('available'):
            return False
        self.selected_plan = {'name': name, 'cost': plan['cost']}
        return True

    def set_members(self, count):
        """Set number of members joining together.

        Args:
            count (int): Number of members.

        Returns:
            bool: True if count is valid (>=1), otherwise False.
        """
        if count < 1:
            return False
        self.members_count = count
        return True

    def add_feature(self, name):
        """Add an additional feature to the membership.

        Args:
            name (str): Feature name.

        Returns:
            bool: True if feature exists and is not already added, otherwise False.
        """
        feature = get_feature(name)
        if not feature or not feature.get('available'):
            return False
        if name in [f['name'] for f in self.features]:
            return False
        self.features.append({'name': name, 'cost': feature['cost']})
        return True

    def has_premium(self):
        """Check if any selected feature is considered premium."""
        premium_keywords = ["Training", "Exclusive", "Specialized"]
        for feature in self.features:
            if any(keyword.lower() in feature['name'].lower()
                for keyword in premium_keywords):
                return True
        return False


    def calculate_total(self):
        """Calculate the final membership total including:
        - Base plan cost
        - Additional features
        - Special discounts ($20 or $50)
        - Premium surcharge (15%)
        - Group discount (10%)

        Returns:
            float: Final rounded membership cost, or -1 if no plan selected.
        """
        if not self.selected_plan:
            return -1

        base = self.selected_plan['cost']
        features_cost = sum(f['cost'] for f in self.features)
        total = base + features_cost

        # Apply special offer discounts
        if total > 400:
            total -= 50
        elif total > 200:
            total -= 20

        # Apply premium surcharge
        if self.has_premium():
            total *= 1.15

        # Apply group membership discount
        if self.members_count >= 2:
            total *= 0.9

        return round(total, 2)

    def get_plans(self):
        """Return a list of available membership plan names."""
        return list(MEMBERSHIP_PLANS.keys())

    def get_features_list(self):
        """Return a list of available additional feature names."""
        return list(ADDITIONAL_FEATURES.keys())
