from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'w-full px-4 py-2 mt-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            field.widget.attrs['placeholder'] = field.label


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'w-full px-4 py-2 mt-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            field.widget.attrs['placeholder'] = field.label

            if field_name == 'password':
                field.widget.attrs['class'] += ' bg-gray-100'
            else:
                field.widget.attrs['class'] += ' bg-white'

            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['aria-label'] = field.label

class HeatTransferForm(forms.Form):
    L1 = forms.FloatField(label='Thickness of layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L2 = forms.FloatField(label='Thickness of layer 2 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L3 = forms.FloatField(label='Thickness of layer 3 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k1 = forms.FloatField(label='Thermal conductivity of layer 1 (W/m.K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k2 = forms.FloatField(label='Thermal conductivity of layer 2 (W/m.K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k3 = forms.FloatField(label='Thermal conductivity of layer 3 (W/m.K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T0 = forms.FloatField(label='Temperature of the gas in contact with layer 1 (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h0 = forms.FloatField(label='Heat transfer coefficient of the gas (W/m^2.K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    Tamb = forms.FloatField(label='Ambient temperature next to layer 3 (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hamb = forms.FloatField(label='Heat transfer coefficient of the ambient (W/m^2.K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm1(forms.Form):
    L1 = forms.FloatField(label='Thickness of Layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L2 = forms.FloatField(label='Thickness of Layer 2 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L3 = forms.FloatField(label='Thickness of Layer 3 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k1 = forms.FloatField(label='Thermal Conductivity of Layer 1 (W/m·K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k2 = forms.FloatField(label='Thermal Conductivity of Layer 2 (W/m·K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k3 = forms.FloatField(label='Thermal Conductivity of Layer 3 (W/m·K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T0 = forms.FloatField(label='Surface Temperature of Layer 1 (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h0 = forms.FloatField(label='Heat Transfer Coefficient of Gas (W/m²·K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    Tamb = forms.FloatField(label='Ambient Temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hamb = forms.FloatField(label='Heat Transfer Coefficient of Ambient (W/m²·K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm2(forms.Form):
    T0 = forms.FloatField(label='Temperature of the hot fluid (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    Tamb = forms.FloatField(label='Ambient temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hi = forms.FloatField(label='Heat transfer coefficient of the hot fluid (W/m²°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hamb = forms.FloatField(label='Heat transfer coefficient of the ambient (W/m²°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kA = forms.FloatField(label='Thermal conductivity of layer A (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kB = forms.FloatField(label='Thermal conductivity of layer B (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kC = forms.FloatField(label='Thermal conductivity of layer C (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kD = forms.FloatField(label='Thermal conductivity of layer D (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L1 = forms.FloatField(label='Thickness of layer A (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L2 = forms.FloatField(label='Thickness of layers B and C (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L3 = forms.FloatField(label='Thickness of layer D (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm3(forms.Form):
    T0 = forms.FloatField(label='Temperature of the hot fluid (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    Tamb = forms.FloatField(label='Ambient temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hi = forms.FloatField(label='Heat transfer coefficient of the hot fluid (W/m²°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    hamb = forms.FloatField(label='Heat transfer coefficient of the ambient (W/m²°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kA = forms.FloatField(label='Thermal conductivity of layer A (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kB = forms.FloatField(label='Thermal conductivity of layer B (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    kC = forms.FloatField(label='Thermal conductivity of layer C (W/m°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L1 = forms.FloatField(label='Thickness of layer A (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L2 = forms.FloatField(label='Thickness of layer B (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    L3 = forms.FloatField(label='Thickness of layer C (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    R_air_gap = forms.FloatField(label='Thermal resistance of the air gap (°C/W)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm4(forms.Form):
    r1 = forms.FloatField(label='Inner radius (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r2 = forms.FloatField(label='Outer radius (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k = forms.FloatField(label='Thermal conductivity (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h_gas = forms.FloatField(label='Heat transfer coefficient of the hot gas (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T_gas = forms.FloatField(label='Temperature of the hot gas (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h_ambient = forms.FloatField(label='Heat transfer coefficient of the ambient air (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T0 = forms.FloatField(label='Ambient temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T_inner = forms.FloatField(label='Inner surface temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T_outer = forms.FloatField(label='Outer surface temperature (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm5(forms.Form):
    r1 = forms.FloatField(label='Inner radius of layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r2 = forms.FloatField(label='Outer radius of layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r3 = forms.FloatField(label='Outer radius of layer 2 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r4 = forms.FloatField(label='Outer radius of layer 3 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k1 = forms.FloatField(label='Thermal conductivity of layer 1 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k2 = forms.FloatField(label='Thermal conductivity of layer 2 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k3 = forms.FloatField(label='Thermal conductivity of layer 3 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T0 = forms.FloatField(label='Temperature of the fluid inside the cylinder (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h0 = forms.FloatField(label='Heat transfer coefficient of the fluid inside the cylinder (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T_infinity = forms.FloatField(label='Ambient temperature outside the cylinder (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h_infinity = forms.FloatField(label='Heat transfer coefficient outside the cylinder (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class HeatTransferForm6(forms.Form):
    r1 = forms.FloatField(label='Inner radius of layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r2 = forms.FloatField(label='Outer radius of layer 1 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r3 = forms.FloatField(label='Outer radius of layer 2 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    r4 = forms.FloatField(label='Outer radius of layer 3 (m)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k1 = forms.FloatField(label='Thermal conductivity of layer 1 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k2 = forms.FloatField(label='Thermal conductivity of layer 2 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k3 = forms.FloatField(label='Thermal conductivity of layer 3 (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T0 = forms.FloatField(label='Temperature of the fluid inside the cylinder (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h0 = forms.FloatField(label='Heat transfer coefficient of the fluid inside the cylinder (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    T_infinity = forms.FloatField(label='Ambient temperature outside the cylinder (°C)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    h_infinity = forms.FloatField(label='Heat transfer coefficient outside the cylinder (W/m²K)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    k_ins = forms.FloatField(label='Thermal conductivity of the insulation material (W/mK)', widget=forms.NumberInput(attrs={
        'class': 'border border-blue-500 rounded p-2 mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
