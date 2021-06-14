# XOR problem using McCulloh Pitts neural-net in python

## The truth table
![image](https://user-images.githubusercontent.com/81920073/121835002-b8856f00-cced-11eb-8d95-c3e53e8a1c08.png)

## The code

### The input vectors
```python
x1=np.array([0,0,1,1])
x2=np.array([0,1,0,1])
```
### The expected output
```python
z=np.array([0,1,1,0])
```
### The parameters used 
```python
#weights w
w11=2 
w12=-1 
w21=-1 
w22=2
#weights v
v1=2 v2=2
#threshhold value theta
theta=2 #int(input('Enter Threshhold value theta: '))
```
### The simple nueral net formula used as
```python
zin1=x1*w11+x2*w21
zin2=x1*w21+x2*w22
```
## The output
![image](https://user-images.githubusercontent.com/81920073/121835953-1b780580-ccf0-11eb-85cf-3885ba131559.png)
