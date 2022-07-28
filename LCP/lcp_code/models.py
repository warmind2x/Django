from django.db import models

# Create your models here.
class Lcp_code(models.Model):
    created_time = models.DateField(("Creacion proyecto"), auto_now=False, auto_now_add=True)
    lcp_code = models.CharField(("Codigo completo ej.LCP-210210-01"), max_length=50)
    lcp_name = models.CharField(("Nombre del proyecto"), max_length=250)
    lcp_description = models.CharField(("Descripcion del proyecto"), max_length=250)
    lcp_type = models.ForeignKey("LcpType", verbose_name=("Capex/Expense/Miscelaneous"), on_delete=models.CASCADE)
    lcp_status = models.BinaryField(("0: open, 1:close"))
    project_type = models.CharField(("Tipo de proyecto"), max_length=100)
    lcp_stake_holder = models.ForeignKey("StakeHolder", verbose_name=("Cliente interno"), on_delete=models.CASCADE)
    buyer_name = models.ForeignKey("Buyer", verbose_name=("Nombre del comprador"), on_delete=models.CASCADE)
    lcp_options = models.JSONField(("Opciones de estado"), encoder=None, decoder=None)
    
    def __str__(self):
        return f'id:{self.id} {self.lcp_name} created time {self.created_time}'
    
    
class Buyer(models.Model):
    buyer_name = models.CharField(("Nombre Comprador"), max_length=250)
    
    def __str__(self) -> str:
        return f'{self.buyer_name}'
    
class StakeHolder(models.Model):
    stake_holder_name = models.CharField(("Nombre del cliente"), max_length=250)
    
    def __str__(self):
        return self.stake_holder_name
    
    
class LcpType(models.Model):
    lcp_type = models.CharField(("Tipo de proyecto Inversion"), max_length=50)
    
    def __str__(self) -> str:
        return f'{self.lcp_type}'