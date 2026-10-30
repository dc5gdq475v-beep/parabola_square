import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📐 平方完成と二次方程式のビジュアル学習")

# サイドバーにスライダーを配置
st.sidebar.header("係数の設定")
a = st.sidebar.slider("a の値", -5.0, 5.0, 1.0, 0.1)
b = st.sidebar.slider("b の値", -10.0, 10.0, -4.0, 0.5)
c = st.sidebar.slider("c の値", -10.0, 10.0, 3.0, 0.5)

# グラフの描画
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

ax.plot(x, y, color='#2b5c8f', linewidth=2.5)
ax.axhline(0, color='black', linewidth=1, linestyle='--')
ax.axvline(0, color='black', linewidth=1, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)

# Streamlitにグラフを表示
st.pyplot(fig)
