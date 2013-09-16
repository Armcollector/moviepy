from moviepy.decorators import audio_video_fx

@audio_video_fx
def audio_fadein(clip, duration):
    """ Return an audio (or video) clip that is first mute, then the
        sound arrives progressively over ``duration`` seconds. """
    fading = lambda gf, t: min(1.0 * t / duration, 1) * gf(t)
    return clip.fl(fading, keep_duration = True)
