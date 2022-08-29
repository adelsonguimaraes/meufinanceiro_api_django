from django.db import models

class TransactionTypeEnum(models.TextChoices):
    DEBIT = "DE"
    CREDIT = "CR"

class ActiveEnum(models.TextChoices):
    ACTIVE = True
    INACTIVE = False