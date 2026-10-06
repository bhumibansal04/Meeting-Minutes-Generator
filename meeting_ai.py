from transformers import pipeline

# ✅ Fine-tuned meeting model
model = pipeline(
    "summarization",
    model="knkarthick/MEETING_SUMMARY"
)

def analyze_meeting(text):

    # -------- SUMMARY (trained model) --------
    summary = model(
        text,
        max_length=200,
        min_length=50,
        do_sample=False
    )[0]["summary_text"]

    # -------- RULE-BASED (meeting specific extraction) --------
    decisions = []
    actions = []
    agenda = []
    entities = []

    for line in text.split("."):
        line = line.strip()

        if "decided" in line.lower() or "agreed" in line.lower():
            decisions.append(line)

        if "will" in line.lower() or "task" in line.lower():
            actions.append(line)

        if "discuss" in line.lower() or "agenda" in line.lower():
            agenda.append(line)

        # simple entity extraction
        for word in line.split():
            if word.istitle():
                entities.append(word)

    return {
        "summary": summary,
        "decisions": list(set(decisions)),
        "actions": list(set(actions)),
        "agenda": list(set(agenda)),
        "entities": list(set(entities))
    }