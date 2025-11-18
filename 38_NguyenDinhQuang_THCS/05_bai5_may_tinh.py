# Bài 5: Một chương trình tính toán tổng quát (nhận biểu thức toán học đơn giản)
# Hỗ trợ các phép toán: +, -, *, /, **, ^ (thay cho **), và ngoặc.
# LƯU Ý: chương trình dùng eval trong phạm vi hạn chế; chỉ cho phép các ký tự an toàn.
import ast

ALLOWED_NODES = {
    'Expression','BinOp','UnaryOp','Num','Constant','Add','Sub','Mult','Div','Pow',
    'USub','UAdd','Load','Tuple','List','Dict','Mod','FloorDiv','Call','Name'
}

SAFE_NAMES = {}  # không cho phép tên biến hoặc hàm nào

class SafeEvalError(Exception):
    pass

def is_safe(node):
    # kiểm tra cây AST để đảm bảo chỉ có các node an toàn
    for child in ast.walk(node):
        name = type(child).__name__
        if name not in ALLOWED_NODES:
            return False, name
        if isinstance(child, ast.Call):
            return False, 'Call not allowed'
        if isinstance(child, ast.Name):
            if child.id not in SAFE_NAMES:
                return False, f'Name {child.id} not allowed'
    return True, ''

def safe_eval(expr):
    expr = expr.replace('^', '**')
    try:
        node = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise SafeEvalError("Cú pháp không hợp lệ.")
    ok, reason = is_safe(node)
    if not ok:
        raise SafeEvalError(f"Biểu thức chứa thành phần không an toàn: {reason}")
    return eval(compile(node, '<string>', 'eval'), {'__builtins__': None}, SAFE_NAMES)

def main():
    print("Máy tính: nhập biểu thức toán học (ví dụ: 2+3*(4-1), 2^8 cho lũy thừa). Enter để thoát.")
    while True:
        s = input(">>> ").strip()
        if not s:
            break
        try:
            res = safe_eval(s)
            print(res)
        except SafeEvalError as e:
            print("Lỗi:", e)
        except Exception as e:
            print("Lỗi khi tính:", e)

if __name__ == '__main__':
    main()
