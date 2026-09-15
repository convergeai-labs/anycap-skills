# Music and audio production

## Music Production

### Text-to-Music

```bash
anycap music generate \
  --prompt "upbeat electronic track with synth leads and driving bass, 120 BPM" \
  --model <model-id> \
  -o background-track.mp3
```

Music generation may return multiple clips. Extract the first:

```bash
anycap music generate --prompt "..." --model <model-id> -o track.mp3 \
  | jq -r '.outputs[0].local_path'
```

### Music Tips

- Be specific about genre, tempo, instruments, and mood in prompts.
- Music generation takes 30-90s. Use async execution when possible.
- Check model parameters via schema -- some models support `duration`, `genre`, `tags`.

### Field Incidents (2026-09)

- **`duration` is seconds at the CLI even when the schema text says
  milliseconds.** A ms value passed through unconverted can be rejected
  upstream (e.g. `music_length_ms must be between 3000 and 600000`). Pass
  seconds, then verify the artifact with `afinfo` — never trust the requested
  duration without measuring. Some models silently ignore `duration` and
  return a full-length track.
- **Output may arrive as a multipart body, not a bare audio file.** If `file`
  reports `data`, look for a `------boundary…` wrapper: the payload starts at
  the audio magic (ID3/RIFF/ftyp/OggS) and ends before the closing boundary,
  possibly with padding bytes. Extract deterministically and validate with a
  full ffmpeg decode.
- **Same-prompt bake-off selection**: when quality gates tie, decide on
  contract adherence (exact duration, requested format), not on vibes.
- Field evidence: [Signal Drift entry](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-09-signal-drift-focus-track)
  in anycap-examples.

## Audio Production

Audio generation covers speech, dialogue, and complete audio scenes generated
from text or reference media. A scene can combine voices, background music,
ambience, and sound effects; use the music capability when the deliverable is
primarily a song or instrumental track.

Discover the live model and schema first:

```bash
anycap audio models
anycap audio models <model-id> schema --mode text-to-audio
```

```bash
# Text to speech/dialogue/scene
anycap audio generate \
  --prompt 'A calm narrator says: "Welcome to the evening program." Soft room ambience underneath.' \
  --model <model-id> \
  --mode text-to-audio \
  -o evening-introduction.mp3

# Reference-guided new performance
anycap audio generate \
  --prompt "create a new spoken welcome with the reference delivery style" \
  --model <model-id> \
  --mode audio-to-audio \
  --param audios=./reference.wav \
  -o guided-welcome.mp3

# Image-guided narrated scene
anycap audio generate \
  --prompt "a guide describes this scene while matching ambience plays underneath" \
  --model <model-id> \
  --mode image-to-audio \
  --param images=./scene.png \
  -o narrated-scene.mp3
```

Use only controls advertised by the live schema. Inspect actual MIME type,
duration, nonblank audio, requested speech/content, unintended private material,
and subtitle output when requested. Audio understanding remains available via
`anycap actions audio-read`.
