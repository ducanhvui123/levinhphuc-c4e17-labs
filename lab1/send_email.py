from gmail import GMail, Message
from random import choice
html_template = '''
<p>mai giỗ tổ h&ugrave;ng vương Trần Duy Hưng discount {{discount}} anh ơiiiiii</p>'''
discount_list = ["gái xinh trẻ đẹp", "bà già u40", "sinh viên"]
discount = choice(discount_list)
html_content = html_template.replace("{{discount}}", discount)
mail = GMail("levinhphuc37@gmail.com","01693962187")
msg = Message("bcs đi :v", to="c4e.201708@gmail.com", html=html_content)
mail.send(msg)

