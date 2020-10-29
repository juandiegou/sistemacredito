from django.db import models

# Create your models here.




class Prestamista(models.Model):
    ci = models.PositiveIntegerField(name='ci',primary_key=True)
    nombre = models.TextField(name='name',max_length=50,null=False)
    apellido = models.TextField(name='last_name',max_length=50,null=False)
    direccion = models.TextField(name='address',max_length=100,null=False)
    telefono = models.TextField(name='phone',max_length=10,null=False)
    fechaNacimiento= models.DateField(name='birthdate')

    
    def __str__(self):
        return str(self.ci)


    def getCi(self):
        return str(self.ci)

    def getNombre(self):
        return str(self.name)

    def getApellido(self):
        return str(self.last_name)
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
       

    
class Prestamos(models.Model):
    identificador=models.PositiveIntegerField(name='id',primary_key=True)
    ci=models.ForeignKey(Prestamista,on_delete=models.DO_NOTHING,blank=False)
    tasa = models.FloatField(name='tasa',blank=False)
    monto= models.PositiveIntegerField(name='interes')

    def __str__(self):
        return str(self.identificador)



class Cuota(models.Model):
    identificador= models.ForeignKey(Prestamos,models.PROTECT,db_column='identificador')
    numeroCuota= models.PositiveIntegerField(name='numeroCuota',primary_key=True, db_column='numeroCuota')
    fechaVencimiento = models.DateTimeField(name='fechaVencimiento',blank=False)
    fechaPago= models.DateTimeField(name='fechaPago')
    numeroCuotas = models.PositiveSmallIntegerField(name='cant_cuotas')
    valor= models.PositiveIntegerField(name='valor',blank=False)


    class Meta:
        unique_together = (('identificador','numeroCuota'),)

        def __str__(self):
                return str(self.unique_together)
