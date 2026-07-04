# Solo Leveling Live Action Prompt Template

This document serves as a prompt template for generating Solo Leveling-specific content within the AI Live Action Studio pipeline. It provides structured templates for character bibles, scene analysis, cinematography planning, and asset generation prompts that maintain visual and narrative consistency across episodes.

## 1. Character Bible Template

Use this template to generate and maintain consistent character references throughout the series.

### Character Core Profile
```
CHARACTER: [Character Name]
AGE: [Exact Age]
NATIONALITY: [Nationality]
HEIGHT: [Exact Height in cm/m]
BUILD: [Body Type Description]
HAIR: [Color, Style, Length]
EYES: [Color, Shape, Distinctive Features]
SKIN_TONE: [Description]
DISTINGUISHING_MARKS: [Scars, tattoos, unique features]
PERSONALITY_CORE: [3-5 key traits that define the character]
BACKSTORY_ESSENTIAL: [Critical background elements that influence behavior]
```

### Wardrobe System
```
CASUAL_WEAR:
  - Description: [Everyday outfit description]
  - Key_Pieces: [List of clothing items]
  - Color_Palette: [Primary/secondary colors]
  - Reference_Images: [Front, side, back views]

HUNTER_WEAR:
  - Description: [Hunter uniform/gear description]
  - Key_Pieces: [Armor, weapons, accessories]
  - Color_Palette: [Primary/secondary colors with accents]
  - Reference_Images: [Front, side, back views, close-ups on gear]

MONARCH_WEAR:
  - Description: [Monarch/formal attire description]
  - Key_Pieces: [Regal elements, symbols of power]
  - Color_Palette: [Regal colors with symbolic meanings]
  - Reference_Images: [Front, side, back views, detail shots]
```

### Expression Library
```
FACIAL_EXPRESSIONS:
  NEUTRAL: [Description] - Reference: [image_ref]
  DETERMINED: [Description] - Reference: [image_ref]
  ANGRY: [Description] - Reference: [image_ref]
  SAD: [Description] - Reference: [image_ref]
  SHOCKED: [Description] - Reference: [image_ref]
  CALCULATING: [Description] - Reference: [image_ref]
  EXHAUSTED: [Description] - Reference: [image_ref]
  JOYOUS: [Description] - Reference: [image_ref]
```

### Pose Library
```
KEY_POSES:
  STANCE_NEUTRAL: [Description] - Reference: [image_ref]
  STANCE_COMBAT_READY: [Description] - Reference: [image_ref]
  WALKING_CASUAL: [Description] - Reference: [image_ref]
  RUNNING_URGENT: [Description] - Reference: [image_ref]
  FIGHTING_STANCE: [Description] - Reference: [image_ref]
  POWER_ACTIVATION: [Description] - Reference: [image_ref]
```

### Jinwoo-Specific Example (Solo Leveling Protagonist)
```
CHARACTER: Sung Jinwoo
AGE: 24
NATIONALITY: Korean
HEIGHT: 182cm
BUILD: Athletic, lean but muscular
HAIR: Black, slightly messy, medium length
EYES: Dark brown, intense gaze
SKIN_TONE: Light olive
DISTINGUISHING_MARKS: None initially (develops subtle marks as powers grow)
PERSONALITY_CORE: Determined, protective, quietly confident, growth-oriented
BACKSTORY_ESSENTIAL: Started as weakest hunter, gained System, now evolving into Shadow Monarch

CASUAL_WEAR:
  - Description: Simple t-shirt and jeans, practical clothing
  - Key_Pieces: Black t-shirt, dark jeans, sneakers
  - Color_Palette: Monochrome with occasional gray
  - Reference_Images: jinwoo_casual_front.jpg, jinwoo_casual_side.jpg, jinwoo_casual_back.jpg

HUNTER_WEAR:
  - Description: Black hunter uniform with red accents, practical for combat
  - Key_Pieces: Tactical shirt, combat pants, boots, utility belt
  - Color_Palette: Black base with crimson red accents
  - Reference_Images: jinwoo_hunter_front.jpg, jinwoo_hunter_side.jpg, jinwoo_hunter_back.jpg

MONARCH_WEAR:
  - Description: Regal black and gold attire reflecting monarch status
  - Key_Pieces: Formal coat, ornate pants, symbolic accessories
  - Color_Palette: Black with gold trim and royal purple accents
  - Reference_Images: jinwoo_monarch_front.jpg, jinwoo_monarch_side.jpg, jinwoo_monarch_back.jpg

FACIAL_EXPRESSIONS:
  NEUTRAL: Calm, alert expression - Reference: jinwoo_neutral.jpg
  DETERMINED: Jaw set, focused eyes - Reference: jinwoo_determined.jpg
  ANGRY: Narrowed eyes, tense jaw - Reference: jinwoo_angry.jpg
  SAD: Downturned mouth, weary eyes - Reference: jinwoo_sad.jpg
  SHOCKED: Widened eyes, slightly open mouth - Reference: jinwoo_shocked.jpg
  CALCULATING: Half-lidded eyes, assessing gaze - Reference: jinwoo_calculating.jpg
  EXHAUSTED: Heavy lids, slack jaw - Reference: jinwoo_exhausted.jpg
  JOYOUS: Rare genuine smile, crinkled eyes - Reference: jinwoo_joyous.jpg
```

## 2. Scene Analysis Framework

Template for converting manga chapters into structured scene data for pipeline processing.

### Scene Data Structure
```
{
  "scene_number": [Integer],
  "location": "[Specific location name]",
  "location_type": "[Dungeon/City/Forest/Castle/etc.]",
  "time_of_day": "[Dawn/Morning/Afternoon/Evening/Night]",
  "weather": "[Clear/Rainy/Snowy/Foggy/Stormy]",
  "lighting_conditions": "[Natural/Artificial/Magic/Mixed]",
  "primary_characters": ["[Char1]", "[Char2]", ...],
  "secondary_characters": ["[Char1]", "[Char2]", ...],
  "action_primary": "[Main action happening in scene]",
  "action_secondary": "[Secondary actions/reactions]",
  "emotional_tone": "[Primary emotion of scene]",
  "duration_estimate": [Float in seconds, 4-10],
  "camera_priority": ["[Wide/Medium/Close-up/Extreme Close]", ...],
  "movement_style": "[Static/Pan/Tilt/Dolly/Tracking/Handheld/Drone]",
  "key_visual_elements": ["[Element1]", "[Element2]", ...],
  "required_effects": ["[VFX1]", "[VFX2]", ...],
  "audio_notes": {
    "dialogue_key": ["[Important line1]", "[Important line2]", ...],
    "ambience": "[Description]",
    "foley_priority": ["[Footsteps]", "[Weapon clashes]", "...]
  }
}
```

### Solo Leveling Location Templates
```
DUNGEON_TEMPLATE:
  location_type: "Dungeon"
  lighting_conditions: "Low artificial, magic glow sources"
  typical_weather: "Stale air, occasional magical mist"
  key_visual_elements: ["Stone corridors", "Arcane symbols", "Demon statues", "Glowing portals"]
  required_effects: ["Particle dust", "Magical energy glows", "Shadow manifestations"]
  audio_notes: {
    ambience: "Dripping water, distant growls, magical hum",
    foley_priority: ["Footsteps on stone", "Weapon impacts", "Magic crackling"]
  }

CITY_TEMPLATE:
  location_type: "Urban"
  lighting_conditions: "Mixed natural/artificial (neon signs, streetlights)"
  typical_weather: "Variable based on scene mood"
  key_visual_elements: ["Modern buildings", "Street level details", "Urban decay elements"]
  required_effects: ["Breach portals", "Demon energy residues", "Structural damage"]
  audio_notes: {
    ambience: "City traffic, distant sirens, wind",
    foley_priority: ["Footsteps on pavement", "Vehicle sounds", "Glass breaking"]
  }

DEMON_CASTLE_TEMPLATE:
  location_type: "Castle/Demon Realm"
  lighting_conditions: "Dramatic chiaroscuro, hellish glows"
  typical_weather: "Ash-filled air, eternal twilight"
  key_visual_elements: ["Gothic architecture", "Lava flows", "Bone structures", "Throne rooms"]
  required_effects: ["Hellfire", "Demonic auras", "Soul particles", "Dimensional rips"]
  audio_notes: {
    ambience: "Low rumbling, distant screams, crackling fire",
    foley_priority: ["Heavy footsteps", "Metal on stone", "Wing flaps"]
  }
```

### Jinwoo Scene Analysis Example
```
{
  "scene_number": 1,
  "location": "Hospital Room",
  "location_type": "Interior/Hospital",
  "time_of_day": "Morning",
  "weather": "Clear (visible through window)",
  "lighting_conditions": "Natural morning light mixed with fluorescent",
  "primary_characters": ["Sung Jinwoo"],
  "secondary_characters": [],
  "action_primary": "Jinwoo awakens in hospital bed, checking his hands",
  "action_secondary": "Monitor beeping, sunlight through blinds",
  "emotional_tone": "Confused, disbelieving, gradual realization",
  "duration_estimate": 8.0,
  "camera_priority": ["Close-up", "Medium", "Wide"],
  "movement_style": "Slow push-in, subtle handheld",
  "key_visual_elements": ["Hospital equipment", "Sunlight patterns", "Jinwoo's expression"],
  "required_effects": ["Subtle system notification glows (if visible)", "Breath vapor in cold room"],
  "audio_notes": {
    "dialogue_key": ["What happened to me?", "...I'm alive?"],
    "ambience": "Heart monitor beeping, distant hospital sounds",
    "foley_priority": ["Blanket rustle", "Fingers on metal rail", "Slow breath"]
  }
}
```

## 3. Cinematography Guidelines

Template for planning camera work that maintains Solo Leveling's cinematic identity.

### Shot Type Specifications
```
SHOT_TYPES:
  EXTREME_WIDE: 
    use: "Establishing scale, dungeon entrances, city panoramas"
    lens_equivalent: "14-24mm"
    depth_of_field: "Deep"
    
  WIDE:
    use: "Character in environment, group shots, establishing movement"
    lens_equivalent: "24-35mm"
    depth_of_field: "Moderate to deep"
    
  MEDIUM:
    use: "Dialogue scenes, character interactions, upper body action"
    lens_equivalent: "35-50mm"
    depth_of_field: "Moderate"
    
  CLOSE_UP:
    use: "Facial expressions, emotional moments, detail work"
    lens_equivalent: "50-85mm"
    depth_of_field: "Shallow"
    
  EXTREME_CLOSE_UP:
    use: "Eye details, weapon textures, magical effects close-ups"
    lens_equivalent: "85mm+ macro"
    depth_of_field: "Very shallow"
```

### Camera Movement Principles
```
MOVEMENT_STYLES:
  STATIC:
    use: "Dialogue-heavy scenes, tense moments, impact shots"
    characteristics: "Locked tripod, precise framing"
    
  PAN:
    use: "Following horizontal action, revealing environments"
    characteristics: "Smooth horizontal tripod movement"
    
  TILT:
    use: "Revealing vertical scale (towers, falling characters)"
    characteristics: "Smooth vertical tripod movement"
    
  DOLLY_IN/OUT:
    use: "Emphasizing character revelation or isolation"
    characteristics: "Smooth forward/backward camera movement"
    
  TRACKING:
    use: "Following character movement, chase sequences"
    characteristics: "Camera moves parallel to subject"
    
  HANDHELD:
    use: "Immediate action, chaotic scenes, intimate moments"
    characteristics: "Controlled shake, immediacy feel"
    
  DRONE/AERIAL:
    use: "Establishing scale, epic reveals, dungeon crawls"
    characteristics: "High altitude, sweeping movements"
    
  RACK_FOCUS:
    use: "Shifting attention between foreground/background elements"
    characteristics: "Focus pull between planes"
```

### Solo Leveling Visual Style Constants
```
STYLE_CONSTANTS:
  LENS_PREFERENCE: "35mm prime for dialogue, 24mm for action, 85mm for close-ups"
  COLOR_GRADING_BASE: 
    shadows: "Slightly crushed blacks with blue undertone"
    midtones: "Natural skin tones with desaturated urban colors"
    highlights: "Controlled roll-off, never blown out"
    overall: "Cool temperature base (6500K) with warm accents for magic"
    
  LIGHTING_PRINCIPLES:
    key_light: "Often practical sources (magic, weapons, neon) supplemented"
    fill_light: "Minimal to maintain dramatic contrast"
    back_light: "Frequently used for silhouette effects and separation"
    practical_lights: "Magic glows, weapon runes, neon signs as sources"
    
  COMPOSITION_RULES:
    rule_of_thirds: "Standard application for balance"
    negative_space: "Used to emphasize isolation or impending danger"
    leading_lines: "Architectural elements, weapon blades, magic trails"
    framing: "Environmental framing (doorways, broken walls, foliage)"
    
    color_accent_strategy: 
      PRIMARY: "Character's signature color (Jinwoo's crimson)"
      SECONDARY: "Magic colors (blue ice, purple shadows, red fire)"
      ENVIRONMENTAL: "Environment tells story (dungeon grays, city neons)"
```

### Jinwoo-Specific Cinematography Examples
```
SCENE_TYPE_EXAMPLES:
  AWAKENING/MOMENT_OF_REALIZATION:
    shot_sequence: [
      {"type": "EXTREME_CLOSE_UP", "duration": 1.5, "movement": "STATIC", "focus": "Eyes opening"},
      {"type": "CLOSE_UP", "duration": 2.0, "movement": "SLOW_PUSH_IN", "focus": "Hands examining"},
      {"type": "MEDIUM", "duration": 2.5, "movement": "STATIC", "focus": "Full torso, realizing change"},
      {"type": "WIDE", "duration": 2.0, "movement": "STATIC", "focus": "Room context, morning light"}
    ]
    lighting_notes: "Morning light creates natural rim light, practical monitor glow as fill"
    
  DUNGEON_ENTRY:
    shot_sequence: [
      {"type": "WIDE", "duration": 2.0, "movement": "STATIC", "focus": "Party approaching dungeon mouth"},
      {"type": "MEDIUM", "duration": 1.5, "movement": "TRACKING_LEFT", "focus": "Jinwoo's determined profile"},
      {"type": "CLOSE_UP", "duration": 1.0, "movement": "STATIC", "focus": "Hand gripping dagger hilt"},
      {"type": "EXTREME_WIDE", "duration": 3.0, "movement": "SLOW_DOLLY_IN", "focus": "Party disappearing into darkness"}
    ]
    lighting_notes: "Key light from dungeon entrance, practical torch/glow sources, heavy contrast"
    
  SHADOW_MONARCH_REVEAL:
    shot_sequence: [
      {"type": "EXTREME_WIDE", "duration": 2.0, "movement": "STATIC", "focus": "Army of shadows revealed"},
      {"type": "MEDIUM", "duration": 1.5, "movement": "STATIC", "focus": "Jinwoo raising hand in command"},
      {"type": "CLOSE_UP", "duration": 2.0, "movement": "STATIC", "focus": "Eyes glowing with power"},
      {"type": "WIDE", "duration": 2.5, "movement": "360_ORBIT", "focus": "Monarch surrounded by shadow army"}
    ]
    lighting_notes: "Backlit by shadow energy, practical glow from monarch aura, rim lighting"
```

## 4. Prompt Builder Templates

Templates for generating consistent prompts across image, video, voice, and effects generation.

### Base Prompt Structure
```
[SUBJECT_DESCRIPTION], [STYLE_MODIFIERS], [LIGHTING_SPECIFICS], [LENS_CAMERA_SPECS], [QUALITY_BOOSTERS]
```

### Style Modifiers Library
```
STYLE_MODIFIERS:
  CINEMATIC_BASE: "Netflix live action production, cinematic lighting, dramatic composition"
  DARK_FANTASY: "Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog"
  URBAN_MODERN: "Contemporary urban setting, realistic textures, modern architecture"
  DEMONIC_REALM: "Hellish landscape, supernatural lighting, otherworldly atmosphere"
  MAGIC_EFFECTS: "Visible magical energy, particle systems, energy glows, rune inscriptions"
  
  QUALITY_BOOSTERS: 
    "8k resolution, ultra detailed, professional film quality, Arri Alexa look"
    "Hollywood blockbuster cinematography, Roger Deakins lighting"
    "Professional color grading, filmic contrast, no CGI look"
```

### Lens/Camera Specs Library
```
LENS_SPECS:
  WIDE_SHOT: "24mm lens, deep focus, f/8"
  MEDIUM_SHOT: "35mm lens, moderate focus, f/4"
  CLOSE_UP: "50mm lens, shallow focus, f/2.0"
  EXTREME_CLOSE: "85mm macro lens, very shallow focus, f/1.4"
  
  CAMERA_MOVEMENT:
    STATIC: "locked tripod, precise framing"
    PAN_LEFT: "smooth horizontal pan left at 5 degrees/sec"
    PAN_RIGHT: "smooth horizontal pan right at 5 degrees/sec"
    TILT_UP: "smooth vertical tilt up at 5 degrees/sec"
    TILT_DOWN: "smooth vertical tilt down at 5 degrees/sec"
    DOLLY_IN: "smooth forward dolly at 0.5m/sec"
    DOLLY_OUT: "smooth backward dolly at 0.5m/sec"
    TRACKING_LEFT: "camera tracking left parallel to subject at subject speed"
    TRACKING_RIGHT: "camera tracking right parallel to subject at subject speed"
```

### Solo Leveling Specific Prompt Templates

#### Character Prompt Template
```
[Character Name], [age] year old [nationality] [build] character, [hair description], [eye description], 
[wearing: [specific outfit]], [expression: [specific expression]], [pose: [specific pose]], 
[location context: [brief description]], 
[STYLE_MODIFIERS.CINEMATIC_BASE], [STYLE_MODIFIERS.DARK_FANTASY if applicable], 
[LENS_SPECS.[appropriate lens]], [QUALITY_BOOSTERS]
```

#### Jinwoo Character Examples
```
# Jinwoo Casual Determined
Sung Jinwoo, 24 year old Korean athletic male, black medium messy hair, dark brown intense eyes,
wearing: black t-shirt and dark jeans, expression: determined jaw set, pose: standing neutral,
location context: hospital room morning light,
Netflix live action production, cinematic lighting, dramatic composition,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Jinwoo Hunter Power Activation
Sung Jinwoo, 24 year old Korean athletic male, black medium messy hair, dark brown glowing eyes,
wearing: black hunter uniform with crimson accents, expression: calculating half-lidded, pose: power activation stance,
location context: dungeon corridor with magical runes glowing on walls,
Netflix live action production, cinematic lighting, dramatic composition,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magic effects: visible blue energy emanating from hands, shadow particles forming,
24mm lens, deep focus, f/8,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

#### Environment Prompt Template
```
[Location type]: [specific location name], [time of day] lighting, [weather conditions], 
[key architectural/natural elements], [atmospheric details], 
[STYLE_MODIFIERS.[appropriate style]], [LENS_SPECS.[appropriate lens]], [QUALITY_BOOSTERS]
```

#### Environment Examples
```
# Solo Leveling Dungeon Entrance
Dungeon entrance: massive stone archway with demonic carvings, evening lighting, clear weather,
towering stone pillars covered in glowing arcane symbols, mist pouring from depths, 
distant demonic growls echoing,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
24mm lens, deep focus, f/8,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Seoul City Street at Night
Seoul city street: busy urban avenue, night time, light rain,
neon signs in Korean and English reflecting on wet pavement, modern skyscrapers in background,
steam rising from manholes, distant traffic,
Netflix live action production, cinematic lighting, dramatic composition,
Urban modern: contemporary urban setting, realistic textures, modern architecture,
35mm lens, moderate focus, f/4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Demon Castle Throne Room
Demon castle throne room: vast gothic chamber, eternal twilight, ash-filled air,
obsidian throne surrounded by lava channels, bone arches supporting ceiling, 
winged demon statues lining walls, hellfire pits casting orange glow,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
DEMONIC_REALM: Hellish landscape, supernatural lighting, otherworldly atmosphere,
14mm lens, ultra wide deep focus, f/11,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

#### Video Generation Prompt Template
```
[Action description], [camera movement description], [duration] seconds, 
[environmental details], [character details if visible], [magic/effects if applicable],
[STYLE_MODIFIERS.[appropriate style]], [QUALITY_BOOSTERS]
```

#### Video Examples
```
# Jinwoo Walking Through Dungeon
Sung Jinwoo walking slowly through dark dungeon corridor, camera tracking left parallel at subject speed, 5 seconds,
stone walls with glowing blue runes on either side, dust particles floating in air, 
Jinwoo in hunter uniform with crimson accents, slight determination in posture,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: subtle shadow particles drifting from feet,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Shadow Monarch Army Reveal
Vast army of shadow soldiers emerging from darkness, camera slow 360 orbit around center point, 8 seconds,
endless ranks of shadow warriors with glowing eyes, obsidian weapons, 
Jinwoo visible in foreground center as commanding figure, 
crimson energy aura pulsing around him,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: shadow energy waves rippling outward, crown of shadow forming above head,
24mm lens, deep focus, f/8,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Igris Sword Collision Closeup
Closeup of Sung Jinwoo's dagger blocking Igris's massive sword, camera extreme close static, 3 seconds,
sparks flying from blade contact, Jinwoo's determined expression visible, 
Igris's shadowy armor details in background,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: blue energy flare on Jinwoo's dagger, red-black energy crackle on Igris's sword,
85mm macro lens, very shallow focus, f/1.4,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

#### Voice Generation Prompt Template
```
[Character Name] speaking with [emotion] emotion: "[dialogue text]", 
[voice characteristics: [pitch, pace, timbre]], 
[context: [brief situation description]]
```

#### Voice Examples
```
# Jinwoo Determined
Sung Jinwoo speaking with determined emotion: "I'll become stronger. No matter what it takes.",
voice characteristics: medium-low pitch, measured pace, slightly rough timbre from resolve,
context: standing in hospital room after awakening to powers

# Jinwoo Calculating
Sung Jinwoo speaking with calculating emotion: "They don't realize what they've awakened.",
voice characteristics: low pitch, slow deliberate pace, cold and precise timbre,
context: observing enemy forces from dungeon shadows

# Igris Threatening
Igris speaking with angry emotion: "You dare challenge the Knight Commander?",
voice characteristics: deep resonant pitch, slow weighty pace, metallic echoing timbre,
context: facing Jinwoo in dual dungeon, massive sword raised

# Narration Style
Narrator speaking with neutral epic emotion: "In a world where hunters battle monsters...",
voice characteristics: medium pitch, steady pace, clear and authoritative timbre,
context: opening sequence establishing world premise
```

#### Music Generation Prompt Template
```
[Scene type]: [description], [emotional arc: [beginning→middle→end]], 
[instruments: [primary→secondary→accent]], 
[style: [genre descriptors]], 
[duration]: [length in minutes/seconds],
[QUALITY_BOOSTERS_MUSIC]
```

#### Music Examples
```
# Opening Theme
Opening theme: Solo Leveling main title sequence, emotional arc: mysterious→building→triumphant,
instruments: [orchestral strings→choir→heavy percussion→electronic elements],
style: Epic dark fantasy soundtrack, Solo Leveling atmosphere, orchestra, choir, intense battle theme,
duration: 1.5 minutes,
Professional film score quality, 24-bit 96kHz, orchestral realism

# Battle Theme
Battle theme: Dungeon boss fight progression, emotional arc: tense→climactic→resolving,
instruments: [distorted electric guitar→taiko drums→dark choir→synth bass],
style: Hybrid orchestral-electronic, aggressive rhythms, dissonant harmonies,
duration: 3.0 minutes,
Professional film score quality, 24-bit 96kHz, mixed with cinematic sound design

# Suspense Theme
Suspense theme: Shadow extraction preparation, emotional arc: quiet tension→building dread→release,
instruments: [low piano notes→single violin→sub bass→reverse cymbals],
style: Minimalist dark ambient, sparse textures, uncomfortable harmonies,
duration: 2.0 minutes,
Professional film score quality, 24-bit 96kHz, focused on emotional manipulation
```

#### Effects Generation Prompt Template
```
[Effect type]: [description], [behavior: [how it moves/changes]], 
[visual properties: [color, density, transparency, glow]], 
[interaction: [how it affects environment/characters]], 
[STYLE_MODIFIERS.MAGIC_EFFECTS], [QUALITY_BOOSTERS]
```

#### Effects Examples
```
# Shadow Extraction
Shadow extraction: swirling vortex of black and crimson energy forming around target,
behavior: particles spiral inward then explode outward in controlled burst,
visual properties: deep black core with crimson edges, semi-transparent, inner glow,
interaction: temporarily immobilizes target, extracts shadow essence,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: energy particles leaving temporary afterimages,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Monarch's Shadow Army
Monarch's shadow army: countless shadow soldiers materializing from darkness,
behavior: holding formation then advancing in synchronized waves,
visual properties: varying transparency from solid to mist-like, deep black with faint purple glow,
interaction: moves as cohesive unit, creates psychological terror,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: individual shadows retain slight autonomy within formation,
8k resolution, ultra detailed, professional film quality, Arri Alexa look

# Magic Barrier
Magic barrier: shimmering hexagonal energy field appearing in mid-air,
behavior: static or slowly rotating, deflects incoming attacks,
visual properties: cyan-blue geometric pattern, semi-transparent, bright inner glow,
interaction: stops physical and magical projectiles, creates tactical advantage,
Dark fantasy live action movie, Unreal Engine 5 quality, volumetric fog,
Magical elements: harmonic resonance visible as concentric rings when struck,
8k resolution, ultra detailed, professional film quality, Arri Alexa look
```

## 5. Consistency Maintenance Rules

Rules to ensure visual and narrative continuity across episodes.

### Character Consistency Rules
```
1. REFERENCE_REUSE: Always use existing character reference images when available
   - Never generate a new full-body reference if one exists in library
   - For new poses/expressions, generate using existing face/body as base

2. WARDROBE_LOCK: Character's outfit must match their current status/rank
   - Casual → Hunter → Monarch progression follows story points
   - Accessories (weapons, jewelry) must be consistent within outfit type

3. EVOLUTION_TRACKING: Physical changes must be documented and gradual
   - Power growth manifests through subtle visual cues (eye glow, aura intensity)
   - Major changes (new forms) require explicit story justification

4. EXPRESSION_LIBRARY_ADHERENCE: Use only approved expressions for emotional states
   - Create new expressions only with clear narrative justification
   - All expressions must be library-registered before use in generation
```

### Environment Consistency Rules
```
1. LOCATION_CANON: Each named location has established visual canon
   - Dungeon levels maintain proportional difficulty/decoration progression
   - City locations show consistent architectural styles and wear patterns
   - Demon realms follow established hellish aesthetics

2. TIME_OF_DAY_CONSISTENCY: Scenes claiming same time must match lighting
   - Morning scenes share similar sun angle and color temperature
   - Night scenes maintain consistent artificial/practical light sources

3. WEATHER_CONTINUITY: Weather changes require narrative justification
   - Rain doesn't start/stop without reason in same location
   - Magical weather effects must have clear source (character power, realm property)
```

### Cinematography Consistency Rules
```
1. LENS_CONSISTENCY: Similar shot types use same lens specifications
   - All dialogue medium shots use 35mm f/4 unless story demands otherwise
   - Action sequences maintain consistent movement patterns for same character

2. COLOR_GRADING_MATCH: Scenes in same location/time share base grading
   - Dungeon scenes share base blue-black grading with location-specific accents
   - City night scenes share neon reflection and wet pavement treatment

3. CAMERA_LANGUAGE: Establish visual vocabulary for characters/situations
   - Jinwoo's power moments often use slow push-ins on eyes/hands
   - Revelation scenes frequently employ 360 orbits or crane reveals
   - Tense moments favor static framing with minimal movement
```

### Prompt Engineering Consistency Rules
```
1. STYLE_MODIFIER_INHERITANCE: All prompts inherit base cinematic style
   - Base modifiers (NETFLIX_CINEMATIC, DARK_FANTASY) never omitted
   - Location/modern/fantasy modifiers added as needed

2. QUALITY_BOOSTER_MANDATORY: All generation prompts include quality boosters
   - Never sacrifice quality for speed in final production
   - Quality boosters updated as technology improves

3. CONTEXT_PROMPTING: All prompts include location/action/character context
   - Never generate floating objects or characters without environment
   - Context prevents "AI look" by grounding in established reality
```

## 6. Usage Guidelines

### How to Use This Template
1. **Character Creation**: Start with Character Bible Template for new characters
2. **Scene Processing**: Use Scene Analysis Framework to break down manga chapters
3. **Shot Planning**: Apply Cinematography Guidelines to plan each shot
4. **Prompt Generation**: Use Prompt Builder Templates to create agent inputs
5. **Quality Check**: Apply Consistency Maintenance Rules before final approval

### Workflow Example: Solo Leveling Chapter Processing
```
MANGA CHAPTER
     ↓
[Scene Analyzer] → Structured Scene Data (using Scene Analysis Framework)
     ↓
[Character Manager] → Verify/Update Character References (using Character Bible)
     ↓
[Environment Manager] → Verify/Update Location References
     ↓
[Shot Planner] → Create Shot List (using Cinematography Guidelines)
     ↓
[Prompt Builder] → Generate All Prompts (using Prompt Builder Templates)
     ↓
[Generation Agents] → Create Assets (Image, Video, Voice, Music, FX)
     ↓
[Editor Agent] → Assemble Final Scene
     ↓
[Consistency Check] → Apply Maintenance Rules
     ↓
FINAL SCENE READY FOR ASSEMBLY
```

### Updating the Template
- Add new character expressions/poses to library as they appear in story
- Update location templates when new significant locations are introduced
- Refine cinematography rules based on what works best in practice
- Add new prompt examples as style evolves
- Always maintain backward compatibility with existing references

---

*This prompt template ensures that all Solo Leveling-specific content generated through the AI Live Action Studio pipeline maintains the visual consistency, narrative coherence, and cinematic quality required for professional live-action adaptation. Use as the foundation for all content generation, updating references as the story progresses.*