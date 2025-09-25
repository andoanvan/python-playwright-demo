import os

exclude_dirs = {'venv', '.git', '__pycache__'}

for root, dirs, files in os.walk("."):
    # Bỏ qua các thư mục không cần
    if any(skip in root for skip in exclude_dirs):
        continue

    # Tạo __init__.py nếu chưa có
    init_file = os.path.join(root, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            pass  # file rỗng
        print(f"Created: {init_file}")