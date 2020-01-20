# Alpha Beta Filters

This is the implementation of the [alpha beta filter](https://en.wikipedia.org/wiki/Alpha_beta_filter).

An alpha beta filter is a simplified form of observer for estimation, data smoothing and control applications. It is closely related to Kalman filters and to linear state observers used in control theory. Its principal advantage is that it does not require a detailed system model to function.

An alpha beta filter assumes that the system can be modelled with two internal states where the first state is obtained by integrating the second state over time. Measured system output values correspond to observations of the first model state plus disturbances. This low order approximation is adequate for many simple systems.

## Mechanical System
Using the mechanical system analogy, the two states are position x and velocity v. Assuming that the velocity remains approximately constant over the small time interval dt between measurements, the position state is projected forward to predict its value at the next sampling time using the following equation.

 
