
from abc import ABC
from profiles import models as pr_models
from external_api import models as eapi_models
import logging


class ExchangeBackend(ABC):
    def __init__(self, vendor_name):
        self.vendor_name = vendor_name
        self.vendor = None

    @classmethod
    def create_customer(cls, user_id):
        return NotImplementedError

    @classmethod
    def bulk_create_customer(cls, user_list):
        return NotImplementedError

    @classmethod
    def generate_aof_image(cls, user_id):
        return NotImplementedError
    
    @classmethod
    def upload_aof_image(cls, user_id):
        return NotImplementedError
    
    def update_ucc(self, user_id, ucc):
        logger = logging.getLogger('django.error')
        try:
            user = pr_models.User.objects.get(id=user_id)
            if not self.vendor:
                self.vendor = eapi_models.Vendor.objects.get(name=self.vendor_name)
            user_vendor = pr_models.UserVendor.objects.update_or_create(user=user, vendor=self.vendor, defaults={'ucc':ucc})
            return user_vendor
        except Exception as e:
            logger.error("Error updating ucc: " + str(e))
        
        return None
    
    def update_mandate_registered(self, user_id):

        logger = logging.getLogger('django.error')
        try:
            user = pr_models.User.objects.get(id=user_id)
            if not self.vendor:
                self.vendor = eapi_models.Vendor.objects.get(name=self.vendor_name)
            user_vendor = pr_models.UserVendor.objects.get(user=user, vendor=self.vendor)
            user_vendor.mandate_registered = True
            user_vendor.save()
            return user_vendor
        except Exception as e:
            logger.error("Error updating ucc: " + str(e))
        return None
    
    def generate_bank_mandate(self, user_id):
        return NotImplementedError

    def upload_bank_mandate(self, user_id):
        return NotImplementedError
    
    def generate_bank_mandate_registration(self, user_id):
        return NotImplementedError
