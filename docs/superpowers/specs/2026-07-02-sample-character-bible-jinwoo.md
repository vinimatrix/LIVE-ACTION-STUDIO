# Sample Character Bible: Sung Jinwoo (Solo Leveling)
## Implementing Best Practices for Consistent AI Generation (July 2026)

This document demonstrates how to create a professional character bible using the best practices outlined in our AI Video Generation Best Practices guide. It serves as a template for all character bibles in the AI Live Action Studio pipeline.

## Table of Contents
1. [Character Core Profile](#1-character-core-profile)
2. [Reference Library](#2-reference-library)
3. [Voice & Audio Identity](#3-voice--audio-identity)
4. [Wardrobe System](#4-wardrobe-system)
5. [Expression Library](#5-expression-library)
6. [Pose Library](#6-pose-library)
7. [Evolution Tracking](#7-evolution-tracking)
8. [Consistency Rules & "Don'ts"](#8-consistency-rules--donts)
9. [Technical Specifications](#9-technical-specifications)
10. [Usage Guidelines](#10-usage-guidelines)

---

## 1. Character Core Profile

```
CHARACTER: Sung Jinwoo
AGE: 24 (at start of Solo Leveling)
NATIONALITY: Korean
HEIGHT: 182cm
BUILD: Athletic, lean but muscular (builds throughout story)
HAIR: Black, slightly messy, medium length (becomes slightly longer/shaggier as story progresses)
EYES: Dark brown, intense gaze (develops subtle golden glow as powers increase)
SKIN_TONE: Light olive
DISTINGUISHING_MARKS: 
  - None initially (develops faint glowing marks on palms during power use)
  - Later: Subtle grayish skin tone when using Shadow Monarch powers
PERSONALITY_CORE: 
  - Determined (never gives up despite odds)
  - Protective (especially of family and comrades)
  - Quietly confident (grows from insecure to assured)
  - Growth-oriented (constantly seeks to become stronger)
  - Strategically thinking (develops from brute fighter to tactician)
BACKSTORY_ESSENTIAL: 
  - Started as "World's Weakest Hunter" (E-rank)
  - Nearly died in double dungeon, granted the "System"
  - Quest log and penalty system drives character progression
  - Secretly evolving toward Shadow Monarch of Shadow Monarch (revealed later)
NINJA_RANK: N/A (Hunter system)
CHAKRA_NATURE: N/A (uses System-based magic/mana)
SPECIAL_ABILITIES: 
  - Shadow Extraction (can extract shadows from dead enemies)
  - Shadow Army (commands extracted shadows)
  - Regenerative healing (accelerated recovery)
  - Enhanced physical stats (strength, speed, endurance)
  - Tactical analysis (passive skill that evaluates threats)
```

## 2. Reference Library

All reference images should be stored in: `references/character/jinwoo/`

### 2.1 Base References (MUST EXIST)
- `jinwoo_base_front.jpg` - Front-facing neutral expression, standard lighting
- `jinwoo_base_3_4_left.jpg` - Left 3/4 angle, neutral expression
- `jinwoo_base_3_4_right.jpg` - Right 3/4 angle, neutral expression
- `jinwoo_base_profile.jpg` - Pure profile, neutral expression
- `jinwoo_base_full_body.jpg` - Full body, neutral stance

### 2.2 Expression References (MUST EXIST)
- `jinwoo_expr_neutral.jpg` - Calm, alert, baseline expression
- `jinwoo_expr_determined.jpg` - Jaw set, narrowed eyes, slight furrowed brow
- `jinwoo_expr_angry.jpg` - Eyebrows furrowed, intense glare, flared nostrils
- `jinwoo_expr_sad.jpg` - Downturned mouth, less energetic posture, downcast eyes
- `jinwoo_expr_shocked.jpg` - Widened eyes, raised eyebrows, slightly open mouth
- `jinwoo_expr_calculating.jpg` - Half-lidded eyes, assessing gaze, finger to chin
- `jinwoo_expr_exhausted.jpg` - Heavy breathing, slumped shoulders, possible sweat
- `jinwoo_expr_joyous.jpg` - Genuine smile showing teeth, crinkled eyes
- `jinwoo_expr_power_realization.jpg` - Eyes widening with golden glow, shocked realization

### 2.3 Pose References (MUST EXIST)
- `jinwoo_pose_standing_neutral.jpg` - Feet shoulder-width apart, hands at sides
- `jinwoo_pose_standing_ready.jpg` - Knees slightly bent, hands ready to fight
- `jinwoo_pose_lying_supine.jpg` - Lying flat on back (hospital/bed scenes)
- `jinwoo_pose_sitting_up.jpg` - Sitting upright in bed or chair
- `jinwoo_pose_walking_casual.jpg` - Natural walking pace, slight arm swing
- `jinwoo_pose_running_urgent.jpg` - Leaning forward, arms pumping
- `jinwoo_pose_fighting_stance.jpg` - Low stance, weight on balls of hands ready
- `jinwoo_pose_power_activation.jpg` - Arms slightly out, palms forward, energy gathering
- `jinwoo_pose_examining_hands.jpg` - Hands raised to face level, fingers spread, examining palms
- `jinwoo_pose_looking_down.jpg` - Head tilted slightly down, evaluating something in hands

### 2.4 Wardrobe References (MUST EXIST)
- `jinwoo_wardrobe_casual_front.jpg` - Black t-shirt, dark jeans, sneakers
- `jinwoo_wardrobe_casual_side.jpg` - Side view of casual outfit
- `jinwoo_wardrobe_hunter_front.jpg` - Black tactical shirt, crimson accents, combat pants
- `jinwoo_wardrobe_hunter_side.jpg` - Side view showing utility belt, boots
- `jinwoo_wardrobe_hunter_back.jpg` - Back view showing gear layout
- `jinwoo_wardrobe_monarch_front.jpg` - Formal black coat with gold trim, regal pants
- `jinwoo_wardrobe_hospital_gown_front.jpg` - Standard light blue hospital patient gown
- `jinwoo_wardrobe_hospital_gown_side.jpg` - Side view showing fit and length

### 2.5 Power/Effect References (MUST EXIST FOR CONSISTENCY)
- `jinwoo_effect_shadow_extraction.jpg` - Black/red vortex forming around target
- `jinwoo_effect_shadow_army.jpg` - Ranks of shadow soldiers with glowing eyes
- `jinwoo_effect_system_glow_hands.jpg` - Faint golden aura around palms
- `jinwoo_effect_system_glow_full.jpg` - Stronger golden aura encompassing forearms
- `jinwoo_effect_monarch_aura.jpg` - Dark regal aura with purple/black accents
- `jinwoo_effect_healing_aura.jpg` - Soft greenish light over injured areas

---

## 3. Voice & Audio Identity

### 3.1 Voice Profile
```
VOICE_ID: "jinwoo_korean_male_24_athletic" (Example ID from ElevenLabs or similar)
SERVICE: ElevenLabs Prime Voice (or equivalent high-quality TTS/voice cloning)
PARAMETERS:
  - Stability: 0.4
  - Clarity: 0.75
  - Style Exaggeration: 0.0
  - Speaker Boost: true
  - Model: multilingual_v2
CHARACTERISTICS:
  - Base Pitch: Medium-low (approx. 110Hz fundamental)
  - Tone: Slightly rough timbre from lack of use (early story), becoming clearer
  - Pace: 
    * Normal: Measured, thoughtful
    * Excited/Angry: Slightly faster, more urgent
    * Calculating: Slow, deliberate, each word weighted
    * Tired: Slower, with slight rasp
  - Accent: Standard Seoul Korean with slight huskiness
  - Unique Traits: 
    * Tendency to lower voice when determining/threatening
    * Slight breathiness when surprised/shocked
    * Clear enunciation when giving orders (develops as leader)
```

### 3.2 Audio References (MUST EXIST)
Store in: `references/voice/jinwoo/`
- `jinwoo_voice_normal.wav` - Neutral tone, conversational
- `jinwoo_voice_determined.wav` - Firm, resolved tone
- `jinwoo_voice_angry.wav` - Low, threatening growl
- `jinwoo_voice_shocked.wav` - Higher pitch, quick intake
- `jinwoo_voice_calculating.wav` - Slow, precise, each word distinct
- `jinwoo_voice_tired.wav` - Slower, slightly strained
- `jinwoo_voice_commanding.wav` - Clear, authoritative (later story)

### 3.3 Sound Effect References
- `jinwoo_sfx_system_activate.wav` - Soft chime when quest appears
- `jinwoo_sfx_level_up.wav` - Gentle ascending chime
- `jinwoo_sfx_shadow_extract.wav` - Deep resonant pull + soft release
- `jinwoo_sfx_heal.wav` - Soft warm glow sound

---

## 4. Wardrobe System

### 4.1 Casual Wear (Early Story - Chapters 1-5)
```
CASUAL_WEAR:
  - Description: Simple t-shirt and jeans, practical clothing for unemployed young man
  - Key_Pieces: 
    * Black cotton t-shirt (crew neck)
    - Dark blue jeans (straight fit)
    - White sneakers (basic canvas)
  - Color_Palette: Monochrome (black/white/blue denim)
  - Reference_Images: jinwoo_wardrobe_casual_front.jpg, jinwoo_wardrobe_casual_side.jpg
  - Usage: Chapters 1-5, everyday scenes, hospital awakening
  - Notes: Shirt sometimes slightly wrinkled from sleeping in it
```

### 4.2 Hunter Wear (Mid Story - Chapters 6-50+)
```
HUNTER_WEAR:
  - Description: Black hunter uniform with crimson accents, practical for combat
  - Key_Pieces: 
    * Tactical shirt (black with crimson shoulder accents)
    - Combat pants (black with reinforced knees)
    - Tactical boots (black leather, steel toe)
    - Utility belt (black nylon, pouches for potions)
    - Fingerless gloves (black, grip-enhanced palms)
  - Color_Palette: Black base with crimson red accents (10-15% of visible area)
  - Reference_Images: jinwoo_wardrobe_hunter_front.jpg, jinwoo_wardrobe_hunter_side.jpg, jinwoo_wardrobe_hunter_back.jpg
  - Usage: Chapters 6-50+, dungeon raids, combat situations
  - Notes: 
    * Uniform shows wear and tear over time (small tears, dirt smudges)
    * Sleeve may be rolled up on left arm to show/watch shadow extraction
    * Always wears fingerless gloves when expecting combat
```

### 4.3 Monarch Wear (Late Story - Major Arcs)
```
MONARCH_WEAR:
  - Description: Regal black and gold attire reflecting Shadow Monarch status
  - Key_Pieces: 
    * Formal coat (black with intricate gold embroidery)
    - Ornate pants (black with subtle gold thread patterns)
    - Dress boots (black leather, polished)
    - Symbolic accessories (simple silver ring on right hand - later becomes significant)
  - Color_Palette: Black with gold trim and accents (20-30% visible area)
  - Reference_Images: jinwoo_wardrobe_monarch_front.jpg (placeholder - create when reaching this arc)
  - Usage: Monarch revelation arcs, formal confrontations
  - Notes: 
    * Reserved for when Jinwoo embraces his monarch destiny
    * May appear in visions/dreams before actual acquisition
    * Should feel imposing yet not ostentatious - power implied, not flashy
```

### 4.4 Special Wear
```
HOSPITAL_GOWN:
  - Description: Standard light blue hospital patient garment
  - Key_Pieces: 
    * Thin cotton-blend gown (light blue, #ADD8E6)
    * Open back design
    * Kneelength
  - Color_Palette: Solid light blue
  - Reference_Images: jinwoo_wardrobe_hospital_gown_front.jpg, jinwoo_wardrobe_hospital_gown_side.jpg
  - Usage: Chapter 1 hospital awakening, any medical recovery scenes
  - Notes: 
    * Often shown slightly askew from sleeping in it
    * May have slight wrinkles from bed movement
    * Never shown clean/pressed - always looks slept-in
```

---

## 5. Expression Library

### 5.1 Usage Guidelines
- **ALWAYS** use reference images for expressions when generating
- **NEVER** invent new expressions without explicit narrative justification
- **MAINTAIN** core facial structure (jawline, nose shape, eye shape) across all expressions
- **ALLOW** minor variation in intensity but not fundamental expression type

### 5.2 Expression Details
| Expression | Description | Key Features | Reference Image |
|------------|-------------|--------------|-----------------|
| **NEUTRAL** | Calm, alert, baseline state | Slightly relaxed jaw, natural eyelid position, eyes forward | `jinwoo_expr_neutral.jpg` |
| **DETERMINED** | Resolved to overcome challenge | Jaw visibly tightened, eyebrows slightly furrowed, eyes narrowed but focused | `jinwoo_expr_determined.jpg` |
| **ANGRY** | Righteous fury or frustration | Eyebrows strongly furrowed, eyes narrowed to slits, nostrils flared, jaw clenched | `jinwoo_expr_angry.jpg` |
| **SAD** | Disappointment or grief | Downturned mouth corners, less tension in forehead, eyes avoiding direct contact | `jinwoo_expr_sad.jpg` |
| **SHOCKED** | Sudden surprise or revelation | Eyes widened (visible sclera above iris), eyebrows raised, mouth slightly open | `jinwoo_expr_shocked.jpg` |
| **CALCULATING** | Assessing situation/threat | Half-lidded eyes, head slightly tilted, minimal facial movement, finger to chin | `jinwoo_expr_calculating.jpg` |
| **EXHAUSTED** | Extreme fatigue or injury | Heavy breathing visible, shoulders slumped, possible sheen of sweat, less eye focus | `jinwoo_expr_exhausted.jpg` |
| **JOYOUS** | Genuine happiness or relief | Full smile showing teeth, eyes crinkled at corners, cheeks slightly raised | `jinwoo_expr_joyous.jpg` |
| **POWER_REALIZATION** | Moment of power awakening/increase | Eyes widened with visible glow, eyebrows raised, slight intake of breath, possible micro-expression of awe | `jinwoo_expr_power_realization.jpg` |

---

## 6. Pose Library

### 6.1 Usage Guidelines
- **ALWAYS** use pose references when character positioning is specified
- **MAINTAIN** anatomical accuracy and natural weight distribution
- **ENSURE** clothing follows body contours realistically
- **ALLOW** minor variations for action but keep core pose recognizable

### 6.2 Pose Details
| Pose | Description | Key Features | Reference Image |
|------|-------------|--------------|-----------------|
| **STANDING_NEUTRAL** | Default standing position | Feet shoulder-width apart, weight evenly distributed, arms relaxed at sides | `jinwoo_pose_standing_neutral.jpg` |
| **STANDING_READY** | Prepared for action | Knees slightly bent (~10°), weight on balls of feet, hands at waist level ready to rise | `jinwoo_pose_standing_ready.jpg` |
| **LYING_SUPINE** | Lying flat on back | Body straight, arms slightly away from sides or resting on pelvis, legs straight or slightly bent | `jinwoo_pose_lying_supine.jpg` |
| **SITTING_UP** | Upright torso from lying/sitting | Back straight, hands on lap or knees, feet flat if seated, legs extended if lying | `jinwoo_pose_sitting_up.jpg` |
| **WALKING_CASUAL** | Natural walking pace | Opposite arm/leg swing, slight pelvic rotation, head level, natural stride | `jinwoo_pose_walking_casual.jpg` |
| **RUNNING_URGENT** | High-speed movement | Pronounced forward lean, arms bent 90° pumping vigorously, knees lifting high, foot strike midfoot/toe | `jinwoo_pose_running_urgent.jpg` |
| **FIGHTING_STANCE** | Defensive/ offensive ready | Weight 60% on rear leg, front foot pointed forward, hands up protecting torso, elbows in | `jinwoo_pose_fighting_stance.jpg` |
| **POWER_ACTIVATION** | Gathering energy for ability | Arms slightly extended forward (~30° from body), palms open and slightly curved, head tilted slightly down | `jinwoo_pose_power_activation.jpg` |
| **EXAMINING_HANDS** | Inspecting palms/objects | Hands raised to eye level, palms facing viewer or slightly angled, fingers naturally curved, relaxed tension | `jinwoo_pose_examining_hands.jpg` |
| **LOOKING_DOWN** | Evaluating held object | Head tilted 15-20° down, eyes focused on hands/object in lap, neck relaxed | `jinwoo_pose_looking_down.jpg` |

---

## 7. Evolution Tracking

Track physical/visual changes that occur naturally through story progression:

### 7.1 Early Story (Chapters 1-10) - "Weak Hunter"
- **Physique**: Slightly underfed appearance, less muscle definition
- **Eyes**: Consistently dark brown, no glow
- **Skin**: Normal tone, possibly slightly pale from lack of sun
- **Hair**: Messy but shorter, less volume
- **Expression Frequency**: 
  - High: Nervous, scared, uncertain
  - Medium: Determined (when pushing through fear)
  - Low: Confident, joyful
- **Wardrobe**: Primarily casual wear, occasionally ill-fitting hunter gear

### 7.2 Mid Story (Chapters 11-50) - "Developing Hunter"
- **Physique**: Noticeably more muscular definition, healthy appearance
- **Eyes**: Dark brown with occasional faint golden flecks during power use
- **Skin**: Healthy tone, gaining slight tan from outdoor activity
- **Hair**: Maintains length but appears healthier/shinier
- **Expression Frequency**:
  - High: Determined, calculating
  - Medium: Focused, alert
  - Low: Shocked (decreases as he experiences more)
  - Rare: Fear (only in truly overwhelming situations)
- **Wardrobe**: Hunter wear standard, casual wear for downtime

### 7.3 Late Story (Chapters 51-100+) - "Shadow Monarch Emerging"
- **Physique**: Peak athletic build, subtle otherworldly presence
- **Eyes**: 
  - Normal state: Dark brown with noticeable depth
  - Power activation: Clear golden glow in iris
  - Monarch activation: Complete golden luminescence (no visible pupil)
- **Skin**: 
  - Normal: Healthy tone
  - Power use: Slight iridescent sheen
  - Monarch moments: Very subtle grayish undertone
- **Hair**: Maintains style but may appear to have subtle movement in stillness (like underwater)
- **Expression Frequency**:
  - High: Calculating, commanding
  - Medium: Determined, focused
  - Low: Surprised (rarely shocked by anything)
  - Very Low: Fearful (essentially none)
  - Occasional: Grim satisfaction (when protecting others)
- **Wardrobe**: 
  - Primary: Hunter wear (shows increased wear/customization)
  - Secondary: Monarch wear (for specific arcs/visions)
  - Special: May show subtle signs of power (faint aura even at rest)

### 7.2 Special State Markers
Document temporary states that require specific references:

```
POWER_ACTIVATION_STAGE_1: 
  - Description: Initial system awakening
  - Visual: Faint golden glow (approx. 5% opacity) emanating from palms/soles
  - Duration: Seconds to minutes during active use
  - Reference: jinwoo_effect_system_glow_hands.jpg

POWER_ACTIVATION_STAGE_2:
  - Description: Moderate power use (skill activation, shadow extraction)
  - Visual: Noticeable golden aura (15-20% opacity) around hands/forearms, possible slight air distortion
  - Duration: Minutes during sustained use
  - Reference: jinwoo_effect_system_glow_full.jpg

MONARCH_PRESENCE:
  - Description: Aura of Shadow Monarch (partial or full)
  - Visual: 
    * Partial: Dark purple/black mist at feet, faint golden outline
    * Full: Pronounced dark aura with golden highlights, subtle distortion effects
  - Duration: Varies (seconds for flash, minutes for sustained)
  - Reference: Create when reaching relevant story points

SHADOW_EXTRACTION_ACTIVE:
  - Description: Process of extracting shadow from defeated enemy
  - Visual: Black/red spiral vortex forming over corpse, extending toward Jinwoo's hand
  - Duration: 2-5 seconds typically
  - Reference: jinwoo_effect_shadow_extraction.jpg

SHADOW_ARMY_SUMMONED:
  - Description: Visible presence of extracted shadows
  - Visual: Semi-transparent black figures with glowing purple eyes, varying opacity based on strength
  - Duration: As long as maintained
  - Reference: jinwoo_effect_shadow_army.jpg
```

---

## 8. Consistency Rules & "Don'ts"

### 8.1 Absolute Requirements (Must Always Follow)
```
1. FACE_STRUCTURE: Jawline, nose bridge, eye shape, and ear placement must remain consistent across all generations
2. HAIRLINE: Natural hairline must be maintained - no sudden widow's peaks or receding unless story-justified
3. EYE_SHAPE: Almond-shaped with slight upward tilt at outer corner - never round or narrowed excessively
4. HEIGHT_PROPORTIONS: Head-to-body ratio must remain ~1:7.5 (adjust slightly for pose perspective)
5. SKIN_TONE_CONSISTENCY: Base undertone (olive) must remain - no sudden pallor or flushing without reason
```

### 8.2 Expression-Specific Rules
```
1. NEUTRAL: Mouth never fully open or closed tightly - natural resting position
2. DETERMINED: Jaw tension visible but never to point of teeth clenching (unless showing extreme effort)
3. ANGRY: Forehead wrinkles appear between brows, never across forehead only
4. SAD: Eyes never fully closed - always showing some level of engagement/world awareness
5. SHOCKED: Eyebrows rise together, never one higher than the other (unless showing specific head tilt)
6. CALCULATING: One hand typically near face/chin, other relaxed at side or on hip
7. EXHAUSTED: Shoulder slump visible but never to point of collapsing posture (unless unconscious)
8. JOYOUS: Eyes crinkle but never completely closed - "smizing" effect present
```

### 8.3 Pose-Specific Rules
```
1. STANDING: Weight distribution always physically plausible - never impossible balances
2. WALKING/running: Limb opposition must be correct (left arm/right leg forward etc.)
3. SITTING: Spine maintains natural curve - never over-straightened or excessively curved
4. REACHING: Arm extension follows natural biomechanics - no hyper-extension beyond joint limits
5. LOOKING: Head turn never exceeds 90° without corresponding body rotation
```

### 8.4 Wardrobe Rules
```
1. FIT: Clothing must follow body contours realistically - no "paint-on" effects unless specified (like combat suit)
2. WRINKLES: Fabric wrinkles follow gravity and movement patterns - never random placement
3. LAYERING: Visible layers (undershirts, etc.) must be logically consistent with stated outfit
4. ACCESSORIES: Consistent placement (watch on left wrist, necklace position, etc.)
5. WEAR_AND_TEAR: Damage accumulates logically - new tears appear in stress areas, not randomly
```

### 8.5 Absolute "Don'ts" (Never Violate)
```
DON'T:
  - Change ear shape/size/position
  - Alter fundamental nose bridge structure
  - Make eyes suddenly round when they're almond-shaped
  - Give character facial hair without explicit story reason (he remains clean-shaven)
  - Change ethnicity appearance (must remain clearly Korean East Asian)
  - Make him significantly taller/shorter than established 182cm
  - Give him permanent scars/marks without story justification and reference update
  - Violate basic human anatomy in poses (impossible joint angles, etc.)
  - Allow clothing to clip through body in impossible ways
  - Change voice pitch/accent without narrative reason and voice reference update
```

---

## 9. Technical Specifications

### 9.1 Generation Parameters (Default)
```
BASE_SEED: 42 (unless specific variation required)
STEPS: 30
CFG_SCALE: 7.5
WIDTH: 3840
HEIGHT: 2160
FPS: 24
```

### 9.2 Model Assignments by Shot Type
```
CLOSE_UPS / EXTREME_CLOSE_UPS: 
  Model: Wan 2.7 (best for facial/hair detail)
  Notes: Use extra attention to eye/region details

MEDIUM_SHOTS / DIALOGUE_SCENES:
  Model: Kling 3.0 (best for lip-sync and natural movement)
  Notes: Enable lip-sync tracking if dialogue present

WIDE_SHOTS / ESTABLISHING:
  Model: Veo 3.1 (best for environmental consistency and depth)
  Notes: Ensure background elements match reference

ACTION_SEQUENCES / COMPLEX_MOTION:
  Model: Seedance 2.0 (multi-reference capable)
  Notes: Provide key pose references for start/middle/end

EFFECTS_ONLY / MAGIC_ELEMENTS:
  Model: Appropriate specialized model or base SDXL with ControlNet
  Notes: Generate on transparent background for compositing
```

### 9.3 Reference Anchoring Requirements
```
MINIMUM_REFERENCES_PER_PROMPT:
  - Character close-ups: 1 pose reference + 1 expression reference
  - Character medium/wide shots: 1 full-body reference OR 2 pose references
  - Establishing environment shots: 1 environment reference
  - Magic/effect shots: 1 effect reference + 1 character/environment reference for interaction
  - Dialogue shots: Voice reference MUST be provided to audio generation
```

---

## 10. Usage Guidelines

### 10.1 For Prompt Engineers
```
1. BEFORE writing prompt:
   - Consult this bible for exact description
   - Verify required references exist in library
   - Check current story point for appropriate wardrobe/evolution stage
   - Note any active power states requiring effect references

2. WHEN writing prompt:
   - Use EXACT phrasing from "Character Core Profile" for base description
   - Insert @reference: tags for all required visual elements
   - Specify technical specs based on shot type
   - Include voice reference for any dialogue
   - Add evolution notes if applicable to current chapter/scene

3. AFTER generation:
   - Verify against this bible during QA
   - Check reference usage in metadata
   - Confirm voice matches specified ID/parameters
```

### 10.2 For Artists/Editors
```
1. REFERENCE USE:
   - Treat references as absolute truth for character appearance
   - Never "improve" upon reference - match it exactly
   - Use references for color picking, texture matching, proportion checking

2. COMPOSITING:
   - Match lighting direction and intensity to environment references
   - Ensure shadow direction consistent across all elements
   - Maintain depth of field as specified in lens specs

3. COLOR GRADING:
   - Use specified LUTs from style constants
   - Match skin tones to reference under same lighting
   - Preserve hair highlights/shadows as seen in references
```

### 10.3 For Quality Assurance
```
CHECKLIST PER ASSET:
  [ ] Character facial structure matches reference library
  [ ] Expression matches specified reference (if applicable)
  [ ] Pose matches specified reference (if applicable)
  [ ] Wardrobe matches current story chapter
  [ ] Evolution stage matches narrative point
  [ ] Technical specs (resolution, fps, etc.) correct
  [ ] References properly cited in prompt metadata
  [ ] Voice matches specified ID/parameters (audio)
  [ ] No "don't" violations present
  [ ] Overall consistency with established canon
```

---

## Appendix: Reference Library Directory Structure
```
references/
└── character/
    └── jinwoo/
        ├── base/
        │   ├── jinwoo_base_front.jpg
        │   ├── jinwoo_base_3_4_left.jpg
        │   ├── jinwoo_base_3_4_right.jpg
        │   ├── jinwoo_base_profile.jpg
        │   └── jinwoo_base_full_body.jpg
        ├── expressions/
        │   ├── jinwoo_expr_neutral.jpg
        │   ├── jinwoo_expr_determined.jpg
        │   ├── jinwoo_expr_angry.jpg
        │   ├── jinwoo_expr_sad.jpg
        │   ├── jinwoo_expr_shocked.jpg
        │   ├── jinwoo_expr_calculating.jpg
        │   ├── jinwoo_expr_exhausted.jpg
        │   ├── jinwoo_expr_joyous.jpg
        │   └── jinwoo_expr_power_realization.jpg
        ├── poses/
        │   ├── jinwoo_pose_standing_neutral.jpg
        │   ├── jinwoo_pose_standing_ready.jpg
        │   ├── jinwoo_pose_lying_supine.jpg
        │   ├── jinwoo_pose_sitting_up.jpg
        │   ├── jinwoo_pose_walking_casual.jpg
        │   ├── jinwoo_pose_running_urgent.jpg
        │   ├── jinwoo_pose_fighting_stance.jpg
        │   ├── jinwoo_pose_power_activation.jpg
        │   ├── jinwoo_pose_examining_hands.jpg
        │   └── jinwoo_pose_looking_down.jpg
        ├── wardrobe/
        │   ├── casual/
        │   │   ├── jinwoo_wardrobe_casual_front.jpg
        │   │   └── jinwoo_wardrobe_casual_side.jpg
        │   ├── hunter/
        │   │   ├── jinwoo_wardrobe_hunter_front.jpg
        │   │   ├── jinwoo_wardrobe_hunter_side.jpg
        │   │   └── jinwoo_wardrobe_hunter_back.jpg
        │   ├── monarch/
        │   │   └── jinwoo_wardrobe_monarch_front.jpg
        │   └── hospital/
        │       ├── jinwoo_wardrobe_hospital_gown_front.jpg
        │       └── jinwoo_wardrobe_hospital_gown_side.jpg
        └── effects/
            ├── jinwoo_effect_shadow_extraction.jpg
            ├── jinwoo_effect_shadow_army.jpg
            ├── jinwoo_effect_system_glow_hands.jpg
            ├── jinwoo_effect_system_glow_full.jpg
            └── jinwoo_effect_monarch_aura.jpg
```

---

## Implementation Notes

### To Create This Bible in Practice:
1. **Generate base references** using detailed prompts from Section 1
2. **Generate expression/pose references** by modifying base with specific description
3. **Create wardrobe references** by dressing base model in specified clothing
4. **Produce effect references** through separate effect generation or compositing
5. **Record voice samples** using specified TTS service or voice actor
6. **Store all references** in the prescribed directory structure
7. **Update this document** with actual filenames as references are created
8. **Review quarterly** to ensure references remain current with story progression

### Maintenance Schedule:
- **Per Chapter**: Verify wardrobe/evolution stage appropriateness
- **Per Major Arc** (25-50 chapters): Update evolution tracking if needed
- **Per Season** (50-100 chapters): Add new expressions/poses if character develops new traits
- **As Needed**: Add effect references for new powers/abilities discovered

This bible ensures that no matter which artist, animator, or AI generator creates content featuring Sung Jinwoo, the output will be visually consistent, narratively appropriate, and professionally polished—eliminating the "AI look" through disciplined reference use rather than relying solely on prompt engineering.