#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os

from pocketsphinx.pocketsphinx import Decoder as _Decoder
# from sphinxbase.sphinxbase import *

class SphinxDecoder(object):
    def __init__(self, kws_threshold = 1e-40):
        # configuration.
        base_dir = os.path.dirname(__file__)
        modeldir = "../../../pocketsphinx/model/en-us"
        config = _Decoder.default_config()
        config.set_string('-hmm', os.path.join(base_dir, modeldir, 'en-us'))
        config.set_string('-dict', os.path.join(base_dir, modeldir, 'cmudict-en-us.dict'))
        config.set_float('-kws_threshold', kws_threshold)
        self.config = config
        self.decoder = None

    def locate(self, keyphrase, wav_stream, buffer_size = 4096 * 4):
        self.config.set_string('-keyphrase', keyphrase)
        if not self.decoder:
            self.decoder = _Decoder(self.config)
        else:
            self.decoder.reinit(self.config)

        decoder = self.decoder
        # https://sourceforge.net/p/cmusphinx/discussion/help/thread/00ad5863/?limit=25
        # copy code from pocketsphinx_continuous.c
        utt_started = False
        frate = float(self.config.get_int('-frate'))
        decoder.start_utt()
        while True:
            buf = wav_stream.read(buffer_size)
            if buf:
                decoder.process_raw(buf, False, False)
            else:
                break
            in_speech = decoder.get_in_speech()
            if in_speech and not utt_started:
                utt_started = True
            if not in_speech and utt_started:
                decoder.end_utt()
                if decoder.hyp():
                    for seg in decoder.seg():
                        yield (seg.word, seg.prob, seg.start_frame / frate, seg.end_frame / frate)
                decoder.start_utt()
                utt_started = False
        decoder.end_utt()
        if utt_started:
            if decoder.hyp():
               for seg in decoder.seg():
                    yield (seg.word, seg.prob, seg.start_frame / frate, seg.end_frame / frate)

    def locate_in_file(self, keyphrase, wav_file, buffer_size = 4096 * 4):
        with open(wav_file, 'rb') as wav_stream:
            rs = self.locate(keyphrase, wav_stream, buffer_size)
            for r in rs:
                yield r

def test():
    decoder = SphinxDecoder()
    rs = decoder.locate_in_file('explain it to me', './test.wav')
    for r in rs:
        print r
    rs = decoder.locate_in_file('insured by my client', './test.wav')
    for r in rs:
        print r

if __name__ == '__main__':
    test()
