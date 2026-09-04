# Image, video, and audio review

## Scenario 2: Image Collaborative Review

Use when you generated an image and need one or more humans to mark desired changes. This scenario shines with **real-time multi-user collaboration** -- multiple reviewers can open the same URL and annotate simultaneously, seeing each other's cursors and drawings in real-time.

> **Note:** Multi-user collaboration is available for image, video, and audio modes. URL/iframe mode is single-user only.

For the complete image-to-image refinement loop (generate -> annotate -> edit -> iterate), read the `anycap-media` skill.

### Start the Session

```bash
# Single reviewer
anycap annotate hero-banner.png --no-wait -o hero-banner-annotated.png

# Multi-user review -- bind to network so teammates can join
anycap annotate hero-banner.png --no-wait -o hero-banner-annotated.png \
  --bind 0.0.0.0 --port 8888
```

### Collect and Use Feedback

```bash
# Poll for result
anycap annotate poll --session <session_id>

# Extract annotation labels for image-to-image prompt
anycap annotate poll --session <session_id> \
  | jq -r '[.annotations[] | select(.label != "") | "#\(.id): \(.label)"] | join(". ")'

# Apply changes via image-to-image
anycap image generate \
  --prompt "<annotations as prompt>. Keep all other elements unchanged." \
  --model nano-banana-2 \
  --mode image-to-image \
  --param images=./hero-banner-annotated.png \
  -o hero-banner-v2.png

# Clean up
anycap annotate stop --session <session_id>
```

---

## Other Media Types

### Video Review

Use when you generated a video or need the human to review video content. The human can pause the video at any frame and annotate it. The annotated image output is a snapshot of the paused frame with all annotations composited on top.

#### Start

```bash
anycap annotate output.mp4 --no-wait
```

Tell the human to pause at key moments, draw annotations on the frame, optionally record with narration, and click Done when finished.

#### Collect and Analyze

```bash
# Poll for result
anycap annotate poll --session <session_id>

# The annotated_image is a snapshot of the paused frame with annotations
# Read the annotations for spatial feedback on that frame
anycap annotate poll --session <session_id> \
  | jq -r '.annotations[] | "#\(.id) [\(.type)]: \(.label)"'

# If recording exists, analyze it for time-specific feedback
RECORDING=$(anycap annotate poll --session <session_id> | jq -r '.recording // empty')
if [ -n "$RECORDING" ]; then
  anycap actions video-read --file "$RECORDING" \
    --instruction "What feedback did the user give about the video? For each issue, note the timestamp in the original video, what is wrong, and what they want changed."
fi

# Clean up
anycap annotate stop --session <session_id>
```

Video feedback typically maps to regeneration with an adjusted prompt, or specific frame-level edits if the model supports it.

### Audio Review

Use when you generated music or audio and need the human to provide feedback. The human sees an audio player with a drawing canvas below it.

#### Start

```bash
anycap annotate track.mp3 --no-wait
```

Tell the human to play the audio, draw annotations on the canvas to mark time regions or sections, add labels describing desired changes, and click Done when finished.

#### Collect and Analyze

```bash
# Poll for result
anycap annotate poll --session <session_id>

# Read annotation labels -- these describe desired audio changes
anycap annotate poll --session <session_id> \
  | jq -r '.annotations[] | "#\(.id) [\(.type)]: \(.label)"'

# If recording exists, analyze the narrated feedback
RECORDING=$(anycap annotate poll --session <session_id> | jq -r '.recording // empty')
if [ -n "$RECORDING" ]; then
  anycap actions video-read --file "$RECORDING" \
    --instruction "What audio changes did the user request? Note any specific time ranges or sections they mentioned."
fi

# Clean up
anycap annotate stop --session <session_id>
```

Audio feedback typically results in re-generation with an adjusted prompt rather than spatial edits.

---
