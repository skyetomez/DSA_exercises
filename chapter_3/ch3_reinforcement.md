# Under construction

## Reinforcement

### R-3.1

```python
import numpy as np

import matplotlib.pyplot as plt


t = np.linspace(1, 10, 100)

y1 = 8 * t
y2 = 4 * t * np.log10(t)
y3 = 2 * t * t
y4 = t * t * t
y5 = np.power(2, t)
plt.loglog(t, y1, label="8t")
plt.loglog(t, y2, label="4tlogt")
plt.loglog(t, y3, label="2t^2")
plt.loglog(t, y4, label="t^3")
plt.loglog(t, y5, label="2^t")
plt.title("log-log plot of R-3.1 functions.")
plt.legend()
plt.grid()
plt.show()



```

### R-3.2

We solve this by insepction of the integer values of the two functions $A[n] =8n\log(n)$ and $B[n]=2n^2$. The output of the print function shows that after $n = 8$, function $B$ becomes worse than $A$.

```python

n = np.linspace(0,10,11)
A = 8*n*np.log(n)
B = 2*n*n
df3 = pd.DataFrame( data = {
    "n" : n,
    "A" : A,
    "B": B
}, 
                   index=n,
                   columns=["A","B"])
print(df3)

```

### R-3.3

We solve this by insepction of the graphs of the two functions $A[n] =40n^2$ and $B[n]=2n^3$. Alebraically we see that after $n=21$ function A becomes better. This can be understood by observing the graph of the slopes of the functions. Around this point, the rate of change of function $B$ increases with the square while that of function $A$ stays constant.

```python

dt = 101
n = np.linspace(0,100, dt)
A = 40*n*n
B = 2*n*n*n
df = pd.DataFrame(data ={
                        "A": A,
                        "B": B,
                        "n" : n 
                        }, 
                  index=n,
                  columns=["A","B"]
                  )
df.plot()
plt.axvline(21, color='r')
plt.grid()
plt.xlim([18,50])
plt.title("Plot of A = 40n^2 vs 2n^3")

```

### R-3.4

The function $y(t) = 8t$ plotted in question 1 remains linear on both the log-log plot and the un scaled plot.

### R-3.5

The funciton $n^c$ on the log-log scale plot is function that increases constantly $c$. This constant increase is linear on the log-log scale.

### R-3.6

By insecption we determine that if $n$ is even then the equation for the sum is $S = \lceil\frac{n}{2}\rceil + n$ and if $n$ is odd $S = \lceil\frac{n}{2}\rceil$

We prove this by induction on $n$.

Let the above be true for $n$ now for $n+1$, if $n$ is even then $n+1$ is odd and if $n$ is odd then $n+1$ is even by the parity property of the integers.

Case I:

If $n+1$ is even then $2(n+1)$ is also even and can be wirtten as $2k$ for some $k\in\mathbf{Z}$. It follows that we can write the sequence of the cumulative sum as:

$$0,1,2,3...,2k-3, 2k-2, 2k-1, 2k$$

We observe that we can pair the numbers such that $0+2k = 2k$, $1+2k-1=2k$ etc. We now only have to count the number of pairs where both elements of the sequence are even. This is exactly the number of even numbers less than $n+1$.

The number of even numbers less than $n+1$ is $p = \lceil \frac{n+1}{2}\rceil$. When $p$ is even, there is an odd number of pairs such that

$$0+2k,1+2k-1,2+2k-2,3+2k-3...+ k=p*2k+k$$

When $p$ is odd there is and even number of pairs such that.

$$0+2k,1+2k-1,2+2k-2,3+2k-3...=p*2k$$

Thus it is true for $n+1$. Therefore if $n$ is odd, the sum of all even numbers from $0$ to $2n$ is $p*2n$ and if $n$ is even, the sum of all even numbers from $0$ to $2n$ is $p*2n+n$.

### R-3.7

```python

```

### R-3.8

Asmptotic growth rate by increasing:

$ 3n + 100\log(n) < 4n < n\log(n) < 4n\log(n) + 2n <  n^2  + 10n < n^3 < 2^{10}< 2^{\log(n)} < 2^n$

### R-3.9

Suppose that $d(n)$ is $O(f(n))$.

We need to show that for any $0<a\in\mathbf{R}$, when $ad(n)$ it has $O(f(n))$

By definition $\exists b\in\mathbf{R}$ such that $\forall n > n_f~bf(n)>d(n)$.

It follows that

$$bd(n)<b(af(n)) = (ab)f(n)$$

There are two cases.

Case I:

If $0<b<1$, then $ab<a$ and $af(n) > abf(n)=b(af(n))>bd(n)$ but then $d(n)$ is still $O(f(n))$

Case II:

If $1<b$, then the equality above is satisfied as $ab$ is still a real number.

Therefore, $d(n)$ is $O(f(n))$ for any real positive real number $b$.

### R-3.10

Suppose that $d(n)$ is $O(f(n))$ and $e(n)$ is $O(g(n))$.

We need to show that $d(n)e(n)$ is $O(f(n)g(n))$.

By definition of big-O.

$$for~n>n_f,~~d(n)<af(n)$$
$$for~n>n_e,~~e(n)<bg(n)$$

Thus,

$$d(n)e(n)<af(n)bg(n) = ab(f(n)g(n)) $$

But $ab$ is a positive real number $K$.

Let $n_0=\max\{(n_e,n_f)\}$

Then the equality is satisfied for $n>n_0~,~d(n)e(n)<K(f(n)g(n))$.

Therefore, $d(n)e(n)$ is $O(f(n)g(n))$.

### R-3.11

Suppose that $d(n)$ is $O(f(n))$ and $e(n)$ is $O(g(n))$.
We need to show that $d(n) + e(n)$ is $O(f(n) + g(n))$.

By definition of big-O.

$$for~n>n_f,~~d(n)<af(n)$$
$$for~n>n_e,~~e(n)<bg(n)$$

Let $ab = K\in\mathbf{R}$

Then,

$$d(n)+e(n)<af(n)+bg(n) < cf(n) + cg(n) = c(f(n) + g(n))$$

Let $n_0=\max\{(n_e,n_f)\}$

Thus the equality is satisfied for $n>n_0~,~d(n)+e(n)<K(f(n)+g(n))$.

Therefore, $d(n) + e(n)$ is $O(f(n) + g(n))$

### R-3.12

Suppose that $d(n)$ is $O(f(n))$ and $e(n)$ is $O(g(n))$.
We need to show that $d(n) -e(n)$ is not necessarily $O(f(n) -g(n))$.

From R-3.12 we see it is possible to get an $O(f(n)-g(n))= O(0)$ if both $e(n)$ and $d(n)$ are the bounded by the same function.

As a counterexample, let $e(n) = 3n^3$ and $d(n)=2n^3-n+1$. It is clear that both are $O(n^3)$ but their difference is:

$$3n^3 - 2n^3-1n+1 = n^3+n-1$$

which is also $O(n^3) and not $O(n^3-n^3) = O(0)$.

### R-3.13

Suppose $d(n)$ is $O(f(n))$ and $f(n)$ is $O(g(n))$.

We need to show that $d(n)$ is $O(g(n))$.

By definition of big-O.

$$for~n>n_f,~~d(n)<af(n)$$
$$for~n>n_g,~~f(n)<bg(n)$$

By subsitution

$$ d(n)<a(f(n))<a(bg(n)) = (ab)g(n) $$

Let $ab=K$ and $n_0 = \max\{(n_f,n_g)\}$

Thus the equality is satisfied for $n>n_0~,~d(n)<Kg(n)$.

Therefore, $d(n)$ is $O(g(n))$ as was to be shown.

### R-3.14

We need to show that $O(\max\{(f(n), g(n))\} = O(f(n)+g(n))$.

We know from R.11 that if $d(n)$ is $O(f(n))$ and $e(n)$ is $O(g(n))$ then $d(n)+e(n)$ is $O(f(n)+g(n))$

Choose $\max\{(f(n), g(n))\}$. Without loss of generality we use $f(n)$. Then,

$$d(n)+e(n)<c(f(n) + g(n)) < c(f(n)+f(n)) = 2cf(n)$$

Let $n_0=\max\{(n_e,n_f)\}$ and $2c=K$.

Thus the equality is satisfied for $n>n_0~,~d(n)+e(n)<Kf(n)$.

To show the reverse,

We start with $O(f(n)+g(n))$. So,

$$d(n)+e(n)<af(n)+bg(n) < c(f(n) + g(n))$$

But this is either less than $c(f(n) + f(n)$ or $c(g(n) + g(n))$.

Therefore, $O(\max\{(f(n), g(n))\} = O(f(n)+g(n))$

### R-3.15

```python

```

### R-3.16

```python

```

### R-3.17

```python

```

### R-3.18

```python

```

### R-3.19

```python

```

### R-3.20

```python

```

### R-3.21

```python

```

### R-3.22

```python

```

### R-3.23

```python

```

### R-3.24

```python

```

### R-3.25

```python

```

### R-3.26

```python

```

### R-3.27

```python

```

### R-3.28

```python

```

### R-3.29

```python

```

### R-3.30

```python

```

### R-3.31

```python

```

### R-3.32

```python

```

### R-3.33

```python

```

### R-3.34

```python

```
