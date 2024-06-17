import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

col1, col2 = st.columns(2)
with col1:
  mu = st.slider('$\mu$', -10., 10.,.0)
with col2:
  sigma = st.slider('$\sigma$',0.1,10.,1.)

fig, ax = plt.subplots()
def f(x, m=mu, s=sigma):
  return np.exp(-(x-m)**2/(2*s**2))/(s*np.sqrt(2*np.pi))
x = np.linspace(-3*sigma + mu,3*sigma + mu,400)
ax.plot(x,f(x))
# ax.plot([0,0],[0,max(f(x))],color ='yellow')

# ax.plot([min(x),max(x)],[0,0], color ='yellow')
ax.axvline(x=0, color='y')
ax.axhline(y=0, color='y')
ax.set_title("Gauss Normal Function")
ax.set_xlabel("x")
ax.set_ylabel("p(x)")
st.pyplot(fig)
