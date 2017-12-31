from pydub import AudioSegment
import numpy as np
import math

attenuate_db = 0
accentuate_db = 2

# https://github.com/paarthmadan/bass-boost/blob/0b58e27049a8ad8d171dae7535384981c741fd58/index.py#L11


def boost(sample):
    """
    Yields None, so you can update informations.
    :param sample:
    :return:
    """
    assert isinstance(sample, AudioSegment)

    # get the raw audio
    yield "loading audio"
    track_raw = sample.get_array_of_samples()

    # as list
    yield "parsing track"
    track_raw = list(track_raw)

    # c-value
    yield "calculating average bass boost needed"
    est_mean = np.mean(track_raw)

    # a-value
    yield "calculating bass boost"
    est_std = 3.0 * np.std(track_raw) / (math.sqrt(2))

    yield "calculating bigger bass boost"
    bass_factor = int(round((est_std - est_mean) * 0.005))

    yield "extracting regions to boost"
    filtered = sample.low_pass_filter(bass_factor)

    yield "applying boosted bass to original track"
    combined = (sample - attenuate_db).overlay(filtered + accentuate_db)
    yield combined
# end def


def boost_complete(sample):
    for x in boost(sample):
        if not isinstance(x, str):
            return x
        # end if
    # end for
# end def