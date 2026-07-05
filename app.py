import gradio as gr
import sympy as sp
from sympy import latex

def solve_math(eq_str):
    try:
        x = sp.symbols('x')
        y = sp.Function('y')(x)

        if "=" not in eq_str:
            return "Please enter an equation with '=' sign."

        lhs_str, rhs_str = eq_str.split("=", 1)
        lhs = sp.sympify(lhs_str)
        rhs = sp.sympify(rhs_str)

        equation = sp.Eq(lhs, rhs)
        sol = sp.dsolve(equation)

        # تبدیل به LaTeX
        sol_latex = latex(sol)

        # نمایش زیبای ریاضی
        return f"### Solution\n$$ {sol_latex} $$"

    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.Interface(
    fn=solve_math,
    inputs=gr.Textbox(
        label="Enter differential equation",
        placeholder="Example: Derivative(y(x), x) - y(x) = 0"
    ),
    outputs=gr.Markdown(),   # مهم! دیگر Textbox نیست
    title="Differential Equation Solver",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
