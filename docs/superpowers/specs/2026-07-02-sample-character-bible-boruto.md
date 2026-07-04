# Sample Character Bible: Boruto Uzumaki (Boruto: Two Blue Vortex)
## Implementing Best Practices for Consistent AI Generation (July 2026)

This document demonstrates how to create a professional character bible for Boruto Uzumaki using the best practices outlined in our AI Video Generation Best Practices guide. It serves as a template for all character bibles in the AI Live Action Studio pipeline, specifically adapted for ninja characters and the Boruto: Two Blue Vortex storyline.

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
CHARACTER: Boruto Uzumaki
AGE: 16 (at start of Boruto: Two Blue Vortex)
NATIONALITY: Japanese (Konohagakure)
HEIGHT: ~170cm
BUILD: Athletic, lean but muscular build typical of teenage ninja
HAIR: Blonde, spiky in front, longer in back (similar to father's style but distinct)
EYES: Blue, later develops Jougan (pure white with blue pupil and pattern)
SKIN_TONE: Light
DISTINGUISHING_MARKS: 
  - Whisker marks on cheeks (inherited from Naruto)
  - Karma seal (dark diamond-shaped mark on palm, spreads when active)
  - Jougan eye (when active: pure white sclera with blue pupil and distinctive pattern)
PERSONALITY_CORE: 
  - Determined (eager to surpass father, prove himself)
  - Somewhat rebellious (challenges expectations, but caring deep down)
  - Protective of friends (especially Sarada, Mitsuki, Kawaki)
  - Energetic and enthusiastic (inherits father's spirit)
  - Strategic thinker (develops from impulsive to tactical)
BACKSTORY_ESSENTIAL: 
  - Son of Naruto Uzumaki (7th Hokage) and Hinata Hyuga
  - Trained by Sasuke Uchiha
  - Carries Karma seal from Momoshiki Otsutsuki (alien parasite granting power)
  - Jougan (pure eye) inherited through complex Otsutsuki/Hyuga lineage
NINJA_RANK: Jonin-level (despite official Genin status due to exceptional skill)
CHAKRA_NATURE: Wind (primary), Lightning (secondary)
SPECIAL_ABILITIES: 
  - Jougan (dojutsu): Enables perception of chakra flow, interdimensional vision, seeing invisible barriers
  - Karma seal (Otsutsuki power): Grants enhanced strength, speed, energy absorption/release
  - Vanishing Rasengan (Wind Release): Rasengan that becomes invisible at high rotation
  - Multiple Rasengan variants (standard, Wind Release: Rasengan, etc.)
  - Expert in taijutsu, ninjutsu, and weaponry
```

## 2. Reference Library

All reference images should be stored in: `references/character/boruto/`

### 2.1 Base References (MUST EXIST)
- `boruto_base_front.jpg` - Front-facing neutral expression, standard lighting
- `boruto_base_3_4_left.jpg` - Left 3/4 angle, neutral expression
- `boruto_base_3_4_right.jpg` - Right 3/4 angle, neutral expression
- `boruto_base_profile.jpg` - Pure profile, neutral expression (showing whisker marks clearly)
- `boruto_base_full_body.jpg` - Full body, neutral stance

### 2.2 Expression References (MUST EXIST)
- `boruto_expr_neutral.jpg` - Calm but alert, slight smirk
- `boruto_expr_determined.jpg` - Jaw set, narrowed eyes, fists clenched
- `boruto_expr_angry.jpg` - Eyebrows furrowed, intense glare, visible whisker marks
- `boruto_expr_sad.jpg` - Downturned mouth, less energetic posture
- `boruto_expr_shocked_surprised.jpg` - Widened eyes (Jougan may activate), raised eyebrows
- `boruto_expr_calculating_strategic.jpg` - Half-lidded eyes, assessing gaze, finger to chin
- `boruto_expr_exhausted_injured.jpg` - Heavy breathing, slumped shoulders, possible blood
- `boruto_expr_joyous_smiling.jpg` - Genuine smile showing teeth, crinkled eyes
- `boruto_expr_serious_focused.jpg` - Intense stare, minimal expression change
- `boruto_expr_playful_mischievous.jpg` - Grinning, eyebrows wiggling, playful stance

### 2.3 Pose References (MUST EXIST)
- `boruto_pose_standing_neutral.jpg` - Standing straight, hands at sides or in pockets
- `boruto_pose_stance_combat.jpg` - Knees bent, hands ready to form seals or grab weapons
- `boruto_pose_walking_casual.jpg` - Hands in pockets, relaxed gait, slight bounce
- `boruto_pose_running_ninja.jpg` - Leaning forward, arms bent back, legs pumping
- `boruto_pose_jumping_acrobatic.jpg` - Mid-air, legs bent, possible hand signs
- `boruto_pose_hand_signs.jpg` - Specific seals for Rasengan variants (especially Vanishing Rasengan)
- `boruto_pose_fighting_stance.jpg` - Low stance, weight on balls of feet, ready to dodge/strike
- `boruto_pose_power_activation_karma.jpg` - 
  * Stage 1: Diamond mark glowing on palm
  * Stage 2: Patterns spreading up arm, faint blue aura
  * Stage 3: Significant coverage, visible blue energy emanating
- `boruto_pose_examining_hands.jpg` - Hands raised, inspecting something (for analytical moments)
- `boruto_pose_looking_distance.jpg` - Gazing into distance (for Jougan usage moments)

### 2.4 Wardrobe References (MUST EXIST)
- `boruto_wardrobe_standard_front.jpg` - Standard ninja outfit: black jacket with orange accents, navy pants, sandals, forehead protector (sideways)
- `boruto_wardrobe_standard_side.jpg` - Side view showing jacket cut, pouch placement
- `boruto_wardrobe_standard_back.jpg` - Back view showing gear layout
- `boruto_wardrobe_karma_front.jpg` - Battle outfit with visible Karma patterns spreading
- `boruto_wardrobe_karma_side.jpg` - Side view showing Karma progression on arms/legs
- `boruto_wardrobe_karma_back.jpg` - Back view showing full Karma coverage
- `boruto_wardrobe_casual_front.jpg` - Modern clothing: orange jacket, black t-shirt, jeans, sneakers
- `boruto_wardrobe_casual_side.jpg` - Side view of casual outfit
- `boruto_wardrobe_casual_back.jpg` - Back view of casual outfit

### 2.5 Power/Effect References (MUST EXIST FOR CONSISTENCY)
- `boruto_expr_jawline_blue_eye.jpg` - Close-up showing Jougan activation (white sclera, blue pupil/pattern)
- `boruto_expr_chakra_wind_faint.jpg` - Faint blue-white chakra aura (Wind Release sensing)
- `boruto_expr_chakra_wind_strong.jpg` - Strong blue Wind chakra aura flaring
- `boruto_expr_karma_seal_stage1.jpg` - Diamond mark glowing on palm
- `boruto_expr_karma_seal_stage2.jpg` - Patterns spreading up arm, faint blue aura
- `boruto_expr_karma_seal_stage3.jpg` - Significant coverage, visible blue energy emanating
- `boruto_expr_vanishing_rasengan.jpg` - Close-up of distorted sphere in hand
- `boruto_effect_wind_release_rasengan.jpg` - Standard Rasengan with Wind chakra
- `boruto_effect_vanishing_rasengan.jpg` - Vanishing Rasengan: distorted sphere, heat-haze effect
- `boruto_effect_chakra_clash.jpg` - Visual of clashing chakra auras (colors specified)
- `boruto_effect_karma_matter_distortion.jpg` - Black/red geometric patterns spreading
- `boruto_effect_jougan_perception.jpg` - Visual of what Jougan sees (chakra flow, barriers)

---

## 3. Voice & Audio Identity

### 3.1 Voice Profile
```
VOICE_ID: "boruto_japanese_male_16_teen_energetic" (Example ID from ElevenLabs or similar)
SERVICE: ElevenLabs (or equivalent high-quality TTS/voice cloning)
PARAMETERS:
  - Stability: 0.3
  - Clarity: 0.7
  - Style Exaggeration: 0.2
  - Speaker Boost: true
  - Model: multilingual_v2
CHARACTERISTICS:
  - Base Pitch: Medium (approx. 145Hz fundamental - teenage male)
  - Tone: Slightly nasal quality common in Japanese teen males, energetic timbre
  - Pace: 
    * Normal: Energetic, slightly quick
    * Excited/Determined: Faster, urgent
    * Angry: Sharp, staccato bursts
    * Calculating: Slower, deliberate but with underlying tension
    * Tired: Slower, with slight rasp
    * Playful: Bouncy, varied pitch, lots of energy
  - Accent: Standard Tokyo Japanese with slight huskiness
  - Unique Traits: 
    * Tendency to end sentences with rising intonation (seeking validation)
    * Short, sharp exhalations when frustrated
    * Clear enunciation when stating goals/declarations
    * Laughs frequently in casual moments
```

### 3.2 Audio References (MUST EXIST)
Store in: `references/voice/boruto/`
- `boruto_voice_normal.wav` - Neutral tone, conversational but energetic
- `boruto_voice_determined.wav` - Firm, urgent tone
- `boruto_voice_angry.wav` - Sharp, frustrated bursts
- `boruto_voice_shocked.wav` - Higher pitch, quick intake
- `boruto_voice_calculating.wav` - Slower, precise, each word distinct
- `boruto_voice_tired.wav` - Slower, slightly strained
- `boruto_voice_playful.wav` - Bouncy, varied pitch, energetic
- `boruto_voice_serious.wav` - Low, intense, minimal variation
- `boruto_voice_commanding.wav` - Clear, authoritative (when giving orders)

### 3.3 Sound Effect References
- `boruto_sfx_rasengan.wav` - Classic swirling sphere sound
- `boruto_sfx_vanishing_rasengan.wav` - High-pitched whine that cuts out when vanished
- `boruto_sfx_karma_activate.wav` - Deep resonant pulse + geometric spread sound
- `boruto_sfx_jougan_activate.wav` - Soft chime + subtle ringing
- `boruto_sfx_wind_release.wav` - Whoosh with slight whistle
- `boruto_sfx_lightning_clash.wav` - Sharp crack + thunder boom
```

---

## 4. Wardrobe System

### 4.1 Standard Ninja Attire (Primary Outfit)
```
STANDARD_NINJA_OUTFIT:
  - Description: Modified ninja outfit reflecting his growth and status
  - Key_Pieces: 
    * Forehead protector with Konoha symbol (worn sideways as signature style)
    * Black combat jacket with orange accents (on shoulders/sleeves)
    * Navy blue pants
    * Ninja sandals (open-toed, strapped)
    * Fingerless gloves (black, grip-enhanced)
    * Weapon pouches (thigh-mounted)
  - Color_Palette: Black base with orange and navy blue accents
  - Reference_Images: boruto_wardrobe_standard_front.jpg, boruto_wardrobe_standard_side.jpg, boruto_wardrobe_standard_back.jpg
  - Usage: Primary outfit for missions, training, combat
  - Notes: 
    * Jacket often unzipped halfway to show undershirt
    * Forehead protector consistently worn sideways (left side down)
    * Gloves worn consistently when expecting combat
    * Sandals show wear on soles from constant movement
```

### 4.2 Special Attire (Karma Activation)
```
KARMA_ACTIVATION_ATTIRE:
  - Description: Battle outfit when Karma seal is significantly active
  - Key_Pieces: 
    * Same base outfit but with visible Karma patterns spreading
    * Special combat tape on arms/legs when using advanced Karma (black with red accents)
    * May remove jacket sleeves for full arm movement in extreme cases
  - Color_Palette: Black with orange accents, plus glowing blue Karma patterns (when active)
  - Reference_Images: boruto_wardrobe_karma_front.jpg, boruto_wardrobe_karma_side.jpg, boruto_wardrobe_karma_back.jpg
  - Usage: High-stakes battles, Karma-powered confrontations
  - Notes: 
    * Karma patterns glow brighter with increased power usage
    * Patterns start as faint diamond on palm, spread to cover arms/chest at peak
    * Combat tape appears when using Karma for physical enhancement
    * Jacket may be discarded in extreme activation states
```

### 4.3 Casual Wear (Off-Duty)
```
CASUAL_WEAR:
  - Description: Modern teenage clothing when off-duty
  - Key_Pieces: 
    * Orange jacket (nod to father's color)
    * Black t-shirt
    * Jeans
    * Sneakers
  - Color_Palette: Orange, black, blue denim
  - Reference_Images: boruto_wardrobe_casual_front.jpg, boruto_wardrobe_casual_side.jpg, boruto_wardrobe_casual_back.jpg
  - Usage: Downtime, school scenes, informal gatherings
  - Notes: 
    * Often wears headphones around neck
    * Jeans may be ripped at knees from activity
    * Orange jacket frequently unzipped
    * Shows typical teenage wear patterns (stains, fading)
```

### 4.4 Specialized Gear
```
SPECIAL_GEAR:
  - SWORD: 
    * Description: Chakra blade (when using specific techniques)
    * Appearance: Energy blade extending from forearm, color varies by chakra type
    * Reference: Create effect reference when needed
    
  - SCIENTIFIC_TOOLS:
    * Description: Ninja tools Mitsuki often provides analytical devices
    * Reference: Include when Mitsuki is present in scene
```

---

## 5. Expression Library

### 5.1 Usage Guidelines
- **ALWAYS** use reference images for expressions when generating
- **MAINTAIN** core facial structure (jawline, nose shape, eye shape, whisker mark placement)
- **RESPECT** distinctive features: whisker marks must be symmetrical and properly placed
- **ALLOW** Jougan activation only when narratively justified (not constant)
- **ENSURE** emotional intensity matches context (no over-acting)

### 5.2 Expression Details
| Expression | Description | Key Features | Reference Image |
|------------|-------------|--------------|-----------------|
| **NEUTRAL** | Calm but alert, baseline state | Slight smirk, relaxed jaw, natural eyelid position, whisker marks visible | `boruto_expr_neutral.jpg` |
| **DETERMINED** | Resolved to overcome challenge | Jaw visibly tightened, eyebrows slightly furrowed, eyes narrowed but focused, fists clenched | `boruto_expr_determined.jpg` |
| **ANGRY** | Righteous fury or frustration | Eyebrows strongly furrowed, eyes narrowed to slits, nostrils flared, jaw clenched, visible whisker marks | `boruto_expr_angry.jpg` |
| **SAD** | Disappointment or grief | Downturned mouth corners, less tension in forehead, eyes avoiding direct contact, slumped posture | `boruto_expr_sad.jpg` |
| **SHOCKED/SURPRISED** | Sudden surprise or revelation | Eyes widened (may show Jougan activation), eyebrows raised, mouth slightly open, head recoil | `boruto_expr_shocked_surprised.jpg` |
| **CALCULATING/STRATEGIC** | Assessing situation/threat | Half-lidded eyes, head slightly tilted, minimal facial movement, finger to chin, evaluating stare | `boruto_expr_calculating_strategic.jpg` |
| **EXHAUSTED/INJURED** | Extreme fatigue or visible injury (INJURED** | Heavy fatigue or visible injury | Heavy breathing, slumped shoulders, possible sheen of sweat/blood, less eye focus, possible grimace | `boruto_expr_exhausted_injured.jpg` |
| **JOYOUS/SMILING** | Genuine happiness or relief | Full smile showing teeth, eyes crinkled at corners, cheeks slightly raised, energetic posture | `boruto_expr_joyous_smiling.jpg` |
| **SERIOUS/FOCUSED** | Intense concentration | Intense stare, minimal expression change, slightly narrowed eyes, upright posture, ready stance | `boruto_expr_serious_focused.jpg` |
| **PLAYFUL/MISCHIEVOUS** | Lighthearted trickster energy | Grinning, eyebrows wiggling, playful stance, hands in pockets or making casual gesture | `boruto_expr_playful_mischievous.jpg` |
| **JOUJAN_ACTIVATED** | Dojutsu perception active | Pure white sclera with distinct blue pupil and pattern, intense focused gaze, possible slight head tilt | `boruto_expr_jawline_blue_eye.jpg` |
| **WIND_CHAKRA_SENSING** | Chakra nature perception | Faint blue-white outline around body, eyes slightly narrowed in assessment | `boruto_expr_chakra_wind_faint.jpg` |
| **WIND_CHAKRA_FLARED** | Active Wind Release chakra | Strong blue aura flaring, hair/movement affected by energy, determined expression | `boruto_expr_chakra_wind_strong.jpg` |

---

## 6. Pose Library

### 6.1 Usage Guidelines
- **ALWAYS** use pose references when character positioning is specified
- **MAINTAIN** anatomical accuracy and natural weight distribution for ninja movements
- **RESPECT** distinctive hairstyle: spiky front, longer back - must maintain silhouette
- **ENSURE** clothing follows body contours realistically during movement
- **ALLOW** variations for action but keep core pose recognizable
- **ACCURATELY** depict hand signs when specified (critical for jutsu identification)

### 6.2 Pose Details
| Pose | Description | Key Features | Reference Image |
|------|-------------|--------------|-----------------|
| **STANDING_NEUTRAL** | Default standing position | Feet shoulder-width apart, weight evenly distributed, arms relaxed at sides or in pockets, slight bounce | `boruto_pose_standing_neutral.jpg` |
| **STANCE_COMBAT_READY** | Prepared for taijutsu/weapon use | Knees bent (~20°), weight on balls of feet, hands at waist level ready to rise or form seals, alert posture | `boruto_pose_stance_combat.jpg` |
| **WALKING_CASUAL** | Natural walking pace | Hands in pockets, relaxed gait with slight bounce, head level, opposite arm/leg swing | `boruto_pose_walking_casual.jpg` |
| **RUNNING_NINJA** | High-speed movement | Pronounced forward lean, arms bent 90° pumping vigorously behind back, knees lifting high, foot strike midfoot/toe | `boruto_pose_running_ninja.jpg` |
| **JUMPING/ACROBATIC** | Mid-air maneuver | Legs bent for propulsion/landing, possible hand signs forming, body twisted for direction change, hair flowing with motion | `boruto_pose_jumping_acrobatic.jpg` |
| **HAND_SIGNS** | Specific seals for jutsu | Fingers positioned precisely for seals (e.g., for Vanishing Rasengan: modified Tiger seal), focused expression, chakra visible at fingertips | `boruto_pose_hand_signs.jpg` |
| **FIGHTING_STANCE** | Defensive/ offensive ready | Low stance (~40° knee bend), weight 60% on rear leg, front foot pointed forward, hands up protecting torso, elbows in, ready to strike/block | `boruto_pose_fighting_stance.jpg` |
| **POWER_ACTIVATION_KARMA_STAGE_1** | Initial Karma awareness | Diamond-shaped mark on palm faintly glowing, slight intake of breath, eyes focused on hand | *See Karma progression references* |
| **POWER_ACTIVATION_KARMA_STAGE_2** | Moderate Karma usage | Patterns spreading up forearm (~50% coverage), faint blue aura emanating, tensed posture, assessing expression | *See Karma progression references* |
| **POWER_ACTIVATION_KARMA_STAGE_3** | Significant Karma activation | Major coverage on arms/chest, visible blue energy emanating (~75% coverage), fighting stance, energy particles in air | *See Karma progression references* |
| **EXAMINING_HANDS** | Inspecting palms/objects | Hands raised to eye level, palms facing viewer or slightly angled, fingers naturally curved, relaxed tension, analytical expression | `boruto_pose_examining_hands.jpg` |
| **LOOKING_DISTANCE** | Gazing into distance (Jougan/scouting) | Head slightly tilted, eyes focused far away, relaxed posture, possible hand shielding eyes, assessing expression | `boruto_pose_looking_distance.jpg` |
| **VANISHING_RASengan_PREP** | Preparing special Rasengan | Hand positioned for sphere formation, chakra visibly gathering, focused expression, stance ready for release | *Context-dependent pose* |
| **VANISHING_RASengan_RELEASE** | Releasing Vanishing Rasengan | Arm extended forward, palm open, distorted sphere visible in hand, motion blur on release, determined expression | *Context-dependent pose* |

---

## 7. Evolution Tracking

Track physical/visual changes that occur naturally through story progression:

### 7.1 Early Two Blue Vortex (Chapters 1-10) - "Establishing the Threat"
- **Physique**: Lean teenage build, slightly less defined than later
- **Eyes**: 
  - Normal state: Clear blue
  - Jougan: Activates intermittently during stress/perception attempts (uncontrolled)
  - Whisker marks: Prominent but not darkened
- **Hair**: Blonde, spiky front longer than canon (still developing style)
- **Expression Frequency**: 
  - High: Energetic, playful, determined
  - Medium: Curious, confused (learning new threats)
  - Low: Serious, calculating (developing)
  - Rare: Fear (only in truly overwhelming situations)
- **Wardrobe**: 
  - Primary: Standard ninja outfit
  - Secondary: Casual wear for downtime
  - Special: Karma seal mostly inactive (faint mark only)
- **Power Manifestation**: 
  - Karma: Faint diamond mark, occasional pulse during stress
  - Jougan: Uncontrolled flashes (white sclera, blue pattern)
  - Chakra: Standard Wind Release blue aura when used

### 7.2 Mid Two Blue Vortex (Chapters 11-30) - "Adapting to the Threat"
- **Physique**: More muscular definition from combat and training
- **Eyes**: 
  - Normal: Steady blue, increased depth
  - Jougan: Longer activation periods, more control (still strains him)
  - Whisker marks: May darken slightly with chakra usage
- **Hair**: Maintains style but appears healthier/shinier from better nutrition
- **Expression Frequency**: 
  - High: Determined, focused, serious
  - Medium: Playful (among friends), calculating
  - Low: Shocked (decreases as he adapts)
  - Very Low: Fear (only in hopeless situations)
- **Wardrobe**: 
  - Primary: Standard ninja outfit (shows customization: tape, adjustments)
  - Secondary: Casual wear (more relaxed fits)
  - Special: Karma seal visible during use, patterns spreading predictably
- **Power Manifestation**: 
  - Karma: Clear patterns on forearm during use, blue aura stronger
  - Jougan: More sustained activation, less physical strain
  - Chakra: Wind Release aura more defined, Lightning secondary visible

### 7.3 Late Two Blue Vortex (Chapters 31-50+) - "Mastering the Power"
- **Physique**: Peak teenage athletic build, subtle otherworldly presence from Karma
- **Eyes**: 
  - Normal: Steady blue with noticeable maturity
  - Jougan: Significant control (activates intentionally for perception)
  - Whisker marks: Clearly defined, may show subtle chakra response
- **Hair**: Maintains signature style but may show slight movement in stillness (Karma influence)
- **Expression Frequency**: 
  - High: Calculating, serious, determined
  - Medium: Focused, protective (of friends)
  - Low: Playful (only in safe moments with close friends)
  - Very Low: Shocked (almost never)
  - Occasional: Grim resolution (when protecting others)
- **Wardrobe**: 
  - Primary: Standard ninja outfit (heavily customized: multiple tape layers, modified fit)
  - Secondary: Casual wear (worn but well-maintained)
  - Special: Karma seal patterns predictable during use, Jougan activation clean
- **Power Manifestation**: 
  - Karma: Patterns spread predictably (forearm → full arm → chest), strong blue aura
  - Jougan: Reliable activation for scanning/perception, clear visual output
  - Chakra: Wind Release highly refined, Lightning secondary well-integrated

### 7.2 Special State Markers
Document temporary states that require specific references:

```
KARMA_SEAL_STAGE_1: 
  - Description: Initial awareness/low-level usage
  - Visual: Faint diamond mark on palm glowing softly (approx. 5% opacity)
  - Duration: Seconds during active use or stress
  - Reference: boruto_expr_karma_seal_stage1.jpg

KARMA_SEAL_STAGE_2:
  - Description: Moderate power use (enhanced physicals, energy techniques)
  - Visual: Patterns spreading up forearm (25-50% coverage), faint blue aura (10-15% opacity)
  - Duration: Minutes during sustained use
  - Reference: boruto_expr_karma_seal_stage2.jpg

KARMA_SEAL_STAGE_3:
  - Description: Significant activation (enhanced strength, energy projection)
  - Visual: Major coverage on arms/chest (50-75%), visible blue energy emanating (20-30% opacity), possible geometric projection
  - Duration: Extended use in battles
  - Reference: boruto_expr_karma_seal_stage3.jpg

JOUJAN_ACTIVATION:
  - Description: Dojutsu perception engaged
  - Visual: 
    * Sclera: Pure white (loss of normal blue)
    * Pupil: Distinct blue color with geometric pattern
    * Perception aura: Subtle distortion effects when active
  - Duration: Varies (seconds for flash, minutes for sustained use)
  - Reference: boruto_expr_jawline_blue_eye.jpg

WIND_CHAKRA_FLARE:
  - Description: Active Wind Release chakra usage
  - Visual: 
    * Aura: Strong blue outline (15-25% opacity) following body contours
    * Effect: Hair/movement slightly affected, chakra particles at extremities
    * Eyes: Slightly narrowed in focus
  - Duration: During technique execution
  - Reference: boruto_expr_chakra_wind_strong.jpg

VANISHING_RASengan_ACTIVE:
  - Description: Vanishing Rasengan in formation/maintenance
  - Visual: 
    * Sphere: Distorted/warped like heat haze at high rotation
    * Core: Denser chakra center
    * Effect: Subtle air distortion, chakra particles flowing outward
    * Hand: Visible chakra flow into sphere
  - Duration: From formation to impact (typically 2-5 seconds)
  - Reference: boruto_expr_vanishing_rasengan.jpg

KARMA_MATTER_DISTORTION:
  - Description: Karma seal used for energy/matter manipulation
  - Visual: 
    * Patterns: Black/red geometric shapes spreading from contact point
    * Effect: Localized space distortion, energy particles
    * Aura: Reddish-black chakra emanation
  - Duration: During active use
  - Reference: boruto_expr_karma_matter_distortion.jpg
```

---

## 8. Consistency Rules & "Don'ts"

### 8.1 Absolute Requirements (Must Always Follow)
```
1. FACE_STRUCTURE: Jawline, nose bridge, eye shape, ear placement, and whisker mark positions must remain consistent
2. HAIRLINE: Natural hairline must be maintained - spiky front longer than back is signature
3. WHISKER_MARKS: Three distinct marks on each cheek - must be symmetrical and properly placed (never missing/misplaced)
4. EYE_SHAPE_NORMAL: Almond-shaped with slight upward tilt - never round or narrowed excessively unless Jougan active
5. EYE_SHAPE_JOUJAN: When active: pure white sclera with blue pupil/pattern - never normal eyes when Jougan supposed active
6. HEIGHT_PROPORTIONS: Head-to-body ratio must remain ~1:7.0 (slightly larger head ratio for teenage character)
7. SKIN_TONE_CONSISTENCY: Base undertone (light) must remain - no sudden pallor or flushing without reason
```

### 8.2 Expression-Specific Rules
```
1. NEUTRAL: Mouth never fully open or closed tightly - natural resting position with slight smirk
2. DETERMINED: Jaw tension visible but never to point of teeth clenching (unless showing extreme effort)
3. ANGRY: Forehead wrinkles appear between brows, never across forehead only; whisker marks must remain visible
4. SAD: Eyes never fully closed - always showing some level of engagement/world awareness
5. SHOCKED/SURPRISED: Eyebrows rise together, never one higher than the other (unless showing specific head tilt)
6. CALCULATING/STRATEGIC: One hand typically near face/chin, other relaxed at side or on hip
7. EXHAUSTED/INJURED: Shoulder slump visible but never to point of collapsing posture (unless unconscious)
8. JOYOUS/SMILING: Eyes crinkle but never completely closed - "smizing" effect present; smile reaches eyes
9. SERIOUS/FOCUSED: Minimal change from neutral but eyes intensely focused; no furrowed brow unless assessing threat
10. PLAYFUL/MISCHIEVOUS: Expression shows genuine amusement; eyes crinkled, posture relaxed but engaged
11. JOUJAN_ACTIVATED: Sclera must be pure white, pupil blue with pattern - never partial or inconsistent activation
12. WIND_CHAKRA_SENSING/FLARED: Aura must follow body contours, never float independently; color must be blue-white
```

### 8.3 Pose-Specific Rules
```
1. STANDING: Weight distribution always physically plausible - never impossible balances
2. WALKING/Running: Limb opposition must be correct (left arm/right leg forward etc.) for ninja running
3. SITTING: Spine maintains natural curve - never over-straightened or excessively curved
4. JUMPING: Limb positions follow biomechanics for propulsion/landing; hair follows motion
5. HAND SIGNS: Finger positions must be anatomically possible and match specified seal references
6. FIGHTING STANCE: Weight distribution ~60% rear leg, hands properly positioned for blocking/striking
7. REACHING: Arm extension follows natural biomechanics - no hyper-extension beyond joint limits
8. LOOKING: Head turn never exceeds 90° without corresponding body rotation (unless supernatural)
9. POWER ACTIVATION: Energy emanation follows stated patterns (Karma: blue, Jougan: perceptual change, Chakra: nature-colored)
```

### 8.4 Wardrobe Rules
```
1. FIT: Clothing must follow body contours realistically - no "paint-on" effects
2. WRINKLES: Fabric wrinkles follow gravity and movement patterns - never random placement
3. LAYERING: Visible layers (undershirts, etc.) must be logically consistent with stated outfit
4. ACCESSORIES: 
   * Forehead protector: Must be worn sideways (left side down) consistently
   * Gloves: Worn when combat expected, removed appropriately
   * Pouches: Positioned logically on thighs/hips
   * Sandals: Straps secure, wear patterns consistent
5. WEAR_AND_TEAR: Damage accumulates logically - new tears appear in stress areas, not randomly
6. KARMA PATTERNS: When visible, must follow established progression (palm → forearm → chest) and glow blue
7. SPECIAL TAPE: When present, must be black with red accents, placed logically on limbs
```

### 8.5 Absolute "Don'ts" (Never Violate)
```
DON'T:
  - Change ear shape/size/position
  - Alter fundamental nose bridge structure
  - Make whisker marks asymmetrical, missing, or extra
  - Give him facial hair (he remains clean-shaven)
  - Change ethnicity appearance (must remain clearly Japanese East Asian)
  - Make him significantly taller/shorter than established ~170cm
  - Give him permanent scars/marks without story justification and reference update
  - Violate basic human anatomy in poses (impossible joint angles, etc.)
  - Allow clothing to clip through body in impossible ways
  - Make forehead protector worn straight or on wrong side
  - Change voice pitch/accent without narrative reason and voice reference update
  - Make Jougan activation inconsistent (partial white sclera, wrong pupil color/pattern)
  - Make Karma patterns wrong color (must be blue when active, not red/green/etc.)
  - Make Wind chakra wrong color (must be blue-white, not red/yellow/etc.)
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
  Model: Wan 2.7 (best for facial/hair/detail - critical for whisker marks, eye details, Jougan)
  Notes: Use extra attention to eye/whisker/region details

MEDIUM_SHOTS / DIALOGUE_SCENES:
  Model: Kling 3.0 (best for lip-sync and natural movement - essential for dialogue-heavy ninja scenes)
  Notes: Enable lip-sync tracking if dialogue present; ensure hand signs are clear

WIDE_SHOTS / ESTABLISHING:
  Model: Veo 3.1 (best for environmental consistency and depth - crucial for showing jutsu scale)
  Notes: Ensure background elements match reference; verify environmental effects (dust, water, etc.)

ACTION_SEQUENCES / COMPLEX_MOTION / TAIJUTSU:
  Model: Seedance 2.0 (multi-reference capable - ideal for complex ninja movement with multiple anchors)
  Notes: Provide key pose references for start/middle/end of fast sequences; verify motion blur appropriateness

EFFECTS_ONLY / MAGIC_ELEMENTS / JUTSU_VISUALS:
  Model: Appropriate specialized model or base SDXL with ControlNet
  Notes: 
    * Generate on transparent background for compositing
    * Pay special attention to chakra aura colors (Wind: blue-white, Lightning: yellow, Karma: reddish-black)
    * Ensure Jougan visual is pure white sclera with blue pupil/pattern
    * Verify Rasengan variants maintain spherical base with appropriate distortion
```

### 9.3 Reference Anchoring Requirements
```
MINIMUM_REFERENCES_PER_PROMPT:
  - Character close-ups: 1 pose reference + 1 expression reference
  - Character medium/wide shots: 1 full-body reference OR 2 pose references (one for stance, one for action)
  - Establishing environment shots: 1 environment reference
  - Jutsu/effect shots: 1 effect reference + 1 character/environment reference for interaction
  - Dialogue shots: Voice reference MUST be provided to audio generation
  - Jougan shots: Expression reference for activated state + eye close-up reference if needed
  - Karma activation shots: Expression/pose reference for activation stage + effect reference for patterns
```

---

## 10. Usage Guidelines

### 10.1 For Prompt Engineers
```
1. BEFORE writing prompt:
   - Consult this bible for exact description
   - Verify required references exist in library
   - Check current story point for appropriate wardrobe/evolution stage
   - Note any active power states requiring effect references (Karma, Jougan, chakra nature)
   - Verify distinctive features: whisker mark placement, hair style, height

2. WHEN writing prompt:
   - Use EXACT phrasing from "Character Core Profile" for base description
   - Insert @reference: tags for all required visual elements (pose, expression, wardrobe, effects)
   - Specify technical specs based on shot type (Wan 2.7 for close-ups, etc.)
   - Include voice reference for any dialogue
   - Add evolution notes if applicable to current chapter/scene
   - Always include distinctive features in description (whisker marks, blonde spiky hair, etc.)

3. AFTER generation:
   - Verify against this bible during QA
   - Check reference usage in metadata
   - Confirm voice matches specified ID/parameters
   - Validate distinctive features are present and correct
```

### 10.2 For Artists/Editors
```
1. REFERENCE USE:
   - Treat references as absolute truth for character appearance
   - Never "improve" upon reference - match it exactly
   - Use references for color picking (especially chakra auras: Wind=blue-white, Karma=reddish-black), texture matching, proportion checking

2. COMPOSITING:
   - Match lighting direction and intensity to environment references
   - Ensure shadow direction consistent across all elements
   - Maintain depth of field as specified in lens specs
   - Verify Jougan activation shows pure white sclera with blue pupil
   - Confirm Karma patterns follow established progression and glow blue

3. COLOR GRADING:
   - Use specified LUTs from style constants
   - Match skin tones to reference under same lighting
   - Preserve hair highlights/shadows as seen in references
   - Ensure special effects match reference colors exactly (no hue shifting)
```

### 10.3 For Quality Assurance
```
CHECKLIST PER ASSET:
  [ ] Character facial structure matches reference library (jawline, nose, eyes, ears)
  [ ] Whisker marks present, symmetrical, correctly placed (3 marks each cheek)
  [ ] Hair style matches reference (blonde, spiky front longer than back)
  [ ] Expression matches specified reference (if applicable)
  [ ] Pose matches specified reference (if applicable)
  [ ] Wardrobe matches current story chapter
  [ ] Evolution stage matches narrative point (Karma/Jougan/chakra level)
  [ ] Technical specs (resolution, fps, etc.) correct
  [ ] References properly cited in prompt metadata
  [ ] Voice matches specified ID/parameters (audio)
  [ ] No "don't" violations present
  [ ] Distinctive features correct:
      * Jougan: pure white sclera with blue pupil/pattern when active
      * Karma: blue energy emanation when active, follows progression
      * Wind chakra: blue-white aura when active
      * Forehead protector: worn sideways consistently
  [ ] Overall consistency with established canon
```

---

## Appendix: Reference Library Directory Structure
```
references/
└── character/
    └── boruto/
        ├── base/
        │   ├── boruto_base_front.jpg
        │   ├── boruto_base_3_4_left.jpg
        │   ├── boruto_base_3_4_right.jpg
        │   ├── boruto_base_profile.jpg
        │   └── boruto_base_full_body.jpg
        ├── expressions/
        │   ├── boruto_expr_neutral.jpg
        │   ├── boruto_expr_determined.jpg
        │   ├── boruto_expr_angry.jpg
        │   ├── boruto_expr_sad.jpg
        │   ├── boruto_expr_shocked_surprised.jpg
        │   ├── boruto_expr_calculating_strategic.jpg
        │   ├── boruto_expr_exhausted_injured.jpg
        │   ├── boruto_expr_joyous_smiling.jpg
        │   ├── boruto_expr_serious_focused.jpg
        │   ├── boruto_expr_playful_mischievous.jpg
        │   ├── boruto_expr_jawline_blue_eye.jpg
        │   ├── boruto_expr_chakra_wind_faint.jpg
        │   └── boruto_expr_chakra_wind_strong.jpg
        ├── poses/
        │   ├── boruto_pose_standing_neutral.jpg
        │   ├── boruto_pose_stance_combat.jpg
        │   ├── boruto_pose_walking_casual.jpg
        │   ├── boruto_pose_running_ninja.jpg
        │   ├── boruto_pose_jumping_acrobatic.jpg
        │   ├── boruto_pose_hand_signs.jpg
        │   ├── boruto_pose_fighting_stance.jpg
        │   ├── boruto_pose_power_activation_karma_stage1.jpg
        │   ├── boruto_pose_power_activation_karma_stage2.jpg
        │   └── boruto_pose_power_activation_karma_stage3.jpg
        ├── wardrobe/
        │   ├── standard/
        │   │   ├── boruto_wardrobe_standard_front.jpg
        │   │   ├── boruto_wardrobe_standard_side.jpg
        │   │   └── boruto_wardrobe_standard_back.jpg
        │   ├── karma/
        │   │   ├── boruto_wardrobe_karma_front.jpg
        │   │   ├── boruto_wardrobe_karma_side.jpg
        │   │   └── boruto_wardrobe_karma_back.jpg
        │   └── casual/
        │       ├── boruto_wardrobe_casual_front.jpg
        │       ├── boruto_wardrobe_casual_side.jpg
        │       └── boruto_wardrobe_casual_back.jpg
        └── effects/
            ├── boruto_expr_vanishing_rasengan.jpg
            ├── boruto_effect_wind_release_rasengan.jpg
            ├── boruto_effect_vanishing_rasengan.jpg
            ├── boruto_effect_chakra_clash.jpg
            ├── boruto_effect_karma_matter_distortion.jpg
            └── boruto_effect_jougan_perception.jpg
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
- **Per Major Arc** (10-15 chapters): Update evolution tracking if needed (Karma/Jougan progression)
- **Per Season** (25-30 chapters): Add new expressions/poses if character develops new traits
- **As Needed**: Add effect references for new powers/abilities discovered (new jutsu, Karma stages, Jougan development)

This bible ensures that no matter which artist, animator, or AI generator creates content featuring Boruto Uzumaki, the output will be visually consistent, narratively appropriate, and professionally polished—eliminating the "AI look" through disciplined reference use rather than relying solely on prompt engineering. The structure mirrors the Jinwoo bible for consistency in your pipeline, while being specifically tailored to ninja characteristics and the Boruto: Two Blue Vortex storyline.