# -*- coding: utf-8 -*-
from django.db import models
 
# Create your models here.
from django.utils.translation import ugettext_lazy as _
 
class Order(models.Model):
    order_no = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(help_text=_('creation date'), auto_now_add = True)
    updated_on = models.DateTimeField(help_text=_('last update date'), auto_now = True)
 
    def __unicode__(self):
        return self.order_no