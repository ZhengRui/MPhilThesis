#! /usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def maxout(x, w, b):
    return np.amax(np.outer(x, np.array(w)) + np.array(b), 1)

x = np.linspace(-5,5,1001)
sigmoid_y = sigmoid(x)
tanh_y = np.tanh(x)
relu_y = x * (x > 0)
leakyrelu_y = 0.2 * x * (x < 0) + x * (x >= 0)
maxout_y = maxout(x, [0.5, 1, 2], [-0.5, 0, -1])


fig = plt.figure()
fig.set_tight_layout(True)
l_maxout, = plt.plot(x, maxout_y, '-', linewidth=2.0, label='Maxout')
l_leakyrelu, = plt.plot(x, leakyrelu_y, '-', linewidth=2.0, label='Leaky ReLU')
l_relu, = plt.plot(x, relu_y, '-', linewidth=2.0, label='ReLU')
l_tanh, = plt.plot(x, tanh_y, '-', linewidth=2.0, label='Tanh')
l_sigmoid, = plt.plot(x, sigmoid_y, '-', linewidth=2.0, label='Sigmoid')

plt.xlim(-4,4)
plt.ylim(-3,3)
plt.legend([l_sigmoid, l_tanh, l_relu, l_leakyrelu, l_maxout], [r'Sigmoid: $\sigma(x) = \frac{1}{1+e^{-x}}$', r'Tanh: $\tanh(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}$' , r'ReLU: $f(x) = \max(0,x)$', r'Leaky ReLU: $f(x) = \mathbb{1}(x<0)(\alpha x)+\mathbb{1}(x\geq 0)(x)$', r'Maxout: $f(x) = \max(x*w_j + b_j), j\in[1,k]$'], loc=4)
plt.show()
fig.savefig('../figure/ch3-activations.pdf')
