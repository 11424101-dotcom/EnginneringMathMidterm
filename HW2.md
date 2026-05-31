#  Problem


Find the Fourier Series of

$$f(x)=x+\pi,\qquad -\pi\le x\le \pi$$

---


# Step 1: Fourier Series Formula


The Fourier Series with period \(2\pi\) is:

$$
f(x)
=
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\left(
a_n\cos nx+b_n\sin nx
\right)
$$



Where

$$
a_0
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\,dx
$$

$$
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\cos(nx)\,dx
$$

$$
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(nx)\,dx
$$

---


# Step 2: Find the Constant Term \(a_0\)



Substitute \(f(x)=x+\pi\)

$$
a_0
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\,dx
$$

$$
=
\frac{1}{\pi}
\left[
\frac{x^2}{2}
+\pi x
\right]_{-\pi}^{\pi}
$$

$$
=
\frac{1}{\pi}
\left(
2\pi^2
\right)
$$

$$
=2\pi
$$



Therefore

$$
\frac{a_0}{2}
=
\pi
$$

---


# Step 3: Find the Cosine Coefficient \(a_n\)

$$
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\cos(nx)\,dx
$$



Split into two integrals

$$
a_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\cos(nx)\,dx
+
\frac{1}{\pi}
\int_{-\pi}^{\pi}
\pi\cos(nx)\,dx
$$




Because

- \(x\) Odd Function
- \(\cos(nx)\) Even Function



Thus

$$
x\cos(nx)
$$

Odd Function

$$
\int_{-\pi}^{\pi}
x\cos(nx)\,dx
=
0
$$

###  Second Integral

$$
\int_{-\pi}^{\pi}
\cos(nx)\,dx
=
0
$$


Therefore

$$
a_n=0
$$

---


# Step 4: Find the Sine Coefficient \(b_n\)

$$
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
(x+\pi)\sin(nx)\,dx
$$


Split into two integrals

$$
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\sin(nx)\,dx
+
\frac{1}{\pi}
\int_{-\pi}^{\pi}
\pi\sin(nx)\,dx
$$

###  Second Integral

$$
\int_{-\pi}^{\pi}
\sin(nx)\,dx
=
0
$$



Therefore

$$
b_n
=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
x\sin(nx)\,dx
$$

---

## Using the Even Function Property



Because

- \(x\) Odd Function
- \(\sin(nx)\) Odd Function



Thus

$$
x\sin(nx)
$$

Even Function

$$
b_n
=
\frac{2}{\pi}
\int_0^{\pi}
x\sin(nx)\,dx
$$

---

## Integration by Parts


Let

$$
u=x
$$

$$
dv=\sin(nx)\,dx
$$


Then

$$
du=dx
$$

$$
v=-\frac{\cos(nx)}{n}
$$


Apply Integration by Parts Formula

$$
\int u\,dv
=
uv-\int v\,du
$$


We obtain

$$
\int x\sin(nx)\,dx
=
-\frac{x\cos(nx)}{n}
+
\frac{\sin(nx)}{n^2}
$$


Substitute the limits

$$
\int_0^\pi
x\sin(nx)\,dx
=
\left[
-\frac{x\cos(nx)}{n}
+
\frac{\sin(nx)}{n^2}
\right]_0^\pi
$$

$$
=
-\frac{\pi\cos(n\pi)}{n}
$$


Because

$$
\cos(n\pi)
=
(-1)^n
$$


Thus

$$
\int_0^\pi
x\sin(nx)\,dx
=
-\frac{\pi(-1)^n}{n}
$$


Therefore

$$
b_n
=
\frac{2}{\pi}
\left(
-\frac{\pi(-1)^n}{n}
\right)
$$

$$
=
\frac{2(-1)^{n+1}}{n}
$$

---

# Step 5: Substitute into the Fourier Series



Since

$$
a_0=2\pi
$$

$$
a_n=0
$$

$$
b_n
=
\frac{2(-1)^{n+1}}{n}
$$



Substitute into the formula

$$
f(x)
=
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
(a_n\cos nx+b_n\sin nx)
$$



We obtain

$$
f(x)
=
\pi
+
\sum_{n=1}^{\infty}
\frac{2(-1)^{n+1}}{n}
\sin(nx)
$$

---

# Final Answer

$$
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
$$


Expanded form

$$
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
$$

$$
-\pi<x<\pi
$$