from django import forms


class AgregarUsuario(forms.Form):
    correo=forms.EmailField(widget=forms.EmailInput(),label="Email")
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellido=forms.CharField(widget=forms.TextInput(),label="Apellido")
    fecha=forms.DateField(widget=forms.SelectDateWidget(years=range(1900,2000)),label="Fecha de Nacimiento")
    region=forms.ChoiceField(choices=(('1', 'Arica'),('2', 'Tarapacá'),('3', 'Antofagasta'),('4', 'Atacama'),('5', 'Coquimbo'),('6', 'Valparaíso'),('7', 'Región Metropolitana'),('8', 'Bernardo OHiggins'),('9', 'Maule'),('10', 'Ñuble'),('11', 'Biobío'),('12', 'Araucanía'),('13', 'Los Lagos')),label="Región")
    ciudad=forms.ChoiceField(choices=(('1', 'Santiago',),),label="Ciudad")
    vivienda=forms.ChoiceField(choices=(('Casa con Patio Grande', 'Casa con Patio Grande'),('Casa con Patio Pequeño', 'Casa con Patio Pequeño'),('Casa sin Patio', 'Casa sin Patio'),('Departamento', 'Departamento')),label="Vivienda")
    rol=forms.ChoiceField(choices=(('Normal', 'Normal'),('Admin','Admin'),),label="Rol del Usuario")






class RegUsuario(forms.Form):
    correo=forms.EmailField(widget=forms.EmailInput(),label="Email")
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellido=forms.CharField(widget=forms.TextInput(),label="Apellido")
    fecha=forms.DateField(widget=forms.SelectDateWidget(years=range(1900,2000)),label="Fecha de Nacimiento")
    region=forms.ChoiceField(choices=(('1', 'Arica'),('2', 'Tarapacá'),('3', 'Antofagasta'),('4', 'Atacama'),('5', 'Coquimbo'),('6', 'Valparaíso'),('7', 'Región Metropolitana'),('8', 'Bernardo OHiggins'),('9', 'Maule'),('10', 'Ñuble'),('11', 'Biobío'),('12', 'Araucanía'),('13', 'Los Lagos'),),label="Región")
    ciudad=forms.ChoiceField(choices=(('1', 'Santiago',),),label="Ciudad")
    vivienda=forms.ChoiceField(choices=(('Casa con Patio Grande', 'Casa con Patio Grande'),('Casa con Patio Pequeño', 'Casa con Patio Pequeño'),('Casa sin Patio', 'Casa sin Patio'),('Departamento', 'Departamento')),label="Vivienda")

class LoginFormulario(forms.Form):
    usr=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    passwd=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")


class RestablecerPasswordForm(forms.Form):
    nuevapass=forms.CharField(widget=forms.PasswordInput(),label="Nueva Password")
    nuevapasscheck=forms.CharField(widget=forms.PasswordInput(),label="Repita la nueva Password")


class RestablecerPasswordMail(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Usuario")

class AgregarMascota(forms.Form):
    pic=forms.ImageField(label="Imagen")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre")
    raza=forms.CharField(widget=forms.TextInput(),label="Raza")
    descripcion=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estado=forms.ChoiceField(choices=(('Rescatado', 'Rescatado'),('Disponible', 'Disponible'),('Adoptado', 'Adoptado')),label="Estado")
