# (5) Solve by Inverse Laplace Transform

Knowing：

```math
F(s)=\frac{1-e^{-3s}}{s(s+4)}
```

---

## Step 1: Separate into Two Parts

Linearity Property

```math
F(s)
=
\frac{1}{s(s+4)}
-
e^{-3s}\frac{1}{s(s+4)}
```

define

```math
G(s)=\frac{1}{s(s+4)}
```

than

```math
F(s)=G(s)-e^{-3s}G(s)
```

---

## Step 2: Partial Fraction Expansion

```math
\frac{1}{s(s+4)}
=
\frac{A}{s}
+
\frac{B}{s+4}
```

Both sides ride together \(s(s+4)\)

```math
1=A(s+4)+Bs
```

define \(s=0\)

```math
1=4A
```

```math
A=\frac14
```

define \(s=-4\)

```math
1=-4B
```

```math
B=-\frac14
```

than

```math
G(s)
=
\frac14\left(\frac1s-\frac1{s+4}\right)
```
---

## Step 3: Apply Inverse Laplace Transform

Basic Formula

```math
\mathcal{L}^{-1}
\left\{
\frac1s
\right\}
=1
```

```math
\mathcal{L}^{-1}
\left\{
\frac1{s+a}
\right\}
=e^{-at}
```

than

```math
g(t)
=
\mathcal{L}^{-1}\{G(s)\}
=
\frac14
\left(
1-e^{-4t}
\right)
```

---

## Step 4: Use the Shifting Theorem

Second Shifting Theorem

```math
\mathcal{L}^{-1}
\{e^{-as}G(s)\}
=
u(t-a)\,g(t-a)
```

＝ \(u(t-a)\)

Unit Step Function

define a=3

```math
\mathcal{L}^{-1}
\left\{
e^{-3s}G(s)
\right\}
=
u(t-3)
\frac14
\left(
1-e^{-4(t-3)}
\right)
```

---

## Step 5: Final Answer

```math
f(t)
=
\frac14(1-e^{-4t})
-
\frac14\,u(t-3)
\left(
1-e^{-4(t-3)}
\right)
```

---

## Answer

```math
\boxed{
f(t)
=
\frac14(1-e^{-4t})
-\frac14\,u(t-3)
\left(1-e^{-4(t-3)}\right)
}
```

```math
u(t-3)
=
\begin{cases}
0, & t<3 \\
1, & t\ge 3
\end{cases}
```

Unit Step Function