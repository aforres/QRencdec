import streamlit as st
import cv2 as cv

st.header("QRcodePlus - Run Encode and then Decode")
raw_text = st.text_area("Text here") 

def run_encode(raw_text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
        
        
    )
    
    

    qr.add_data(raw_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",
                        back_color="white").convert('RGB')
    img.save("sample.png")
    st.image("sample.png")



   

    im = cv.imread('sample.png')
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)

    logo_display = Image.open('profile.png')
    
    logo_display.thumbnail((60,60))

    logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
                (img.size[1] - logo_display.size[1]) // 2)

    img.paste(logo_display, logo_pos)

    print(retval)
    img.save("sample2.png")
    st.image("sample2.png")
    st.write(retval)


st.button('Encode and Decode', on_click=run_encode(raw_text))


                
