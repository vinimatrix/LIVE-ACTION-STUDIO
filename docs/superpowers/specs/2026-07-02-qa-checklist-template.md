# Quality Assurance Checklist Template
## For AI Live Action Studio Asset Validation

This template provides a standardized quality assurance checklist for validating AI-generated assets in the AI Live Action Studio pipeline. It incorporates the consistency rules and best practices from our documentation.

## Table of Contents
1. [Universal QA Checklist](#1-universal-qa-checklist)
2. [Asset-Specific Checklists](#2-asset-specific-checklists)
3. [Consistency Verification](#3-consistency-verification)
4. [Technical Validation](#4-technical-validation)
5. [Audio-Visual Synchronization](#5-audio-visual-synchronization)
6. [Usage Instructions](#6-usage-instructions)

---

## 1. Universal QA Checklist

Apply these checks to ALL assets (image, video, audio, etc.):

### 1.1 Identity Verification
- [ ] **Character Identity**: If character-present, matches established appearance from character bible
- [ ] **Environment Identity**: If environment-present, matches established location canon
- [ ] **Identity Preservation**: No unintended changes to core features (face shape, ethnicity, etc.)

### 1.2 Technical Compliance
- [ ] **Resolution**: Meets minimum requirement (3840x2160 for final output)
- [ ] **Frame Rate**: Correct fps (24.000 for cinematic, or specified alternative)
- [ ] **Bit Depth**: 10-bit color minimum for video/image
- [ ] **File Format**: Correct format (MP4, WAV, PNG, etc. as specified)
- [ ] **Color Space**: DCI-P3 for video, sRGB/AdobeRGB for stills as appropriate

### 1.3 Source Attribution
- [ ] **Reference Citations**: All required @reference: tags present in prompt metadata
- [ ] **Technical Specs**: Model, seed, steps, cfg_scale documented
- [ ] **Style Modifiers**: Correct series-specific modifiers applied
- [ ] **Quality Boosters**: Required quality enhancers present

### 1.4 Content Appropriateness
- [ ] **Narrative Fit**: Content appropriate for scene/story point
- [ ] **Wardrobe Correctness**: Matches character's current status/rank
- [ ] **Expression Accuracy**: Matches emotional context of scene
- [ ] **Pose Logic**: Physically plausible and intention-aligned
- [ ] **Environment Consistency**: Lighting, time of day, weather coherent

---

## 2. Asset-Specific Checklists

### 2.1 Image Generation (Reference Frames, Key Stills)
- [ ] **Sharpness**: Subject in focus where intended (per lens specs)
- [ ] **Exposure**: Properly exposed (no blown highlights or crushed shadows unless intentional)
- [ ] **Color Accuracy**: Skin tones, clothing colors match references under same lighting
- [ ] **Background Consistency**: Environmental elements match referenced location
- [ ] **Artifact Check**: No AI-specific artifacts (morphing, duplication, nonsense text)
- [ ] **Composition**: Follows rule of thirds/framing guidelines from cinematography guide
- [ ] **Reference Overlay**: When aligned with reference image, key features match within 2px tolerance

### 2.2 Video Segments
- [ ] **Temporal Consistency**: No sudden jumps in appearance, position, or lighting between frames
- [ ] **Motion Naturalism**: Movement follows biomechanics and physics principles
- [ ] **Expression Continuity**: Facial expressions transition naturally (no popping)
- [ ] **Hair/Cloth Simulation**: Secondary motion follows primary movement realistically
- [ ] **Lighting Consistency**: Light direction/intensity stable unless intentionally changing
- [ ] **Background Lock**: Static elements remain fixed (no drifting walls/furniture)
- [ ] **Edge Integrity**: No haloing, fringing, or separation at subject/background boundaries
- [ ] **Motion Blur**: Appropriate for speed (none for slow motion, correct amount for fast action)

### 2.3 Audio Elements (Voice, Music, SFX)
- [ ] **Voice Identity**: Matches specified voice ID/parameters (pitch, timbre, accent)
- [ ] **Emotional Accuracy**: Performance matches emotional context of scene
- [ ] **Pronunciation**: Clear articulation (unless character trait indicates otherwise)
- [ ] **Pacing**: Appropriate speed for content (not rushed or dragging)
- [ ] **Background Noise**: Consistent room tone/noise floor (unless intentional change)
- [ ] **Clipping**: No audio distortion (peaks below 0dBFS)
- [ ] **Dynamic Range**: Appropriate contrast between loud/quiet passages
- [ ] **Lip Sync Readiness**: Visible mouth movements correspond to phonemes (for voice)

### 2.4 Music Tracks
- [ ] **Thematic Alignment**: Matches emotional arc specified in prompt
- [ ] **Instrumentation**: Correct instruments used as specified
- [ ] **Arrangement**: Proper intro/development/resolution structure
- [ ] **Mix Balance**: No instrument overpowering others unless intended
- [ ] **Loop Points**: Seamless if intended to loop (no audible click/pop)
- [ ] **Frequency Balance**: Appropriate bass/mid/treble distribution for scene mood

### 2.5 Sound Effects
- [ ] **Source Authenticity**: Sound matches described action (sword cut sounds like sword, etc.)
- [ ] **Spatial Placement**: Appropriate stereo/mono positioning for 3D space
- [ ] **Reverb**: Matches environment size/material (small room vs. large hall)
- [ ] **Duration**: Correct length for action (neither truncated nor overly extended)
- [ ] **Layering**: Multiple SFX elements properly balanced when combined
- [ ] **Fade In/Out**: Natural attack and decay (no clicks unless intentional)

### 2.6 Visual Effects (VFX) Elements
- [ ] **Integration**: Elements blend naturally with background (correct edges, lighting)
- [ ] **Interaction**: Properly affects environment (casts shadows, illuminates nearby objects)
- [ ] **Physics**: Behaves according to stated properties (fire rises, water flows, etc.)
- [ ] **Consistency**: Same element appears identical across shots when reused
- [ ] **Alpha Quality**: Clean edges, no fringing or premature transparency
- [ ] **Color Matching**: Hue/saturation matches references under same lighting
- [ ] **Animation**: Cyclical or progressive motion appears natural (not robotic)

---

## 3. Consistency Verification

### 3.1 Character Consistency (Across Shots)
- [ ] **Facial Landmarks**: Key points (eyes, nose, mouth corners, jaw) align within 3px tolerance
- [ ] **Head Shape**: Cranium outline matches reference within 2% variation
- [ ] **Hairline**: Frontal and temporal hairlines consistent
- [ ] **Eye Color/Shape**: Iris color, pupil shape, eye opening consistent
- [ ] **Distinguishing Marks**: Scars, tattoos, unique features present/absent as required
- [ ] **Hair Style**: Overall shape, part, flow consistent (accounting for movement/wind)
- [ ] **Build Proportions**: Shoulder width, waist, height ratios consistent

### 3.2 Environment Consistency (Across Shots)
- [ ] **Lighting Direction**: Key light angle consistent (unless time of day change justified)
- [ ] **Light Quality**: Hard/soft shadow quality matches time/weather
- [ ] **Color Temperature**: White balance consistent (unless mixed lighting specified)
- [ ] **Background Elements**: Permanent fixtures (windows, doors, furniture) in same positions
- [ ] **Weather Effects**: Rain/snow/fog density and direction consistent
- [ ] **Time Indicators**: Shadow length/position logical for time of day
- [ ] **Perspective**: Vanishing points, scale consistent across shots

### 3.3 Wardrobe Continuity
- [ ] **Outfit Match**: Exact clothing items match character bible for story point
- [ ] **Fit & Drape**: Fabric falls naturally on body type
- [ ] **Accessories**: Correct items present (watch, jewelry, etc.) in correct positions
- [ ] **Wear Patterns**: Dirt, wrinkles, wear match activity level and time since last change
- [ ] **Layering Logic**: Undergarments/overgarments logically sequenced
- [ ] **Color Fastness**: Dyes don't suddenly change shade between shots

### 3.4 Prop & Object Consistency
- [ ] **Identity**: Objects match description (correct weapon, tool, device)
- [ ] **Condition**: Wear/damage matches usage history and story events
- [ ] **Placement**: Objects in logical locations based on character actions
- [ ] **Lighting Interaction**: Objects cast/receive light consistently with environment
- [ ] **Scale**: Object size consistent relative to character and environment
- [ ] **Material Properties**: Reflectivity, transparency, texture appropriate to material

---

## 4. Technical Validation

### 4.1 Resolution & Aspect Ratio
- [ ] **Native Resolution**: 3840x2160 (16:9) or approved variant
- [ ] **Scaling**: No unnecessary upscaling/downscaling in pipeline
- [ ] **Pixel Aspect**: Square pixels (1:1) unless anamorphic intentionally used
- [ ] **Safe Titles**: Critical action within 90% action safe, text within 80% title safe

### 4.2 Frame Rate & Temporal
- [ ] **Frame Consistency**: Exact frame rate maintained (no dropped/duplicated frames)
- [ ] **Timecode**: Continuous, non-dropping timecode if applicable
- [ ] **Keyframe Interval**: Appropriate for codec (typically 1-2 seconds for delivery)
- [ ] **Motion Cadence**: Consistent 24fps look (no accidental 30fps "video" look)

### 4.3 Color & Encoding
- [ ] **Color Space**: Correctly tagged (DCI-P3 for cinema, Rec.709 for broadcast if needed)
- [ ] **Transfer Function**: PQ (ST 2084) for HDR, BT.1886 for SDR if applicable
- [ ] **Bit Depth**: Maintained throughout pipeline (no banding from 8-bit conversion)
- [ ] **Compression Artifacts**: Minimal blocking, mosquito noise, or blur from compression
- [ ] **Legal Levels**: Luma/chroma within broadcast-safe limits if required

### 4.4 Audio Technical
- [ ] **Sample Rate**: 48kHz (or 96kHz for masters) as specified
- [ ] **Bit Depth**: 24-bit minimum for production, 16-bit for delivery if required
- [ ] **Channel Configuration**: Correct (stereo, 5.1, etc.)
- [ ] **Phase Coherence**: No phase cancellation issues in stereo/mono summation
- [ ] **Loudness**: Integrated LUFS within target range (-23 LUFS for broadcast, -14 to -16 for streaming)
- [ ] **True Peak**: Below -1dBTP to prevent inter-sample clipping

---

## 5. Audio-Visual Synchronization

### 5.1 Lip Sync (For Dialogue)
- [ ] **Viseme Accuracy**: Mouth shapes correspond to phonemes (with allowances for speech rate)
- [ ] **Temporal Alignment**: Audio events lead/lag visual by no more than 3 frames (±125ms at 24fps)
- [ ] **Emotional Match**: Vocal intensity matches facial expression intensity
- [ ] **Breathing Sounds**: Inhalation audible before speech where appropriate
- [ ] **Consonant Plosives**: "p", "b", "t", "d" sounds correlate with lip closure/release
- [ ] **Vowel Sustain**: Mouth openness corresponds to vowel duration/openness

### 5.2 Music Cue Points
- [ ] **Hit Points**: Musical accents align with visual actions (punches, impacts, reveals)
- [ ] **Mood Shifts**: Musical changes correspond to emotional/narrative shifts
- [ ] **Source Music**: Diegetic music (radios, instruments) spatially placed correctly
- [ ] **Swells/Decrescendos**: Musical intensity builds/releases with visual tension

### 5.3 Sound Effect Timing
- [ ] **Impact Sync**: SFX transients align with visual impact/contact frames
- [ ] **Action Precedence**: Sounds slightly precede or coincide with visible action (per psychoacoustics)
- [ ] **Reverb Tail**: Decay matches environment size and material
- [ ] **Foley Synchronization**: Footsteps, cloth movement, prop handling precisely timed
- [ ] **Environmental Ambience**: Background sounds continuous and logically sourced

### 5.4 Musical Underscore
- [ ] **Speech Clearance**: Music volume reduced during dialogue (typically -18 to -24dB under voice)
- [ ] **Emotional Support**: Melody/harmony supports, never contradicts, on-screen emotion
- [ ] **Source Transition**: Seamless shifts between score, source music, and silence
- [ ] **Thematic Consistency**: Leitmotifs, instruments, styles consistent with character/theme

---

## 6. Usage Instructions

### 6.1 When to Apply This Checklist
```
- After every asset generation (image, video, audio)
- Before asset enters editing/compositing pipeline
- After any significant modification (color grading, VFX, audio mixing)
- Prior to final render/export
- During daily review sessions (random sampling of that day's output)
- As part of formal delivery approval process
```

### 6.2 Scoring System
```
PASS: All applicable items checked (0 deviations)
MINOR: 1-2 non-critical items unchecked (can proceed with notes)
MAJOR: 3-5 items unchecked or 1+ critical item (requires correction before proceeding)
CRITICAL: 6+ items unchecked or multiple critical items (reject and regenerate)
```

### 6.3 Critical Items (Must Never Be Unchecked)
```
- Character identity violations
- Resolution/frame rate deviations
- Missing required references
- Voice identity mismatches
- Impossible physics/anatomical errors
- Wardrobe inconsistencies with story timeline
- Audio clipping or distortion
- Missing audio for dialogue scenes
```

### 6.4 Reporting Format
```
ASSET ID: [shot001_v02]
ASSET TYPE: [video_segment]
REVIEWER: [initials]
DATE: [timestamp]
STATUS: [PASS/MINOR/MAJOR/CRITICAL]
NOTES: 
  - [Specific observations for any unchecked items]
  - [Suggested corrections if applicable]
  - [Overall impression: excellent/good/acceptable/needs work]
```

### 6.5 Escalation Path
```
1. First failure: Artist/technician corrects and resubmits
2. Second failure: Lead artist/supervisor reviews
3. Third failure: Creative director review + possible pipeline adjustment
4. Pattern of failures: Process review and potential retraining
```

---

## 7. Integration with Pipeline

### 7.1 Points of Application
```
PRE-GENERATION:
  - Verify prompt includes all required references and technical specs
  - Check character/environment/wardrobe appropriateness for scene

POST-GENERATION (PRE-COMPOSITING):
  - Apply full checklist to raw generated asset
  - Flag any issues for regeneration before investing in post-production

POST-COMPOSITING:
  - Verify integration maintains all individual asset qualities
  - Check that combined elements don't introduce new inconsistencies
  - Validate final color grading doesn't violate referenced appearances

FINAL DELIVERY:
  - Apply strictest version of checklist (zero tolerance for critical errors)
  - Prepare QC report for client/stakeholder review
```

### 7.2 Automated Checks (Where Possible)
Consider implementing these automated validations:
```
- Perceptual hashing for frame-to-reference comparison
- Optical flow analysis for motion consistency
- Audio waveform analysis for clipping and loudness
- Metadata verification for required tags
- Resolution/fps verification through ffprobe/ffmpeg
- Color space validation through appropriate tools
```

---

## Conclusion

This QA checklist transforms quality assurance from a subjective opinion-based process into an objective, standards-driven evaluation system. By consistently applying these checks:

1. **Consistency is measurable**: Deviations can be quantified and tracked
2. **Feedback is actionable**: Specific, clear notes guide corrections
3. **Standards are maintainable**: Evolution of standards is documented and transparent
4. **Trust is built**: Stakeholders know exactly what quality means in this context
5. **Efficiency improves**: Less time wasted on subjective debates, more on productive creation

Remember: The goal is not to eliminate all creative interpretation, but to ensure that interpretation serves the story and maintains the trust of the audience through unwavering consistency in the presentation of characters, worlds, and narratives.

This checklist should be reviewed and updated quarterly to incorporate new lessons learned and evolving production standards.