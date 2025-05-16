import streamlit as st
import time

st.set_page_config(page_title="Sorpresa", page_icon='🎂')


if 'giusto_premuto' not in st.session_state:
    st.session_state.giusto_premuto = False
# Inizializza una variabile di stato se non esiste
if 'wrong_button_clicked' not in st.session_state:
    st.session_state.wrong_button_clicked = False
if 'counter' not in st.session_state:
    st.session_state.counter=0

if st.session_state.giusto_premuto:
    st.markdown("<h1 style='text-align: center; color: red;'>🎉 AUGURI! 🎉</h1>", unsafe_allow_html=True)
    st.balloons()
    if st.session_state.counter< 7:
        st.caption('Complimenti, non pensavo saresti stato così veloce!')
    if st.session_state.counter> 7 and st.session_state.counter <= 14:
        st.caption("Veloce, non velocissimo, bravo!")
    if st.session_state.counter> 14 and st.session_state.counter <= 21:
        st.caption("Potevi fare di meglio...ma bravo")
    if st.session_state.counter> 21 and st.session_state.counter <= 35:
        st.caption("Un po' lentino eh, ci siamo arrivati finalmente")
    if st.session_state.counter== 36:
        st.caption("Finalmente! più aiuti di così non potevo dartene")
    if st.session_state.counter> 36:
        st.caption("Penso che dovresti farti controllare il cervello.")
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
        st.session_state.counter +=1
        if st.session_state.counter <= 3:
            st.write("### ❌ Riprova...")
            time.sleep(1)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter== 4:
            st.write("### ❌ Riprova...")
            st.caption('Forza!')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter == 5:
            st.write("### ❌ Riprova...")
            st.caption('Ce la puoi fare!')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter==6:
            st.write("### ❌ Riprova...")
            st.caption('Ci stiamo annoiandoo')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False    
        if st.session_state.counter>= 7 and st.session_state.counter <= 14:
            st.write("### ❌ Riprova...")
            st.caption('Non serve premerli tutti, pensa bene e RIPROVA')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter>14 and st.session_state.counter <= 21:
            st.write("### ❌ Riprova...")
            st.caption('Non stai guardando nel posto giusto! RIPROVA')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter>21 and st.session_state.counter <= 35:
            st.write("### ❌ Riprova...")
            st.caption('Non stai guardando il BOTTONE giusto! RIPROVA')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter==36:
            st.write("### ❌ Riprova...")
            st.caption('Guarda la scritta !! ')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        if st.session_state.counter>36:
            st.write("### ❌ Riprova...")
            st.caption('Guarda la CAZZO DI SCRITTA !! ')
            time.sleep(2)  # breve pausa per far vedere il messaggio
            st.session_state.wrong_button_clicked=False
        st.rerun()

    col1_new,col2_new,col3_new,col4_new,col5_new,col6_new = st.columns(6,vertical_alignment="top")

    col1_new.button('🍆',key='b1_col1',use_container_width=True,on_click=riprova)
    col1_new.button('pick me!',key='b2_col1',use_container_width=True,on_click=riprova)
    col1_new.button('chose me!',key='b3_col1',use_container_width=True,on_click=riprova)
    col1_new.button('love me!',key='b4_col1',use_container_width=True,on_click=riprova)
    col1_new.button('😏',key='b5_col1',use_container_width=True,on_click=riprova)
    col1_new.button('dai',key='b6_col1',use_container_width=True,on_click=riprova)

    col2_new.button('non me!',key='b1_col2',use_container_width=True,on_click=riprova)
    col2_new.button('🌸',key='b2_col2',use_container_width=True,on_click=riprova)
    col2_new.button('eccomi!',key='b3_col2',use_container_width=True,on_click=riprova)
    col2_new.button('🤡',key='b4_col2',use_container_width=True,on_click=riprova)
    col2_new.button('pigia!',key='b5_col2',use_container_width=True,on_click=riprova)
    col2_new.button('daje!',key='b6_col2',use_container_width=True,on_click=riprova)

    col3_new.button('cmon!',key='b1_col3',use_container_width=True,on_click=riprova)
    col3_new.button('veloce!',key='b2_col3',use_container_width=True,on_click=riprova)
    col3_new.button('🦀',key='b3_col3',use_container_width=True,on_click=riprova)
    col3_new.button('boom!',key='b4_col3',use_container_width=True,on_click=riprova)
    col3_new.button('☠️',key='b5_col3',use_container_width=True,on_click=riprova)
    col3_new.button('no!',key='b6_col3',use_container_width=True,on_click=riprova)

    col4_new.button('☘️',key='b1_col4',use_container_width=True,on_click=riprova)
    col4_new.button('noo!',key='b2_col4',use_container_width=True,on_click=riprova)
    col4_new.button('polizia!',key='b3_col4',use_container_width=True,on_click=riprova)
    col4_new.button('nooo!',key='b4_col4',use_container_width=True,on_click=riprova)
    col4_new.button('🦵',key='b5_col4',use_container_width=True,on_click=riprova)
    col4_new.button('🦖',key='b6_col4',use_container_width=True,on_click=riprova)

    col5_new.button('lirilì!',key='b1_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🥠',key='b2_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🤠',key='b3_col5',use_container_width=True,on_click=riprova)
    col5_new.button('larilà!',key='b4_col5',use_container_width=True,on_click=riprova)
    col5_new.button('lesgoski!',key='b5_col5',use_container_width=True,on_click=riprova)
    col5_new.button('🤭',key='b6_col5',use_container_width=True,on_click=riprova)

    col6_new.button('bro!',key='b1_col6',use_container_width=True,on_click=riprova)
    col6_new.button('SAHUR!',key='b2_col6',use_container_width=True,on_click=riprova)
    col6_new.button('manco io!',key='b3_col6',use_container_width=True,on_click=riprova)
    col6_new.button('👽',key='b4_col6',use_container_width=True,on_click=riprova)
    col6_new.button('💎',key='b5_col6',use_container_width=True,on_click=riprova)
    col6_new.button('please!',key='b6_col6',use_container_width=True,on_click=riprova)