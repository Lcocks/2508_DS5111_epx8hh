from abc import ABC, abstractmethod
class GainerBase:
    def __init__(self):
        pass

    @abstractmethod
    def download_html(self):
        pass

    @abstractmethod
    def extract_csv(self):
        pass

    @abstractmethod
    def normalize_data(self):
        pass
