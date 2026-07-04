# Enhanced Prompt Templates for AI Live Action Studio
## Integrating Current Best Practices for Consistent Video Generation (July 2026)

This document provides enhanced versions of the Solo Leveling and Boruto: Two Blue Vortex prompt templates that incorporate current industry best practices for AI video generation. These enhancements focus on achieving professional-level consistency through reference anchoring, seed control, model specialization, and technical precision.

## Table of Contents
1. [Enhanced Prompt Structure](#1-enhanced-prompt-structure)
2. [Solo Leveling Enhancements](#2-solo-leveling-enhancements)
3. [Boruto: Two Blue Vortex Enhancements](#3-boruto-two-blue-vortex-enhancements)
4. [Implementation Guide](#4-implementation-guide)
5. [Quality Assurance Integration](#5-quality-assurance-integration)

---

## 1. Enhanced Prompt Structure

The enhanced prompt structure builds upon the existing base format while integrating critical consistency mechanisms:

```
[ENHANCED_SUBJECT_DESCRIPTION], [REFERENCE_ANCHORS], [TECHNICAL_SPECS], [STYLE_MODIFIERS], [QUALITY_BOOSTERS]
```

### Key Enhancements:
- **ENHANCED_SUBJECT_DESCRIPTION**: More detailed, includes pose/expression references
- **REFERENCE_ANCHORS**: Explicit character/environment pose references using `@reference:`
- **TECHNICAL_SPECS**: Model, seed, steps, resolution, fps specifications
- **STYLE_MODIFIERS**: Unchanged from original (maintains series identity)
- **QUALITY_BOOSTERS**: Unchanged from original (maintains quality standards)

---

## 2. Solo Leveling Enhancements

### 2.1 Enhanced Character Prompt Template
```
[Character Name], [age] year old [nationality] [build] character, [hair description], [eye description], 
[wearing: [specific outfit]], [expression: [specific expression] @reference:character-[name]_[expression].jpg], 
[pose: [specific pose] @reference:character-[name]_[pose].jpg], 
[location context: [brief description] @reference:environment-[location]_[view].jpg], 
[STYLE_MODIFIERS.CINEMATIC_BASE], [STYLE_MODIFIERS.DARK_FANTASY if applicable], 
[TECHNICAL_SPECS.[appropriate model]], [LENS_SPECS.[appropriate lens]], [QUALITY_BOOSTERS]
```

### 2.2 Enhanced Jinwoo Examples

#### Jinwoo Casual Determined (Enhanced)
```
Sung Jinwoo, 24 year old Korean athletic male, black medium messy hair, dark brown intense eyes,
wearing: black t-shirt and dark jeans, expression: determined jaw set @reference:character-jinwoo_determined.jpg, 
pose: standing neutral @reference:character-jinwoo_standing_neutral.jpg, 
location context: hospital room morning light @reference:environment-hospital_room_wide_am.jpg,
Netflix live action production, cinematic lighting, dramatic composition,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
TECHNICAL_SPECS.WAN_2_7_CLOSE_UP, 
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

#### Jinwoo Hunter Power Activation (Enhanced)
```
Sung Jinwoo, 24 year old Korean athletic male, black medium messy hair, dark brown glowing eyes,
wearing: black hunter uniform with crimson accents, expression: calculating half-lidded @reference:character-jinwoo_calculating.jpg, 
pose: power activation stance @reference:character-jinwoo_power_activation.jpg, 
location context: dungeon corridor with magical runes glowing on walls @reference:environment-dungeon_corridor_mid.jpg,
Netflix live action production, cinematic lighting, dramatic composition,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magic effects: visible blue energy emanating from hands, shadow particles forming,
TECHNICAL_SPECS.SEEDANCE_2_0_MULTI_REF, 
24mm lens, deep focus, f/8,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

### 2.3 Enhanced Environment Prompt Template
```
[Location type]: [specific location name], [time of day] lighting, [weather conditions], 
[key architectural/natural elements], [atmospheric details], 
@reference:environment-[location]_[specific_view].jpg, 
[STYLE_MODIFIERS.[appropriate style]], [LENS_SPECS.[appropriate lens]], [QUALITY_BOOSTERS]
```

#### Enhanced Hospital Room Example
```
Hospital Room: standard patient room, morning light, clear weather,
hospital bed with medical equipment, IV stand, heart monitor beeping softly,
morning light casting horizontal blinds patterns on floor and wall,
@reference:environment-hospital_room_morning_blinds.jpg,
Urban modern: contemporary urban setting, realistic textures, modern architecture,
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

### 2.4 Enhanced Video Generation Prompt Template
```
[Action description], [camera movement description], [duration] seconds, 
[environmental details @reference:environment-[location]_[specific_angle].jpg], 
[character details if visible @reference:character-[name]_[action_pose].jpg], 
[magic/effects if applicable @reference:effect-[effect_name].jpg],
[STYLE_MODIFIERS.[appropriate style]], [QUALITY_BOOSTERS],
[TECHNICAL_SPECS.[appropriate model_for_motion]]
```

#### Enhanced Jinwoo Examining Hands Example
```
Sung Jinwoo's hands slowly lifting from blanket to examine palms, camera smooth forward dolly at 0.3m/sec, 2.0 seconds,
hospital bed sheets with subtle wrinkles @reference:environment-hospital_bed_sheets.jpg, 
morning light creating soft shadows on fabric,
Jinwoo wearing hospital gown, expression: focused concentration on hands @reference:character-jinwoo_focused_hands.jpg, 
brows slightly furrowed,
faint golden system-like glow beginning to emanate from palms (early power awareness) @reference:effect-system_awakening_glow.jpg,
Netflix live action production, cinematic lighting, dramatic composition,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: subtle energy particles (if story-appropriate for power realization),
TECHNICAL_SPECS.KLING_3_0_DIALOGUE_SCENE, 
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

---

## 3. Boruto: Two Blue Vortex Enhancements

### 3.1 Enhanced Character Prompt Template
```
[Character Name], [age] year old [nationality] [ninja rank] ninja, [hair description], [eye description] [eye details if applicable], 
[wearing: [specific outfit] @reference:character-[name]_[outfit].jpg], 
[expression: [specific expression] @reference:character-[name]_[expression].jpg], 
[pose: [specific pose] @reference:character-[name]_[pose].jpg], 
[chakra aura: [description] @reference:effect-chakra-[nature]_[level].jpg if applicable], 
[special markings: [description] @reference:effect-[marking_type].jpg if applicable], 
[location context: [brief description] @reference:environment-[location]_[view].jpg], 
[STYLE_MODIFIERS.[appropriate ninja base]], [STYLE_MODIFIERS.[appropriate village/location]], 
[TECHNICAL_SPECS.[appropriate model]], [LENS_SPECS.[appropriate lens]], [QUALITY_BOOSTERS]
```

### 3.2 Enhanced Boruto Uzumaki Examples

#### Boruto Determined (Enhanced)
```
Boruto Uzumaki, 16 year old Japanese Konoha ninja Jonin-level, blonde spiky hair in front longer back, blue eyes (Jougan inactive),
wearing: standard ninja outfit with forehead protector worn sideways @reference:character-boruto_standard_outfit.jpg, 
expression: determined jaw set @reference:character-boruto_determined.jpg, 
pose: ready stance, weight on balls of feet @reference:character-boruto_ready_stance.jpg, 
chakra aura: faint blue-white outline (Wind Release chakra sensing) @reference:effect-wind_chakra_faint.jpg, 
location context: Konoha training grounds morning light @reference:environment-training_grounds_morning.jpg,
Dynamic ninja action, sharp movements, detailed costume textures, authentic ninja gear,
Hidden Leaf Village setting, traditional Japanese architecture with hidden modern elements,
TECHNICAL_SPECS.KLING_3_0_ACTION_SCENE, 
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

#### Boruto Vanishing Rasengan Close Impact (Enhanced)
```
Close impact of Boruto's Vanishing Rasengan making contact with target, camera extreme close static, 3 seconds,
sparks and distortion from high-speed rotation, 
Boruto in orange-accented outfit with blue Wind chakra flaring on blocks @reference:character-boruto_vanishing_rasengan_impact.jpg, 
visible chakra aura clashing: Boruto's blue-white vs target's energy,
Wind Release: Vanishing Rasengan: sphere of chakra that becomes optically distorted at high rotation,
visual properties: starts blue-white, becomes distorted/warped like heat haze at peak speed,
interaction: concentrated piercing damage due to focused energy,
Dynamic ninja action, sharp movements, detailed costume textures, authentic ninja gear,
Chakra Visual: Visible colored energy aura, chakra particles flowing, technique-specific visual effects,
Jutsu Effects: Shape transformation (distorted sphere), elemental manifestation (Wind),
TECHNICAL_SPECS.WAN_2_7_EXTREME_CLOSE_UP, 
85mm macro lens, very shallow focus, f/1.4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

### 3.3 Enhanced Video Generation Prompt Template (Ninja Action)
```
[Action description], [camera movement description], [duration] seconds, 
[environmental details @reference:environment-[location]_[specific_angle].jpg], 
[character details: [char1] @reference:character-[char1]_[action].jpg, [char2] @reference:character-[char2]_[action].jpg], 
[chakra visuals: [description] @reference:effect-chakra-[nature]_[intensity].jpg], 
[jutsu effects: [description] @reference:effect-[jutsu_name].jpg if applicable],
[STYLE_MODIFIERS.[appropriate ninja base]], [STYLE_MODIFIERS.[appropriate village/location]], 
[TECHNICAL_SPECS.[appropriate model_for_action]], [QUALITY_BOOSTERS]
```

#### Enhanced High-Speed Taijutsu Exchange Example
```
Boruto Uzumaki and Kawaki exchanging rapid blows in close combat, camera circling at character height to show 360 action, 4 seconds,
training ground dirt field @reference:environment-training_grounds_dirt.jpg,
occasional slow-mo on impact points showing shockwaves, clear visibility of blocks and counters,
Kawaki in black jacket with visible crimson-black Karma patterns flaring on impact @reference:character-kawaki_karma_impact.jpg,
Boruto in orange-accented outfit with blue Wind chakra flaring on blocks @reference:character-boruto_wind_chakra_flare.jpg,
visible chakra auras clashing: Kawaki's reddish-black vs Boruto's blue-white @reference:effect-chakra_clash_wind_vs_karma.jpg,
Dynamic ninja action, sharp movements, detailed costume textures, authentic ninja gear,
Chakra Visual: Visible colored energy aura, chakra particles flowing, technique-specific visual effects,
Jutsu Effects: Energy constructs, matter distortion (Karma), shape transformation (Rasengan variants),
Circling shot at character height to show full body movement,
TECHNICAL_SPECS.SEEDANCE_2_0_MULTI_REF_ACTION, 
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

---

## 4. Implementation Guide

### 4.1 Reference System Setup
Before using enhanced templates, establish your reference library:

```
references/
├── characters/
│   ├── jinwoo/
│   │   ├── jinwoo_determined.jpg
│   │   ├── jinwoo_standing_neutral.jpg
│   │   ├── jinwoo_power_activation.jpg
│   │   ├── jinwoo_calculating.jpg
│   │   ├── jinwoo_focused_hands.jpg
│   │   └── ... (all expressions/poses)
│   ├── boruto/
│   │   ├── boruto_determined.jpg
│   │   ├── boruto_ready_stance.jpg
│   │   ├── boruto_standard_outfit.jpg
│   │   ├── boruto_vanishing_rasengan_impact.jpg
│   │   └── ...
│   └── kawaki/
│       ├── kawaki_serious.jpg
│       ├── kawaki_karma_impact.jpg
│       └── ...
├── environments/
│   ├── hospital_room/
│   │   ├── hospital_room_wide_am.jpg
│   │   ├── hospital_room_morning_blinds.jpg
│   │   ├── hospital_bed_sheets.jpg
│   │   └── ...
│   ├── training_grounds/
│   │   ├── training_grounds_morning.jpg
│   │   ├── training_grounds_dirt.jpg
│   │   └── ...
│   └── dungeon/
│       ├── dungeon_corridor_mid.jpg
│       └── ...
└── effects/
    ├── system_awakening_glow.jpg
    ├── wind_chakra_faint.jpg
    ├── effect-chakra_clash_wind_vs_karma.jpg
    └── ...
```

### 4.2 Technical Specifications Reference
Create a `TECHNICAL_SPECS` reference document (or integrate into your prompt builder):

```
TECHNICAL_SPECS:
  WAN_2_7_CLOSE_UP: 
    model: "wan2.7-i2v-closeup"
    seed: 42
    steps: 30
    cfg_scale: 7.5
    width: 3840
    height: 2160
    fps: 24
    
  KLING_3_0_DIALOGUE_SCENE:
    model: "kling3.0-dialogue"
    seed: 42
    steps: 25
    cfg_scale: 8.0
    width: 3840
    height: 2160
    fps: 24  (native)
    
  VEO_3_1_ESTABLISHING_SHOT:
    model: "veo3.1-establishing"
    seed: 42
    steps: 35
    cfg_scale: 7.0
    width: 3840
    height: 2160
    fps: 24
    
  SEEDANCE_2_0_MULTI_REF:
    model: "seedance2.0-multiref"
    seed: 42
    steps: 28
    cfg_scale: 7.5
    width: 3840
    height: 2160
    fps: 24
    
  KLING_3_0_ACTION_SCENE:
    model: "kling3.0-action"
    seed: 42
    steps: 25
    cfg_scale: 8.0
    width: 3840
    height: 2160
    fps: 24
```

### 4.3 Integration Workflow
1. **Pre-production**: 
   - Scene Analyzer outputs include required reference specifications
   - Character Manager verifies/updates reference sets
   - Environment Manager generates/maintains environment references
   - Prompt Builder incorporates reference anchors and technical specs

2. **Production**:
   - Image Generation Agents: Use reference anchors for consistency
   - Video Generation Agents: Apply technical specs + reference anchoring
   - Voice Generation Agents: Include voice ID/parameters from character bible
   - Music/FX Generation Agents: Apply same consistency principles

3. **Post-production**:
   - Editor Agent: Validate reference usage in generated assets
   - Consistency Checker: Verify reference anchoring and technical compliance

---

## 5. Quality Assurance Integration

Add these checkpoints to your existing Consistency Maintenance Rules:

### 5.1 Reference Anchoring Rule
```
REFERENCE_ANCHORING: All prompts must include explicit @reference: anchors for:
   - Character poses/expressions when visible
   - Environment key angles when establishing location
   - Effect layers when magic/visual effects are present
   - Never generate floating objects/characters without environment reference
```

### 5.2 Seed Consistency Rule
```
SEED_CONSISTENCY: 
   - Fixed seed (42) used for all reproducible generations
   - Seed documented in TECHNICAL_SPECS and referenced in prompts
   - Never randomize seed in final production (except for intentional variations)
```

### 5.3 Model Selection Rule
```
MODEL_SELECTION: 
   - Wan 2.7 for close-ups, extreme close-ups, fine detail work
   - Kling 3.0 for dialogue scenes, action sequences, lip-sync critical shots
   - Veo 3.1 for establishing shots, cinematic wide shots, environmental showcases
   - Seedance 2.0 for multi-reference workflows, complex motion with multiple anchors
   - Model choice documented in prompt and validated in QA
```

### 5.4 Technical Specifications Compliance
```
TECHNICAL_SPECS_COMPLIANCE:
   - Resolution: 3840x2160 (4K UHD) minimum
   - Frame Rate: 24.000 fps cinematic standard
   - Bit Depth: 10-bit color minimum
   - All specifications must match TECHNICAL_SPECS reference
   - Deviations require explicit justification and re-approval
```

### 5.5 Temporal & Audio-Visual Sync Rule
```
TEMPORAL_AV_SYNC:
   - Keyframes generated at critical poses/expressions
   - Interpolation quality checked between keyframes (optical flow analysis)
   - Lip-sync validated using automated tools (Rhubarb or similar)
   - Audio timing validated against visual cues (<5ms drift threshold)
```

---

## Conclusion

These enhanced prompt templates transform your AI Live Action Studio from a promising concept into a production-ready system capable of delivering broadcast-quality, consistent anime/manga adaptations. By implementing these enhancements:

1. **You eliminate drift** through explicit reference anchoring
2. **You ensure reproducibility** through fixed seeds and documented technical specs
3. **You optimize quality** through model specialization per shot type
4. **You maintain your series identity** through preserved style modifiers and quality boosters
5. **You integrate with professional pipelines** through standards-compliant specifications

The templates are designed to be drop-in replacements for your existing prompt structures, requiring only the establishment of a reference library and technical specifications reference. Your team can begin implementing these enhancements immediately to see measurable improvements in generation consistency and quality.

**Next Steps:**
1. Establish your reference library structure
2. Create your TECHNICAL_SPECS reference document
3. Train your team on the enhanced prompt structure
4. Begin generating test assets using the enhanced templates
5. Implement the QA checkpoints in your review process

This approach turns AI video generation from a hit-or-miss prompt engineering exercise into a disciplined, repeatable production process capable of delivering professional results at scale.