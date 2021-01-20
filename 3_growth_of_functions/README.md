# Asymptotic Notation

- Θ− Notation，Big-Theta

  - def: Θ(g(n)) = {there exist constant positive constants c1, c2 and n0 such that 0≤c1g(n)≤f(n)≤c2g(n) for all n >= n0}
  - Big-Theta(Θ(·))是同時找到 f(n)的「上界(upper bound)」與「下界(lower bound)」，像是三明治一樣把 f(n)夾住。

- O− Notation，Big-O(upper bound)
  - def: O(g(n)) = {f(n) exist positive constants c and n0 such that 0≤f(n)≤cg(n) for all n >= n0}
- Ω−Notation，Big-Omega(lower bound)

  - def: Ω(g(n)) = f(n) there exist positive constants c and n0 such that 0≤cg(n)≤f(n) for all n >= n0

- o− Notation，Littel-o(similar as O-notation) the main different is holds all constants c > 0 that function f(n) becomes insignificant(夾較不緊的上界)

- ω− Notation，Littel-omega(smimilar as Ω−Notation) the main different is holds all constants c > 0 that function f(n) becomes insignificant(夾較不緊的下界)
