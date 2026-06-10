# Problem 2: Transient Response of a Series RLC Circuit


Given the parameters of the series RLC circuit:

```math
R=8\Omega,\quad L=1H,\quad C=0.25F
```

Initial Conditions:

```math
u_C(0)=0V
```

```math
i_L(0)=0A
```

Input Voltage:

```math
U_s=12V
```

Find the transient response of the capacitor voltage.

---

# Step 1: Establish the Differential Equation


Using Kirchhoff's Voltage Law:

```math
u_R(t)+u_L(t)+u_C(t)=U_s
```


Substitute the element equations:

```math
Ri(t)+L\frac{di(t)}{dt}+u_C(t)=12
```


Since

```math
i(t)=C\frac{du_C(t)}{dt}
```

```math
C=0.25
```

Therefore

```math
i(t)=0.25\frac{du_C(t)}{dt}
```

Substituting:

```math
8\left(0.25\frac{du_C}{dt}\right)
+\frac{d}{dt}\left(0.25\frac{du_C}{dt}\right)
+u_C=12
```


Simplify:

```math
2\frac{du_C}{dt}
+0.25\frac{d^2u_C}{dt^2}
+u_C
=12
```


Multiply both sides by 4:

```math
\frac{d^2u_C}{dt^2}
+8\frac{du_C}{dt}
+4u_C
=48
```

---

# Step 2: Apply Laplace Transform

From the initial conditions

```math
u_C(0)=0
```

```math
i(0)=0
```


We obtain

```math
u_C'(0)=0
```


Taking Laplace transforms:

```math
s^2U(s)+8sU(s)+4U(s)=\frac{48}{s}
```


Rearrange:

```math
U(s)
=
\frac{48}{s(s^2+8s+4)}
```

---

# Step 3: Partial Fraction Expansion

特徵方程：

Characteristic equation:

```math
s^2+8s+4
=
(s+4-2\sqrt3)(s+4+2\sqrt3)
```


Therefore

```math
U(s)
=
\frac{12}{s}
-\frac{12(s+4)}{(s+4)^2-12}
-\frac{48}{(s+4)^2-12}
```

---

# Step 4: Apply Inverse Laplace Transform


Using the formulas:

```math
\mathcal{L}^{-1}
\left\{
\frac{s+a}{(s+a)^2-b^2}
\right\}
=
e^{-at}\cosh(bt)
```

```math
\mathcal{L}^{-1}
\left\{
\frac{b}{(s+a)^2-b^2}
\right\}
=
e^{-at}\sinh(bt)
```


Where

```math
b=2\sqrt3
```

We obtain

```math
u_C(t)
=
12
-12e^{-4t}\cosh(2\sqrt3\,t)
-8\sqrt3\,e^{-4t}\sinh(2\sqrt3\,t)
```

---

# Final Answer

```math
\boxed{
u_C(t)
=
12
-12e^{-4t}\cosh(2\sqrt3\,t)
-8\sqrt3\,e^{-4t}\sinh(2\sqrt3\,t)
}
```

---

# Verification

```math
u_C(0)=0V
```

```math
\lim_{t\to\infty}u_C(t)=12V
```


This agrees with the physical behavior that the capacitor voltage eventually reaches the source voltage.