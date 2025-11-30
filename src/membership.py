from src.data import get_plan, get_feature, MEMBERSHIP_PLANS
from src.data import ADDITIONAL_FEATURES


class MembershipManager:

    # inicializa el gestor vacio
    def __init__(self):
        self.selected_plan = None
        self.features = []
    
    # seleccionar un plan de membresía
    def select_plan(self, name):
        plan = get_plan(name)
        if not plan or not plan.get('available'):
            return False
        self.selected_plan = {'name': name, 'cost': plan['cost']}
        return True
    
    # agg una característica adicional
    def add_feature(self, name):
        feature = get_feature(name)
        if not feature or not feature.get('available'):
            return False
        if name in [f['name'] for f in self.features]:
            return False
        self.features.append({'name': name, 'cost': feature['cost']})
        return True
    
    # calcula el costo total
    def calculate_total(self):
        if not self.selected_plan:
            return -1
        base = self.selected_plan['cost']
        features_cost = sum(f['cost'] for f in self.features)
        return base + features_cost
    
    # lista de todos los planes
    def get_plans(self):
        return list(MEMBERSHIP_PLANS.keys())
    
    # lista de todas las características disponibles
    def get_features_list(self):
        return list(ADDITIONAL_FEATURES.keys())