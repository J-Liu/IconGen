import os
import sys
from PIL import Image

def create_icns(prefix="nn"):
    """
    根据指定前缀的图片自动生成 macOS .icns 图标文件。
    前提：当前目录下需要有 {prefix}_16.png 到 {prefix}_1024.png 的完整尺寸图片。
    """
    # macOS .iconset 标准命名映射
    # (源图片尺寸, iconset中的目标文件名)
    sizes = [
        (16, "icon_16x16.png"),
        (32, "icon_16x16@2x.png"),
        (32, "icon_32x32.png"),
        (64, "icon_32x32@2x.png"),
        (128, "icon_128x128.png"),
        (256, "icon_128x128@2x.png"),
        (256, "icon_256x256.png"),
        (512, "icon_256x256@2x.png"),
        (512, "icon_512x512.png"),
        (1024, "icon_512x2x.png"),  # 1024 对应 512@2x
    ]

    iconset_dir = f"{prefix}.iconset"
    icns_file = f"{prefix}.icns"

    # 1. 创建 .iconset 目录
    if os.path.exists(iconset_dir):
        # 如果已存在则清空，防止残留旧文件
        for f in os.listdir(iconset_dir):
            os.remove(os.path.join(iconset_dir, f))
    else:
        os.makedirs(iconset_dir)

    print(f"📂 正在处理 {prefix} 系列图标...")

    # 2. 复制并重命名图片
    missing_files = []
    for size, filename in sizes:
        src = f"{prefix}_{size}.png"
        if os.path.exists(src):
            img = Image.open(src)
            # 校验尺寸，防止图片实际尺寸与文件名不符
            if img.size != (size, size):
                print(f"   ⚠️ {src} 尺寸不符，正在缩放至 {size}x{size}...")
                img = img.resize((size, size), Image.LANCZOS)
            img.save(os.path.join(iconset_dir, filename))
        else:
            missing_files.append(src)

    if missing_files:
        print(f"❌ 缺少以下尺寸的图片: {missing_files}")
        return

    # 3. 调用 macOS 系统命令打包
    print(f"⚙️ 正在打包生成 {icns_file}...")
    exit_code = os.system(f"iconutil -c icns {iconset_dir}")

    if exit_code == 0:
        print(f"✅ 转换成功！已生成: {icns_file}")
    else:
        print("❌ 打包失败，请确保在 macOS 系统下运行此脚本。")

if __name__ == "__main__":
    # 默认前缀为 nn，你也可以在命令行传入其他前缀，例如: python make_icon.py app
    prefix = sys.argv[1] if len(sys.argv) > 1 else "nn"
    create_icns(prefix)
