## Overview
1. One time setup: activation functions, preprocessing, weight initialization, regularization, gradient checking
2. Training dynamics: babysitting the learning process, parameter updates, hyperparameter optimization
3. Evaluation: model ensembles

## Part 1

- Activation functions
- Data preprocessing
- Weight initialization, 
- Batch Normalization
- Babysitting the learning process
- Hyperparameter Optimization

### Activation Function

#### Sigmoid

\[\sigma(x)=\frac{1}{1+e^{-x}}\]

![Screen Shot 2020-05-02 at 12.32.12 PM.png](resources/BB906A83B67EC1585A56FFED50753BBE.png)

- if get high value -> approach to 1, low -> 0
- problem 1: if **too** large, then the value is 1, or **too** small, then the value is 0 (killed gradient when saturated)
- problem 2: not zero-centered (gradient on w is always all positive or negative) which makes the parameter update inefficient
- problem 3: $e^{-x}$ is computation expensive

#### tanh

\[tanh(x)\]

![Screen Shot 2020-05-02 at 12.42.30 PM.png](resources/8088CDEA0DF6B9324787F00D698258C9.png)

- in a range of [-1, 1]
- it's now zero centered (flip between - and + for same weight)
- problem 1: still kill gradient when saturated

#### ReLU

\[f(x)=max(0,x)\]

![Screen Shot 2020-05-02 at 12.45.23 PM.png](resources/40031CD80CA314E99EAFA55207AA28CB.png)

- doesn't saturated **in positive region**
- computation efficient
- converge faster than sigmoid and tanh
- biologically plausible than sigmoid
- problem 1: not zero-centered
- problem 2: negative still saturated (annoyance, dead relu region)

#### Leaky ReLU and Parametric Rectifier

\[f(x)=max(0.01x, x)\] and \[f(x)=max(\alpha x, x)\]

![Screen Shot 2020-05-03 at 3.49.29 PM.png](resources/30D7C14D49A45B106440C1F06091CD37.png)

- Does not saturate
- Computationally efficient
- Converge much faster than sigmoid/tanh in practice
- will not "die"  (no platu)

#### Exponential Linear Unit (ELU)

f(x)=x if x > 0
f(x)= alpha (exp(x)-1) if x <= 0

![Screen Shot 2020-05-03 at 3.53.36 PM.png](resources/CD7229E86B9969684103B3594A4A18B0.png)

- all benefits of ReLU
- closer to zero mean outputs
- negative sarturation regime compared with Leaky ReLU adds some robustness to noise
- problem 1: computation requires exp()

#### Conclusion

- Use ReLU
- Try out Leaky ReLU/Maxout/ELU
- Try tanh but don't expect too much
- Don't use sigmoid

### Data Preprocessing

for image, stick with zero-mean



