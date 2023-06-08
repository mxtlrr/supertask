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
k_i = \left(10, 10\right) \quad i=0\\
k_i = \left(\frac{k_{i-1}}{2}, k_{i-1}\right) \quad i=1\\
\cdots\\
k_i = \left(?, ?\right) \quad i = \infty\\
$$

## What does this program try to accomplish?
This program is a theoretical implementation of a supertask. It is not a
"true" supertask, as there are some limitations (see [this section](#limitations) for info) to implementating a REAL supertask.

The way it does this is defining a function, $f$ as such:

$$
f(x) = \frac{1}{2^{x}}\\
$$

It keeps track of a variable $k$, which starts at $k=1$. It firstly, waits
1 minute and does $k_n = f(k)$. Then, it waits half that time (30 sec) and
performs $k_n = f(k_n)$. It repeats this infinitely.


# Limitations

As supertasks are impossible in the real world, this is just a theoretical
model. For example, the program will definently fail at around $10 \cdot 2^{1023}$ (or $898846567431157953864652595394512366808988489471153286367150405788663379027504815663542386612037680105600569399356966788293948844072083112464237153197370621888839467124327426381511098006230470597265414760425028844190753411712314407369565552704136185816752553422931491199736229692398581524176781648121120686080$) iterations.