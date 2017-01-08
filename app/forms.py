from django import forms

class InsertarRestaurante(forms.Form):
    id_restaurante = forms.IntegerField(label="ID Restaurante", required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce el ID del restaurante'}))
    nombre = forms.CharField(label="Nombre", max_length=256, required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre del restaurante'}))
    edificio = forms.IntegerField(label="Edificio", required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce el numero del edificio del restaurante'}))
    calle = forms.CharField(label="Calle", max_length=256, required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce la calle del restaurante'}))
    codigo_postal = forms.IntegerField(label="Codigo postal", required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce codigo postal del restaurante'}))
    barrio = forms.CharField(label="Barrio", max_length=256, required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce el barrio del restaurante'}))
    tipo_cocina = forms.CharField(label="Tipo cocina", max_length=256, required=True, widget=forms.TextInput(attrs={'placeholder': 'Introduce el tipo de cocina del restaurante'}))
    calificacion = forms.CharField(label="Calificacion", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la calificacion del restaurante'}))
    puntuacion = forms.IntegerField(label="Puntuacion", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la puntuacion del restaurante'}))

class ModificarRestaurante(forms.Form):
    id_restaurante = forms.CharField(label="ID Restaurante", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el ID del restaurante', 'readonly':'readonly'}))
    nombre = forms.CharField(label="Nombre", required=False, max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre del restaurante', 'readonly':'readonly'}))
    edificio = forms.IntegerField(label="Edificio", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el numero del edificio del restaurante'}))
    calle = forms.CharField(label="Calle", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la calle del restaurante'}))
    codigo_postal = forms.IntegerField(label="Codigo postal", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce codigo postal del restaurante'}))
    barrio = forms.CharField(label="Barrio", required=False, max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Introduce el barrio del restaurante'}))
    tipo_cocina = forms.CharField(label="Tipo cocina", required=False, max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Introduce el tipo de cocina del restaurante'}))

class BuscarRestaurante(forms.Form):
    id_restaurante = forms.CharField(label="ID Restaurante", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre del restaurante'}))
    nombre = forms.CharField(label="Nombre", max_length=256, required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre del restaurante'}))
    barrio = forms.CharField(label="Barrio", max_length=256, required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el barrio del restaurante'}))
    tipo_cocina = forms.CharField(label="Tipo cocina", max_length=256, required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce el tipo de cocina del restaurante'}))
    calle = forms.CharField(label="Calle", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la calle del restaurante'}))
    codigo_postal = forms.IntegerField(label="Codigo postal", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce codigo postal del restaurante'}))
    calificacion = forms.CharField(label="Calificacion", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la calificacion del restaurante'}))
    puntuacion = forms.IntegerField(label="Puntuacion", required=False, widget=forms.TextInput(attrs={'placeholder': 'Introduce la puntuacion del restaurante'}))
