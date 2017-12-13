# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.


# Model for grouping code for accounts
from django.forms import model_to_dict
from django.utils.timezone import now
from smart_selects.db_fields import ChainedForeignKey

from ERP.models import Pais, Estado, Municipio, Bank
from Logs.controller import Logs


class GroupingCode(models.Model):
    level = models.CharField(verbose_name="Nivel", max_length=5,)
    grouping_code = models.DecimalField(verbose_name="Código Agrupador", max_digits=20, decimal_places=2,)
    account_name = models.CharField(verbose_name="Nombre de la Cuenta y/o subcuenta", max_length=500,)

    def __str__(self):
        return str(self.grouping_code) + ": " + self.account_name

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.grouping_code) + ": " + self.account_name

    class Meta:
        verbose_name_plural = 'Código Agrupador de Cuentas del SAT.'
        verbose_name = 'Código Agrupador de Cuentas del SAT.'

class Account(models.Model):
    ACTIVE = 1
    NON_ACTIVE = 2

    STATUS_CHOICES = (
        (ACTIVE, 'Activa'),
        (NON_ACTIVE, 'Inactiva'),
    )

    DEBIT = 1    #PAYABLE RECEIVABLE
    CREDIT = 2
    DEBIT_CREDIT_CHOICES = (
        (DEBIT, "Deudora"),
        (CREDIT, "Acreedora"),
    )

    LEDGER = 1
    NO_LEDGER = 2
    LG_ACCOUNT_CHOICES = (
        (LEDGER,"Si"),
        (NO_LEDGER,"No"),
    )

    number = models.IntegerField(verbose_name="Número de Cuenta", null=False,)
    name = models.CharField(verbose_name="Nombre de la Cuenta", max_length=500, null=False,)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE, verbose_name='Estatus')

    nature_account = models.IntegerField(choices=DEBIT_CREDIT_CHOICES, default=DEBIT, verbose_name='Naturaleza de Cuenta')
    ledger_account = models.IntegerField(choices=LG_ACCOUNT_CHOICES, default=LEDGER, verbose_name='Cuenta de Mayor')
    level = models.CharField(verbose_name="Nivel", max_length=500, null=False,)
    item = models.CharField(verbose_name="Rubro", max_length=500, null=False,)



    #foreign
    grouping_code = models.ForeignKey(GroupingCode, verbose_name="Código Agrupador SAT",)
    subsidiary_account = models.ForeignKey('self', verbose_name='Subcuenta de', null=True, blank=True)

    def __str__(self):
        return str(self.number) + ": " + self.name

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.number) + ": " + self.name

    class Meta:
        verbose_name_plural = 'Cuentas'
        verbose_name = 'Cuenta'

# Model for accounting policy
class FiscalPeriod(models.Model):
    OPENED = 1
    CLOSED = 2
    AUDITED = 3

    STATUS_CHOICES = (
        (OPENED, 'Abierto'),
        (CLOSED, 'Cerrado'),
        (AUDITED, 'Auditado'),
    )

    accounting_year = models.IntegerField(verbose_name="Ejercicio Contable", null=False, )
    account_period = models.IntegerField(verbose_name="Periodo Contable", null=False, )
    status = models.IntegerField(choices=STATUS_CHOICES, default=OPENED, verbose_name='Estatus')

    def __str__(self):
        return str(self.accounting_year) + ": " + self.account_period

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.accounting_year) + ": " + self.account_period

    class Meta:
        verbose_name_plural = 'Año contable'
        verbose_name = 'Año Contable'

# Model for accounting policy
class TypePolicy(models.Model):
    AVERAGE = 1
    EXPENSES = 2
    DAILY = 3

    TYPE_CHOICES = (
        (AVERAGE, 'Ingresos'),
        (EXPENSES, 'Egresos'),
        (DAILY, 'Diario'),
    )

    name = models.IntegerField(choices=TYPE_CHOICES, default=AVERAGE, verbose_name='Tipo de Póliza')
    balanced_accounts = models.BooleanField(verbose_name="Cuadrar póliza", default=False)


    def __str__(self):
        return str(self.name)

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Tipos de Póliza'
        verbose_name = 'Tipo de Póliza'

# Model for accounting policy
class AccountingPolicy(models.Model):
    fiscal_period = models.ForeignKey(FiscalPeriod, verbose_name='Periodo Fiscal', null=False, blank=False)
    type_policy = models.ForeignKey(TypePolicy, verbose_name='Tipo de Póliza', null=False, blank=False)
    folio =  models.IntegerField("Folio", blank=True, null=True)
    registry_date = models.DateField(default=now(), null=False, blank=False, verbose_name="Fecha de Registro")
    description = models.CharField(verbose_name="Concepto", max_length=4096, null=False, blank=False)

    def __str__(self):
        return str(self.type_policy) + ": " + self.folio

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.type_policy) + ": " + self.folio

    class Meta:
        verbose_name_plural = 'Pólizas Contables'
        verbose_name = 'Póliza contable'

# Model for accounting policy
class AccountingPolicyDetail(models.Model):
    accounting_policy = models.ForeignKey(AccountingPolicy, verbose_name='Póliza', null=False, blank=False)
    account = models.ForeignKey(Account, verbose_name='Cuenta', null=False, blank=False)
    description = models.CharField(verbose_name="Concepto", max_length=4096, null=False, blank=False)
    debit=models.FloatField(verbose_name="Debe", null=False, blank=False, default=0)
    credit=models.FloatField(verbose_name="Haber", null=False, blank=False,default=0)
    registry_date = models.DateField(default=now(), null=False, blank=False, verbose_name="Fecha de Registro")

    def __str__(self):
        return str(self.account.number) + ": " + self.account.name

    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.account.number) + ": " + self.account.name

    class Meta:
        verbose_name_plural = 'Detalle de Pólizas'
        verbose_name = 'Detalle de Póliza'

class Provider(models.Model):
    ACTIVE = 1
    NON_ACTIVE = 2

    STATUS_CHOICES = (
        (ACTIVE, 'Activo'),
        (NON_ACTIVE, 'Inactivo'),
    )

    name = models.CharField(verbose_name='Nombre', max_length=50, null=False, blank=False, editable=True)
    colony = models.CharField(verbose_name="Colonia", max_length=255, null=False, blank=False)
    street = models.CharField(verbose_name="Calle", max_length=255, null=False, blank=False)
    outdoor_number = models.CharField(verbose_name="No. Exterior", max_length=10, null=False, blank=False)
    indoor_number = models.CharField(verbose_name="No. Interior", max_length=10, null=True, blank=True)
    zip_code = models.CharField(verbose_name="Código Postal", max_length=5, null=False, blank=False)
    rfc = models.CharField(verbose_name='RFC', max_length=20, null=False, blank=False, editable=True)
    curp = models.CharField(verbose_name="CURP", max_length=18, null=False, blank=False, unique=True)
    phone_number = models.CharField(verbose_name="Teléfono", max_length=20, null=False, blank=False)
    cellphone_number = models.CharField(verbose_name="Celular", max_length=20, null=False, blank=True)
    office_number = models.CharField(verbose_name="Teléfono de Oficina", max_length=20, null=False, blank=True)
    extension_number = models.CharField(verbose_name="Número de Extensión", max_length=10, null=False, blank=True)

    # Attribute for the Chained Keys.
    country = models.ForeignKey(Pais, verbose_name="País", null=False, blank=False)
    state = ChainedForeignKey(Estado,
                              chained_field="country",
                              chained_model_field="pais",
                              show_all=False,
                              auto_choose=True,
                              sort=True,
                              verbose_name="Estado")
    town = ChainedForeignKey(Municipio,
                             chained_field="state",
                             chained_model_field="estado",
                             show_all=False,
                             auto_choose=True,
                             sort=True,
                             verbose_name="Municipio")

    last_edit_date = models.DateTimeField(auto_now_add=True)

    accounting_account = models.ForeignKey(Account, verbose_name="Cuenta Contable", blank=False, null=False)
    bank = models.ForeignKey(Bank, verbose_name="Banco", null=True, blank=False)
    bank_account_name = models.CharField(verbose_name="Nombre de la Persona", max_length=512, default="", null=True,
                                         blank=True)
    bank_account = models.CharField(verbose_name="Cuenta Bancaria", max_length=16, default="", null=True, blank=True)
    # CLABE = models.CharField(verbose_name="CLABE Interbancaria", max_length=18, default="", null=True, blank=True)
    employer_registration_number = models.CharField(verbose_name="Número de Registro Patronal", max_length=24,
                                                    default="", null=True, blank=True)
    services = models.CharField(verbose_name="Servicios que presta", max_length=4096, default="", null=True, blank=True)

    FISICA = "f"
    MORAL = "m"

    TYPE_CHOICES = (
        (FISICA, 'Física'),
        (MORAL, 'Moral'),
    )
    tax_person_type = models.CharField(verbose_name="Tipo de Persona", max_length=1, default=MORAL, null=False,
                                       blank=False, choices=TYPE_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE, verbose_name='Estatus')

    class Meta:
        verbose_name_plural = 'Proveedores'

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['name'] = str(self.nombreContratista)
        ans['street'] = str(self.calle)
        ans['number'] = str(self.numero)
        ans['outdoor_number'] = str(self.colonia)
        ans['town'] = str(self.municipio.nombreMunicipio)
        ans['state'] = str(self.estado.nombreEstado)
        ans['country'] = str(self.pais.nombrePais)
        ans['cp'] = str(self.cp)
        ans['rfc'] = str(self.rfc)

        return ans

    def __str__(self):
        return self.nombreContratista

    def save(self, *args, **kwargs):
        can_save = True

        if can_save:
            self.last_edit_date = now()
            Logs.log("Saving new Proveedor", "Te")
            super(Provider, self).save(*args, **kwargs)
        else:
            Logs.log("Couldn't save")