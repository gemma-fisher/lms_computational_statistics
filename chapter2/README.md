## MRC LMS - Introduction to probability, statistics and hypothesis testing

### Jesús Urtasun Elizari, MRC LMS & RCDS ICL

LMS email address `Jesus.Urtasun@lms.mrc.ac.uk`

ICL email address `jurtasun@ic.ac.uk`

<img src="/readme_figures/ukri_lms_logo.png" width = 700>

### Chapter 2. Predictive probability.

- Definition of probability and random events.
- Discrete and continous probability distributions.
- Mean and variance as expected values.

```latex
% =====================================================================
\subsection*{Discrete Distributions}

\paragraph{Bernoulli distribution.}
Let \(X\sim\mathrm{Bern}(p)\) with \(\mathbb{P}(X=1)=p\) and \(\mathbb{P}(X=0)=1-p\).
\[
\mathbb{E}[X]=1\cdot p+0\cdot(1-p)=p,
\]
\[
\operatorname{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2=p-p^2=p(1-p).
\]

\paragraph{Binomial distribution.}
Let \(X\sim\mathrm{Bin}(n,p)\). Writing \(X=\sum_{i=1}^n X_i\), where the \(X_i\) are i.i.d.\ Bernoulli\((p)\),
\[
\mathbb{E}[X]=\sum_{i=1}^n \mathbb{E}[X_i]=np,
\]
\[
\operatorname{Var}(X)=\sum_{i=1}^n \operatorname{Var}(X_i)=np(1-p).
\]

\paragraph{Discrete uniform distribution.}
Let \(X\) be uniformly distributed on \(\{1,\dots,n\}\).
\[
\mathbb{E}[X]=\frac{1}{n}\sum_{k=1}^n k=\frac{n+1}{2},
\]
\[
\operatorname{Var}(X)
=\frac{1}{n}\sum_{k=1}^n k^2-\left(\frac{n+1}{2}\right)^2
=\frac{n^2-1}{12}.
\]

\paragraph{Poisson distribution.}
Let \(X\sim\mathrm{Pois}(\lambda)\).
Using the series definition of the exponential function,
\[
\mathbb{E}[X]
=\sum_{k=0}^\infty k\frac{\lambda^k e^{-\lambda}}{k!}
=\lambda,
\qquad
\operatorname{Var}(X)=\lambda.
\]

% =====================================================================
\subsection*{Continuous Distributions}

\paragraph{Gaussian distribution.}
Let \(X\sim\mathcal{N}(\mu,\sigma^2)\).
Symmetry of the density about \(\mu\) implies \(\mathbb{E}[X]=\mu\). A direct computation of
\(\mathbb{E}[(X-\mu)^2]\) using Gaussian integrals yields
\[
\operatorname{Var}(X)=\sigma^2.
\]

\paragraph{Exponential distribution.}
Let \(X\sim\mathrm{Exp}(\lambda)\) with density \(f(x)=\lambda e^{-\lambda x}\) for \(x\ge0\).
\[
\mathbb{E}[X]=\int_0^\infty x\lambda e^{-\lambda x}\,dx=\frac{1}{\lambda},
\]
\[
\operatorname{Var}(X)
=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx-\frac{1}{\lambda^2}
=\frac{1}{\lambda^2}.
\]

\paragraph{Continuous uniform distribution.}
Let \(X\sim\mathrm{Unif}(a,b)\).
\[
\mathbb{E}[X]=\frac{1}{b-a}\int_a^b x\,dx=\frac{a+b}{2},
\]
\[
\operatorname{Var}(X)
=\frac{1}{b-a}\int_a^b (x-\mu)^2\,dx=\frac{(b-a)^2}{12}.
\]
```
