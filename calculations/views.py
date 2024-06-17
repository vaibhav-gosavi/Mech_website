import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, HeatTransferForm, HeatTransferForm1, HeatTransferForm2, HeatTransferForm3, HeatTransferForm4, HeatTransferForm5, HeatTransferForm6
from django.core.mail import send_mail
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from django.conf import settings
import io
import urllib
import base64
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def home(request):
    problems = [
        {
            'title': 'Problem -1 Composite wall with 3 layers in series',
            'description': 'Calculate temperature distribution and heat flux for a 3-layer composite wall.',
            'url_name': 'problem'
        },
        {
            'title': 'Problem -2 Composite wall with 3 layers in series',
            'description': 'Taking 3 different values of thermal conductivity for each of the 3 layers to obtain a superimposed graphs.',
            'url_name': 'problem_1'
        },
        {

            'title': 'Composite wall with parallel resistance to heat flow',
            'description': 'obtain the temperature distribution through the composite wall and calculate the convective as well as conductive heat transfer rates or heat flux. Plot the temperature distribution.',
            'url_name': 'problem_2'
        },
        {

            'title': 'Heat Transfer Calculation with Air Gap',
            'description': 'Calculate temperature distribution and heat flux for a 3-layer composite wall.',
            'url_name': 'problem_3'
        },
        {

            'title': 'Heat Transfer Calculation in a Cylinder',
            'description': 'Obtain the conduction heat transfer rate and the temperature distribution across the cross section of the cylinder',
            'url_name': 'problem_4'
        },
        {

            'title': 'Heat Transfer Calculation in Composite Cylinder',
            'description': 'Obtain the heat transfer rate and the temperature distribution/profile through the composite cylinder.',
            'url_name': 'problem_5'
        },
        {

            'title': 'Critical Thickness of Insulation Calculation',
            'description': 'Obtain the heat transfer rate and the temperature distribution/profile through the composite cylinder',
            'url_name': 'problem_6'
        }

        # Add more problems as needed
    ]
    return render(request, 'calculations/home.html', {'problems': problems})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Send the feedback via email
            send_mail(
                'New Problem Reported',
                f"Problem Title: {form.cleaned_data['problem_title']}\nDescription: {form.cleaned_data['description']}",
                settings.EMAIL_HOST_USER,  # From email
                settings.EMAIL_RECIPIENTS,  # To email
                fail_silently=False,
            )
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'calculations/feedback.html', {'form': form})

def thank_you_view(request):
    return render(request, 'calculations/thank_you.html')

@login_required(login_url='/login/')
def problems(request):
    return render(request,'calculations/problems.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'calculations/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'calculations/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'calculations/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def index(request):
    if request.method == 'POST':
        form = HeatTransferForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations(data)
            return render(request, 'calculations/result.html', context)
    else:
        form = HeatTransferForm()
    return render(request, 'calculations/index.html', {'form': form})


def perform_calculations(data):
    L1 = data['L1']
    L2 = data['L2']
    L3 = data['L3']
    k1 = data['k1']
    k2 = data['k2']
    k3 = data['k3']
    T0 = data['T0']
    h0 = data['h0']
    Tamb = data['Tamb']
    hamb = data['hamb']
    A = 1.0

    R_conv1 = 1 / (h0 * A)
    R1 = L1 / (k1 * A)
    R2 = L2 / (k2 * A)
    R3 = L3 / (k3 * A)
    R_conv2 = 1 / (hamb * A)

    R_total = R_conv1 + R1 + R2 + R3 + R_conv2

    Q = (T0 - Tamb) / R_total

    T1 = T0 - Q * R_conv1
    T2 = T1 - Q * R1
    T3 = T2 - Q * R2
    T4 = T3 - Q * R3

    Q_conv1 = h0 * A * (T0 - T1)
    Q_conv2 = hamb * A * (T4 - Tamb)

    context = {
        'Q': Q,
        'T1': T1,
        'T2': T2,
        'T3': T3,
        'T4': T4,
        'Q_conv1': Q_conv1,
        'Q_conv2': Q_conv2,
        'R_total': R_total,
        'R_conv1': R_conv1,
        'R1': R1,
        'R2': R2,
        'R3': R3,
        'R_conv2': R_conv2,
        'x': [-0.01, 0, L1, L1 + L2, L1 + L2 + L3, L1 + L2 + L3 + 0.1],
        'T': [T0, T1, T2, T3, T4, Tamb],
    }
    return context


def index_1(request):
    if request.method == 'POST':
        form = HeatTransferForm1(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_1(data)
            return render(request, 'calculations/result1.html', context)
    else:
        form = HeatTransferForm1()
    return render(request, 'calculations/index1.html', {'form': form})


def perform_calculations_1(data):
    L1 = data['L1']
    L2 = data['L2']
    L3 = data['L3']
    k1 = data['k1']
    k2 = data['k2']
    k3 = data['k3']
    T0 = data['T0']
    h0 = data['h0']
    Tamb = data['Tamb']
    hamb = data['hamb']
    A = 1.0

    R_conv1 = 1 / (h0 * A)
    R1 = L1 / (k1 * A)
    R2 = L2 / (k2 * A)
    R3 = L3 / (k3 * A)
    R_conv2 = 1 / (hamb * A)

    R_total = R_conv1 + R1 + R2 + R3 + R_conv2

    Q = (T0 - Tamb) / R_total

    T1 = T0 - Q * R_conv1
    T2 = T1 - Q * R1
    T3 = T2 - Q * R2
    T4 = T3 - Q * R3

    Q_conv1 = h0 * A * (T0 - T1)
    Q_conv2 = hamb * A * (T4 - Tamb)

    x = [-0.01, 0, L1, L1 + L2, L1 + L2 + L3, L1 + L2 + L3 + 0.1]
    T = [T0, T1, T2, T3, T4, Tamb]

    # Plot the temperature distribution
    plt.plot(x, T, marker='o', label='Temperature Distribution')
    plt.xlabel('Position (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution through the Composite Wall')
    plt.legend()
    plt.grid(True)

    # Save plot to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to be displayed in HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'Q': Q,
        'T1': T1,
        'T2': T2,
        'T3': T3,
        'T4': T4,
        'Q_conv1': Q_conv1,
        'Q_conv2': Q_conv2,
        'R_total': R_total,
        'R_conv1': R_conv1,
        'R1': R1,
        'R2': R2,
        'R3': R3,
        'R_conv2': R_conv2,
        'x': x,
        'T': T,
        'graphic': graphic,
    }
    return context


def index_2(request):
    if request.method == 'POST':
        form = HeatTransferForm2(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_2(data)
            return render(request, 'calculations/result2.html', context)
    else:
        form = HeatTransferForm2()
    return render(request, 'calculations/index2.html', {'form': form})


def perform_calculations_2(data):
    T0 = data['T0']
    Tamb = data['Tamb']
    hi = data['hi']
    hamb = data['hamb']
    kA = data['kA']
    kB = data['kB']
    kC = data['kC']
    kD = data['kD']
    L1 = data['L1']
    L2 = data['L2']
    L3 = data['L3']
    A = 1.0  # Assuming area is 1 m^2 for simplicity

    # Thermal resistances
    R_conv_hot = 1 / (hi * A)  # Convective resistance on the hot side
    R_A = L1 / (kA * A)        # Conductive resistance of layer A
    R_B = L2 / (kB * A)        # Conductive resistance of layer B
    R_C = L2 / (kC * A)        # Conductive resistance of layer C
    R_D = L3 / (kD * A)        # Conductive resistance of layer D
    R_conv_amb = 1 / (hamb * A)  # Convective resistance on the ambient side

    # Total thermal resistance for each parallel path
    R_parallel_2 = 1 / (1 / R_B + 1 / R_C)
    R_path = R_A + R_parallel_2 + R_D

    # Overall thermal resistance
    R_total = R_conv_hot + R_path + R_conv_amb

    # Heat transfer rate (Q)
    Q = (T0 - Tamb) / R_total

    # Interface temperatures
    T1 = T0 - Q * R_conv_hot
    T2 = T1 - Q * R_A
    T3 = T2 - Q * R_parallel_2
    T4 = T3 - Q * R_D

    # Plotting temperature distribution
    x = [-0.01, 0, L1, L1 + L2, L1 + L2 + L3, L1 + L2 + L3 + 0.1]
    T = [T0, T1, T2, T3, T4, Tamb]

    plt.plot(x, T, marker='o')
    plt.xlabel('Distance (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution Across Composite Wall')
    plt.grid(True)

    # Save plot to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    # Encode the image to be displayed in HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'Q': Q,
        'T1': T1,
        'T2': T2,
        'T3': T3,
        'T4': T4,
        'R_conv_hot': R_conv_hot,
        'R_A': R_A,
        'R_B': R_B,
        'R_C': R_C,
        'R_D': R_D,
        'R_conv_amb': R_conv_amb,
        'R_parallel_2': R_parallel_2,
        'R_total': R_total,
        'graphic': graphic,
        'x': json.dumps(x),  # Serialize to JSON
        'T': json.dumps(T)   # Serialize to JSON
    }
    return context


def index_3(request):
    if request.method == 'POST':
        form = HeatTransferForm3(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_3(data)
            return render(request, 'calculations/result3.html', context)
    else:
        form = HeatTransferForm3()
    return render(request, 'calculations/index3.html', {'form': form})


def perform_calculations_3(data):
    T0 = data['T0']
    Tamb = data['Tamb']
    hi = data['hi']
    hamb = data['hamb']
    kA = data['kA']
    kB = data['kB']
    kC = data['kC']
    L1 = data['L1']
    L2 = data['L2']
    L3 = data['L3']
    R_air_gap = data['R_air_gap']
    A = 1.0  # Assuming area is 1 m^2 for simplicity

    # Thermal resistances
    R_conv_hot = 1 / (hi * A)  # Convective resistance on the hot side
    R_A = L1 / (kA * A)        # Conductive resistance of layer A
    R_B = L2 / (kB * A)        # Conductive resistance of layer B
    R_C = L3 / (kC * A)        # Conductive resistance of layer C
    R_conv_amb = 1 / (hamb * A)  # Convective resistance on the ambient side

    # Total thermal resistance
    R_total = R_conv_hot + R_A + R_air_gap + R_B + R_C + R_conv_amb

    # Heat transfer rate (Q)
    Q = (T0 - Tamb) / R_total

    # Interface temperatures
    T1 = T0 - Q * R_conv_hot
    T2 = T1 - Q * R_A
    T2_prime = T2 - Q * R_air_gap
    T3 = T2_prime - Q * R_B
    T4 = T3 - Q * R_C

    # Plotting temperature distribution
    x = [-0.01, 0, L1, L1, L1 + L2, L1 + L2 + L3, L1 + L2 + L3 + 0.1]
    T = [T0, T1, T2, T2_prime, T3, T4, Tamb]

    plt.plot(x, T, marker='o')
    plt.xlabel('Distance (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution Across Composite Wall with Air Gap')
    plt.grid(True)

    # Save plot to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to be displayed in HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'Q': Q,
        'T1': T1,
        'T2': T2,
        'T2_prime': T2_prime,
        'T3': T3,
        'T4': T4,
        'R_conv_hot': R_conv_hot,
        'R_A': R_A,
        'R_air_gap': R_air_gap,
        'R_B': R_B,
        'R_C': R_C,
        'R_conv_amb': R_conv_amb,
        'R_total': R_total,
        'graphic': graphic,
    }
    return context


def index_4(request):
    if request.method == 'POST':
        form = HeatTransferForm4(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_4(data)
            return render(request, 'calculations/result4.html', context)
    else:
        form = HeatTransferForm4()
    return render(request, 'calculations/index4.html', {'form': form})


def perform_calculations_4(data):
    # Length of the cylinder, m (arbitrary since it cancels out in 1D problem)
    L = 1.0
    r1 = data['r1']  # Inner radius, m
    r2 = data['r2']  # Outer radius, m
    k = data['k']  # Thermal conductivity, W/mK
    h_gas = data['h_gas']  # Heat transfer coefficient of the hot gas, W/m^2K
    T_gas = data['T_gas']  # Temperature of the hot gas, °C
    # Heat transfer coefficient of the ambient air, W/m^2K
    h_ambient = data['h_ambient']
    T0 = data['T0']  # Ambient temperature, °C
    T_inner = data['T_inner']  # Inner surface temperature, °C
    T_outer = data['T_outer']  # Inner surface temperature, °C

    # Heat flux at the inner surface
    R2 = 1 / (h_gas * 2 * np.pi * r1 * L)
    q_inner = (T_gas - T_inner) / R2

    # Solve for temperature distribution coefficients
    A = (T_inner - T_outer) / np.log(r1 / r2)
    C = (T_inner - T_outer) * np.log(r1) / np.log(r1 / r2)
    B = T_inner - C

    # Temperature distribution function
    def temperature_distribution(r):
        return A * np.log(r) + B

    # Temperature at the outer surface
    T_outer = temperature_distribution(r2)

    # Conduction heat flux
    R1 = np.log(r2 / r1) / (2 * np.pi * k * L)
    q_cond = (T_inner - T_outer) / R1

    # Heat flux expelled at the outer surface due to convection
    q_conv = h_ambient * (T_outer - T0)

    # Radial points for plotting
    r = np.linspace(r1, r2, 100)
    T = temperature_distribution(r)

    # Plotting the temperature distribution
    plt.plot(r, T, label='Temperature Distribution')
    plt.xlabel('Radius (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution along the Thickness of the Cylinder')
    plt.legend()
    plt.grid(True)

    # Save plot to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to be displayed in HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'T_outer': T_outer,
        'q_inner': q_inner,
        'q_cond': q_cond,
        'q_conv': q_conv,
        'graphic': graphic,
    }
    return context


def index_5(request):
    if request.method == 'POST':
        form = HeatTransferForm5(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_5(data)
            return render(request, 'calculations/result5.html', context)
    else:
        form = HeatTransferForm5()
    return render(request, 'calculations/index5.html', {'form': form})


def perform_calculations_5(data):
    r1 = data['r1']
    r2 = data['r2']
    r3 = data['r3']
    r4 = data['r4']
    k1 = data['k1']
    k2 = data['k2']
    k3 = data['k3']
    T0 = data['T0']
    h0 = data['h0']
    T_infinity = data['T_infinity']
    h_infinity = data['h_infinity']
    L = 1.0  # Length of the cylinder (arbitrary for 1D analysis)

    # Thermal resistances
    R_conv_inner = 1 / (h0 * 2 * np.pi * r1 * L)
    R1 = np.log(r2 / r1) / (2 * np.pi * k1 * L)
    R2 = np.log(r3 / r2) / (2 * np.pi * k2 * L)
    R3 = np.log(r4 / r3) / (2 * np.pi * k3 * L)
    R_conv_outer = 1 / (h_infinity * 2 * np.pi * r4 * L)

    # Total thermal resistance
    R_total = R_conv_inner + R1 + R2 + R3 + R_conv_outer

    # Heat transfer rate
    Q = (T0 - T_infinity) / R_total

    # Interfacial temperatures
    T2 = T0 - Q * (R_conv_inner + R1)
    T3 = T0 - Q * (R_conv_inner + R1 + R2)
    T4 = T0 - Q * (R_conv_inner + R1 + R2 + R3)

    # Temperature distribution functions
    def T1_dist(r):
        return T0 - (Q * R_conv_inner) - (Q / (2 * np.pi * k1 * L)) * np.log(r / r1)

    def T2_dist(r):
        return T2 - (Q / (2 * np.pi * k2 * L)) * np.log(r / r2)

    def T3_dist(r):
        return T3 - (Q / (2 * np.pi * k3 * L)) * np.log(r / r3)

    # Radial points for plotting
    r1_points = np.linspace(r1, r2, 100)
    r2_points = np.linspace(r2, r3, 100)
    r3_points = np.linspace(r3, r4, 100)

    T1_points = T1_dist(r1_points)
    T2_points = T2_dist(r2_points)
    T3_points = T3_dist(r3_points)

    # Plotting the temperature distribution
    plt.plot(r1_points, T1_points, label='Layer 1 Temperature')
    plt.plot(r2_points, T2_points, label='Layer 2 Temperature')
    plt.plot(r3_points, T3_points, label='Layer 3 Temperature')
    plt.xlabel('Radius (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution in Composite Cylinder')
    plt.legend()
    plt.grid(True)

    # Save plot to a string buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to be displayed in HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'Q': Q,
        'T2': T2,
        'T3': T3,
        'T4': T4,
        'graphic': graphic,
    }
    return context


def index_6(request):
    if request.method == 'POST':
        form = HeatTransferForm6(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context = perform_calculations_6(data)
            return render(request, 'calculations/result6.html', context)
    else:
        form = HeatTransferForm6()
    return render(request, 'calculations/index6.html', {'form': form})


def composite_cylinder(r1: float, r2: float, r3: float, r4: float, k1: float, k2: float, k3: float, T0: float, h0: float, T_infinity: float, h_infinity: float, r_ins: float = None, k_ins: float = None):
    L = 1.0  # Length of the cylinder (arbitrary for 1D analysis)

    if r1 <= 0 or r2 <= r1 or r3 <= r2 or r4 <= r3:
        raise ValueError("Radii must satisfy 0 < r1 < r2 < r3 < r4")

    if any(k <= 0 for k in [k1, k2, k3]):
        raise ValueError("Thermal conductivities must be positive")

    if h0 <= 0 or h_infinity <= 0:
        raise ValueError("Heat transfer coefficients must be positive")

    # Thermal resistances
    R_conv_inner = 1 / (h0 * 2 * np.pi * r1 * L)
    R1 = np.log(r2 / r1) / (2 * np.pi * k1 * L)
    R2 = np.log(r3 / r2) / (2 * np.pi * k2 * L)
    R3 = np.log(r4 / r3) / (2 * np.pi * k3 * L)
    R_conv_outer = 1 / (h_infinity * 2 * np.pi * r4 * L)

    if r_ins and k_ins:
        if r_ins <= r4:
            raise ValueError("Insulation radius must be greater than r4")
        if k_ins <= 0:
            raise ValueError(
                "Insulation thermal conductivity must be positive")

        R_ins = np.log(r_ins / r4) / (2 * np.pi * k_ins * L)
        R_conv_outer = 1 / (h_infinity * 2 * np.pi * r_ins * L)
        R_total = R_conv_inner + R1 + R2 + R3 + R_ins + R_conv_outer
    else:
        R_total = R_conv_inner + R1 + R2 + R3 + R_conv_outer

    # Heat transfer rate
    Q = (T0 - T_infinity) / R_total

    # Interfacial temperatures
    T2 = T0 - Q * (R_conv_inner + R1)
    T3 = T0 - Q * (R_conv_inner + R1 + R2)
    T4 = T0 - Q * (R_conv_inner + R1 + R2 + R3)

    if r_ins and k_ins:
        T5 = T4 - Q * R_ins
        return Q, T2, T3, T4, T5

    return Q, T2, T3, T4


def find_critical_thickness(r1: float, r2: float, r3: float, r4: float, k1: float, k2: float, k3: float, T0: float, h0: float, T_infinity: float, h_infinity: float, k_ins: float):
    Q_original, T2_original, T3_original, T4_original = composite_cylinder(
        r1, r2, r3, r4, k1, k2, k3, T0, h0, T_infinity, h_infinity)

    Q_target = 0.05 * Q_original

    thickness_guess = 0.01
    r_ins = r4 + thickness_guess

    while True:
        Q_new, T2_new, T3_new, T4_new, _ = composite_cylinder(
            r1, r2, r3, r4, k1, k2, k3, T0, h0, T_infinity, h_infinity, r_ins, k_ins)
        if Q_new <= Q_target:
            break
        thickness_guess += 0.001
        r_ins = r4 + thickness_guess

    return thickness_guess, Q_new, T2_original, T3_original, T4_original


def perform_calculations_6(data):
    r1 = data['r1']
    r2 = data['r2']
    r3 = data['r3']
    r4 = data['r4']
    k1 = data['k1']
    k2 = data['k2']
    k3 = data['k3']
    T0 = data['T0']
    h0 = data['h0']
    T_infinity = data['T_infinity']
    h_infinity = data['h_infinity']
    k_ins = data['k_ins']

    # Find critical thickness
    thickness, Q_new, T2_original, T3_original, T4_original = find_critical_thickness(
        r1, r2, r3, r4, k1, k2, k3, T0, h0, T_infinity, h_infinity, k_ins)

    # Original heat flux without insulation
    Q_original = composite_cylinder(
        r1, r2, r3, r4, k1, k2, k3, T0, h0, T_infinity, h_infinity)[0]

    context = {
        'thickness': thickness,
        'Q_new': Q_new,
        'Q_original': Q_original,
        'T2_original': T2_original,
        'T3_original': T3_original,
        'T4_original': T4_original,
    }
    return context
