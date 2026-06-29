import os
import pytest
from app.agents.editor.editor import EditorAgent


def test_editor_initialization():
    agent = EditorAgent()
    assert agent is not None
    assert hasattr(agent, 'output_dir')


def test_assemble_video():
    agent = EditorAgent()
    video_clip = {"file_path": "/fake/video.mp4"}
    audio_tracks = [{"file_path": "/fake/voice.wav"}]
    effect_layers = [{"file_path": "/fake/fx.mov"}]
    music_track = {"file_path": "/fake/music.mp3"}
    subtitle_data = {"language": "en", "text": "Hello"}

    result = agent.assemble_video(
        video_clip=video_clip,
        audio_tracks=audio_tracks,
        effect_layers=effect_layers,
        music_track=music_track,
        subtitle_data=subtitle_data
    )

    assert "file_path" in result
    assert result["file_path"].endswith(".mp4")
    assert result["mime_type"] == "video/mp4"
    assert result["video_clip"] == video_clip["file_path"]
    assert result["music_track"] == music_track["file_path"]
    assert len(result["audio_tracks"]) == 1
    assert len(result["effect_layers"]) == 1
    assert "generation_params" in result

    if os.path.exists(result["file_path"]):
        os.remove(result["file_path"])
