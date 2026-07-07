DIRECTOR_STYLES = {
    "michael_bay": {
        "action_moods": ["explosive", "intense", "epic", "dramatic"],
        "preferred_movements": ["360_orbit", "crane_up", "drone_sweep", "whip_pan"],
        "preferred_shot_types": ["low_angle", "extreme_wide", "close_up"],
        "slow_motion": {"enabled": True, "fps": 120, "min_duration": 2.0, "max_duration": 4.0},
        "lens_flare": True,
        "dutch_angle": 5,
        "shot_duration_range": (1.5, 6.0),
        "explosion_intensity": "heavy",
        "action_pattern": "fast_cutting",
        "color_grading": "teal_orange_high_contrast",
        "lighting_contrast": "high",
    },
    "russo_brothers": {
        "action_moods": ["intense", "epic", "tactical", "dramatic"],
        "preferred_movements": ["handheld", "steadicam", "360_orbit", "tracking"],
        "preferred_shot_types": ["medium", "close_up", "over_the_shoulder"],
        "slow_motion": {"enabled": True, "fps": 60, "min_duration": 1.5, "max_duration": 3.0},
        "lens_flare": False,
        "handheld_intensity": 0.4,
        "shot_duration_range": (2.0, 8.0),
        "action_pattern": "tactical_beats",
        "color_grading": "natural_saturated",
        "lighting_contrast": "natural",
    },
    "sam_raimi": {
        "action_moods": ["intense", "epic", "dramatic", "chaotic"],
        "preferred_movements": ["crash_zoom", "whip_pan", "dutch_angle", "pov_raimi", "handheld"],
        "preferred_shot_types": ["low_angle", "close_up", "extreme_close_up", "pov"],
        "slow_motion": {"enabled": False},
        "lens_flare": False,
        "dutch_angle": 25,
        "shot_duration_range": (1.0, 4.0),
        "explosion_intensity": "over_the_top",
        "action_pattern": "rapid_montage",
        "color_grading": "saturated_contrast",
        "lighting_contrast": "high",
    },
    "christopher_nolan": {
        "action_moods": ["intense", "epic", "dramatic", "suspense"],
        "preferred_movements": ["imax_steady", "tracking", "arm_car_mount", "technocrane", "dolly"],
        "preferred_shot_types": ["medium", "wide", "imax_close_up", "extreme_wide"],
        "slow_motion": {"enabled": False},
        "lens_flare": True,
        "shot_duration_range": (3.0, 15.0),
        "color_grading": "natural_muted",
        "lighting_contrast": "natural",
    },
    "akira_kurosawa": {
        "action_moods": ["epic", "dramatic", "intense"],
        "preferred_movements": ["static", "slow_dolly", "tracking_multi_cam", "axial_cut"],
        "preferred_shot_types": ["wide", "medium", "telephoto_compression", "deep_focus"],
        "slow_motion": {"enabled": False},
        "lens_flare": True,
        "shot_duration_range": (4.0, 12.0),
        "color_grading": "high_contrast_bw",
        "lighting_contrast": "dramatic",
    },
    "james_gunn": {
        "action_moods": ["epic", "intense", "chaotic", "comedic"],
        "preferred_movements": ["stedicam_hybrid", "handheld", "whip_pan", "tracking"],
        "preferred_shot_types": ["medium", "close_up", "wide", "over_the_shoulder"],
        "slow_motion": {"enabled": True, "fps": 48, "min_duration": 1.0, "max_duration": 3.0},
        "lens_flare": False,
        "shot_duration_range": (2.0, 7.0),
        "color_grading": "vivid_colorful",
        "lighting_contrast": "medium",
    },
}

STYLE_MOOD_MAP = {
    "explosive": "michael_bay",
    "intense": "russo_brothers",
    "epic": "akira_kurosawa",
    "dramatic": "sam_raimi",
    "tactical": "russo_brothers",
    "tension": "sam_raimi",
    "suspense": "christopher_nolan",
    "chaotic": "james_gunn",
    "comedic": "james_gunn",
}


def resolve_style(director_style=None, mood="neutral"):
    if director_style and director_style in DIRECTOR_STYLES:
        return director_style
    if director_style and director_style not in DIRECTOR_STYLES:
        return STYLE_MOOD_MAP.get(mood, None)
    return STYLE_MOOD_MAP.get(mood, None)
