from src.membership import MembershipManager


class TestRequirement1:
    def test_select_valid_plan(self):
        manager = MembershipManager()
        assert manager.select_plan("Basic") is True
        assert manager.selected_plan['name'] == "Basic"
    
    def test_select_invalid_plan(self):
        manager = MembershipManager()
        assert manager.select_plan("Invalid") is False
    
    def test_get_plans_list(self):
        manager = MembershipManager()
        plans = manager.get_plans()
        assert "Basic" in plans
        assert "Premium" in plans
        assert "Family" in plans


class TestRequirement2:
    def test_add_valid_feature(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Personal Training") is True
    
    def test_add_invalid_feature(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Invalid") is False
    
    def test_add_duplicate_feature(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Personal Training")
        assert manager.add_feature("Personal Training") is False
    
    def test_get_features_list(self):
        manager = MembershipManager()
        features = manager.get_features_list()
        assert "Personal Training" in features
        assert "Group Classes" in features


class TestRequirement3:
    def test_calculate_basic_cost(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.calculate_total() == 50
    
    def test_calculate_premium_cost(self):
        manager = MembershipManager()
        manager.select_plan("Premium")
        assert manager.calculate_total() == 100
    
    def test_calculate_with_features(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Personal Training")
        assert manager.calculate_total() == 100  # 50 + 50
    
    def test_calculate_no_plan(self):
        manager = MembershipManager()
        assert manager.calculate_total() == -1

class TestRequirement4:
    def test_group_discount_applied(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.set_members(2)
        assert manager.calculate_total() == 45  # 50 - 10%

    def test_group_discount_not_applied(self):
        manager =MembershipManager()
        manager.select_plan("Basic")
        manager.set_members(1)
        assert manager.calculate_total() == 50
            
class TestRequirement5:
    def test_discount_20_applies(self):
        manager = MembershipManager()
        manager.select_plan("Premium")  # 100
        manager.add_feature("Personal Training")  # 50
        manager.add_feature("Nutritionist")  # 40
        assert manager.calculate_total() == 190

        manager.add_feature("Group Classes") 
        assert manager.calculate_total() == 230

    def test_discount_50_applies(self):
        manager = MembershipManager()
        manager.select_plan("Family")  # 150
        manager.add_feature("Personal Training")  
        manager.add_feature("Group Classes")  
        manager.add_feature("Nutritionist")  

        manager.features.append({"name": "Extra Feature", "cost": 200})
        # total = 470 → -50 = 420 → surcharge 15% = 483
        assert manager.calculate_total() == 483


class TestRequirement6:
    def test_premium_feature_surcharge(self):
        manager = MembershipManager()
        manager.select_plan("Basic")  # 50
        manager.add_feature("Personal Training")  # premium
        assert manager.calculate_total() == 115 # 100 * 1.15
    
    def test_no_premium_surcharge(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        manager.add_feature("Group Classes")  # no premium
        assert manager.calculate_total() == 80


class TestRequirement7:
    def test_validate_plan_availability(self):
        manager = MembershipManager()
        assert manager.select_plan("Basic") is True
        assert manager.select_plan("NonExistent") is False
    
    def test_validate_feature_availability(self):
        manager = MembershipManager()
        manager.select_plan("Basic")
        assert manager.add_feature("Personal Training") is True
        assert manager.add_feature("NonExistent") is False


class TestIntegration:
    def test_complete_flow(self):
        manager = MembershipManager()
        manager.select_plan("Premium")
        manager.add_feature("Personal Training")
        manager.add_feature("Group Classes")
        total = manager.calculate_total()
        assert total == 207  