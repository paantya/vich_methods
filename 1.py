#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def p(x):
	return 1/np.sqrt(x+3)#np.exp(x/2)
	
def q(x):
	return 1/(x+4) #(1 - np.power(np.cos(x*np.pi/2),2)/4)

def f(x):
	return np.log(x+5) #np.sqrt(x + 1)
	
def printArray(ar,n):
	for i in np.arange(n+1):
		for j in np.arange(n+1):
			print ar[i,j]

ll = raw_input('Введите значения коэффицентов(g1, g2, g3, g4, g5, g6 ,x0, xn)\ng1 * y(x0) + g2 * y]\'(x0) = g3\ng4 * y(xn) + g5 * y]\'(xn) = g6:\n').split()
g1 = float(ll[0])
g2 = float(ll[1])
g3 = float(ll[2])
g4 = float(ll[3])
g5 = float(ll[4])
g6 = float(ll[5])
x0 = float(ll[6])
xn = float(ll[7])

n = 13
h = (xn - x0) /n

'''
arr = np.zeros((n,n))#=[[0.0*i*j for i in np.arange(n+1)] for j in np.arange(n+1)]
for i in np.arange(n):
	for j in np.arange(n):
		#print(i,j)
		if (i == (j+1)):
			arr[i,j] = 1 / np.power(h,2) - p(x0+i*h) /(2*n)
		if ((i + 1) == j):
			arr[i,j] = 1 / np.power(h,2) + p(x0+i*h) /(2*n)
		if (i == j):
			arr[i,j] = 2 / np.power(h,2) - q(x0+i*h)
'''

alfa = np.zeros((n+1))
beta = np.zeros((n+1))
y = np.zeros((n+1))

w = ((np.power(h,2)*q(x0) - 2)*g2 + h*(2 - h * p(x0))*g1)
alfa[0] = 2 * g2 / w
beta[0] = np.power(h,2) * f(x0) * g2 + h * (2 - h * p(x0)*g3 )
print(alfa[0],beta[0])
for i in np.arange(1,n+1):
	w = ((2*np.power(h,2)*q(x0+h*i) - 4) - alfa[i-1]*(2 - h * p(x0 + h*i)))
	alfa[i] = (2 + h * p(x0 + h*i)) / w
	beta[i] = (2 * np.power(h,2) * f(x0 + i * h) - (2 - h * p(x0 + i*h))*beta[i-1])/w

#for i in np.arange(n+1):
#	print(i,alfa[i],beta[i])

y[n] =float(( 2 * h * g6 + ((beta[n-1] - beta[n])/alfa[n])*g5 ) / (2.0*h*g4 + (alfa[n-1] - 1/alfa[n])*g5))

for i in np.arange(n-1,-1,-1):
	 y[i] = beta[i] - alfa[i] * y[i+1]
x = [x0+h*i for i in np.arange(0,n+1)]
print 'xi \t yi \t ai \t bi'
for xi,yi,ai,bi in zip(x,y,alfa,beta):
	print round(xi,4),'\t',round(yi,4),'\t',round(ai,3),'\t',round(bi,3)

			
#printArray(arr,n)
