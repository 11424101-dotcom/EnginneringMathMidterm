#  Problem


Find the Fourier Series of

```math
f(x)=x+\pi,\qquad -\pi\le x\le \pi
```
---


# Step 1: Fourier Series Formula


The Fourier Series with period $$\(2\pi\)$$ is:

```math
f(x)
=
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\left(
a_n\cos nx+b_n\sin nx
\right)
```



Where

```math
a_0
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\,dx
```

```math
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\cos(nx)\,dx
```

```math
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(nx)\,dx
```

---


# Step 2: Find the Constant Term $$\(a_0\)$$



Substitute $$\(f(x)=x+\pi\)$$

```math
a_0
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\,dx
```

```math
=
\frac{1}{\pi}
\left[
\frac{x^2}{2}
+\pi x
\right]_{-\pi}^{\pi}
```

```math
=
\frac{1}{\pi}
\left(
2\pi^2
\right)


=2\pi

```


Therefore

```math
\frac{a_0}{2}
=
\pi
```

---


# Step 3: Find the Cosine Coefficient \(a_n\)

```math
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\cos(nx)\,dx
```



Split into two integrals

```math
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\cos(nx)\,dx
+
\frac{1}{\pi}
\int_{-\pi}^{\pi}
\pi\cos(nx)\,dx

```



Because
```math
- \(x\) Odd Function
- \(\cos(nx)\) Even Function
```


Thus


$$x\cos(nx)$$


Odd Function

```math
\int_{-\pi}^{\pi}
x\cos(nx)\,dx
=
0
```


###  Second Integral

```math
\int_{-\pi}^{\pi}
\cos(nx)\,dx
=
0
```


Therefore


$$a_n=0$$


---


# Step 4: Find the Sine Coefficient $$\(b_n\)$$

```math
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\sin(nx)\,dx
```


Split into two integrals

```math
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\sin(nx)\,dx
+
\frac{1}{\pi}
\int_{-\pi}^{\pi}
\pi\sin(nx)\,dx
```

###  Second Integral

```math
\int_{-\pi}^{\pi}
\sin(nx)\,dx
=
0
```

Therefore

```math
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\sin(nx)\,dx
```

---

## Using the Even Function Property

Because

- \(x\) Odd Function
- \(\sin(nx)\) Odd Function

Thus

```math
x\sin(nx)
```

Even Function

```math
b_n
=
\frac{2}{\pi}
\int_0^{\pi}
x\sin(nx)\,dx
```

---

## Integration by Parts

Let

```math
u=x
```

```math
dv=\sin(nx)\,dx
```

Then

```math
du=dx
```

```math
v=-\frac{\cos(nx)}{n}
```

Apply Integration by Parts Formula

```math
\int u\,dv
=
uv-\int v\,du
```

We obtain

```math
\int x\sin(nx)\,dx
=
-\frac{x\cos(nx)}{n}
+
\frac{\sin(nx)}{n^2}
```

Substitute the limits

```math
\int_0^\pi
x\sin(nx)\,dx
=
\left[
-\frac{x\cos(nx)}{n}
+
\frac{\sin(nx)}{n^2}
\right]_0^\pi
```
```math
=
-\frac{\pi\cos(n\pi)}{n}
```

Because

```math
\cos(n\pi)
=
(-1)^n
```

Thus

```math
\int_0^\pi
x\sin(nx)\,dx
=
-\frac{\pi(-1)^n}{n}
```

Therefore

```math
b_n
=
\frac{2}{\pi}
\left(
-\frac{\pi(-1)^n}{n}
\right)
```

```math
=
\frac{2(-1)^{n+1}}{n}
```

---

# Step 5: Substitute into the Fourier Series

Since

```math
a_0=2\pi
```

```math
a_n=0
```

```math
b_n
=
\frac{2(-1)^{n+1}}{n}
```

Substitute into the formula

```math
f(x)
=
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
(a_n\cos nx+b_n\sin nx)
```

We obtain

```math
f(x)
=
\pi
+
\sum_{n=1}^{\infty}
\frac{2(-1)^{n+1}}{n}
\sin(nx)
```

---

# Final Answer

```math
\boxed{
x+\pi
=
\pi
+
2
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n}
\sin(nx)
}
```

Expanded form

```math
\boxed{
x+\pi
=
\pi
+
2
\left(
\sin x
-\frac{\sin 2x}{2}
+\frac{\sin 3x}{3}
-\frac{\sin 4x}{4}
+\cdots
\right)
}
```

```math
-\pi<x<\pi
```