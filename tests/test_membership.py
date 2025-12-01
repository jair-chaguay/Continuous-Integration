"""Unit tests for the MembershipManager class and all project requirements."""

from src.membership import MembershipManager


class TestRequirement1:
    """Tests for Requirement 1: selecting membership plans."""

    def test_select_valid_plan(self):
        """Selecting a valid membership plan should succeed."""
        manager = MembershipManager()
        assert manager.select_plan("Basic") is True
        assert manager.selected_plan["name"] == "Basic"

    def test_select_invalid_plan(self):
        """Selecting an invalid membership plan should return False."""
        manager = MembershipManager()
        assert manager.select_plan("Invalid") is False

    def test_get_plans_list(self):
        """Returned plan list should include all expected plans."""
        manager = MembershipManager()
        plans = manager.get_plans()
        assert "Basic" in plans
        assert "Premium" in plans
        assert "Family" in plans


class TestRequirement2:
    """Tests for Requirement 2: adding membership features."""

    def test_add_valid_feature(self):
        """Adding a valid feature should succeed."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Personal Training") is True

    def test_add_invalid_feature(self):
        """Adding an invalid feature should fail."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Invalid") is False

    def test_add_duplicate_feature(self):
        """Adding a duplicate feature should return False."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Personal Training")
        assert manager.add_feature("Personal Training") is False

    def test_get_features_list(self):
        """Returned features list should include expected items."""
        manager = MembershipManager()
        features = manager.get_features_list()
        assert "Personal Training" in features
        assert "Group Classes" in features


class TestRequirement3:
    """Tests for Requirement 3: membership cost calculation."""

    def test_calculate_basic_cost(self):
        """Basic plan should cost 50."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.calculate_total() == 50

    def test_calculate_premium_cost(self):
        """Premium plan should cost 100 because no surcharge applies."""
        manager = MembershipManager()
        manager.select_plan("Premium")
        assert manager.calculate_total() == 100

    def test_calculate_with_features(self):
        """Feature costs should add correctly to the base cost."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Personal Training")
        assert manager.calculate_total() == 115

    def test_calculate_no_plan(self):
        """If no plan is selected, total should be -1."""
        manager = MembershipManager()
        assert manager.calculate_total() == -1


class TestRequirement4:
    """Tests for Requirement 4: group discounts."""

    def test_group_discount_applied(self):
        """10% discount should apply when two or more members join."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.set_members(2)
        assert manager.calculate_total() == 45

    def test_group_discount_not_applied(self):
        """No group discount should apply when only one member joins."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.set_members(1)
        assert manager.calculate_total() == 50


class TestRequirement5:
    """Tests for Requirement 5: special offer discounts based on total cost."""

    def test_discount_20_applies(self):
        """Discount of $20 should apply when total exceeds 200."""
        manager = MembershipManager()
        manager.select_plan("Premium")
        manager.add_feature("Personal Training")
        manager.add_feature("Nutritionist")
        assert manager.calculate_total() == 190

        manager.add_feature("Group Classes")
        assert manager.calculate_total() == 200 # 220 - 20 discount = 200

    def test_discount_50_applies(self):
        """Discount of $50 should apply when total exceeds 400."""
        manager = MembershipManager()
        manager.select_plan("Family")
        manager.add_feature("Personal Training")
        manager.add_feature("Group Classes")
        manager.add_feature("Nutritionist")
        manager.features.append({"name": "Extra Feature", "cost": 200})
        assert manager.calculate_total() == 420  # 470 - 50 discount = 420


class TestRequirement6:
    """Tests for Requirement 6: premium feature surcharge."""

    def test_premium_feature_surcharge(self):
        """Premium feature should add a 15% surcharge."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Personal Training")
        assert manager.calculate_total() == 115

    def test_no_premium_surcharge(self):
        """Non-premium features should not trigger surcharge."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Group Classes")
        assert manager.calculate_total() == 80


class TestRequirement7:
    """Tests for Requirement 7: availability validation."""

    def test_validate_plan_availability(self):
        """Selecting nonexistent plans should return False."""
        manager = MembershipManager()
        assert manager.select_plan("Basic") is True
        assert manager.select_plan("NonExistent") is False

    def test_validate_feature_availability(self):
        """Adding nonexistent features should return False."""
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Personal Training") is True
        assert manager.add_feature("NonExistent") is False


# pylint: disable=R0903
class TestIntegration:
    """Full integration test."""

    def test_complete_flow(self):
        """A complete flow should yield correct total."""
        manager = MembershipManager()
        manager.select_plan("Premium")
        manager.add_feature("Personal Training")
        manager.add_feature("Group Classes")
        assert manager.calculate_total() == 180
