from src.data import get_plan, get_feature, MEMBERSHIP_PLANS
from src.data import ADDITIONAL_FEATURES


class MembershipManager:

    # inicializa el gestor vacio
    def __init__(self):
        self.selected_plan = None
        self.features = []
        self.members_count = 1
    
    # seleccionar un plan de membresía
    def select_plan(self, name):
        plan = get_plan(name)
        if not plan or not plan.get('available'):
            return False
        self.selected_plan = {'name': name, 'cost': plan['cost']}
        return True
    
    # settear numero de miembros
    def set_members(self, count):
        if count < 1:
            return False
        self.members_count = count
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
    
    #si alguno es miembro
    def has_premium(self):
        premium_plans = ["Training", "Exclusive", "Specialized"]
        for f in self.features:
            if any(key.lower() in f['name'].lower() for key in premium_plans):
                return True
        return False
    
    # calcula el costo total
    def calculate_total(self):
        if not self.selected_plan:
            return -1
        base = self.selected_plan['cost']
        features_cost = sum(f['cost'] for f in self.features)
        total = base + features_cost

        if total > 400 : 
            total -= 50
        elif total > 200 :
            total -= 20

        if self.has_premium():
            total *= 1.15

        if self.members_count >= 2:
            total *= 0.9

        return round(total, 2)
    
    # lista de todos los planes
    def get_plans(self):
        return list(MEMBERSHIP_PLANS.keys())
    
    # lista de todas las características disponibles
    def get_features_list(self):
        return list(ADDITIONAL_FEATURES.keys())