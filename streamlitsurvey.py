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
<model-viewer src="../../assets/ShopifyModels/Chair.glb" poster="../../assets/ShopifyModels/Chair.webp" shadow-intensity="1" ar camera-controls touch-action="pan-y" alt="A 3D model carousel">
  
  <button slot="ar-button" id="ar-button">
    View in your space
  </button>

  <div id="ar-prompt">
    <img src="../../assets/hand.png">
  </div>

  <button id="ar-failure">
    AR is not tracking!
  </button>

  <div class="slider">
    <div class="slides">
      <button class="slide selected" onclick="switchSrc(this, 'Chair')" style="background-image: url('../../assets/ShopifyModels/Chair.webp');">

      </button><button class="slide" onclick="switchSrc(this, 'Mixer')" style="background-image: url('../../assets/ShopifyModels/Mixer.webp');">

      </button><button class="slide" onclick="switchSrc(this, 'GeoPlanter')" style="background-image: url('../../assets/ShopifyModels/GeoPlanter.webp');">
      
      </button><button class="slide" onclick="switchSrc(this, 'ToyTrain')" style="background-image: url('../../assets/ShopifyModels/ToyTrain.webp');">
      
      </button><button class="slide" onclick="switchSrc(this, 'Canoe')" style="background-image: url('../../assets/ShopifyModels/Canoe.webp');">    
    </button></div>
  </div>
</model-viewer>

<script type="module">
  const modelViewer = document.querySelector("model-viewer");

  window.switchSrc = (element, name) => {
    const base = "../../assets/ShopifyModels/" + name;
    modelViewer.src = base + '.glb';
    modelViewer.poster = base + '.webp';
    const slides = document.querySelectorAll(".slide");
    slides.forEach((element) => {element.classList.remove("selected");});
    element.classList.add("selected");
  };

  document.querySelector(".slider").addEventListener('beforexrselect', (ev) => {
    // Keep slider interactions from affecting the XR scene.
    ev.preventDefault();
  });
</script>

<style>
  /* This keeps child nodes hidden while the element loads */
  :not(:defined) > * {
    display: none;
  }

  model-viewer {
    background-color: #eee;
    overflow-x: hidden;
  }

  #ar-button {
    background-image: url(../../assets/ic_view_in_ar_new_googblue_48dp.png);
    background-repeat: no-repeat;
    background-size: 20px 20px;
    background-position: 12px 50%;
    background-color: #fff;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    white-space: nowrap;
    bottom: 132px;
    padding: 0px 16px 0px 40px;
    font-family: Roboto Regular, Helvetica Neue, sans-serif;
    font-size: 14px;
    color:#4285f4;
    height: 36px;
    line-height: 36px;
    border-radius: 18px;
    border: 1px solid #DADCE0;
  }

  #ar-button:active {
    background-color: #E8EAED;
  }

  #ar-button:focus {
    outline: none;
  }

  #ar-button:focus-visible {
    outline: 1px solid #4285f4;
  }

  @keyframes circle {
    from { transform: translateX(-50%) rotate(0deg) translateX(50px) rotate(0deg); }
    to   { transform: translateX(-50%) rotate(360deg) translateX(50px) rotate(-360deg); }
  }

  @keyframes elongate {
    from { transform: translateX(100px); }
    to   { transform: translateX(-100px); }
  }

  model-viewer > #ar-prompt {
    position: absolute;
    left: 50%;
    bottom: 175px;
    animation: elongate 2s infinite ease-in-out alternate;
    display: none;
  }

  model-viewer[ar-status="session-started"] > #ar-prompt {
    display: block;
  }

  model-viewer > #ar-prompt > img {
    animation: circle 4s linear infinite;
  }

  model-viewer > #ar-failure {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 175px;
    display: none;
  }

  model-viewer[ar-tracking="not-tracking"] > #ar-failure {
    display: block;
  }

  .slider {
    width: 100%;
    text-align: center;
    overflow: hidden;
    position: absolute;
    bottom: 16px;
  }

  .slides {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }

  .slide {
    scroll-snap-align: start;
    flex-shrink: 0;
    width: 100px;
    height: 100px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #fff;
    margin-right: 10px;
    border-radius: 10px;
    border: none;
    display: flex;
  }

  .slide.selected {
    border: 2px solid #4285f4;
  }

  .slide:focus {
    outline: none;
  }

  .slide:focus-visible {
    outline: 1px solid #4285f4;
  }

</style>
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
