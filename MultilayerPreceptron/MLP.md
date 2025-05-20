## For weights:

$$
E = \frac{1}{2}(a(z(w))-y)^2
$$

---

### In layer *L*:

The equation is:

$$
\frac{dE}{dw^{L}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{dw^{L}}
$$

The full derivative is:

$$
\frac{dE}{dw^{L}} =
a^{L} - y \times
a^{L} (1-a^{L}) \times
a^{L-1}
$$

---

### In layer *L-1*:

The equation is:

$$
\frac{dE}{dw^{L-1}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{da^{L-1}} \times
\frac{da^{L-1}}{dz^{L-1}} \times
\frac{dz^{L-1}}{dw^{L-1}}
$$

The full derivative is:

$$
\frac{dE}{dw^{L-1}} =
a^{L} - y \times
a^{L} (1-a^{L}) \times
w^{L} \times
a^{L-1} (1-a^{L-1}) \times
a^{L-2}
$$

---

### In layer *L-2*:

The equation is:

$$
\frac{dE}{dw^{L-2}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{da^{L-1}} \times
\frac{da^{L-1}}{dz^{L-1}} \times
\frac{dz^{L-1}}{da^{L-2}} \times
\frac{da^{L-2}}{dz^{L-2}} \times
\frac{dz^{L-2}}{dw^{L-2}}
$$

The full derivative is:

$$
\frac{dE}{dw^{L-2}} =
a^{L} - y \times
a^{L} (1-a^{L}) \times
w^{L} \times
a^{L-1} (1-a^{L-1}) \times
w^{L-1} \times
a^{L-2} (1-a^{L-2}) \times
x^{L-2}
$$

---

## For biases:

The general equation is:

$$
E = \frac{1}{2}(a(z(b))-y)^2
$$

---

### In layer *L*:

The equation is:

$$
\frac{dE}{db^{L}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{db^{L}}
$$

The full derivative is:

$$
\frac{dE}{db^{L}} =
a^{L} - y \times
a^{L} (1-a^{L})
$$

---

### In layer *L-1*:

The equation is:

$$
\frac{dE}{db^{L-1}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{da^{L-1}} \times
\frac{da^{L-1}}{dz^{L-1}} \times
\frac{dz^{L-1}}{db^{L-1}}
$$

The full derivative is:

$$
\frac{dE}{db^{L-1}} =
a^{L} - y \times
a^{L} (1-a^{L}) \times
w^{L} \times
a^{L-1}(1-a^{L-1})
$$

---

### In layer *L-2*:

The equation is:

$$
\frac{dE}{db^{L-2}} =
\frac{dE}{da^{L}} \times
\frac{da^{L}}{dz^{L}} \times
\frac{dz^{L}}{da^{L-1}} \times
\frac{da^{L-1}}{dz^{L-1}} \times
\frac{dz^{L-1}}{da^{L-2}} \times
\frac{da^{L-2}}{dz^{L-2}} \times
\frac{dz^{L-2}}{db^{L-2}}
$$

The full derivative is:

$$
\frac{dE}{db^{L-2}} =
a^{L} - y \times
a^{L} (1-a^{L}) \times
w^{L} \times
a^{L-1}(1-a^{L-1}) \times
w^{L-1} \times
a^{L-2}(1-a^{L-2})
$$














