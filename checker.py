from modules.denic import Denic

class Checker():
    modules = [
        Denic()
    ]

    def check_domain(self, domain):
        for module in self.modules:
            if not module.is_responsible(domain):
                continue
            success, result = module.check_domain(domain)
            if not success:
                continue

            return (True, result)
        return (False, None)
