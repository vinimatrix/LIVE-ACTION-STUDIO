# Sample Character Bible: Mitsuki (Boruto: Two Blue Vortex)
## Implementing Best Practices for Consistent AI Generation (July 2026)

This document demonstrates how to create a professional character bible for Mitsuki using the best practices outlined in our AI Video Generation Best Practices guide. It serves as a template for all character bibles in the AI Live Action Studio pipeline, specifically adapted for his unique synthetic nature and sage abilities in Boruto: Two Blue Vortex.

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
CHARACTER: Mitsuki
AGE: 16 (at start of Boruto: Two Blue Vortex)
NATIONALITY: Japanese (Synthetic Human - Orochimaru's creation)
HEIGHT: ~172cm
BUILD: Slim, androgynous, deceptively strong (snake-like musculature)
HAIR: Silver-white, medium length, slightly wavy, often partially covering left eye
EYES: Yellow, slit-pupiled (snake-like), often golden hue when using senjutsu
SKIN_TONE: Pale with slight yellowish undertone (reflects snake heritage)
DISTINGUISHING_MARKS: 
  - Snake-like eyes (yellow, slit pupils)
  - Pale skin with faintly scaly texture visible upon close inspection
  - Ability to shed skin (rarely shown, but potential for regeneration)
  - Can extend arms like snakes (elasticity)
PERSONALITY_CORE: 
  - Curious (constantly seeks to understand humanity and emotions)
  - Loyal (to his "parents" - Orochimaru and Log, and friends - Boruto, Sarada)
  - Analytical (approaches everything as an experiment or observation)
  - Calm (rarely shows strong emotion, maintains composure)
  - Adaptable (adjusts behavior based on observations)
  - Ethically ambiguous (may prioritize knowledge over conventional morality)
BACKSTORY_ESSENTIAL: 
  - Artificial human created by Orochimaru using genetic engineering
  - Designed to be the "perfect vessel" for senjutsu (natural energy)
  - Left Orochimaru's care to follow his own path and understand his "will"
  - Joined Boruto and Sarada as teammate in Konoha
  - Constantly experiments to understand human emotions and social bonds
  - Recently discovered connection to Otsutsuki clan through his lineage
NINJA_RANK: Chunin-level (despite young age, due to exceptional abilities)
CHAKRA_NATURE: Wind (primary), Lightning (secondary), Sage Energy (unique)
SPECIAL_ABILITIES: 
  - Sage Mode (Snake Sage): Can harness natural energy for enhanced perception and power
  - Stretchable Limbs: Can elongate arms like snakes for grappling/striking
  - Snake Summoning: Can summon and communicate with snakes
  - Venom Secretion: Can produce various venoms (paralytic, corrosive, etc.)
  - Soft Physique Modification: Can alter body density and flexibility
  - Enhanced Senses: Particularly smell and vibration detection
  - Regeneration: Can heal injuries rapidly (including limb regeneration)
  - Limited Shape-shifting: Minor facial/body changes for disguise
```

## 2. Reference Library

All reference images should be stored in: `references/character/mitsuki/`

### 2.1 Base References (MUST EXIST)
- `mitsuki_base_front.jpg` - Front-facing neutral expression, standard lighting
- `mitsuki_base_3_4_left.jpg` - Left 3/4 angle, neutral expression
- `mitsuki_base_3_4_right.jpg` - Right 3/4 angle, neutral expression
- `mitsuki_base_profile.jpg` - Pure profile, neutral expression (showing snake-like eyes clearly)
- `mitsuki_base_full_body.jpg` - Full body, neutral stance (showing slender build)

### 2.2 Expression References (MUST EXIST)
- `mitsuki_expr_neutral.jpg` - Calm, curious, slightly tilted head
- `mitsuki_expr_determined.jpg` - Jaw set, narrowed eyes, focused intensity
- `mitsuki_expr_angry.jpg` - Rare: Eyebrows furrowed, eyes narrowed, rare show of temper
- `mitsuki_expr_sad.jpg` - Downturned mouth, less energetic posture, withdrawn
- `mitsuki_expr_shocked_surprised.jpg` - Widened eyes (yellow, slit pupils), raised eyebrows, slight head tilt
- `mitsuki_expr_calculating_strategic.jpg` - Half-lidded eyes, assessing gaze, finger to chin, analytical
- `mitsuki_expr_exhausted_injured.jpg` - Heavy breathing, slumped shoulders, possible scale texture visible
- `mitsuki_expr_joyous_smiling.jpg` - Rare: Small genuine smile, eyes crinkled, rare posture relaxation
- `mitsuki_expr_serious_focused.jpg` - Intense stare, minimal expression change, observing posture
- `mitsuki_expr_playful_mischievous.jpg` - Rare: Slight smirk, relaxed posture, head tilt (with close friends)
- `mitsuki_expr_snake_smile.jpg` - Unique: Slightly wider smile showing faint fangs
- `mitsuki_expr_sage_mode_eyes.jpg` - Eyes glowing gold, pupils slightly dilated, intense focus
- `mitsuki_expr_stretch_limb.jpg` - Arm extended unnaturally, focused expression
- `mitsuki_expr_venom_secrete.jpg` - Hand showing droplets of venom, analytical expression
- `mitsuki_expr_regenerating.jpg` - Wound closing rapidly, scales visible, focused observation
- `mitsuki_expr_detached_observing.jpg` - Empty gaze, head tilted, observing like a specimen

### 2.3 Pose References (MUST EXIST)
- `mitsuki_pose_standing_neutral.jpg` - Standing straight, hands loose at sides or slightly forward
- `mitsuki_pose_stance_combat.jpg` - Knees slightly bent, hands ready to strike or extend
- `mitsuki_pose_walking_casual.jpg` - Smooth gliding gait, hands loose, slight sway
- `mitsuki_pose_running_urgent.jpg` - Leaned forward, arms back, legs extending, slight undulation in movement
- `mitsuki_pose_jumping_acrobatic.jpg` - Mid-air, legs bent, possible arm extension, body twisted
- `mitsuki_pose_hand_signs.jpg` - Standard ninja seals (for jutsu that require them)
- `mitsuki_pose_fighting_stance.py` - Low stance, weight balanced, hands ready to strike/extend
- `mitsuki_pose_stretch_arm_left.jpg` - Left arm extended like a snake, palm open or fist
- `mitsuki_pose_stretch_arm_right.jpg` - Right arm extended like a snake, palm open or fist
- `mitsuki_pose_stretch_both_arms.jpg` - Both arms extended, serpentine movement
- `mitsuki_pose_snake_coiled.jpg` - Body coiled like a spring, head elevated, ready to strike
- `mitsuki_pose_snake_strike.jpg` - Lunging forward, neck/arm extended, mouth open (showing fangs)
- `mitsuki_pose_sensing_sage.jpg` - Eyes closed or half-lidded, head tilted, hands relaxed (gathering natural energy)
- `mitsuki_pose_summoning_snake.jpg` - Hand extended forward, palm up, serpentine gesture
- `mitsuki_pose_analyzing.jpg` - Head tilted, hands in observation pose (like examining specimen)
- `mitsuki_pose_meditating.jpg` - Seated lotus, hands on knees, eyes closed (senjutsu practice)
- `mitsuki_pose_shearing_skin.jpg` - Back slightly arched, skin appearing to separate (rare)
- `mitsuki_pose_regenerating_limb.jpg` - Limb in regeneration process, visible cellular activity

### 2.4 Wardrobe References (MUST EXIST)
- `mitsuki_wardrobe_standard_front.jpg` - Standard outfit: white high-collared jacket, dark pants, sandals
- `mitsuki_wardrobe_standard_side.jpg` - Side view showing jacket cut, sleeve design
- `mitsuki_wardrobe_standard_back.jpg` - Back view showing gear layout, possible sheath
- `mitsuki_wardrobe_sage_mode_front.jpg` - Sage mode activation: natural energy aura visible
- `mitsuki_wardrobe_sage_mode_side.jpg` - Side view showing aura flow, posture
- `mitsuki_wardrobe_snake_features.jpg` - Close-up showing scale texture, eye details, fangs
- `mitsuki_wardrobe_experiment_notes.jpg` - Shows notebook/scroll he often carries
- `mitsuki_wardrobe_medical_supplies.jpg` - Small pouch with vials, bandages (for experiments)

### 2.5 Power/Effect References (MUST EXIST FOR CONSIDERATION)
- `mitsuki_expr_sage_mode_aura.jpg` - Golden natural energy aura flowing around body
- `mitsuki_expr_snake_eyes_glow.jpg` - Eyes glowing brighter yellow during focus
- `mitsuki_expr_stretch_limb_left.jpg` - Left arm extended unnaturally, visible tendon-like strands
- `mitsuki_expr_stretch_limb_right.jpg` - Right arm extended unnaturally
- `mitsuki_expr_summoning_snake.jpg` - Snake emerging from sleeve or ground
- `mitsuki_expr_venom_droplet.jpg` - Clear or colored droplet forming at fingertip
- `mitsuki_expr_venom_spray.jpg` - Fine mist of venom exiting mouth or hand
- `mitsuki_expr_skin_shedding.jpg` - Outer layer of skin peeling away (rare)
- `mitsuki_expr_regenerating_limb.jpg` - Limb rebuilding, visible cellular activity
- `mitsuki_expr_sensing_vibration.jpg` - Head tilted, hand on ground sensing vibrations
- `mitsuki_expr_sensing_smell.jpg` - Nostrils flared, inhaling deeply (enhanced smell)
- `mitsuki_expr_snake_coiled_attack.jpg` - Body coiled, ready to strike like a serpent
- `mitsuki_expr_snake_strike_extend.jpg` - Neck/arm fully extended, mouth open (fangs visible)

---

## 3. Voice & Audio Identity

### 3.1 Voice Profile
```
VOICE_ID: "mitsuki_japanese_male_16_synthetic" (Example ID from ElevenLabs or similar)
SERVICE: ElevenLabs (or equivalent high-quality TTS/voice cloning)
PARAMETERS:
  - Stability: 0.7
  - Clarity: 0.9
  - Style Exaggeration: 0.0
  - Speaker Boost: false
  - Model: multilingual_v2
CHARACTERISTICS:
  - Base Pitch: Medium (approx. 135Hz fundamental - slightly androgynous)
  - Tone: Flat, slightly hollow, almost mechanical quality (synthetic nature)
  - Pace: 
    * Normal: Even, measured, slightly slow (observational pace)
    * Excited/Curious: Slightly faster but still measured (when discovering something new)
    * Angry: Rarely raises voice; low, dangerous intensity when provoked
    * Analytical: Very slow, precise, pauses between observations
    * Tired: Even slower, with slight electronic undertone
    * Detached: Monotone, minimal inflection (pure observation mode)
    * Protective: Slightly warmer but still analytical
  - Accent: Standard Tokyo Japanese with slight artificial undertone
  - Unique Traits: 
    * Tendency to speak in observational statements ("Interesting.", "Fascinating.")
    * Rarely uses contractions; speaks in full, precise sentences
    * Voice drops slightly when sharing sensitive information
    * Almost never laughs; when he does, it's soft and brief (like a chuckle)
    * Breathing often very controlled and minimal
    * Speaks with slight urgency when protecting friends
    * May tilt head slightly when speaking (observational habit)
```

### 3.2 Audio References (MUST EXIST)
Store in: `references/voice/mitsuki/`
- `mitsuki_voice_normal.wav` - Normal tone: even, measured, slightly observational
- `mitsuki_voice_determined.wav` - Firmer, focused but still measured
- `mitsuki_voice_angry.wav` - Rare: low, dangerous intensity (when truly provoked)
- `mitsuki_voice_shocked.wav` - Slight intake, eyes widen (yellow, slit pupils)
- `mitsuki_voice_calculating.wav` - Very slow, precise, distinct pauses (analyzing)
- `mitsuki_voice_tired.wav` - Even slower, slight electronic undertone
- `mitsuki_voice_detached.wav` - Monotone, minimal inflection (pure observation)
- `mitsuki_voice_protective.wav` - Slightly warmer but still analytical
- `mitsuki_voice_curious.wav` - Slightly faster, interested tone (discovering something)
- `mitsuki_voice_laugh.wav` - Rare: soft, brief chuckle (only with close friends)
- `mitsuki_voice_whisper.wav` - Near-whisper for sensitive information
- `mitsuki_voice_sage_mode.wav` - Slightly resonant, deeper tone (when using senjutsu)
- `mitsuki_voice_stretch_limb.wav` - Slight effort sound when extending limbs
- `mitsuki_voice_venom_hiss.wav` - Soft hiss when secreting venom

### 3.3 Sound Effect References
- `mitsuki_sfx_stretch_limb.wav` - Soft tearing/stretching sound (like rubber)
- `mitsuki_sfx_snake_slide.wav` - Light sliding sound (movement like a snake)
- `mitsuki_sfx_snake_hiss.wav` - Soft hiss (when agitated or preparing to strike)
- `mitsuki_sfx_sage_mode_activate.wav` - Deep hum + natural energy crackle
- `mitsuki_sfx_summon_snake.wav` - Soft rustling + gentle thud (snake appearing)
- `mitsuki_sfx_venom_drop.wav` - Small liquid droplet sound
- `mitsuki_sfx_venom_spray.wav` - Fine mist spraying sound
- `mitsuki_sfx_skin_shed.wav` - Soft tearing + light dust (skin shedding)
- `mitsuki_sfx_regenerate.wav` - Soft bubbling + tingling (tissue regeneration)
- `mitsuki_sfx_sensing_vibration.wav` - Soft tapping + resonance (ground sensing)
- `mitsuki_sfx_sensing_smell.wav` - Soft inhalation + subtle sniff (enhanced smell)
```

---

## 4. Wardrobe System

### 4.1 Standard Outfit (Primary Attire)
```
STANDARD_OUTFIT:
  - Description: White high-collared jacket, dark pants (his typical attire)
  - Key_Pieces: 
    * White high-collared jacket (reaches mid-cheek, loosely fitted)
    * Dark gray/black pants (straight fit, comfortable for movement)
    * Open-toed sandals (simple straps, allows for toe movement)
    * No visible shirt (jacket covers torso)
    * Small pouch on right thigh (carries scrolls, vials, small tools)
    * Possible bandages on arms/legs (from experiments, usually hidden)
  - Color_Palette: Monochrome white/dark gray with possible accent colors in pouch
  - Reference_Images: mitsuki_wardrobe_standard_front.jpg, mitsuki_wardrobe_standard_side.jpg, mitsuki_wardrobe_standard_back.jpg
  - Usage: Primary outfit for all situations (missions, training, daily life, experiments)
  - Notes: 
    * Jacket often slightly loose to allow for limb extension movements
    * High collar serves to partially conceal neck/jaw (less expressive than human)
    * Pants show minimal wear (durable material, less active taijutsu)
    * Sandals show even wear (smooth, gliding movement pattern)
    * Pouch contents vary: scrolls (observations), vials (samples/venom), small tools
```

### 4.2 Sage Mode Attire (Enhanced State)
```
SAGE_MODE_ATTIRE:
  - Description: Visual indicators when using senjutsu (natural energy)
  - Key_Pieces: 
    * Same base outfit but with visible golden energy aura flowing around body
    * Possible slight levitation (few centimeters off ground)
    * Hair may float slightly upward due to energy
    * Eyes glow brighter yellow with subtle pattern
  - Color_Palette: Same base outfit, plus golden yellow energy aura
  - Reference_Images: mitsuki_wardrobe_sage_mode_front.jpg, mitsuki_wardrobe_sage_mode_side.jpg
  - Usage: When actively sensing or manipulating natural energy
  - Notes: 
    * Aura intensity varies with sage mode level (faint to bright)
    * May see slight distortion in air around him (heat-haze effect)
    * Posture often more upright and balanced when using sage mode
    * Movements become more fluid and precise
    * Jungle green accents may appear in energy (natural energy manifestation)
```

### 4.3 Experimental/Research Gear
```
EXPERIMENTAL_GEAR:
  - NOTEBOOK/SCROLL:
    * Description: Carries for recording observations and experiments
    * Appearance: Small bound notebook or sealed scroll in thigh pouch
    * Reference: Create when showing documentation behavior
    
  - SAMPLE_VIALS:
    * Description: Contains blood, tissue, or chemical samples for analysis
    * Appearance: Small glass or crystal vials with stoppers
    * Reference: Create when conducting experiments
    
  - MEDICAL_SUPPLIES:
    * Description: Bandages, antiseptics, tools for self-experimentation
    * Appearance: Small pouch with various medical items
    * Reference: Create when showing self-modification or healing tests
    
  - SENSE_ENHANCERS:
    * Description: Devices to temporarily enhance specific senses
    * Appearance: Small devices worn on ears, nose, or fingers
    * Reference: Create when testing sensory limits
```

---

## 5. Expression Library

### 5.1 Usage Guidelines
- **ALWAYS** use reference images for expressions when generating
- **MAINTAIN** core facial structure (jawline, nose shape, eye shape - snake-like pupils)
- **RESPECT** distinctive features: yellow slit-pupiled eyes must be consistent
- **ENSURE** emotional range is appropriately limited (he shows little overt emotion)
- **ALLOW** sage mode effects only when narratively justified
- **VERIFY** expressions match his generally curious/analytical demeanor

### 5.2 Expression Details
| Expression | Description | Key Features | Reference Image |
|------------|-------------|--------------|-----------------|
| **NEUTRAL** | Default state: curious, observant | Slight head tilt, relaxed jaw, eyes alert but unfocused, faint smile possible | `mitsuki_expr_neutral.jpg` |
| **DETERMINED** | Resolved to overcome challenge | Jaw set, narrowed eyes, focused intensity, posture forward, minimal excess movement | `mitsuki_expr_determined.jpg` |
| **ANGRY** | Rare frustration or protection violation | Eyebrows slightly furrowed, eyes narrowed, rare tension in jaw, dangerous calm | `mitsuki_expr_angry.jpg` |
| **SAD** | Disappointment or loss of subject | Downturned mouth corners, less energetic posture, withdrawn gaze, head down | `mitsuki_expr_sad.jpg` |
| **SHOCKED/SURPRISED** | Sudden surprise or discovery | Eyes widened (yellow, slit pupils), eyebrows raised, slight head tilt, intake | `mitsuki_expr_shocked_surprised.jpg` |
| **CALCULATING/STRATEGIC** | Assessing situation/threat | Half-lidded eyes, assessing gaze, finger to chin, analytical posture, minimal movement | `mitsuki_expr_calculating_strategic.jpg` |
| **EXHAUSTED/INJURED** | Extreme fatigue or injury | Heavy breathing, slumped shoulders, possible scale texture visible, less focus | `mitsuki_expr_exhausted_injured.jpg` |
| **JOYOUS/SMILING** | Rare genuine pleasure (with friends) | Small genuine smile, eyes crinkled, rare posture relaxation, head tilt | `mitsuki_expr_joyous_smiling.jpg` |
| **SERIOUS/FOCUSED** | Intense observation or analysis | Intense stare, minimal expression change, observing posture, head often tilted | `mitsuki_expr_serious_focused.jpg` |
| **PLAYFUL/MISCHIEVOUS** | Rare lightheartedness (with close friends) | Slight smirk, relaxed posture, head tilt, occasional playful gesture | `mitsuki_expr_playful_mischievous.jpg` |
| **SNAKE_SMILE** | Unique slightly wider smile | Smile showing faint suggestion of fangs, eyes crinkled, analytical curiosity | `mitsuki_expr_snake_smile.jpg` |
| **SAGE_MODE_EYES** | Activated senjutsu perception | Eyes glowing gold, pupils slightly dilated, intense focus, natural energy sensing | `mitsuki_expr_sage_mode_eyes.jpg` |
| **STRETCH_LIMB** | Limb extension ability | Arm extended unnaturally like a snake, visible tendon-like strands, focused expression | `mitsuki_expr_stretch_limb.jpg` |
| **VENOM_SECRETE** | Producing venom | Hand showing droplets or mist of venom, analytical expression, ready for use | `mitsuki_expr_venom_secrete.jpg` |
| **REGENERATING** | Healing injury rapidly | Wound closing visibly, cellular activity visible, focused observation | `mitsuki_expr_regenerating.jpg` |
| **DETACHED_OBSERVING** | Pure observation mode | Empty gaze, head tilted, observing like a specimen, minimal blinking, monotone | `mitsuki_expr_detached_observing.jpg` |
| **SENSING_VIBRATION** | Detecting ground vibrations | Hand on ground or foot planted, head tilted slightly, focused expression | `mitsuki_expr_sensing_vibration.jpg` |
| **SENSING_SMELL** | Enhancing olfactory sense | Nostrils flared, inhaling deeply, eyes slightly closed in concentration | `mitsuki_expr_sensing_smell.jpg` |
| **SNAKE_COILED** | Ready to strike like serpent | Body coiled like spring, head elevated, eyes focused, coiled tension visible | `mitsuki_expr_snake_coiled.jpg` |
| **SNAKE_STRIKE** | Lunging forward to strike | Neck/arm fully extended, mouth open (fangs visible), target-focused | `mitsuki_expr_snake_strike.jpg` |
| **SUMMONING_SNAKE** | Calling serpent companion | Hand extended forward, palm up, serpentine gesture, expecting arrival | `mitsuki_expr_summoning_snake.jpg` |

---

## 6. Pose Library

### 6.1 Usage Guidelines
- **ALWAYS** use pose references when character positioning is specified
- **MAINTAIN** anatomical accuracy and natural weight distribution (with snake-like flexibility)
- **RESPECT** distinctive features: yellow slit-pupiled eyes must be consistent
- **ENSURE** clothing follows body contours realistically during movement (accounting for stretch)
- **ALLOW** variations for action but keep core pose recognizable
- **ACCURATELY** depict limb extension, sage mode aura, and special abilities when specified
- **NOTE** his distinctive smooth, gliding movement pattern (less bipedal, more serpentine)

### 6.2 Pose Details
| Pose | Description | Key Features | Reference Image |
|------|-------------|--------------|-----------------|
| **STANDING_NEUTRAL** | Default standing position | Feet shoulder-width apart, weight evenly distributed, hands loose at sides, slight head tilt | `mitsuki_pose_standing_neutral.jpg` |
| **STANCE_COMBAT_READY** | Prepared for strike/defense | Knees slightly bent, weight balanced, hands ready to strike or extend, alert posture | `mitsuki_pose_stance_combat.jpg` |
| **WALKING_CASUAL** | Natural walking pace | Smooth gliding gait, minimal vertical movement, hands loose, slight sway in hips | `mitsuki_pose_walking_casual.jpg` |
| **RUNNING_URGENT** | High-speed movement | Leaned forward, arms back slightly, legs extending, undulation in torso movement | `mitsuki_pose_running_urgent.jpg` |
| **JUMPING/ACROBATIC** | Mid-air maneuver | Legs bent for propulsion/landing, possible arm extension, body twisted for direction | `mitsuki_pose_jumping_acrobatic.jpg` |
| **FOLLOWING_SNAKE** | Snake-like locomotion | Body moving in undulating wave, limbs coordinating with motion, head leading | *Context-dependent* |
| **HAND_SIGNS** | Standard ninja seals | Fingers positioned precisely for required seal, focused expression, minimal excess movement | `mitsuki_pose_hand_signs.jpg` |
| **FIGHTING_STANCE** | Defensive/ offensive ready | Low stance (~30° knee bend), weight balanced, hands ready to strike/extend, observing | `mitsuki_pose_fighting_stance.jpg` |
| **STRETCH_ARM_LEFT** | Left arm extension | Left arm extended unnaturally like snake, palm open or fist, focused expression | `mitsuki_pose_stretch_arm_left.jpg` |
| **STRETCH_ARM_RIGHT** | Right arm extension | Right arm extended unnaturally like snake, palm open or fist, focused expression | `mitsuki_pose_stretch_arm_right.jpg` |
| **STRETCH_BOTH_ARMS** | Both arms extension | Both arms extended symmetrically, serpentine movement, focused expression | `mitsuki_pose_stretch_both_arms.jpg` |
| **STRETCH_NECK_HEAD** | Neck/head extension | Head extended forward on elongated neck, eyes focused, minimal jaw movement | *Context-dependent* |
| **SNAKE_COILED** | Defensive/ready to strike | Body coiled like spring, weight on balls of feet, head elevated, ready to launch | `mitsuki_pose_snake_coiled.jpg` |
| **SNAKE_STRIKE** | Lunging forward strike | Body uncoiling rapidly, neck/arm extending, mouth open (fangs visible), target focus | `mitsuki_pose_snake_strike.jpg` |
| **SAGE_MODE_SENSING** | Gathering natural energy | Eyes closed or half-lidded, head tilted, hands relaxed at sides, peaceful expression | `mitsuki_pose_sensing_sage.jpg` |
| **SAGE_MODE_ACTIVE** | Using senjutsu abilities | Eyes glowing gold, slight levitation, energy aura visible, balanced posture | *Context-dependent* |
| **SUMMONING_SNAKE** | Calling serpent companion | Hand extended forward, palm up, slight gesture, expecting arrival, attentive posture | `mitsuki_pose_summoning_snake.jpg` |
| **VENOM_APPLICATION** | Applying venom to target | Hand near target, droplets/mist visible, focused expression, ready for effect | *Context-dependent* |
| **REGENERATING_LIMB** | Healing limb rapidly | Limb in regeneration process, visible cellular activity, focused observation | `mitsuki_pose_regenerating_limb.jpg` |
| **SENSING_VIBRATION** | Detecting ground tremors | Hand or foot on ground, slight lean forward, head tilted, focused expression | `mitsuki_pose_sensing_vibration.jpg` |
| **SENSING_SMELL** | Enhancing smell detection | Nostrils flared, inhaling deeply, eyes slightly closed in concentration, still posture | `mitsuki_pose_sensing_smell.jpg` |
| **ANALYZING_SPECIMEN** | Examining object/subject | Head tilted, hands in observation pose (like holding specimen), intense focus | `mitsuki_pose_analyzing.jpg` |
| **MEDITATING** | Senjutsu practice/training | Seated lotus, hands on knees, eyes closed, peaceful expression, upright posture | `mitsuki_pose_meditating.jpg` |
| **SHEARING_SKIN** | Rare skin shedding | Back slightly arched, skin appearing to separate at edges, focused observation | *Context-dependent* |
| **ACROBATIC_FLIP** | Complex aerial maneuver | Body rotating in air, limbs coordinating, landing preparation visible | *Context-dependent* |
| **DEFLECTING_PROJECTILE** | Blocking with extended limb | Arm extended to intercept, hand open or shaped, focused expression, ready to counter | *Context-dependent* |

---

## 7. Evolution Tracking

Track physical/visual changes that occur naturally through story progression:

### 7.1 Early Two Blue Vortex (Chapters 1-10) - "Observing the New Threat"
- **Physique**: Slim, androgynous build, less defined musculature
- **Eyes**: 
  - Consistently yellow, slit-pupiled
  - Slightly more expressive than usual (adjusting to new stimuli)
  - Sage mode activation rare and unstable
- **Hair**: Silver-white, medium length, slightly wavy (may be messier from travel)
- **Expression Frequency**: 
  - High: Curious, neutral, observing
  - Medium: Detached, calculating
  - Low: Shocked, sad, determined
  - Very Rare: Joyous, playful, angry
- **Wardrobe**: 
  - Primary: Standard outfit (may be slightly worn from travel)
  - Secondary: No sage mode use visible yet
  - Special: Minimal experimental gear (basic notebook only)
- **Power Manifestation**: 
  - Sage Mode: Rare, brief activation, weak aura
  - Stretch Limb: Short extension, limited control
  - Venom: Basic types, limited control
  - Regeneration: Slow, visible scarring
  - Sensing: Basic vibration/smell enhancement

### 7.2 Mid Two Blue Vortex (Chapters 11-30) - "Understanding the Bonds"
- **Physique**: Developing musculature from training and combat
- **Eyes**: 
  - Consistently yellow, slit-pupiled
  - More controlled expressions (less reactive)
  - Sage mode activation more frequent and stable
- **Hair**: Maintains style but appears healthier/shinier from better diet/nutrition
- **Expression Frequency**: 
  - High: Curious, calculating, observing
  - Medium: Determined, serious/focused
  - Low: Shocked, sad
  - Very Rare: Joyous, playful (only with Boruto/Sarada in safe moments)
  - Occasional: Detached (when overwhelmed by emotions)
- **Wardrobe**: 
  - Primary: Standard outfit (well-fitted, shows minor wear)
  - Secondary: Sage mode visible during training/experiments
  - Special: Expanded experimental gear (various vials, tools, notes)
- **Power Manifestation**: 
  - Sage Mode: More stable, longer duration, visible golden aura
  - Stretch Limb: Greater extension, better control (up to 3x normal length)
  - Venom: Variety of types (paralytic, corrosive, etc.), better aim
  - Regeneration: Faster, cleaner healing, less scarring
  - Sensing: Enhanced range and precision (vibration, smell, etc.)
  - Summoning: Able to call specific snake types for specific tasks

### 7.3 Late Two Blue Vortex (Chapters 31-50+) - "Mastering the Balance"
- **Physique**: Lean but defined musculature from training and experimentation
- **Eyes**: 
  - Consistently yellow, slit-pupiled
  - Highly controlled expressions (minimal wasted expression)
  - Sage mode activation very stable and controllable
- **Hair**: Maintains style but may show slight movement in stillness (subtle energy)
- **Expression Frequency**: 
  - High: Calculating, serious/focused, observing
  - Medium: Curious, determined
  - Low: Shocked, sad
  - Very Rare: Joyous, playful (only in completely safe moments with close friends)
  - Occasional: Detached (when analyzing dangerous situations objectively)
- **Wardrobe**: 
  - Primary: Standard outfit (well-maintained, shows experimental modifications)
  - Secondary: Sage mode frequent and stable during use
  - Special: Comprehensive experimental gear (advanced tools, samples, notes)
- **Power Manifestation**: 
  - Sage Mode: Near-constant low-level activation, high-level when needed
  - Stretch Limb: Great extension and control (up to 5x normal length), precise
  - Venom: Sophisticated mixtures, precise application, controlled effects
  - Regeneration: Rapid, nearly scar-free, can regenerate complex tissues
  - Sensing: Exceptional range and precision (detecting lies, emotions, etc.)
  - Summoning: Able to summon specialized snakes for combat, scouting, etc.
  - Special: Beginning to show limited shape-shifting for disguise

### 7.2 Special State Markers
```
SAGE_MODE_ACTIVATION_LEVEL_1:
  - Description: Low-level natural energy sensing
  - Visual: 
    * Eyes: Slight golden glow in irises
    * Aura: Faint golden outline (5-10% opacity) around body
    * Effect: Enhanced perception of energy flows, life forces
  - Duration: Seconds to minutes (passive sensing)
  - Reference: mitsuki_expr_sage_mode_eyes.jpg

SAGE_MODE_ACTIVATION_LEVEL_2:
  - Description: Active sage mode usage
  - Visual: 
    * Eyes: Clearly glowing gold, pupils slightly dilated
    * Aura: Visible golden energy flowing (15-25% opacity)
    * Effect: Enhanced strength, speed, perception, energy sensing
  - Duration: Minutes during active use
  - Reference: Create when showing active sage mode

SAGE_MODE_PERFECT:
  - Description: Perfect sage mode balance
  - Visual: 
    * Eyes: Intense gold glow, distinct pattern in pupil
    * Aura: Strong, steady golden flow (25-35% opacity)
    * Effect: Peak physical and sensory enhancement
  - Duration: Extended periods (requires significant focus)
  - Reference: Create when showing peak sage mode

STRETCH_LIMB_LEVEL_1:
  - Description: Minor limb extension
  - Visual: 
    * Limb: Extended 1-2x normal length
    * Effect: Visible tendon-like strands, slight skin stretching
  - Duration: During use
  - Reference: mitsuki_expr_stretch_limb_left.jpg

STRETCH_LIMB_LEVEL_2:
  - Description: Significant limb extension
  - Visual: 
    * Limb: Extended 3-5x normal length
    * Effect: Clear tendon-like structures, skin stretching visible
  - Duration: During use
  - Reference: Create when showing significant extension

VENOM_VARIETY:
  - Description: Different venom types and applications
  - Visual: 
    * Paralytic: Clear or slightly blue viscous fluid
    * Corrosive: Greenish or yellowish, smoking slightly
    * Hemotoxic: Reddish, causes localized swelling
    * Neurotoxic: Purplish, causes numbness/tingling
  - Duration: From secretion to effect
  - Reference: Create when showing specific venom types

REGENERATION_STAGE_1:
  - Description: Initial wound response
  - Visual: 
    * Wound: Bleeding slowed, edges beginning to close
    * Effect: Visible cellular activity at wound edges
  - Duration: First minutes after injury
  - Reference: Create when showing early healing

REGENERATION_STAGE_2:
  - Description: Active tissue rebuilding
  - Visual: 
    * Wound: Nearly closed, visible cellular matrix forming
    * Effect: Active cell migration and proliferation
  - Duration: Middle phase of healing
  - Reference: Create when showing active regeneration

REGENERATION_STAGE_3:
  - Description: Near-complete healing
  - Visual: 
    * Wound: Nearly invisible seam, slight texture difference
    * Effect: Final tissue remodeling and strengthening
  - Duration: Final healing phase
  - Reference: Create when showing near-complete healing

DETECTING_LIE:
  - Description: Using enhanced senses to detect deception
  - Visual: 
    * Eyes: Narrowed in focus
    * Nostrils: Slightly flared (scent detection)
    * Head: Tilted slightly (processing auditory/visual cues)
    * Posture: Slightly forward lean (intense concentration)
  - Duration: During active assessment
  - Reference: Create when showing lie detection

ANALYZING_EMOTION:
  - Description: Observing and interpreting human emotions
  - Visual: 
    * Head: Tilted, observing subject
    * Hands: Often in observation position (like holding specimen)
    * Expression: Intense focus, minimal movement
    * Posture: Slight forward lean (engaged observation)
  - Duration: During active analysis
  - Reference: Create when showing emotion analysis
```

---

## 8. Consistency Rules & "Don'ts"

### 8.1 Absolute Requirements (Must Always Follow)
```
1. FACE_STRUCTURE: Jawline, nose bridge, eye shape (yellow, slit-pupiled), ear placement must remain consistent
2. EYE_APPEARANCE: Eyes must remain yellow with slit pupils - never round or normal pupils unless showing sage mode glow
3. HAIR_COLOR: Must remain silver-white - never darken or change color without story reason
4. HEIGHT_PROPORTIONS: Head-to-body ratio must remain ~1:7.0 (slightly slender build)
5. SKIN_TONE_CONSISTENCY: Base undertone (pale with yellowish) must remain - no sudden flush or pallor without reason
6. BODY_STRUCTURE: Must retain slim, androgynous frame - never become overly muscular or bulky without story reason
7. MOVEMENT_PATTERN: Must retain smooth, gliding quality (less bipedal, more serpentine) - never stiff or robotic
```

### 8.2 Expression-Specific Rules
```
1. NEUTRAL: Expression shows mild curiosity - head tilt possible, eyes alert but unfocused
2. DETERMINED: Jaw tension visible but never to point of teeth clenching (unless extreme effort)
3. ANGRY: Extremely rare - only when protecting friends or violating core principles; never loud or explosive
4. SAD: Eyes never fully closed - always showing some level of engagement/world awareness
5. SHOCKED/SURPRISED: Eyebrows rise together, never one higher than the other (unless specific head tilt)
6. CALCULATING/STRATEGIC: One hand typically near face/chin, other relaxed at side or on hip
7. EXHAUSTED/INJURED: Shoulder slump visible but never to point of collapsing posture (unless unconscious)
8. JOYOUS/SMILING: Eyes crinkle but never completely closed - rare occurrence, small genuine smile
9. SERIOUS/FOCUSED: Minimal change from neutral but eyes intensely focused; no furrowed brow unless assessing threat
10. PLAYFUL/MISCHIEVOUS: Extremely rare - only with close bonds, expression shows rare relaxation and humor
11. SNAKE_SMILE: Slightly wider smile showing faint fang suggestion - never full snarl or threat display
12. SAGE_MODE_EYES: Eyes must show gold glow when active - never normal eyes when sage mode supposed active
13. STRETCH_LIMB: Limb extension must follow serpentine motion - never rigid or jointed like machinery
14. VENOM_SECRETE: Must show appropriate viscosity and color for venom type (clear, green, red, purple, etc.)
15. REGENERATING: Must show visible cellular activity - never instant healing without process
16. DETECTING_LIE: Must show appropriate sensory engagement (nostrils flared, head tilted, etc.)
17. ANALYZING_EMOTION: Must show observational posture (head tilted, hands in observation pose)
```

### 8.3 Pose-Specific Rules
```
1. STANDING: Weight distribution always physically plausible - never impossible balances
2. WALKING: Movement must show smooth gliding quality - never stiff, jerky, or robotic walking
3. RUNNING: Must show forward lean and arm/leg coordination - never rigid or mechanical
4. JUMPING: Limb positions follow biomechanics for propulsion/landing; hair follows motion
5. FOLLOWING_SNAKE: Body movement must show undulating wave - never segmented or jointed
6. HAND SIGNS: Finger positions must be anatomically possible and match specified seal references
7. FIGHTING STANCE: Weight distribution must be balanced for quick movement in any direction
8. STRETCH_LIMB: Limb extension must follow anatomical plausibility - no impossible stretching without visual indication
9. SNAKE_COILED/STRIKE: Must show proper coiling/uncoiling mechanics - never rigid or jerky motion
10. SAGE_MODE: When active, must show appropriate energy aura and physiological changes
11. VENOM_SECRETE: When visible, must show correct emission point and substance properties
12. REGENERATING: When visible, must show logical healing progression - never skip stages
13. SENSE_ENHANCEMENT: When visible, must show appropriate physiological response (nostrils, pupils, etc.)
14. IMPLANTS/MODIFICATIONS: When visible, must match stated capabilities and limitations
```

### 8.4 Wardrobe Rules
```
1. FIT: Clothing must follow body contours realistically - no "paint-on" effects
2. WRINKLES: Fabric wrinkles follow gravity and movement patterns - never random placement
3. LAYERING: Visible layers (undershirts, wraps, etc.) must be logically consistent with stated outfit
4. ACCESSORIES: 
   * High collar jacket: Must cover lower face partially consistently
   * Pouch: Must be positioned on thigh consistently
   * Sandals: Straps secure, wear patterns consistent
   * Experimental gear: Must be logically placed and functionally consistent
5. WEAR_AND_TEAR: Damage accumulates logically - new tears appear in stress areas, not randomly
6. SAGE_MODE AURA: When visible, must follow body contours and show proper energy flow
7. SPECIAL FEATURES: When visible (scales, fangs, etc.), must be anatomically correct and consistent
```

### 8.5 Absolute "Don'ts" (Never Violate)
```
DON'T:
  - Change ear shape/size/position
  - Alter fundamental nose bridge structure
  - Give him normal/pupiled eyes (they are permanently yellow/slit-pupiled due to snake heritage)
  - Change ethnicity appearance (must remain clearly Japanese East Asian)
  - Make him significantly taller/shorter than established ~172cm
  - Give him excessive musculature (he remains slim and androgynous)
  - Make his movement stiff or robotic (he moves with smooth, gliding, serpentine quality)
  - Make his eyes round or normal-pupiled (exception: sage mode gold glow)
  - Make his hair dark or change color without story reason
  - Make his skin flush or pale without story reason (except for temporary exertion)
  - Make his expressions overly expressive (he is fundamentally observational and calm)
  - Make his movements jerky or unnatural (he flows like water or a snake)
  - Make his clothing overly tight or restrictive (he needs freedom for limb extension)
  - Make his expressions inconsistent with his observational nature (no exaggerated cartoon expressions)
  - Make his sage mode aura wrong color (must be gold/yellow, not blue/red/etc.)
  - Make his limb extensions rigid or jointed (they should flow like snake movement)
  - Make his venom the wrong color or consistency for the stated type
  - Make his regeneration instantaneous without visible process
  - Make his sensory enhancements incorrect (wrong nostrils, pupils, etc.)
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
  Model: Wan 2.7 (best for facial/hair/detail - critical for snake eyes, expressions, subtle features)
  Notes: Use extra attention to eye/pupil detail, jaw tension, hair texture, skin texture

MEDIUM_SHOTS / DIALOGUE_SCENES:
  Model: Kling 3.0 (best for lip-sync and natural movement - essential for his sparse but meaningful dialogue)
  Notes: Enable lip-sync tracking; ensure sparse dialogue matches his speech patterns

WIDE_SHOTS / ESTABLISHING:
  Model: Veo 3.1 (best for environmental consistency and depth - crucial for showing his presence in scenes)
  Notes: Ensure background elements match reference; verify environmental effects (dust, particles, etc.)

ACTION_SEQUENCES / COMPLEX_MOTION / COMBAT:
  Model: Seedance 2.0 (multi-reference capable - ideal for his distinctive movement patterns with multiple anchors)
  Notes: 
    * Provide key pose references for standing, walking, stretching, striking poses
    * Verify motion blur appropriateness for his smooth, gliding movement
    * Check that his distinctive gait is preserved (less bipedal, more serpentine)
    * Verify limb extensions follow anatomical plausibility

EFFECTS_ONLY / MAGIC_ELEMENTS / SAGE_ABILITIES:
  Model: Appropriate specialized model or base SDXL with ControlNet
  Notes: 
    * Generate on transparent background for compositing
    * Pay special attention to sage mode energy colors (gold/yellow, not blue/red/etc.)
    * Ensure his snake-like eyes remain yellow/slit-pupiled unless showing sage mode glow
    * Verify limb extensions follow biological plausibility
    * Verify emissions (venom, energy, etc.) follow physical laws
    * Verify regeneration shows logical healing progression
    * Verify sensory enhancements show correct physiological responses
```

### 9.3 Reference Anchoring Requirements
```
MINIMUM_REFERENCES_PER_PROMPT:
  - Character close-ups: 1 pose reference + 1 expression reference
  - Character medium/wide shots: 1 full-body reference OR 2 pose references (one for stance, one for action)
  - Establishing environment shots: 1 environment reference
  - Sage mode/effect shots: 1 effect reference + 1 character/environment reference for interaction
  - Dialogue shots: Voice reference MUST be provided to audio generation
  - Limb extension shots: Expression reference + pose reference showing extension
  - Venom secretion shots: Expression reference + close-up showing emission/substance
  - Regeneration shots: Expression reference + close-up showing healing process
  - Sensory enhancement shots: Expression reference + close-up showing activated sense
  - Eye state shots: Expression reference + close-up showing pupil/iris state
  - Movement pattern shots: Pose reference showing gait/posture + expression reference
```

---

## 10. Usage Guidelines

### 10.1 For Prompt Engineers
```
1. BEFORE writing prompt:
   - Consult this bible for exact description
   - Verify required references exist in library
   - Check current story point for appropriate wardrobe/evolution stage
   - Note any active sage mode states or special abilities requiring effect references
   - Verify distinctive features: snake eyes (yellow/slit), silver-white hair, slim build, smooth movement
   - Check for visible special abilities if relevant (stretching, venom, regeneration, etc.)

2. WHEN writing prompt:
   - Use EXACT phrasing from "Character Core Profile" for base description
   - Insert @reference: tags for all required visual elements (pose, expression, wardrobe, effects)
   - Specify technical specs based on shot type (Wan 2.7 for close-ups, etc.)
   - Include voice reference for any dialogue
   - Add evolution notes if applicable to current chapter/scene
   - Always include distinctive features in description (snake eyes, silver-white hair, etc.)
   - Include special ability details when relevant (sage mode level, extension length, etc.)

3. AFTER generation:
   - Verify against this bible during QA
   - Check reference usage in metadata
   - Confirm voice matches specified ID/parameters
   - Validate distinctive features are present and correct:
      * Eyes: yellow, slit-pupiled (exception: sage mode gold glow)
      * Hair: silver-white, medium length, slightly wavy
      * Build: slim, androgynous, deceptively strong
      * Movement: smooth, gliding quality (less bipedal, more serpentine)
      * Skin: pale with yellowish undertone
      * Special abilities: visible when active (stretching, venom, regeneration, etc.)
      * Sage mode: gold/yellow aura when active, correct intensity
```

### 10.2 For Artists/Editors
```
1. REFERENCE USE:
   - Treat references as absolute truth for character appearance
   - Never "improve" upon reference - match it exactly
   - Use references for color picking (especially eye color, hair color, skin tone, energy auras)
   - Use references for texture matching (skin, hair, clothing, scale texture)
   - Use references for proportion checking (especially height, build, limb proportions)
   - Use references for movement analysis (gait, posture, extension patterns)

2. COMPOSITING:
   - Match lighting direction and intensity to environment references
   - Ensure shadow direction consistent across all elements
   - Maintain depth of field as specified in lens specs
   - Verify snake eyes show yellow with slit pupils (unless sage mode gold glow)
   - Confirm hair shows silver-white color with slight wave
   - Validate movement follows smooth, gliding pattern (less bipedal, more serpentine)
   - Check that special effects (sage aura, extensions, emissions) follow physical laws
   - Verify skin tone maintains pale/yellowish undertone
   - Ensure clothing follows body contours realistically

3. COLOR GRADING:
   - Use specified LUTs from style constants
   - Match skin tones to reference under same lighting (pale with yellowish)
   - Preserve hair highlights/shadows as seen in references
   - Ensure special effects match reference colors exactly (no hue shifting for sage mode: gold/yellow)
   - Verify scar tissue colors remain consistent (if any)
   - Ensure clothing colors match references (white jacket, dark pants)
```

### 10.3 For Quality Assurance
```
CHECKLIST PER ASSET:
  [ ] Character facial structure matches reference library (jawline, nose, eyes, ears)
  [ ] Eyes: yellow, slit-pupiled (exception: sage mode gold glow)
  [ ] Hair: silver-white, medium length, slightly wavy
  [ ] Build: slim, androgynous, deceptively strong (not bulky)
  [ ] Movement: smooth, gliding quality (less bipedal, more serpentine in stills)
  [ ] Skin: pale with yellowish undertone
  [ ] Expression matches specified reference
  [ ] Pose matches specified reference (if applicable)
  [ ] Wardrobe matches current story chapter
  [ ] Evolution stage matches narrative point (sage mode level, special abilities)
  [ ] Technical specs (resolution, fps, etc.) correct
  [ ] References properly cited in prompt metadata
  [ ] Voice matches specified ID/parameters (audio)
  [ ] No "don't" violations present
  [ ] Distinctive features correct:
      * Eyes: yellow, slit-pupiled (exception: sage mode gold glow)
      * Hair: silver-white, medium length, slightly wavy
      * Build: slim, androgynous, deceptively strong
      * Movement: smooth, gliding quality (less bipedal, more serpentine)
      * Skin: pale with yellowish undertone
      * Special abilities: visible when active (stretching, venom, regeneration, etc.)
      * Sage mode: gold/yellow aura when active, correct intensity and flow
      * Clothing: white jacket, dark pants, sandals, thigh pouch
      * Experimental gear: present when relevant (notebook, vials, tools)
  [ ] Overall consistency with established canon
```

---

## Appendix: Reference Library Directory Structure
```
references/
└── character/
    └── mitsuki/
        ├── base/
        │   ├── mitsuki_base_front.jpg
        │   ├── mitsuki_base_3_4_left.jpg
        │   ├── mitsuki_base_3_4_right.jpg
        │   ├── mitsuki_base_profile.jpg
        │   └── mitsuki_base_full_body.jpg
        ├── expressions/
        │   ├── mitsuki_expr_neutral.jpg
        │   ├── mitsuki_expr_determined.jpg
        │   ├── mitsuki_expr_angry.jpg
        │   ├── mitsuki_expr_sad.jpg
        │   ├── mitsuki_expr_shocked_surprised.jpg
        │   ├── mitsuki_expr_calculating_strategic.py
        │   ├── mitsuki_expr_exhausted_injured.jpg
        │   ├── mitsuki_expr_joyous_smiling.jpg
        │   ├── mitsuki_expr_serious_focused.jpg
        │   ├── mitsuki_expr_playful_mischievous.jpg
        │   ├── mitsuki_expr_snake_smile.jpg
        │   ├── mitsuki_expr_sage_mode_eyes.jpg
        │   ├── mitsuki_expr_stretch_limb.jpg
        │   ├── mitsuki_expr_venom_secrete.jpg
        │   ├── mitsuki_expr_regenerating.jpg
        │   ├── mitsuki_expr_detached_observing.jpg
        │   ├── mitsuki_expr_sensing_vibration.jpg
        │   ├── mitsuki_expr_sensing_smell.jpg
        │   └── mitsuki_expr_snake_coiled.jpg
        ├── poses/
        │   ├── mitsuki_pose_standing_neutral.jpg
        │   ├── mitsuki_pose_stance_combat.jpg
        │   ├── mitsuki_pose_walking_casual.py
        │   ├── mitsuki_pose_running_urgent.jpg
        │   ├── mitsuki_pose_jumping_acrobatic.jpg
        │   ├── mitsuki_pose_fighting_stance.jpg
        │   ├── mitsuki_pose_stretch_arm_left.jpg
        │   ├── mitsuki_pose_stretch_arm_right.jpg
        │   ├── mitsuki_pose_stretch_both_arms.jpg
        │   ├── mitsuki_pose_snake_coiled.jpg
        │   ├── mitsuki_pose_snake_strike.jpg
        │   ├── mitsuki_pose_sensing_sage.jpg
        │   ├── mitsuki_pose_summoning_snake.jpg
        │   ├── mitsuki_pose_venom_application.jpg
        │   ├── mitsuki_pose_regenerating_limb.jpg
        │   ├── mitsuki_pose_sensing_vibration.jpg
        │   ├── mitsuki_pose_sensing_smell.jpg
        │   ├── mitsuki_pose_analyzing.jpg
        │   ├── mitsuki_pose_meditating.py
        │   └── mitsuki_pose_shearing_skin.jpg
        ├── wardrobe/
        │   ├── standard/
        │   │   ├── mitsuki_wardrobe_standard_front.jpg
        │   │   ├── mitsuki_wardrobe_standard_side.jpg
        │   │   └── mitsuki_wardrobe_standard_back.jpg
        │   ├── sage_mode/
        │   │   ├── mitsuki_wardrobe_sage_mode_front.jpg
        │   │   └── mitsuki_wardrobe_sage_mode_side.jpg
        │   └── features/
        │       ├── mitsuki_wardrobe_snake_features.jpg
        │       └── mitsuki_wardrobe_experiment_notes.jpg
        └── effects/
            ├── mitsuki_expr_sage_mode_aura.jpg
            ├── mitsuki_expr_snake_eyes_glow.jpg
            ├── mitsuki_expr_stretch_limb_left.jpg
            ├── mitsuki_expr_stretch_limb_right.jpg
            ├── mitsuki_expr_summoning_snake.jpg
            ├── mitsuki_expr_venom_droplet.jpg
            ├── mitsuki_expr_venom_spray.jpg
            ├── mitsuki_expr_skin_shedding.jpg
            ├── mitsuki_expr_regenerating_limb.jpg
            ├── mitsuki_expr_sensing_vibration.jpg
            ├── mitsuki_expr_sensing_smell.jpg
            └── mitsuki_expr_snake_strike.jpg
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
- **Per Major Arc** (10-15 chapters): Update evolution tracking if needed (sage mode development, ability refinement)
- **Per Season** (25-30 chapters): Add new expressions/poses if character develops new traits
- **As Needed**: Add effect references for new powers/abilities discovered (new venom types, advanced sage abilities, etc.)

This bible ensures that no matter which artist, animator, or AI generator creates content featuring Mitsuki, the output will be visually consistent, narratively appropriate, and professionally polished—eliminating the "AI look" through disciplined reference use rather than relying solely on prompt engineering. The structure mirrors the Jinwoo, Boruto, and Kawaki bibles for consistency in your pipeline, while being specifically tailored to his unique synthetic physiology, sage abilities, and curious/analytical personality in Boruto: Two Blue Vortex.