from abc import abstractmethod

class Module():
    def __init__(self, tlds):
        self.handled_tlds = tlds

    def is_responsible(self, domain):
        return domain.split('.')[-1] in self.handled_tlds

    @abstractmethod
    def check_domain(self, domain):
        return
