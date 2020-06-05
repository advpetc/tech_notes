CNN is good for spacial structure

![Screen Shot 2020-04-30 at 3.16.20 PM.png](resources/922A0B6231B7496A918187CC27BE1DF8.png =939x441)

## Filter

![Screen Shot 2020-04-30 at 3.18.29 PM.png](resources/F2547EEE1E666E119CE67B25694802D2.png =385x430)

1. stride (3 in this case): number of steps to move for each progress
2. dimentino size: n * n
3. filter size: F

Output size = (N - F)/stride+1 => e.g. stride size = 3 won't work
1. To make this case working, adding a border surrounded (padding) will make N divisable (now N is 9 instead of 7)
2. To make the size remain the same dimentionally, we also use padding.

## Conv Layer

* Accpets a volume of size $W_1\times H_1 \times D_1$
* Requires four hyperparameters:
  * Number of filters K,
  * their spatial extent F (or filter dimension),
  * the stride S,
  * the amount of zero padding P.
* Produces a volume of size $W_2$ $\times$ $H_2$ $\times$ $D_2$
  * $W_2 = (W_1 - F + 2P)/S + 1$ 
  * $H_2 = (H_1 - F + 2P)/s + 1$ (width and height are the same size)
  * $D_2 = K$
* With parameter sharing, it produces $F \times F \times D_1$ weights per filter, for a total of $(F \cdot F \cdot D_1) * K$ weights
* In the output volume, the d-th depth slice (of size $W_2 \times H_2$) is the result of performing a valid convolution of the d-th filter over the input volume with a stride of $S$, and then offset by d-th bias

## Pooling Layer

![Screen Shot 2020-04-30 at 5.41.32 PM.png](resources/98BCE97DA55191702740A5E953B290EE.png =665x490)

input depth would be the same, and width and height would be shrink down by a factor

### Max-Pooling Layer

![Screen Shot 2020-04-30 at 5.42.45 PM.png](resources/C9064878B8E00661B86A55C23F7C7B26.png =912x447)

Choosing the maximum within each filter. Find the region that has fired with higher value from the other region.

### Summary

* Accepts a volume of size W1×H1×D1
* Requires two hyperparameters:
  * their spatial extent F,
  * the stride S,
* Produces a volume of size W2×H2×D2 where:
  * $W_2=(W_1−F)/S+1$
  * $H_2=(H_1−F)/S+1$
  * $D_2=D_1$
* Introduces zero parameters since it computes a fixed function of the input
* For Pooling layers, it is not common to pad the input using zero-padding.

It is worth noting that there are only two commonly seen variations of the max pooling layer found in practice: A pooling layer with $F=3,S=2$ (also called overlapping pooling), and more commonly $F=2,S=2$. Pooling sizes with larger receptive fields are too destructive.

## Fully Connected Layer (FC)

Stretch out to 1-d array, usually on the last layer.









