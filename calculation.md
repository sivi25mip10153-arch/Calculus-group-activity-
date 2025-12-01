# CALCULATIONS AND WORKING – GREEN'S THEOREM PROJECT

This document contains all handwritten-style calculations used in the project.  
It explains the example step-by-step in simple language.

---

# 1. Vector Field Used

We take the vector field:

P(x, y) = –y  
Q(x, y) = x  

These are the two functions used in Green's Theorem.

---

# 2. Region Selected

We consider a **unit square** with corners:

(0,0)  
(1,0)  
(1,1)  
(0,1)

So:

x ranges from 0 to 1  
y ranges from 0 to 1  

Area of the square = 1 × 1 = **1**

---

# 3. Step 1: Partial Derivatives

We need the following:

dQ/dx = derivative of Q with respect to x  
dP/dy = derivative of P with respect to y  

### Finding dQ/dx:
Q(x, y) = x  
Derivative with respect to x = 1  

So, dQ/dx = 1

### Finding dP/dy:
P(x, y) = –y  
Derivative with respect to y = –1  

So, dP/dy = –1

### Combine them:
dQ/dx – dP/dy = 1 – (–1)  
= 1 + 1  
= **2**

So the value inside the double integral is a constant 2.

---

# 4. Step 2: Double Integral Over the Region

We calculate:

Double Integral = (dQ/dx – dP/dy) × Area

We already found:

dQ/dx – dP/dy = 2  
Area = 1  

So:

Double Integral  
= 2 × 1  
= **2**

---

# 5. Step 3: Line Integral Around the Boundary

We now calculate the line integral along all four sides:

Integral of (P dx + Q dy) around the boundary.

We divide the calculation into 4 parts.

---

## SIDE 1: Bottom side (from (0,0) to (1,0))

Here:
x goes from 0 to 1  
y = 0 → constant  

dx = positive  
dy = 0  

P(x, 0) = –0 = 0  
Q(x, 0) = x  

So line integral = ∫(0 dx + x dy) = ∫(0) = 0

Contribution from Side 1 = **0**

---

## SIDE 2: Right side (from (1,0) to (1,1))

Here:
x = 1 → constant  
y goes from 0 to 1  

dx = 0  
dy = positive  

P(1, y) = –y  
Q(1, y) = 1  

Line integral = ∫(P dx + Q dy)  
= ∫(1 dy) from y = 0 to y = 1  
= 1 × (1 – 0)  
= **1**

Contribution from Side 2 = **1**

---

## SIDE 3: Top side (from (1,1) to (0,1))

This is in the reverse direction.

Here:
y = 1  
x goes from 1 to 0  

dx = negative  
dy = 0  

P(x, 1) = –1  
Q(x, 1) = x  

Line integral = ∫(P dx + Q dy)  
= ∫(–1)(dx)  
= – ∫ dx from x = 1 to 0  
= – (0 – 1)  
= – (–1)  
= **1**

Contribution from Side 3 = **1**

---

## SIDE 4: Left side (from (0,1) to (0,0))

Here:
x = 0 → constant  
y goes from 1 to 0 (downwards)

dx = 0  
dy = negative  

P(0, y) = –y  
Q(0, y) = 0  

Line integral = ∫(0 dx + 0 dy)  
= 0  

Contribution from Side 4 = **0**

---

# 6. Step 4: Add All Side Results

Total line integral:

Side 1 = 0  
Side 2 = 1  
Side 3 = 1  
Side 4 = 0  

Total = 0 + 1 + 1 + 0  
Total = **2**

---

# 7. Final Verification

Double Integral = 2  
Line Integral = 2  

Since both values are equal:

**Green's Theorem is VERIFIED.**

---

# 8. Summary

- dQ/dx – dP/dy = 2  
- Area = 1  
- Double Integral = 2  
- Line Integral = 2  
- Both sides are equal  

Therefore, the example satisfies Green’s Theorem perfectly.

---

# END OF CALCULATIONS FILE

