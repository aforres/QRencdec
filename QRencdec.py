import streamlit as st
import qrcode

st.header("QRCode+ - encoder")

def testfn():
    raw_text = st.text_area("Enter message here and click button to encode") 
    
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
    img.save("image_folder/sample.png")
    st.image("image_folder/sample.png")


if st.button('Click Me'):
    testfn()



# im = cv.imread('sample.png')
# det = cv.QRCodeDetector()
# retval, points, straight_qrcode = det.detectAndDecode(im)

# logo_display = Image.open('profile.png')

# logo_display.thumbnail((60,60))

# logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
#             (img.size[1] - logo_display.size[1]) // 2)

# img.paste(logo_display, logo_pos)

# print(retval)
# img.save("sample2.png")
# st.image("sample2.png")
# st.write(retval)


# #st.button('Encode and Decode', on_click=run_encode(raw_text))


                
