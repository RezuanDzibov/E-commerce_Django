from abc import ABC, abstractmethod

from django.http import HttpRequest


class BaseService(ABC):
    def __init__(self, request: HttpRequest):
        """
        @param request: Authenticated HttpRequest.
        """
        self.request = request

    @abstractmethod
    def execute(self):
        pass
