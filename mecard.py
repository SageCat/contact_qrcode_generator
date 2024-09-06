import re
import qrcode
from PIL import Image
from MyConfig import MyConfig


def read_info():
    conf = MyConfig("config.ini")
    full_name = conf.get('card_info', 'full_name')
    phone_no = conf.get('card_info', 'phone_no')
    email_id = conf.get('card_info', 'email_id')
    address = conf.get('card_info', 'address')
    website = conf.get('card_info', 'website')
    company_name = conf.get('card_info', 'company_name')
    position = conf.get('card_info', 'position')
    return ("MECARD:N:{};TEL:{};EMAIL:{};ADR:{};URL:{};ORG:{};TITLE:{};".
            format(full_name, phone_no, email_id, address, website, company_name, position))


def get_logo_path():
    conf = MyConfig("config.ini")
    return conf.get('logo', 'logo_path')


def generate_qr_code(data, logo_path):
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # 打开 logo 图片
    logo_img = Image.open(logo_path)

    # 添加 logo 到二维码中心
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo_img.size
    # resized_image = logo_img.resize((int(logo_width * 1.5), int(logo_height *1.5)), Image.LANCZOS)
    logo_position = ((qr_width - int(logo_width)) // 2, (qr_height - int(logo_height)) // 2)
    qr_img.paste(logo_img, logo_position)

    # 保存生成的二维码图片
    match = re.search(r'N:([^;]+);', data)
    if match:
        name = match.group(1)
        print("Name:", name)
        qr_img.save(f".\images\{name}.png")
    else:
        print("name is not defined")


if __name__ == '__main__':
    generate_qr_code(read_info(), get_logo_path())
