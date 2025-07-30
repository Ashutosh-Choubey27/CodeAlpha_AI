function translateText() {
  const inputText = document.getElementById("inputText").value;
  const sourceLang = document.getElementById("sourceLang").value;
  const targetLang = document.getElementById("targetLang").value;

  if (!inputText.trim()) {
    alert("Please enter some text.");
    return;
  }

  fetch("https://google-translate113.p.rapidapi.com/api/v1/translator/text", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-RapidAPI-Key": "7fe8d8c9dcmshf7acd7f51d16340p1a4e1ajsnd3b121618e6c", // 👈 Replace with your own key
      "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    },
    body: JSON.stringify({
      from: sourceLang,
      to: targetLang,
      text: inputText
    })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerText = data.trans;
    })
    .catch(err => {
      console.error("Translation error:", err);
      alert("Something went wrong during translation.");
    });
}



function copyText() {
  const text = document.getElementById("output").innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert("Translated text copied to clipboard!");
  });
}

function speakText() {
  const text = document.getElementById("output").innerText;
  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
}
