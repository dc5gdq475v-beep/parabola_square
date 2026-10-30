import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📐 平方完成と二次方程式のビジュアル学習")

# サイドバーにスライダーを配置
st.sidebar.header("係数の設定")
a = st.sidebar.slider("a の値", -5.0, 5.0, 1.0, 0.1)
b = st.sidebar.slider("b の値", -10.0, 10.0, -4.0, 0.5)
c = st.sidebar.slider("c の値", -10.0, 10.0, 3.0, 0.5)

if a == 0:
    st.warning("⚠️ $a = 0$ のときは二次関数になりません。スライダーで $a$ を 0 以外にしてください。")
else:
    # 1. 平方完成の計算: y = a(x - p)^2 + q
    p = -b / (2 * a)
    q = c - (b**2) / (4 * a)

    # 2. 二次方程式の解の計算 (ax^2 + bx + c = 0)
    D = b**2 - 4 * a * c

    # --- 計算結果のテキスト表示 ---
    st.subheader("📝 計算結果と式の変形")
    
    # 符号の調整（表示を綺麗にするため）
    sign_p = "-" if p >= 0 else "+"
    abs_p = abs(p)
    sign_q = "+" if q >= 0 else "-"
    abs_q = abs(q)

    # LaTeXを使った美しい数式表示
    st.latex(f"y = {a}(x {sign_p} {abs_p:.2f})^2 {sign_q} {abs_q:.2f}")
    st.write(f"**頂点**: $({p:.2f}, {q:.2f})$")

    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2 * a)
        x2 = (-b - np.sqrt(D)) / (2 * a)
        st.write(f"**二次方程式の解 ($y=0$ となる点)**: $x = {x1:.2f}, {x2:.2f}$ (実数解 2つ)")
    elif D == 0:
        st.write(f"**二次方程式の解 ($y=0$ となる点)**: $x = {p:.2f}$ (重解)")
    else:
        st.write("**二次方程式の解 ($y=0$ となる点)**: 実数解なし ($x$ 軸との交点なし)")

    # --- グラフの描画 ---
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    # 放物線の描画
    ax.plot(x, y, color='#2b5c8f', linewidth=2.5, label='y = ax² + bx + c')
    ax.axhline(0, color='black', linewidth=1, linestyle='--')
    ax.axvline(0, color='black', linewidth=1, linestyle='--')

    # 頂点をプロット
    ax.plot(p, q, 'ro', markersize=8, label=f'Vertex: ({p:.1f}, {q:.1f})')

    # 解（x軸との交点）をプロット
    if D > 0:
        ax.plot([x1, x2], [0, 0], 'go', markersize=8, label='Roots (x-intercepts)')
    elif D == 0:
        ax.plot([p], [0], 'go', markersize=8, label='Root (Vertex on x-axis)')

    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_ylim(-20, 20)  # グラフが飛び出しすぎないように調整
    ax.legend()

    # Streamlitにグラフを表示
    st.pyplot(fig)
