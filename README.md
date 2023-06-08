# supertask
A theoretical implementation of a supertask written in Python 3.11.

# FAQ

## What is a supertask?
Essentially, a supertask is a **infinite** amount of actions being performed in an **finite** amount of time. A popular example of this was featured in [this video by VSauce:](https://www.youtube.com/watch?v=ffUnNaQTfZE)
1. Take a square, with dimensions $x$ by $y$
2. Wait 1 minute.
3. Cut the square in half vertically, such that its dimensions are $\frac{x}{2}$ by $y$.
4. Wait half the time
5. Repeat steps 3, 4 infinitely.

Mathematically, this procedure would be written as the following, assuming that the dimensions are $x=10$, $y=10$

$$
k_i = \left(10, 10\right) \quad i=0
$$

$$
k_i = \left(\frac{k_{i-1}}{2}, k_{i-1}\right) \quad i=1
$$

$$
\cdots
$$

$$
k_i = \left(?, ?\right) \quad i = \infty
$$

## What does this program try to accomplish?
This program is a theoretical implementation of a supertask. It is not a
"true" supertask, as there are some limitations (see [this section](#limitations) for info) to implementating a REAL supertask.

The way it does this is defining a function, $f$ as such:

$$
f(x) = \frac{1}{2^{x}}
$$

It keeps track of a variable $k$, which starts at $k=1$. It firstly, waits
1 minute and does $k_n = f(k)$. Then, it waits half that time (30 sec) and
performs $k_n = f(k_n)$. It repeats this infinitely.

## But this isn't a supertask!! it's an X!!!
No. It isn't. By definition, a supertask, is:
> a **COUNTABLY** INFINITE number of tasks in a **FINITE** interval of time.

Countable sets are sets that have 1:1 correspondence to $\mathbb{N}_0$. If you really want a proof:

We can define a set, $A$, that is all numbers we deal with.
$$
A = \{1, 0.25, 0.125, 0.0625,\dots\}
$$

We can assign a value from $\mathbb{N}_0$ to each element of $A$:

<!-- i fucking hate having to do this -->
<!-- but github is so wacky -->
$$
0 \longrightarrow 1
$$

$$
1 \longrightarrow 0.25
$$

$$
\dots
$$

We can do this infinitely. Thus, $A$ is countable.

# Limitations

As supertasks are impossible in the real world, this is just a theoretical
model. The program uses floating point accuracy, defined by the specification IEEE 754. Thus, it can only have around $5\cdot10^{-324}$ decimal points.

Obviously, this doesn't happen in real life. $5 \cdot 10^{-324}$ is *not* the smallest number! (You could go into ZFC set theory and ordinals/cardinals, but I won't.)
