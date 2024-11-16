import qrcode
from PIL import Image


# 1. 得到需要编码成2维QR码图的字符串 
url = "https://www.baidu.com" # 待编码字符串


# 2. 实例化QR码并生成QR图像（包括颜色设置）
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill="black", back_color="white").convert('RGB')


# 3. 在QR码中间加上图片
logo = Image.open("IP.png")  
logo_size = (qr_img.size[0] // 5, qr_img.size[1] // 5)  # 将引入图片放到中间位置
logo = logo.resize(logo_size, Image.LANCZOS)

if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

logo_mask = logo.split()[3]  

logo_pos = ((qr_img.size[0] - logo_size[0]) // 2, (qr_img.size[1] - logo_size[1]) // 2) # 重计算位置

qr_img.paste(logo, logo_pos, mask=logo_mask) # 将mask添加到QR码的中间


# 4. 保存图片
qr_img.show() 
qr_img.save("baidu.png") 
