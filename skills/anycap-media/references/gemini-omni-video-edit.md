# Gemini Omni video edit through AnyCap

Use only when the live AnyCap catalog exposes a Gemini Omni model with an
`edit-video`-style mode. Preview model names and fields are mutable; verify the
catalog, selected schema and upstream model documentation at run time.

## Fit

Prefer this route for one narrow change to an existing short video: replace or
remove an object, use a product reference image, relight/restyle a scene, or
preserve a person and camera motion while changing one element. Choose another
route when the request requires long-form generation, multi-video state,
first/last-frame controls or provider-only conversation state not exposed by
the live schema.

## Workflow

1. Inspect the source video, references, duration, aspect ratio and output path.
2. Run `anycap video models`, select the matching model, then inspect only its
   edit schema.
3. Write one narrow prompt: requested change, exact reference role, protected
   identity/scene/motion/audio properties, and “keep everything else the same.”
4. Pass the source and references only with fields present in the live schema.
5. Inspect the MP4 with `ffprobe`, representative frames, direct playback and
   an AnyCap video-read when useful.
6. Retry only for a named failure such as identity drift, hand artifacts,
   flicker, reference mismatch or unintended scene change.

Return the actual command summary, local output, QA checks, limitations and one
concrete next prompt when the result does not pass. Do not claim that a preview
model preserved content without inspecting the rendered video.
