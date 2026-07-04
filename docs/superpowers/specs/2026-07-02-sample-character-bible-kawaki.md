# Sample Character Bible: Kawaki (Boruto: Two Blue Vortex)
## Implementing Best Practices for Consistent AI Generation (July 2026)

This document demonstrates how to create a professional character bible for Kawaki using the best practices outlined in our AI Video Generation Best Practices guide. It serves as a template for all character bibles in the AI Live Action Studio pipeline, specifically adapted for his unique appearance and the Karma seal storyline in Boruto: Two Blue Vortex.

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
CHARACTER: Kawaki
AGE: 16 (at start of Boruto: Two Blue Vortex)
NATIONALITY: Japanese (Artificial Human/Kara experiment defector)
HEIGHT: ~175cm
BUILD: Athletic, heavily muscled (due to Karma seal enhancement and artificial nature)
HAIR: Ash-gray, messy, medium length (often falls in eyes)
EYES: Pale, almost white, with no visible pupil (due to impairment from Kara experiments)
SKIN_TONE: Pale with slight grayish undertone
DISTINGUISHING_MARKS: 
  - Karma seal (prominent black geometric mark on left palm, spreads when active)
  - Artificial organs/implants (scars on chest/abdomen from Kara experiments)
  - Possible faint circuitry patterns under skin when Karma highly active
PERSONALITY_CORE: 
  - Serious (rarely shows emotion, often grim)
  - Protective (especially of those he considers family - Naruto, Himawari)
  - Distrustful (of outsiders, due to Kara upbringing)
  - Pragmatic (focuses on results, not morality)
  - Lethally efficient (eliminates threats without hesitation)
  - Internally conflicted (between Kara programming and growing attachments)
BACKSTORY_ESSENTIAL: 
  - Created as a vessel for Isshiki Otsutsuki by Kara
  - Granted Karma seal (more potent than Boruto's due to being primary vessel)
  - Has impaired vision due to experiments (eyes pale, no visible pupil)
  - Defected from Kara after realizing Isshiki's true intentions
  - Taken in by Naruto Uzumaki as adopted son
  - Constantly struggles with his Otsutsuki/Kara nature vs. his chosen path
NINJA_RANK: Not applicable (not a traditional ninja, but combat-capable)
CHAKRA_NATURE: N/A (uses Karma/Otsutsuki power rather than traditional chakra)
SPECIAL_ABILITIES: 
  - Karma seal (Otsutsuki power): Enhanced strength, speed, energy absorption/release, matter manipulation
  - Augmented physiology: Enhanced strength, speed, durability, healing
  - Energy projection: Can fire energy blasts from palms
  - Matter decomposition: Can disintegrate matter on touch (advanced Karma)
  - Heightened senses: Despite vision impairment, enhanced hearing/smell
  - Weapon generation: Can form weapons from his own body (blades, shields)
```

## 2. Reference Library

All reference images should be stored in: `references/character/kawaki/`

### 2.1 Base References (MUST EXIST)
- `kawaki_base_front.jpg` - Front-facing neutral expression, standard lighting
- `kawaki_base_3_4_left.jpg` - Left 3/4 angle, neutral expression
- `kawaki_base_3_4_right.jpg` - Right 3/4 angle, neutral expression
- `kawaki_base_profile.jpg` - Pure profile, neutral expression (showing impaired eyes clearly)
- `kawaki_base_full_body.jpg` - Full body, neutral stance

### 2.2 Expression References (MUST EXIST)
- `kawaki_expr_neutral.jpg` - Serious, almost grim, minimal expression
- `kawaki_expr_determined.jpg` - Jaw set, narrowed eyes, intense focus
- `kawaki_expr_angry.jpg` - Eyebrows furrowed, intense glare, possible snarl
- `kawaki_expr_sad.jpg` - Downturned mouth, less energetic posture, possible tear tracks
- `kawaki_expr_shocked_surprised.jpg` - Widened eyes (still pale/no pupil), raised eyebrows, slight intake
- `kawaki_expr_calculating_strategic.jpg` - Half-lidded eyes, assessing gaze, minimal movement
- `kawaki_expr_exhausted_injured.jpg` - Heavy breathing, slumped shoulders, possible blood/scar visibility
- `kawaki_expr_joyous_smiling.jpg` - Rare: Small, genuine smile (usually reserved for Himawari/Naruto)
- `kawaki_expr_serious_grim.jpg` - Default expression: intense stare, minimal movement
- `kawaki_expr_playful_mischievous.jpg` - Very rare: Slight smirk, relaxed posture (only with close ones)
-early bonds)
- `kawaki_expr_detached_cold.jpg` - Empty stare, minimal facial movement (Kara programming surfacing)
- `kawaki_expr_protective_intense.jpg` - Fierce focus, slightly narrowed eyes, protective stance
- `kawaki_expr_pain_resignation.jpg` - Grimace of pain, accepting expression (when Karma acts up)

### 2.3 Pose References (MUST EXIST)
- `kawaki_pose_standing_neutral.jpg` - Standing straight, hands at sides or slightly forward (ready)
- `kawaki_pose_stance_combat.jpg` - Knees bent, weight forward, hands ready to strike or activate Karma
- `kawaki_pose_walking_casual.jpg` - Relaxed gait, hands often in pockets, slight forward lean
- `kawaki_pose_running_urgent.jpg` - Pronounced forward lean, arms pumping, legs extending fully
- `kawaki_pose_jumping_acrobatic.jpg` - Mid-air, legs bent, possible arm extension for balance
- `kawaki_pose_hand_signs.jpg` - Less relevant (Karma not hand-sign based), but may show defensive postures
- `kawaki_pose_fighting_stance.jpg` - Low stance, weight on balls of feet, hands ready to strike/block
- `kawaki_pose_power_activation_karma_stage1.jpg` - 
  * Stage 1: Karma mark glowing on left palm
  * Stage 2: Patterns spreading up arm, faint black/red aura
  * Stage 3: Significant coverage, visible dark energy emanating
- `kawaki_pose_examining_hands.jpg` - Hands raised, inspecting something (analytical moments)
- `kawaki_pose_looking_distance.jpg` - Gazing into distance (despite impairment, uses other senses)
- `kawaki_pose_weight_forward.jpg` - Distinctive stance: weight ~70% on front legs, ready to lunge
- `kawaki_pose_arms_crossed.jpg` - Defensive posture, arms crossed over chest (showing implants/scars)
- `kawaki_pose_karma_blade.jpg` - Arm extended, blade formed from Karma energy
- `kawaki_pose_karma_shield.jpg` - Arms forward, shield formed from Karma energy

### 2.4 Wardrobe References (MUST EXIST)
- `kawaki_wardrobe_standard_front.jpg` - Standard outfit: black high-collar jacket, dark pants, sandals
- `kawaki_wardrobe_standard_side.jpg` - Side view showing jacket cut, pant fit
- `kawaki_wardrobe_standard_back.jpg` - Back view showing gear layout, possible implant scars visible
- `kawaki_wardrobe_karma_front.jpg` - Battle outfit with visible Karma patterns spreading
- `kawaki_wardrobe_karma_side.jpg` - Side view showing Karma progression on arms/legs/torso
- `kawaki_wardrobe_karma_back.jpg` - Back view showing full Karma coverage, possible energy aura
- `kawaki_wardrobe_casual_front.jpg` - Modern clothing when off-duty (rare)
- `kawaki_wardrobe_casual_side.jpg` - Side view of casual outfit
- `kawaki_wardrobe_casual_back.jpg` - Back view of casual outfit

### 2.5 Power/Effect References (MUST EXIST FOR CONSISTENCY)
- `kawaki_expr_karma_seal_stage1.jpg` - Close-up: faint diamond mark glowing on left palm
- `kawaki_expr_karma_seal_stage2.jpg` - Close-up: patterns spreading up forearm, faint black/red aura
- `kawaki_expr_karma_seal_stage3.jpg` - Close-up: major coverage, visible dark energy emanating
- `kawaki_expr_karma_eye_glow.jpg` - Eyes showing faint black/red glow when Karma highly active
- `kawaki_expr_karma_matter_distortion.jpg` - Hand touching surface, black/red geometric patterns spreading
- `kawaki_expr_karma_energy_blast.jpg` - Palm firing concentrated energy blast
- `kawaki_expr_karma_blade_form.jpg` - Arm forming blade from Karma energy
- `kawaki_expr_karma_shield_form.jpg` - Arms forming shield from Karma energy
- `kawaki_expr_karma_implant_glow.jpg` - Chest/abdomen area showing faint circuitry glow
- `kawaki_expr_detached_stare.jpg` - Empty, unfocused gaze (Kara programming active)
- `kawaki_expr_protective_striker.jpg` - Mid-motion: arm extended, fist clenched, intense focus
- `kawaki_expr_weight_forward_lunge.jpg` - Body extended forward, weight on front leg, ready to strike

---

## 3. Voice & Audio Identity

### 3.1 Voice Profile
```
VOICE_ID: "kawaki_japanese_male_16_detached" (Example ID from ElevenLabs or similar)
SERVICE: ElevenLabs (or equivalent high-quality TTS/voice cloning)
PARAMETERS:
  - Stability: 0.6
  - Clarity: 0.8
  - Style Exaggeration: 0.1
  - Speaker Boost: false
  - Model: multilingual_v2
CHARACTERISTICS:
  - Base Pitch: Medium-low (approx. 120Hz fundamental - lower due to seriousness)
  - Tone: Flat, slightly hollow quality (reflects emotional detachment)
  - Pace: 
    * Normal: Slow, deliberate, each word weighted
    * Excited/Determined: Slightly faster but still measured
    * Angry: Low, dangerous growl (rarely raises volume)
    * Calculating: Very slow, precise, pauses between thoughts
    * Tired: Even slower, with slight rasp
    * Detached: Monotone, minimal inflection
    * Protective: Slightly warmer but still serious
  - Accent: Standard Tokyo Japanese with slight rasp
  - Unique Traits: 
    * Tendency to speak in short, clipped sentences
    * Rarely uses honorifics unless speaking to Naruto/Himawari
    * Voice drops to near-whisper when sharing important information
    * Almost never laughs; when he does, it's brief and humorless
    * Breathing often audible (suggests constant exertion or tension)
    * Speaks with slight urgency when protecting others
```

### 3.2 Audio References (MUST EXIST)
Store in: `references/voice/kawaki/`
- `kawaki_voice_normal.wav` - Normal tone: slow, deliberate, slightly detached
- `kawaki_voice_determined.wav` - Firmer, more urgent but still measured
- `kawaki_voice_angry.wav` - Low growl, dangerous intensity
- `kawaki_voice_shocked.wav` - Slight intake, eyes widen (still pale)
- `kawaki_voice_calculating.wav` - Very slow, precise, distinct pauses
- `kawaki_voice_tired.wav` - Even slower, slight rasp
- `kawaki_voice_detached.wav` - Monotone, minimal inflection (Kara programming)
- `kawaki_voice_protective.wav` - Slightly warmer but still serious
- `kawaki_voice_pain.wav` - Grimace of pain, strained but enduring
- `kawaki_voice_whisper.wav` - Near-whisper for important information
- `kawaki_voice_laugh.wav` - Rare: brief, humorless chuckle

### 3.3 Sound Effect References
- `kawaki_sfx_karma_activate.wav` - Deep resonant pulse + geometric spread sound
- `kawaki_sfx_karma_blast.wav` - Concentrated energy discharge (sharp crack + hum)
- `kawaki_sfx_karma_blade.wav` - Metallic shimmer + energy hum
- `kawaki_sfx_karma_shield.wav` - Deep thud + energy absorption sound
- `kawaki_sfx_karma_implant.wav` - Subtle pulsing from chest/abdomen area
- `kawaki_sfx_footsteps_heavy.wav` - Heavy, deliberate steps (enhanced physiology)
- `kawaki_sfx_breathing_heavy.wav` - Slightly labored breathing (constant exertion)
```

---

## 4. Wardrobe System

### 4.1 Standard Outfit (Primary Attire)
```
STANDARD_OUTFIT:
  - Description: Black high-collar jacket, dark pants (his usual attire)
  - Key_Pieces: 
    * Black high-collar jacket (reaches mid-cheek, covers lower face partially)
    * Dark gray/black pants (straight fit, durable material)
    * Open-toed sandals (simple straps, durable)
    * No shirt visible (jacket covers torso)
    * Possible bandages/wraps under jacket (hiding implant scars)
  - Color_Palette: Monochrome black/dark gray
  - Reference_Images: kawaki_wardrobe_standard_front.jpg, kawaki_wardrobe_standard_side.jpg, kawaki_wardrobe_standard_back.jpg
  - Usage: Primary outfit for all situations (missions, training, daily life)
  - Notes: 
    * Jacket often slightly unzipped at top to improve vision/breathing
    * High collar serves to partially conceal his face and expression
    * Pants show wear at knees from constant movement
    * Sandals show significant sole wear
    * Jacket may have hidden when using Karma extensively (sleeves rolled/pushed up)
```

### 4.2 Special Attire (Karma Activation)
```
KARMA_ACTIVATION_ATTIRE:
  - Description: Outfit when Karma seal is significantly active
  - Key_Pieces: 
    * Same base outfit but with visible Karma patterns spreading
    * May remove jacket sleeves entirely for full arm movement in extreme cases
    * Possible additional wraps/bandages when using advanced Karma
  - Color_Palette: Black with dark gray accents, plus glowing black/red Karma patterns (when active)
  - Reference_Images: kawaki_wardrobe_karma_front.jpg, kawaki_wardrobe_karma_side.jpg, kawaki_wardrobe_karma_back.jpg
  - Usage: High-stakes battles, Karma-powered confrontations
  - Notes: 
    * Karma patterns glow brighter with increased power usage
    * Patterns start as faint mark on left palm, spread to cover arms/chest/torso at peak
    * Jacket sleeves often discarded/pushed back for unrestricted arm movement
    * High collar remains (habit/concealment)
    * Pants may show tearing at seams from muscle expansion during activation
```

### 4.3 Rare Casual Wear (Off-Duty with Naruto)
```
CASUAL_WEAR:
  - Description: Modern clothing when off-duty (extremely rare - only with Naruto/Himawari)
  - Key_Pieces: 
    * Dark hoodie or sweater
    * Jeans
    * Sneakers
  - Color_Palette: Dark colors (black, gray, navy)
  - Reference_Images: kawaki_wardrobe_casual_front.jpg, kawaki_wardrobe_casual_side.jpg, kawaki_wardrobe_casual_back.jpg
  - Usage: Extremely rare downtime (only when feeling safe with Naruto family)
  - Notes: 
    * Clothing often too large (donated by Naruto)
    * Shows signs of being uncomfortable in casual wear
    * Frequently adjusts clothing (not used to loose fit)
    * May keep jacket on underneath (habit/comfort)
```

### 4.4 Medical/Specialized Gear
```
MEDICAL_GEAR:
  - BANDAGES/WRAPS:
    * Description: Used to cover implant scars or stabilize injuries
    * Appearance: White or black medical tape/wraps
    * Reference: Create when visible in scene
    
  - VISION_AID:
    * Description: Experimental device to compensate for impaired vision
    * Appearance: Visor-like device over eyes (rarely seen, mostly experimental)
    * Reference: Create when Mitsuki or Naruto provides it
    
  - WEIGHTS:
    * Description: Training weights he wears constantly
    * Appearance: Ankle/wrist weights (discreet, under clothing)
    * Reference: Create when showing training regimen
```

---

## 5. Expression Library

### 5.1 Usage Guidelines
- **ALWAYS** use reference images for expressions when generating
- **MAINTAIN** core facial structure (jawline, nose shape, eye shape, impaired eye appearance)
- **RESPECT** distinctive features: pale eyes with no visible pupil must be consistent
- **ENSURE** emotional range is appropriately limited (he shows little emotion)
- **ALLOW** Karma activation effects only when narratively justified
- **VERIFY** expressions match his generally serious/detached demeanor

### 5.2 Expression Details
| Expression | Description | Key Features | Reference Image |
|------------|-------------|--------------|-----------------|
| **NEUTRAL** | Default state: serious, almost grim | Minimal expression, slight jaw tension, eyes pale/no pupil, mirada vacía | `kawaki_expr_neutral.jpg` |
| **DETERMINED** | Resolved to overcome challenge | Jaw visibly tightened, eyebrows slightly furrowed, eyes narrowed in focus, posture forward | `kawaki_expr_determined.jpg` |
| **ANGRY** | Righteous fury or frustration | Eyebrows strongly furrowed, eyes narrowed to slits, nostrils flared, jaw clenched, intense stare | `kawaki_expr_angry.jpg` |
| **SAD** | Disappointment or grief | Downturned mouth corners, less tension in forehead, eyes avoiding contact, slumped posture | `kawaki_expr_sad.jpg` |
| **SHOCKED/SURPRISED** | Sudden surprise or revelation | Eyes widened (still pale/no pupil), eyebrows raised, mouth slightly open, head recoil | `kawaki_expr_shocked_surprised.jpg` |
| **CALCULATING/STRATEGIC** | Assessing situation/threat | Half-lidded eyes, head slightly tilted, minimal facial movement, finger to chin, evaluating stare | `kawaki_expr_calculating_strategic.jpg` |
| **EXHAUSTED/INJURED** | Extreme fatigue or visible injury | Heavy breathing, slumped shoulders, possible sheen of sweat/blood, less eye focus, possible grimace | `kawaki_expr_exhausted_injured.jpg` |
| **JOYOUS/SMILING** | Genuine happiness or relief (RARE) | Small, genuine smile showing few teeth, eyes slightly crinkled, rare posture relaxation | `kawaki_expr_joyous_smiling.jpg` |
| **SERIOUS/GRIM** | Default serious expression | Intense stare, minimal expression change, slightly narrowed eyes, upright posture, ready stance | `kawaki_expr_serious_grim.jpg` |
| **PLAYFUL/MISCHIEVOUS** | Lighthearted energy (EXTREMELY RARE) | Slight smirk, relaxed shoulders, hands loose at sides, rare moment of ease | `kawaki_expr_playful_mischievous.jpg` |
| **DETACHED/COLD** | Kara programming surfacing | Empty, unfocused gaze, minimal facial movement, monotone voice, mechanical movements | `kawaki_expr_detached_cold.jpg` |
| **PROTECTIVE_INTENSE** | Fierce protection of loved ones | Intense focus, slightly narrowed eyes, body angled to shield, ready to strike | `kawaki_expr_protective_intense.jpg` |
| **PAIN_RESIGNATION** | Accepting pain from Karma | Grimace of pain, eyes closed or looking down, posture relaxed but enduring | `kawaki_expr_pain_resignation.jpg` |
| **KARMA_SEAL_STAGE_1** | Initial Karma awareness | Faint diamond mark on left palm glowing softly, slight intake of breath, focused on hand | *See Karma progression* |
| **KARMA_SEAL_STAGE_2** | Moderate Karma usage | Patterns spreading up forearm (~30-50% coverage), faint black/red aura, tensed posture | *See Karma progression* |
| **KARMA_SEAL_STAGE_3** | Significant Karma activation | Major coverage on arms/chest/torso, visible dark energy emanating, fighting stance | *See Karma progression* |
| **KARMA_ENERGY_BLAST** | Firing concentrated energy | Palm open, focused energy gathering, intense stare, stance ready for release | *Context-dependent* |
| **KARMA_BLADE_FORM** | Forming weapon from Karma | Arm extended, hand shaping blade, energy visible along forearm, determined expression | *Context-dependent* |
| **KARMA_SHIELD_FORM** | Forming shield from Karma | Arms forward, hands shaping shield, energy visible between palms, defensive stance | *Context-dependent* |
| **WEIGHT_FORWARD_LUNGE** | Preparing to strike | Body extended ~70% weight on front leg, arms ready, intense focus, coiled like spring | `kawaki_expr_weight_forward_lunge.jpg` |
| **IMPLANTS_VISIBLE** | Scars/implants showing | Chest/abdomen area visible, surgical scars, possible faint circuitry, matter-of-fact expression | *Context-dependent* |
| **DETACHED_STARE** | Empty, unfocused gaze | Eyes looking through object/person, minimal blinking, posture relaxed but alert, voice monotone | `kawaki_expr_detached_stare.jpg` |

---

## 6. Pose Library

### 6.1 Usage Guidelines
- **ALWAYS** use pose references when character positioning is specified
- **MAINTAIN** anatomical accuracy and natural weight distribution (enhanced physiology)
- **RESPECT** distinctive features: impaired eyes (pale, no pupil) must be consistent
- **ENSURE** clothing follows body contours realistically during movement
- **ALLOW** variations for action but keep core pose recognizable
- **ACCURATELY** depict Karma activation patterns when specified (critical for power visualization)
- **NOTE** his distinctive weight-forward stance when preparing to strike

### 6.2 Pose Details
| Pose | Description | Key Features | Reference Image |
|------|-------------|--------------|-----------------|
| **STANDING_NEUTRAL** | Default standing position | Feet shoulder-width apart, weight evenly distributed, arms relaxed at sides or slightly forward, slightly forward lean | `kawaki_pose_standing_neutral.jpg` |
| **STANCE_COMBAT_READY** | Prepared for strike/Karma use | Knees bent (~25°), weight ~60% front leg, hands at waist ready to strike or activate Karma, alert posture | `kawaki_pose_stance_combat.jpg` |
| **WALKING_CASUAL** | Natural walking pace | Relaxed gait, hands often in pockets or loose at sides, slight forward lean, head level | `kawaki_pose_walking_casual.jpg` |
| **RUNNING_URGENT** | High-speed movement | Pronounced forward lean, arms pumping vigorously behind back, knees lifting high, foot strike midfoot/toe | `toe` | `kawaki_pose_running_urgent.jpg` |
| **JUMPING/ACROBATIC** | Mid-air maneuver | Legs bent for propulsion/landing, possible arm extension for balance, body twisted for direction change | `kawaki_pose_jumping_acrobatic.jpg` |
| **FIGHTING_STANCE** | Defensive/ offensive ready | Low stance (~40° knee bend), weight 60% on rear leg, front foot pointed forward, hands up protecting torso, elbows in, ready to strike/block | `kawaki_pose_fighting_stance.jpg` |
| **POWER_ACTIVATION_KARMA_STAGE_1** | Initial Karma awareness | Faint diamond mark on left palm glowing, slight intake of breath, eyes focused on hand, slight tensing | *See Karma progression* |
| **POWER_ACTIVATION_KARMA_STAGE_2** | Moderate Karma usage | Patterns spreading up forearm (~30-50% coverage), faint black/red aura (~10-15% opacity), tensed posture, assessing expression | *See Karma progression* |
| **POWER_ACTIVATION_KARMA_STAGE_3** | Significant Karma activation | Major coverage on arms/chest/torso (~50-75%), visible dark energy emanating (~20-30% opacity), fighting stance, energy particles in air | *See Karma progression* |
| **EXAMINING_HANDS** | Inspecting palms/objects | Hands raised to eye level, palms facing viewer or slightly angled, fingers naturally curved, relaxed tension, analytical expression | `kawaki_pose_examining_hands.jpg` |
| **LOOKING_DISTANCE** | Gazing into distance (using other senses) | Head slightly tilted, eyes unfocused but alert, relaxed posture, slight head turn as if listening, assessing expression | `kawaki_pose_looking_distance.jpg` |
| **WEIGHT_FORWARD_STANCE** | Distinctive ready stance | Weight ~70% on front leg, rear leg bent for balance, arms ready to strike, intense focus, coiled posture | `kawaki_pose_weight_forward.jpg` |
| **WEIGHT_FORWARD_LUNGE** | Preparing to strike | Body extended forward, weight ~80% on front leg, rear legstraight back, arms ready to strike, intense focus | `kawaki_expr_weight_forward_lunge.jpg` |
| **ARMS_CROSSED** | Defensive posture | Arms crossed firmly over chest, hands gripping opposite shoulders, serious expression, slight forward lean | `kawaki_pose_arms_crossed.jpg` |
| **KARMA_BLADE_FORM** | Forming weapon from Karma | Arm extended, palm open, energy shaping along forearm into blade, focused expression, stance ready | `kawaki_pose_karma_blade.jpg` |
| **KARMA_SHIELD_FORM** | Forming shield from Karma | Arms forward, palms facing outward, energy shaping between palms into shield, defensive stance | `kawaki_pose_karma_shield.jpg` |
| **KARMA_ENERGY_BLAST** | Firing energy blast | Palm open and forward, energy gathering visible in palm, intense focus, stance ready for release, slight recoil anticipation | *Context-dependent* |
| **RECOIL_AFTER_BLAST** | After firing energy blast | Body slightly jerked backward, arm recovering, intense focus, preparing for next action | *Context-dependent* |
| **IMPLANTS_VISIBLE** | Chest/abdomen area exposed | Jacket open or removed, surgical scars visible, possible faint circuitry glow, matter-of-fact expression | *Context-dependent* |
| **KNEELING_PROTECTIVE** | Shielding someone | One knee down, body angled to protect, arms raised to shield, intense focus, ready to strike | *Context-dependent* |
| **STANDING_PROTECTIVE** | Shielding stance | Feet wide, arms extended to sides or front, intense focus, ready to intervene, protective posture | *Context-dependent* |
| **SITTING_REFLECTIVE** | Thinking/planning | Sitting upright, hands on knees or loose in lap, gaze unfocused but alert, slight forward lean | *Context-dependent* |

---

## 7. Evolution Tracking

Track physical/visual changes that occur naturally through story progression:

### 7.1 Early Two Blue Vortex (Chapters 1-10) - "Adjusting to New Life"
- **Physique**: Heavily muscled but less defined than later (still adjusting to freedom)
- **Eyes**: 
  - Persistently pale/almost white, no visible pupil
  - Possible slight light sensitivity (squinting in bright light)
  - No Karma glow in eyes normally
- **Hair**: Ash-gray, messy, medium length (may be slightly longer from captivity)
- **Expression Frequency**: 
  - High: Serious/grim, detached/cold
  - Medium: Determined, calculating
  - Low: Shocked, sad
  - Very Rare: Joyous, playful
- **Wardrobe**: 
  - Primary: Standard outfit (jacket may be ill-fitting from captivity)
  - Secondary: Rare casual wear (only with Naruto family)
  - Special: Karma seal mostly inactive (faint mark only on palm)
- **Power Manifestation**: 
  - Karma: Faint mark on left palm, occasional pulse during stress or anger
  - Physiology: Enhanced strength/speed noticeable but not maximized
  - Implants: Scar tissue visible but not glowing

### 7.2 Mid Two Blue Vortex (Chapters 11-30) - "Finding His Place"
- **Physique**: More defined musculature from training and combat
- **Eyes**: 
  - Persistently pale/almost white, no visible pupil
  - Possible slight improvement in light adaptation
  - Karma may cause faint black/red glow in eyes during high activation
- **Hair**: Maintains style but appears healthier/shinier from better nutrition
- **Expression Frequency**: 
  - High: Serious/grim, determined, protective_intense
  - Medium: Calculating, weight_forward_stance
  - Low: Shocked, sad, detached/cold
  - Very Rare: Joyous, playful (only with Himawari in safe moments)
- **Wardrobe**: 
  - Primary: Standard outfit (well-fitted, shows customization: tape, adjustments)
  - Secondary: Casual wear (extremely rare, uncomfortable)
  - Special: Karma seal visible during use, spreading predictably
- **Power Manifestation**: 
  - Karma: Clear patterns on forearm during use, black/red aura stronger
  - Physiology: Enhanced strength/speed/healing at peak
  - Implants: Scar tissue may show faint circuitry glow during high Karma
  - Vision: Possible slight impairment compensation (squinting less)

### 7.3 Late Two Blue Vortex (Chapters 31-50+) - "Embracing His Path"
- **Physique**: Peak athletic build, subtle otherworldly presence from Karma
- **Eyes**: 
  - Persistently pale/almost white, no visible pupil
  - Karma activation may cause distinct black/red glow in eyes
  - Possible adaptation to light (less squinting)
- **Hair**: Maintains style but may show slight movement in stillness (Karma influence)
- **Expression Frequency**: 
  - High: Protective_intense, determined, calculating
  - Medium: Serious/grim, weight_forward_stance
  - Low: Shocked, sad
  - Very Rare: Joyous, playful (only with Himawari/Naruto in completely safe moments)
  - Occasional: Detached/cold (only when Kara programming surges strongly)
- **Wardrobe**: 
  - Primary: Standard outfit (heavily customized: multiple tape layers, modified fit, possible sleeve removal)
  - Secondary: Casual wear (still rare, but slightly more comfortable)
  - Special: Karma seal patterns predictable during use, Jougan activation clean
- **Power Manifestation**: 
  - Karma: Patterns spread predictably (palm → forearm → full arm → chest/torso), strong black/red aura
  - Physiology: Enhanced strength/speed/healing maximized, rapid recovery
  - Implants: Scar tissue shows clear circuitry glow during high Karma
  - Karma Effects: Energy blasts, blades, shields more refined and controllable
  - Vision: May show slight improvement or compensation mechanisms

### 7.2 Special State Markers
Document temporary states that require specific references:

```
KARMA_SEAL_STAGE_1: 
  - Description: Initial awareness/low-level usage
  - Visual: Faint diamond mark on left palm glowing softly (approx. 5% opacity)
  - Duration: Seconds during active use or stress
  - Reference: kawaki_expr_karma_seal_stage1.jpg

KARMA_SEAL_STAGE_2:
  - Description: Moderate power use (enhanced physicals, energy techniques)
  - Visual: Patterns spreading up forearm (25-50% coverage), faint black/red aura (10-15% opacity)
  - Duration: Minutes during sustained use
  - Reference: kawaki_expr_karma_seal_stage2.jpg

KARMA_SEAL_STAGE_3:
  - Description: Significant activation (enhanced strength, energy projection)
  - Visual: Major coverage on arms/chest/torso (50-75%), visible black/red energy emanating (20-30% opacity), possible geometric projection
  - Duration: Extended use in battles
  - Reference: kawaki_expr_karma_seal_stage3.jpg

KARMA_EYE_GLOW:
  - Description: Karma highly active Karma affecting vision
  - Visual: 
    * Eyes: Faint black/red glow in irises (when highly active)
    * Effect: Slight visual distortion, enhanced perception
  - Duration: During peak Karma activation
  - Reference: kawaki_expr_karma_eye_glow.jpg

KARMA_ENERGY_BLAST:
  - Description: Firing concentrated energy blast from palm
  - Visual: 
    * Palm: Open and forward, energy gathering visible
    * Blast: Concentrated beam of black/red energy
    * Effect: Air distortion, particulate matter in beam
  - Duration: From charge to release (typically 1-3 seconds)
  - Reference: kawaki_expr_karma_energy_blast.jpg

KARMA_BLADE_FORM:
  - Description: Forming weapon from Karma energy
  - Visual: 
    * Arm: Extended, palm open, energy shaping along forearm
    * Blade: Taking shape as black/red energy construct
    * Effect: Energy particles flowing along blade edges
  - Duration: During formation (typically 1-2 seconds)
  - Reference: kawaki_expr_karma_blade_form.jpg

KARMA_SHIELD_FORM:
  - Description: Forming defensive shield from Karma energy
  - Visual: 
    * Arms: Forward, palms facing outward, energy shaping between palms
    * Shield: Taking shape as black/red energy construct
    * Effect: Energy particles flowing along shield edges
  - Duration: During formation (typically 1-2 seconds)
  - Reference: kawaki_expr_karma_shield_form.jpg

KARMA_MATTER_DISTORTION:
  - Description: Karma seal used for matter decomposition
  - Visual: 
    * Palm: Open and touching surface, energy visible
    * Effect: Black/red geometric patterns spreading from contact point
    * Result: Localized area disintegrating to dust
  - Duration: During active use (typically contact to completion)
  - Reference: kawaki_expr_karma_matter_distortion.jpg

DETACHED_COLD_STATE:
  - Description: Kara programming temporarily overriding personality
  - Visual: 
    * Eyes: Empty, unfocused gaze (looking through objects)
    * Face: Minimal expression, muscles slightly tense
    * Posture: Slightly rigid, mechanical movements
    * Voice: Monotone, minimal inflection
  - Duration: Varies (seconds for flash, minutes for sustained)
  - Reference: kawaki_expr_detached_cold.jpg

PROTECTIVE_INTENSE_STATE:
  - Description: Fierce protection of loved ones activated
  - Visual: 
    * Eyes: Intense focus, slightly narrowed
    * Posture: Body angled to shield, weight forward, ready to strike
    * Effect: Adrenaline surge, enhanced reaction time
  - Duration: During active protection scenario
  - Reference: kawaki_expr_protective_intense.jpg

WEIGHT_FORWARD_LUNGE_STATE:
  - Description: Preparing to strike with weight-forward stance
  - Visual: 
    * Weight: ~70-80% on front leg, rear leg bent for balance
    * Posture: Body extended forward, arms ready, coiled like spring
    * Effect: Maximum force generation for strike
  - Duration: From readiness to release (typically contact or release)
  - Reference: kawaki_expr_weight_forward_lunge.jpg
```

---

## 8. Consistency Rules & "Don'ts"

### 8.1 Absolute Requirements (Must Always Follow)
```
1. FACE_STRUCTURE: Jawline, nose bridge, eye shape (palm, no pupil), ear placement must remain consistent
2. EYE_APPEARANCE: Eyes must remain pale/almost white with no visible pupil - never normal eyes unless specifically showing Karma glow
3. WHISKER_MARKS: Kawaki does NOT have whisker marks - never add them
4. HAIRLINE: Natural hairline must be maintained - ash-gray, messy, medium length
5. HEIGHT_PROPORTIONS: Head-to-body ratio must remain ~1:6.8 (slightly smaller head ratio for heavily muscled build)
6. SKIN_TONE_CONSISTENCY: Base undertone (pale with grayish) must remain - no sudden flush or pallor without reason
7. IMPLANTS/SCARS: Surgical scars on chest/abdomen must be present/logically consistent - never remove without story reason
```

### 8.2 Expression-Specific Rules
```
1. NEUTRAL/SERIOUS_GRIM: Expression shows minimal change - jaw tension possible, eyes alert but unfocused
2. DETERMINED: Jaw tension visible but never to point of teeth clenching (unless showing extreme effort)
3. ANGRY: Forehead wrinkles appear between brows, never across forehead only; eyes remain pale/no pupil
4. SAD: Eyes never fully closed - always showing some level of engagement/world awareness
5. SHOCKED/SURPRISED: Eyebrows rise together, never one higher than the other (unless showing specific head tilt)
6. CALCULATING/STRATEGIC: One hand typically near face/chin, other relaxed at side or on hip
7. EXHAUSTED/INJURED: Shoulder slump visible but never to point of collapsing posture (unless unconscious)
8. JOYOUS/SMILING: Eyes crinkle but never completely closed - rare occurrence, small genuine smile
9. SERIOUS/GRIM: Minimal change from neutral but eyes intensely focused; no furrowed brow unless assessing threat
10. PLAYFUL/MISCHIEVOUS: Extremely rare - only with close bonds, expression shows rare relaxation
11. DETACHED/COLD: Eyes empty and unfocused, minimal facial movement, voice monotone
12. PROTECTIVE_INTENSE: Intense focus, body angled to shield, ready to strike
13. KARMA ACTIVATION: Energy must follow established patterns (black/red, not blue/yellow/etc.), progression must be logical (palm → arm → chest)
14. WEIGHT_FORWARD: Posture must show distinct forward weight distribution, never impossible balance
15. IMPLANTS_VISIBLE: Scars must appear anatomically correct and consistent with stated medical history
```

### 8.3 Pose-Specific Rules
```
1. STANDING: Weight distribution always physically plausible - never impossible balances
2. WALKING/Running: Limb opposition must be correct (left arm/right leg forward etc.)
3. SITTING: Spine maintains natural curve - never over-straightened or excessively curved
4. JUMPING: Limb positions follow biomechanics for propulsion/landing; hair follows motion
5. FIGHTING STANCE: Weight distribution ~60% rear leg, hands properly positioned for blocking/striking
6. WEIGHT_FORWARD: Weight distribution must show clear forward bias (~70% front leg), never reversed or equal
7. REACHING: Arm extension follows natural biomechanics - no hyper-extension beyond joint limits
8. LOOKING: Head turn never exceeds 90° without corresponding body rotation (atasaray supernatural)
9. POWER ACTIVATION: Energy emanation follows stated patterns (Karma: black/red, implants: faint circuitry glow)
10. KARMA BLAST/SHIELD/BLADE: Energy constructs must follow physical laws (trajectory, dissipation, etc.)
11. IMPLANTS_VISIBLE: When visible, scars must match reference locations and appearance
```

### 8.4 Wardrobe Rules
```
1. FIT: Clothing must follow body contours realistically - no "paint-on" effects
2. WRINKLES: Fabric wrinkles follow gravity and movement patterns - never random placement
3. LAYERING: Visible layers (undershirts, wraps, etc.) must be logically consistent with stated outfit
4. ACCESSORIES: 
   * High collar jacket: Must cover lower face partially consistently
   * Sandals: Straps secure, wear patterns consistent
   * Bandages/wraps: Present when treating injuries or covering implants
   * Weights: Ankle/wrist weights present when showing training (discreet under clothing)
5. WEAR_AND_TEAR: Damage accumulates logically - new tears appear in stress areas, not randomly
6. KARMA PATTERNS: When visible, must follow established progression (palm → forearm → chest) and glow black/red
7. SPECIAL WRAPS/BANDAGES: When present, must be medically appropriate and logically placed
```

### 8.5 Absolute "Don'ts" (Never Violate)
```
DON'T:
  - Change ear shape/size/position
  - Alter fundamental nose bridge structure
  - Give him whisker marks (he does NOT have them)
  - Make his eyes normal/pupiled (they are permanently pale/no pupil due to impairment)
  - Change ethnicity appearance (must remain clearly Japanese East Asian)
  - Make him significantly taller/shorter than established ~175cm
  - Give him permanent scars/marks without story justification and reference update
  - Violate basic human anatomy in poses (impossible joint angles, etc.)
  - Allow clothing to clip through body in impossible ways
  - Make high collar jacket worn low or not covering lower face
  - Change voice pitch/accent without narrative reason and voice reference update
  - Make Karma patterns wrong color (must be black/red when active, not blue/green/etc.)
  - Make his weight-forward stance reversed or equal distribution
  - Make implants disappear or change location without story reason
  - Make him show excessive emotion (he is fundamentally serious/detached)
  - Make his impaired vision suddenly normal without story justification and aid device
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
  Model: Wan 2.7 (best for facial/hair/detail - critical for impaired eyes, facial tension, implant scars)
  Notes: Use extra attention to eye/jaw/implant region details; ensure pupil absence is clear

MEDIUM_SHOTS / DIALOGUE_SCENES:
  Model: Kling 3.0 (best for lip-sync and natural movement - essential for his sparse but meaningful dialogue)
  Notes: Enable lip-sync tracking; ensure sparse dialogue matches his speech patterns

WIDE_SHOTS / ESTABLISHING:
  Model: Veo 3.1 (best for environmental consistency and depth - crucial for showing his presence in scenes)
  Notes: Ensure background elements match reference; verify environmental effects (dust, debris, etc.)

ACTION_SEQUENCES / COMPLEX_MOTION / COMBAT:
  Model: Seedance 2.0 (multi-reference capable - ideal for his distinctive movement patterns with multiple anchors)
  Notes: 
    * Provide key pose references for weight-forward stance, combat ready, striking poses
    * Verify motion blur appropriateness for his enhanced physiology
    * Check that his distinctive gait is preserved

EFFECTS_ONLY / MAGIC_ELEMENTS / KARMA_VISUALS:
  Model: Appropriate specialized model or base SDXL with ControlNet
  Notes: 
    * Generate on transparent background for compositing
    * Pay special attention to Karma energy colors (black/red, not blue/yellow/etc.)
    * Ensure his impaired eyes remain pale/no pupil unless showing Karma glow
    * Verify energy blasts, blades, shields follow physical laws
    * Verify implant scars remain visible and consistent when torso exposed
```

### 9.3 Reference Anchoring Requirements
```
MINIMUM_REFERENCES_PER_PROMPT:
  - Character close-ups: 1 pose reference + 1 expression reference
  - Character medium/wide shots: 1 full-body reference OR 2 pose references (one for stance, one for action)
  - Establishing environment shots: 1 environment reference
  - Karma/effect shots: 1 effect reference + 1 character/environment reference for interaction
  - Dialogue shots: Voice reference MUST be provided to audio generation
  - Impairment shots: Expression reference for neutral/serious + eye close-up reference if needed
  - Karma activation shots: Expression/pose reference for activation stage + effect reference for patterns
  - Implant visibility shots: Expression reference + torso reference showing scars/implants
  - Weight-forward shots: Pose reference for weight_forward_stance/lunge + expression reference
```

---

## 10. Usage Guidelines

### 10.1 For Prompt Engineers
```
1. BEFORE writing prompt:
   - Consult this bible for exact description
   - Verify required references exist in library
   - Check current story point for appropriate wardrobe/evolution stage
   - Note any active Karma states requiring effect references
   - Verify distinctive features: impaired eyes (pale/no pupil), high collar jacket, hair style, height
   - Check for implant visibility if torso exposed

2. WHEN writing prompt:
   - Use EXACT phrasing from "Character Core Profile" for base description
   - Insert @reference: tags for all required visual elements (pose, expression, wardrobe, effects, implants)
   - Specify technical specs based on shot type (Wan 2.7 for close-ups, etc.)
   - Include voice reference for any dialogue
   - Add evolution notes if applicable to current chapter/scene
   - Always include distinctive features in description (impaired eyes, high collar, ash-gray hair, etc.)
   - Include Karma progression details when power active

3. AFTER generation:
   - Verify against this bible during QA
   - Check reference usage in metadata
   - Confirm voice matches specified ID/parameters
   - Validate distinctive features are present and correct:
      * Eyes: pale/almost white, no visible pupil (unless Karma glow active)
      * High collar jacket: covering lower face partially
      * Hair: ash-gray, messy, medium length
      * Height: consistent with ~175cm reference
      * Karma patterns: black/red when active, following progression
      * Implants: visible/scarred when torso exposed, anatomically correct
```

### 10.2 For Artists/Editors
```
1. REFERENCE USE:
   - Treat references as absolute truth for character appearance
   - Never "improve" upon reference - match it exactly
   - Use references for color picking (especially Karma auras: black/red, implant scars: accurate tones)
   - Use references for texture matching (skin, hair, clothing, scar tissue)
   - Use references for proportion checking (especially height, weight distribution)

2. COMPOSITING:
   - Match lighting direction and intensity to environment references
   - Ensure shadow direction consistent across all elements
   - Maintain depth of field as specified in lens specs
   - Verify impaired eyes show pale/almost white with no visible pupil (unless Karma glow)
   - Confirm high collar jacket covers lower face appropriately
   - Validate Karma patterns follow established progression and glow black/red
   - Check that energy blasts, blades, shields follow physical laws
   - Ensure implant scars remain consistent when torso exposed

3. COLOR GRADING:
   - Use specified LUTs from style constants
   - Match skin tones to reference under same lighting (pale with grayish undertone)
   - Preserve hair highlights/shadows as seen in references
   - Ensure special effects match reference colors exactly (no hue shifting for Karma: black/red)
   - Verify scar tissue colors remain consistent
```

### 10.3 For Quality Assurance
```
CHECKLIST PER ASSET:
  [ ] Character facial structure matches reference library (jawline, nose, eyes, ears)
  [ ] Eyes: pale/almost white, no visible pupil (unless Karma glow active)
  [ ] Hair style matches reference (ash-gray, messy, medium length)
  [ ] High collar jacket: covering lower face partially (consistently)
  [ ] Expression matches specified reference (if applicable)
  [ ] Pose matches specified reference (if applicable)
  [ ] Wardrobe matches current story chapter
  [ ] Evolution stage matches narrative point (Karma level, implant visibility)
  [ ] Technical specs (resolution, fps, etc.) correct
  [ ] References properly cited in prompt metadata
  [ ] Voice matches specified ID/parameters (audio)
  [ ] No "don't" violations present
  [ ] Distinctive features correct:
      * Eyes: pale/almost white, no visible pupil (exception: Karma glow active)
      * High collar jacket: consistently covering lower face partially
      * Hair: ash-gray, messy, medium length
      * Height: consistent with reference
      * Karma: black/red energy when active, follows logical progression
      * Implants: scar tissue visible when torso exposed, anatomically correct
      * Weight-forward stance: present when preparing to strike (~70% front leg weight)
  [ ] Overall consistency with established canon
```

---

## Appendix: Reference Library Directory Structure
```
references/
└── character/
    └── kawaki/
        ├── base/
        │   ├── kawaki_base_front.jpg
        │   ├── kawaki_base_3_4_left.jpg
        │   ├── kawaki_base_3_4_right.jpg
        │   ├── kawaki_base_profile.jpg
        │   └── kawaki_base_full_body.jpg
        ├── expressions/
        │   ├── kawaki_expr_neutral.jpg
        │   ├── kawaki_expr_determined.jpg
        │   ├── kawaki_expr_angry.jpg
        │   ├── kawaki_expr_sad.jpg
        │   ├── kawaki_expr_shocked_surprised.jpg
        │   ├── kawaki_expr_calculating_strategic.jpg
        │   ├── kawaki_expr_exhausted_injured.jpg
        │   ├── kawaki_expr_joyous_smiling.jpg
        │   ├── kawaki_expr_serious_grim.jpg
        │   ├── kawaki_expr_playful_mischievous.jpg
        │   ├── kawaki_expr_detached_cold.jpg
        │   ├── kawaki_expr_protective_intense.jpg
        │   ├── kawaki_expr_pain_resignation.jpg
        │   ├── kawaki_expr_karma_seal_stage1.jpg
        │   ├── kawaki_expr_karma_seal_stage2.jpg
        │   ├── kawaki_expr_karma_seal_stage3.jpg
        │   ├── kawaki_expr_karma_eye_glow.jpg
        │   ├── kawaki_expr_karma_matter_distortion.jpg
        │   ├── kawaki_expr_karma_energy_blast.jpg
        │   ├── kawaki_expr_karma_blade_form.jpg
        │   └── kawaki_expr_karma_shield_form.jpg
        ├── poses/
        │   ├── kawaki_pose_standing_neutral.jpg
        │   ├── kawaki_pose_stance_combat.jpg
        │   ├── kawaki_pose_walking_casual.jpg
        │   ├── kawaki_pose_running_urgent.jpg
        │   ├── kawaki_pose_jumping_acrobatic.jpg
        │   ├── kawaki_pose_fighting_stance.jpg
        │   ├── kawaki_pose_weight_forward.jpg
        │   ├── kawaki_pose_weight_forward_lunge.jpg
        │   ├── kawaki_pose_arms_crossed.jpg
        │   ├── kawaki_pose_examining_hands.jpg
        │   ├── kawaki_pose_looking_distance.jpg
        │   ├── kawaki_pose_karma_blade.jpg
        │   └── kawaki_pose_karma_shield.jpg
        ├── wardrobe/
        │   ├── standard/
        │   │   ├── kawaki_wardrobe_standard_front.jpg
        │   │   ├── kawaki_wardrobe_standard_side.jpg
        │   │   └── kawaki_wardrobe_standard_back.jpg
        │   ├── karma/
        │   │   ├── kawaki_wardrobe_karma_front.jpg
        │   │   ├── kawaki_wardrobe_karma_side.jpg
        │   │   └── kawaki_wardrobe_karma_back.jpg
        │   └── casual/
        │       ├── kawaki_wardrobe_casual_front.jpg
        │       ├── kawaki_wardrobe_casual_side.jpg
        │       └── kawaki_wardrobe_casual_back.jpg
        └── effects/
            ├── kawaki_expr_karma_seal_stage1.jpg
            ├── kawaki_expr_karma_seal_stage2.jpg
            ├── kawaki_expr_karma_seal_stage3.jpg
            ├── kawaki_expr_karma_eye_glow.jpg
            ├── kawaki_expr_karma_matter_distortion.jpg
            ├── kawaki_expr_karma_energy_blast.jpg
            ├── kawaki_expr_karma_blade_form.jpg
            └── kawaki_expr_karma_shield_form.jpg
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
- **Per Major Arc** (10-15 chapters): Update evolution tracking if needed (Karma progression)
- **Per Season** (25-30 chapters): Add new expressions/poses if character develops new traits
- **As Needed**: Add effect references for new powers/abilities discovered (new Karma techniques, implant-related effects)

This bible ensures that no matter which artist, animator, or AI generator creates content featuring Kawaki, the output will be visually consistent, narratively appropriate, and professionally polished—eliminating the "AI look" through disciplined reference use rather than relying solely on prompt engineering. The structure mirrors the Jinwoo and Boruto bibles for consistency in your pipeline, while being specifically tailored to his unique impaired physiology, Karma seal powers, and serious/detached personality in Boruto: Two Blue Vortex.