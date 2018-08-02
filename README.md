
This is step by step applying kalman filter to estimate car position in a very simple situation that car only moving forward and velocity is constant. This code estimate the x and P, current position and the uncertainty probability. 

Because all of calculate of Kalman_filter is base on Matrix, therefore first we need to make some calculation with matrix first. The code bellow describes that.

After that, we just apply the formulas of Kalman filter and rewrite the funtionc. Here I make two version, one in python and C++, C++ is a little bit longer but if will fix if your project writes in c++. 

Below I also want to explain the methods to read informarion on internet or wiki, then rewrites them in our code, 

Because on wiki they write the functions in general and more mathematics, therefore we need to understand and then transform it to code.


 
