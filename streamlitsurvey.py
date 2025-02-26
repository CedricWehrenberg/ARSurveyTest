import streamlit as st
import datetime
import json

# Titel der Umfrage
st.set_page_config(page_title="AR Möbel-Umfrage", layout="centered")

st.title("🛋️ Augmented Reality Möbel-Umfrage")
st.write("**Bitte testen Sie das Möbelstück in AR und beantworten Sie anschließend die Fragen.**")

# Model Viewer (AR-Modell einbinden)
st.subheader("📱 Möbelstück in AR platzieren")
st.write("Klicken Sie auf das Möbelstück und wählen Sie 'In AR anzeigen', um es in Ihrem Raum zu platzieren.")

model_html = """
<model-viewer src="https://modelviewer.dev/shared-assets/models/Chair.glb" 
    ar ar-modes="webxr scene-viewer quick-look" 
    camera-controls auto-rotate style="width: 100%; height: 400px;">
</model-viewer>
"""

st.components.v1.html(model_html, height=450)

# Umfrage-Fragen
st.subheader("📝 Ihre Meinung zum Möbelstück")

zufriedenheit = st.slider("Wie zufrieden sind Sie mit dem Produkt in AR? (1 = Gar nicht zufrieden, 5 = Sehr zufrieden)", 1, 5, 3)

realismus = st.radio("Wie realistisch wirkte das Möbelstück in AR?", 
                     ["Sehr unrealistisch", "Eher unrealistisch", "Neutral", "Eher realistisch", "Sehr realistisch"])

kaufentscheidung = st.radio("Würde AR Ihre Kaufentscheidung beeinflussen?", 
                            ["Ja, positiv", "Nein", "Ja, negativ"])

kommentar = st.text_area("Haben Sie Anmerkungen zur AR-Erfahrung?")

# Antworten speichern
if st.button("✅ Antworten absenden"):
    umfrage_daten = {
        "timestamp": str(datetime.datetime.now()),
        "zufriedenheit": zufriedenheit,
        "realismus": realismus,
        "kaufentscheidung": kaufentscheidung,
        "kommentar": kommentar
    }

    # JSON speichern
    with open("umfrage_ergebnisse.json", "a") as f:
        json.dump(umfrage_daten, f, indent=4)
        f.write("\n")

    st.success("Danke für Ihre Teilnahme! 😊")
