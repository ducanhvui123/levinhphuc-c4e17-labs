from gmail import GMail, Message
import datetime
now = datetime.datetime.now()

html_template ='''
<p> Chao Anh<span style="color #ff0000: "><strong> Huydeptrai</strong></span></p>
<p> hom nay ngu day thay long the bat an nen sang nay em xin nghi, de di kham benh {{benh}}, anh phai cho em nghi khong em lay {{benh}} cho anh day :D</p>
<p> hoc tro yeu quy cua anh.</p>'''
from random import choice 
benh_list =["Giang mai", "Lau", "Kiet ly", "ebola", "ung the vu", "tho huyet", "ghe"]
benh = choice(benh_list)

html_content= html_template.replace("{{benh}}",benh)
mail=GMail("levinhphuc37@gmail.com","01693962187")
msg= Message("Hom nay em om", to='levinhphuc37@gmail.com', html=html_content)
if now.hour > 7:
    mail.send(msg)