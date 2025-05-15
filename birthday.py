import streamlit as st
import time

st.set_page_config(page_title="Sorpresa", page_icon='🎂')


if 'giusto_premuto' not in st.session_state:
    st.session_state.giusto_premuto = False
# Inizializza una variabile di stato se non esiste
if 'wrong_button_clicked' not in st.session_state:
    st.session_state.wrong_button_clicked = False

if st.session_state.giusto_premuto:
    st.markdown("<h1 style='text-align: center; color: red;'>🎉 AUGURI! 🎉</h1>", unsafe_allow_html=True)
    st.balloons()
    st.caption("ci hai messo un po', ma ci sei riuscito")
    st.stop()


# Funzione da chiamare quando si clicca un bottone sbagliato
def riprova():
    st.session_state.wrong_button_clicked = True

st.write("# Facciamo un gioco!")
col1,col2,col3,col4,col5,col6,col7 = st.columns([0.05,0.03,0.07,0.06,0.06,0.07,0.33],vertical_alignment="center")
col1.write('Trova')
col2.write('il')
giusto=col3.button('bottone',type="tertiary")
col4.write('giusto')
col5.write('nella')
col6.write('pagina')


# Se è stato premuto il bottone giusto in precedenza, mostra solo AUGURI
if giusto:
    st.session_state.giusto_premuto = True
    st.rerun()
else:
    # Se è stato premuto un bottone sbagliato, mostra messaggio e resetta
    if st.session_state.wrong_button_clicked:
        st.write("### ❌ Riprova...")
        time.sleep(1)  # breve pausa per far vedere il messaggio
        st.session_state.wrong_button_clicked=False
        st.rerun()

    col1_new,col2_new,col3_new,col4_new,col5_new,col6_new = st.columns(6,vertical_alignment="top")

    bottone=col1_new.button('🍆',key='b1_col1',use_container_width=True,on_click=riprova)
    bottone=col1_new.button('pick me!',key='b2_col1',use_container_width=True,on_click=riprova)
    col1_new.button('chose me!',key='b3_col1',use_container_width=True,on_click=riprova)
    col1_new.button('love me!',key='b4_col1',use_container_width=True,on_click=riprova)
    col1_new.button('😏',key='b5_col1',use_container_width=True,on_click=riprova)
    col1_new.button('dai',key='b6_col1',use_container_width=True,on_click=riprova)

    col2_new.button('non me!',key='b1_col2',use_container_width=True,on_click=riprova)
    col2_new.button('🌸',key='b2_col2',use_container_width=True,on_click=riprova)
    col2_new.button('love me!',key='b3_col2',use_container_width=True,on_click=riprova)
    col2_new.button('🤡',key='b4_col2',use_container_width=True,on_click=riprova)
    col2_new.button('love me!',key='b5_col2',use_container_width=True,on_click=riprova)
    col2_new.button('dai!',key='b6_col2',use_container_width=True,on_click=riprova)

    col3_new.button('allora!',key='b1_col3',use_container_width=True,on_click=riprova)
    col3_new.button('su! su!',key='b2_col3',use_container_width=True,on_click=riprova)
    col3_new.button('🦀',key='b3_col3',use_container_width=True,on_click=riprova)
    col3_new.button('hurry up!',key='b4_col3',use_container_width=True,on_click=riprova)
    col3_new.button('☠️',key='b5_col3',use_container_width=True,on_click=riprova)
    col3_new.button('hurry up!',key='b6_col3',use_container_width=True,on_click=riprova)

    col4_new.button('☘️',key='b1_col4',use_container_width=True,on_click=riprova)
    col4_new.button('hurry up!',key='b2_col4',use_container_width=True,on_click=riprova)
    col4_new.button('allora!',key='b3_col4',use_container_width=True,on_click=riprova)
    col4_new.button('hurry up!',key='b4_col4',use_container_width=True,on_click=riprova)
    col4_new.button('🦵',key='b5_col4',use_container_width=True,on_click=riprova)
    col4_new.button('🦖',key='b6_col4',use_container_width=True,on_click=riprova)

    col5_new.button('allora!',key='b1_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🥠',key='b2_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🤠',key='b3_col5',use_container_width=True,on_click=riprova)
    col5_new.button('hurry up!',key='b4_col5',use_container_width=True,on_click=riprova)
    col5_new.button('allora!',key='b5_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🤭',key='b6_col5',use_container_width=True,on_click=riprova)

    col6_new.button('allora!',key='b1_col6',use_container_width=True,on_click=riprova)
    col6_new.button('hurry up!',key='b2_col6',use_container_width=True,on_click=riprova)
    col6_new.button('allora!',key='b3_col6',use_container_width=True,on_click=riprova)
    col6_new.button('👽',key='b4_col6',use_container_width=True,on_click=riprova)
    col6_new.button('💎',key='b5_col6',use_container_width=True,on_click=riprova)
    col6_new.button('hurry up!',key='b6_col6',use_container_width=True,on_click=riprova)